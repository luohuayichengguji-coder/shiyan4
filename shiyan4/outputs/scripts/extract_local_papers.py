from __future__ import annotations

import csv
import json
import re
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[2]
PDF_ROOT = ROOT / "眼底视网膜病变分割-论文PDF"
OUT = ROOT / "outputs"
TABLES = OUT / "tables"
NOTES = OUT / "notes"


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"-\n(?=[a-z])", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def category_from_path(path: Path) -> str:
    return path.relative_to(PDF_ROOT).parts[0]


def infer_direction(category: str, name: str) -> str:
    lower = name.lower()
    if category == "SAM相关":
        if any(k in lower for k in ["medsam", "medical_sam", "sam-med", "medical_images"]):
            return "医学 SAM / 医学图像适配"
        return "通用 SAM / 高质量或快速分割"
    if category == "SAM模型蒸馏":
        return "SAM 轻量化 / 蒸馏"
    if category == "医学图像增强":
        return "医学图像增强 / 修复 / 超分"
    if category == "眼底视网膜病变分割":
        if any(k in lower for k in ["enhancement", "sat-net", "low-quality"]):
            return "低质量眼底图像增强"
        if "deep learning system" in lower or "-nc-" in lower or "diagnosis" in lower:
            return "眼底病变检测 / 诊断关联"
        return "眼底 DR 病灶分割"
    return "其他"


def extract_arxiv_from_name_or_text(name: str, text: str) -> str:
    m = re.search(r"arXiv(\d{4}\.\d{4,5})", name, flags=re.I)
    if m:
        return m.group(1)
    m = re.search(r"arXiv[:\s]*(\d{4}\.\d{4,5})", text, flags=re.I)
    return m.group(1) if m else ""


def extract_doi(text: str) -> str:
    m = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", text, flags=re.I)
    return m.group(0).rstrip(".,);") if m else ""


def extract_title(doc: fitz.Document, fallback: str) -> str:
    meta_title = (doc.metadata or {}).get("title") or ""
    meta_title = clean_text(meta_title)
    if meta_title and len(meta_title) > 8 and not meta_title.lower().endswith(".pdf"):
        return meta_title

    first = clean_text(doc[0].get_text("text")[:3000])
    lines = [line.strip() for line in re.split(r"\s{2,}|\n", first) if line.strip()]
    candidates = []
    for line in lines[:30]:
        if len(line) < 8 or len(line) > 240:
            continue
        if re.search(r"^(arxiv|abstract|introduction|conference|journal|proceedings)\b", line, re.I):
            continue
        if line.count(".") > 3:
            continue
        candidates.append(line)
    if candidates:
        return candidates[0]
    title = re.sub(r"^\d{4}[_-]?", "", fallback)
    title = re.sub(r"_arXiv\d{4}\.\d{4,5}", "", title, flags=re.I)
    title = title.replace("_", " ").replace(".pdf", "")
    return title


def find_section(text: str, start_terms: list[str], end_terms: list[str], max_chars: int = 2600) -> str:
    lower = text.lower()
    starts = []
    for term in start_terms:
        idx = lower.find(term.lower())
        if idx >= 0:
            starts.append(idx)
    if not starts:
        return ""
    start = min(starts)
    end = min([lower.find(t.lower(), start + 20) for t in end_terms if lower.find(t.lower(), start + 20) > 0] or [start + max_chars])
    return clean_text(text[start:end])[:max_chars]


def extract_snippets(path: Path) -> dict:
    doc = fitz.open(path)
    pages = len(doc)
    first_pages = []
    for i in range(min(pages, 5)):
        first_pages.append(doc[i].get_text("text"))
    text5 = clean_text("\n".join(first_pages))

    all_text_for_ids = text5
    if pages > 5:
        all_text_for_ids += " " + clean_text(doc[min(5, pages - 1)].get_text("text"))

    title = extract_title(doc, path.stem)
    abstract = find_section(text5, ["abstract"], ["introduction", "1 introduction", "keywords", "index terms"], 1900)
    intro = find_section(text5, ["introduction", "1 introduction"], ["related work", "method", "methods", "materials"], 1800)
    datasets = sorted(set(re.findall(r"\b(IDRiD|DDR|FGADR|APTOS|EyePACS|Messidor(?:-2)?|e-ophtha|CHASE_DB1|DRIVE|STARE|REFUGE|RIM-ONE|DIARETDB1|ROSE|PALM|HRF)\b", all_text_for_ids, flags=re.I)))
    metrics = sorted(set(re.findall(r"\b(Dice|IoU|AUC|Sensitivity|Specificity|F1|Accuracy|Precision|Recall|mAP|MAE|PSNR|SSIM|LPIPS|FLOPs|FPS)\b", all_text_for_ids, flags=re.I)))
    arxiv = extract_arxiv_from_name_or_text(path.name, all_text_for_ids)
    doi = extract_doi(all_text_for_ids)
    doc.close()
    return {
        "title": title,
        "pages": pages,
        "abstract": abstract,
        "intro": intro,
        "datasets_mentioned": "; ".join(datasets),
        "metrics_mentioned": "; ".join(metrics),
        "arxiv": arxiv,
        "doi": doi,
    }


