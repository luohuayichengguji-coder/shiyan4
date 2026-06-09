from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("usage: make_contact_sheet.py output.png input1.png [input2.png ...]")
    out = Path(sys.argv[1])
    paths = [Path(p) for p in sys.argv[2:]]
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((260, 368))
        thumbs.append((path, img.copy()))

    cols = 4
    pad = 18
    label_h = 22
    cell_w = 260 + pad * 2
    cell_h = 368 + label_h + pad * 2
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)

    for idx, (path, img) in enumerate(thumbs):
        r, c = divmod(idx, cols)
        x0, y0 = c * cell_w, r * cell_h
        x = x0 + (cell_w - img.width) // 2
        y = y0 + pad
        sheet.paste(img, (x, y))
        draw.rectangle([x - 1, y - 1, x + img.width, y + img.height], outline=(190, 190, 190))
        label = path.stem
        draw.text((x0 + pad, y0 + pad + 368 + 4), label, fill=(0, 0, 0))

    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
