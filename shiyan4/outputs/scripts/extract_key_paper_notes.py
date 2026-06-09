from __future__ import annotations

import json
import re
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"
PDF_ROOT = ROOT / "眼底视网膜病变分割-论文PDF"
LOCAL_INDEX = OUT / "tables" / "local_paper_index.json"
NOTES = OUT / "notes"

KEY_IDS = {
    "P13": "SAM 原始模型，提供 promptable segmentation 与 SA-1B 数据引擎，是所有适配方案的技术起点。",
    "P09": "MedSAM，代表大规模医学图像微调路线，可作为医学 SAM 适配的主线背景。",
    "P10": "Medical SAM Adapter，代表参数高效 adapter/提示适配路线。",
    "P11": "SAM-Med2D，代表 2D 医学 SAM 大数据集、多提示微调路线。",
    "P15": "SAM 2，代表图像/视频统一和记忆机制，对连续眼底随访和高效提示有启发。",
    "P23": "RTNet，代表眼底 DR 多病灶分割中利用病灶-血管关系和 transformer 的专用模型。",
    "P25": "GlanceSeg，代表 gaze/saliency prompt + SAM 处理微小微动脉瘤的眼底场景适配。",
    "P21": "IDRiD 病灶分割基线与对抗学习，体现早期针对小病灶/边缘的分割损失设计。",
    "P28": "SAT-Net，代表低质量眼底图像增强和结构感知增强，可对接低质量感知增强模块。",
    "P06": "KD-SAM，代表医学 SAM 蒸馏和轻量化部署方向。",
    "P01": "EdgeSAM，代表 prompt-in-the-loop 蒸馏，可借鉴到眼底病灶交互式/自动提示蒸馏。",
}

SECTION_TERMS = [
    ("abstract", ["abstract"], ["introduction", "1 introduction"]),
    ("introduction", ["introduction", "1 introduction"], ["related work", "method", "methods", "2 "]),
    ("method", ["method", "methods", "methodology", "proposed method", "our method", "framework"], ["experiment", "experiments", "results", "evaluation"]),
    ("experiment", ["experiment", "experiments", "experimental results", "evaluation"], ["conclusion", "discussion", "references"]),
    ("conclusion", ["conclusion", "discussion"], ["references", "appendix"]),
]


def clean_text(text: str) -> str:
    text = re.sub(r"-\n(?=[a-z])", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def find_section(text: str, starts: list[str], ends: list[str], max_chars: int = 2200) -> str:
    lower = text.lower()
    positions = [lower.find(s) for s in starts if lower.find(s) >= 0]
    if not positions:
        return ""
    start = min(positions)
    end_positions = [lower.find(e, start + 30) for e in ends if lower.find(e, start + 30) > 0]
    end = min(end_positions) if end_positions else start + max_chars
    return clean_text(text[start:end])[:max_chars]


def paper_text(path: Path) -> str:
    doc = fitz.open(path)
    chunks = []
    for i in range(len(doc)):
        chunks.append(doc[i].get_text("text"))
    doc.close()
    return clean_text("\n".join(chunks))


def main() -> None:
    NOTES.mkdir(parents=True, exist_ok=True)
    rows = {r["id"]: r for r in json.loads(LOCAL_INDEX.read_text(encoding="utf-8"))}
    detail = {}
    md = [
        "# 重点论文阅读笔记",
        "",
        "说明：本文件按 nature-reader 的“源文件定位 + 结构化阅读”思想建立，但任务目标是技术调研而非全文翻译，因此保留题名、来源、关键段落线索和人工综合笔记，不复制整篇论文正文。",
        "",
    ]
    for pid, reason in KEY_IDS.items():
        r = rows[pid]
        path = ROOT / r["local_file"]
        text = paper_text(path)
        sections = {}
        for name, starts, ends in SECTION_TERMS:
            sections[name] = find_section(text, starts, ends)
        datasets = sorted(set(re.findall(r"\b(IDRiD|DDR|FGADR|APTOS|EyePACS|Messidor(?:-2)?|Retinal-Lesions|Kvasir-SEG|ISIC 2017|Fetal Head Ultrasound|Breast Ultrasound|COCO|LVIS|SA-1B)\b", text, flags=re.I)))
        losses = sorted(set(re.findall(r"\b(Dice loss|cross[- ]entropy|focal loss|MSE|perceptual loss|adversarial loss|boundary loss|Lovasz|Tversky|Hausdorff)\b", text, flags=re.I)))
        methods = sorted(set(re.findall(r"\b(SAM|MedSAM|adapter|Transformer|cross-attention|self-attention|prompt|distillation|encoder|decoder|saliency|gaze|CLAHE|cGAN|HEDNet|task-adaptive|structure-aware|Flash Attention|knowledge distillation)\b", text, flags=re.I)))[:20]
        detail[pid] = {
            "reason": reason,
            "row": r,
            "sections": sections,
            "datasets": datasets,
            "losses": losses,
            "method_keywords": methods,
        }
        md += [
            f"## {pid} {r['title']}",
            "",
            f"- 选择理由：{reason}",
            f"- 本地文件：`{r['local_file']}`",
            f"- 类别/方向：{r['category']} / {r['direction']}",
            f"- 年份与标识：{r['year']}；{('arXiv:' + r['arxiv']) if r['arxiv'] else ('DOI:' + r['doi'] if r['doi'] else '未抽取')}",
            f"- 自动抽取数据集线索：{'; '.join(datasets) if datasets else r['datasets_mentioned'] or '未抽取'}",
            f"- 自动抽取损失/训练线索：{'; '.join(losses) if losses else '未抽取'}",
            f"- 方法关键词：{'; '.join(methods) if methods else '未抽取'}",
            "",
            "### 结构化阅读线索",
            "",
        ]
        for sec in ["abstract", "method", "experiment", "conclusion"]:
            val = sections.get(sec) or "未抽取到稳定片段。"
            md += [f"**{sec}**", "", "```text", val[:1600], "```", ""]
        md += [
            "### 人工综合要点",
            "",
            "- 研究问题：见后续 `key_paper_analysis.md` 的人工归纳表。",
            "- 方法、数据集、指标、优势、不足和可借鉴点：在后续综合表中统一给出，避免仅凭 PDF 自动抽取片段下结论。",
            "",
        ]

    (NOTES / "key_paper_reader_notes.md").write_text("\n".join(md), encoding="utf-8")
    (NOTES / "key_paper_reader_notes.json").write_text(json.dumps(detail, ensure_ascii=False, indent=2), encoding="utf-8")
    print(NOTES / "key_paper_reader_notes.md")


if __name__ == "__main__":
    main()