def main() -> None:
    TABLES.mkdir(parents=True, exist_ok=True)
    NOTES.mkdir(parents=True, exist_ok=True)

    rows = []
    for pdf in sorted(PDF_ROOT.glob("*/*.pdf")):
        category = category_from_path(pdf)
        try:
            data = extract_snippets(pdf)
            status = "ok"
        except Exception as exc:  # keep batch moving and make extraction failures explicit
            data = {
                "title": re.sub(r"_", " ", pdf.stem),
                "pages": "",
                "abstract": "",
                "intro": "",
                "datasets_mentioned": "",
                "metrics_mentioned": "",
                "arxiv": extract_arxiv_from_name_or_text(pdf.name, ""),
                "doi": "",
            }
            status = f"extract_failed: {exc}"
        year_match = re.search(r"(20\d{2})", pdf.name)
        year = year_match.group(1) if year_match else ""
        rows.append({
            "id": f"P{len(rows)+1:02d}",
            "year": year,
            "category": category,
            "direction": infer_direction(category, pdf.name),
            "title": data["title"],
            "local_file": str(pdf.relative_to(ROOT)),
            "pages": data["pages"],
            "arxiv": data["arxiv"],
            "doi": data["doi"],
            "datasets_mentioned": data["datasets_mentioned"],
            "metrics_mentioned": data["metrics_mentioned"],
            "extraction_status": status,
            "abstract_or_summary_snippet": data["abstract"] or data["intro"],
        })

    csv_path = TABLES / "local_paper_index.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    json_path = TABLES / "local_paper_index.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    md_lines = [
        "# 本地论文索引表",
        "",
        "说明：本表由 `outputs/scripts/extract_local_papers.py` 使用 PyMuPDF 自动抽取 PDF 元数据、题名、页数、arXiv/DOI 线索、摘要/引言片段，并按课程任务方向人工规则分类。抽取结果用于后续人工综合，不能替代全文精读。",
        "",
        "| ID | 年份 | 类别 | 调研方向 | 题名 | 本地文件 | 页数 | arXiv/DOI | 数据集线索 | 指标线索 |",
        "|---|---:|---|---|---|---|---:|---|---|---|",
    ]
    for r in rows:
        ids = []
        if r["arxiv"]:
            ids.append(f"arXiv:{r['arxiv']}")
        if r["doi"]:
            ids.append(f"DOI:{r['doi']}")
        md_lines.append(
            "| {id} | {year} | {category} | {direction} | {title} | `{local_file}` | {pages} | {ids} | {datasets} | {metrics} |".format(
                id=r["id"],
                year=r["year"],
                category=r["category"],
                direction=r["direction"],
                title=r["title"].replace("|", "\\|"),
                local_file=r["local_file"],
                pages=r["pages"],
                ids="<br>".join(ids) if ids else "未抽取",
                datasets=r["datasets_mentioned"] or "未抽取",
                metrics=r["metrics_mentioned"] or "未抽取",
            )
        )
    (TABLES / "local_paper_index.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    notes_lines = [
        "# 本地 PDF 摘要与引言抽取片段",
        "",
        "用途：为阶段3重点论文阅读笔记提供可追溯原始线索。长篇正文未在此处全文复制，避免把 PDF 抽取误差直接写入报告。",
        "",
    ]
    for r in rows:
        notes_lines += [
            f"## {r['id']} {r['title']}",
            "",
            f"- 类别：{r['category']} / {r['direction']}",
            f"- 本地文件：`{r['local_file']}`",
            f"- 页数：{r['pages']}；标识：{('arXiv:' + r['arxiv']) if r['arxiv'] else r['doi'] or '未抽取'}",
            f"- 数据集线索：{r['datasets_mentioned'] or '未抽取'}",
            f"- 指标线索：{r['metrics_mentioned'] or '未抽取'}",
            "",
            "```text",
            (r["abstract_or_summary_snippet"] or "未抽取到摘要/引言片段")[:1800],
            "```",
            "",
        ]
    (NOTES / "local_pdf_extracted_snippets.md").write_text("\n".join(notes_lines), encoding="utf-8")

    print(f"Wrote {len(rows)} paper records")
    print(csv_path)
    print(TABLES / "local_paper_index.md")
    print(NOTES / "local_pdf_extracted_snippets.md")


if __name__ == "__main__":
    main()
