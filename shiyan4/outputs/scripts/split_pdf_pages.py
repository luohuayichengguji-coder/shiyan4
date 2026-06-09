from __future__ import annotations

import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: split_pdf_pages.py input.pdf output_dir")
    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(src))
    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)
        out_path = out_dir / f"page_{i:02d}.pdf"
        with out_path.open("wb") as f:
            writer.write(f)
    print(len(reader.pages))


if __name__ == "__main__":
    main()
