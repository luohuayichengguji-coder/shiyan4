from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"
RENDER = OUT / "render_checks"


def convert_to_pdf(input_file: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    profile = output_dir / "lo_profile"
    profile.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["HOME"] = str(profile)
    env["XDG_CONFIG_HOME"] = str(profile / "xdg_config")
    env["XDG_CACHE_HOME"] = str(profile / "xdg_cache")
    Path(env["XDG_CONFIG_HOME"]).mkdir(parents=True, exist_ok=True)
    Path(env["XDG_CACHE_HOME"]).mkdir(parents=True, exist_ok=True)

    cmd = [
        "soffice",
        f"-env:UserInstallation=file://{profile.resolve()}",
        "--invisible",
        "--headless",
        "--norestore",
        "--convert-to",
        "pdf",
        "--outdir",
        str(output_dir),
        str(input_file),
    ]
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
    log = output_dir / f"{input_file.stem}_soffice.log"
    log.write_text(
        "CMD: " + " ".join(cmd) + "\n"
        + f"EXIT: {proc.returncode}\n"
        + "STDOUT:\n" + proc.stdout + "\nSTDERR:\n" + proc.stderr,
        encoding="utf-8",
    )
    expected = output_dir / f"{input_file.stem}.pdf"
    if expected.exists() and expected.stat().st_size > 0:
        return expected
    pdfs = sorted(output_dir.glob("*.pdf"), key=lambda p: p.stat().st_mtime, reverse=True)
    if pdfs:
        return pdfs[0]
    raise RuntimeError(f"LibreOffice conversion failed for {input_file}; see {log}")


def render_pdf(pdf: Path, output_dir: Path, prefix: str, dpi: int = 130) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf)
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    pages = []
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        path = output_dir / f"{prefix}_page_{i:02d}.png"
        pix.save(path)
        pages.append(path)
    doc.close()
    return pages


def make_contact_sheet(images: list[Path], output: Path, title: str, thumb_w: int = 260) -> None:
    thumbs = []
    for path in images:
        img = Image.open(path).convert("RGB")
        ratio = thumb_w / img.width
        thumb_h = int(img.height * ratio)
        img = img.resize((thumb_w, thumb_h))
        thumbs.append((path.name, img))
    cols = 3
    pad = 24
    label_h = 28
    title_h = 44
    rows = (len(thumbs) + cols - 1) // cols
    cell_h = max((img.height for _, img in thumbs), default=0) + label_h
    sheet = Image.new("RGB", (cols * thumb_w + (cols + 1) * pad, title_h + rows * cell_h + (rows + 1) * pad), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((pad, 14), title, fill=(31, 41, 55))
    for idx, (name, img) in enumerate(thumbs):
        r, c = divmod(idx, cols)
        x = pad + c * (thumb_w + pad)
        y = title_h + pad + r * cell_h
        sheet.paste(img, (x, y))
        draw.rectangle([x, y, x + img.width, y + img.height], outline=(203, 213, 225), width=1)
        draw.text((x, y + img.height + 6), name, fill=(75, 85, 99))
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def check_file(input_file: Path, kind: str) -> dict:
    out_dir = RENDER / kind
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = convert_to_pdf(input_file, out_dir)
    pages = render_pdf(pdf, out_dir, kind)
    sheet = out_dir / f"{kind}_contact_sheet.png"
    make_contact_sheet(pages, sheet, f"{kind.upper()} render check: {input_file.name}")
    return {
        "input": str(input_file),
        "pdf": str(pdf),
        "pages": len(pages),
        "contact_sheet": str(sheet),
    }


def main() -> None:
    docx = OUT / "AI开发技术-实验4.1-医学图像技术调研报告.docx"
    pptx = OUT / "AI开发技术-实验4.1-医学图像技术调研汇报.pptx"
    results = [
        check_file(docx, "docx"),
        check_file(pptx, "pptx"),
    ]
    for r in results:
        print(r)


if __name__ == "__main__":
    main()
