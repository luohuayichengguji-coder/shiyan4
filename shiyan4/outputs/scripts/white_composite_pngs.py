from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


def main() -> None:
    if len(sys.argv) < 3:
        raise SystemExit("usage: white_composite_pngs.py output_dir input1.png [input2.png ...]")
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    for src_s in sys.argv[2:]:
        src = Path(src_s)
        img = Image.open(src).convert("RGBA")
        white = Image.new("RGBA", img.size, (255, 255, 255, 255))
        white.alpha_composite(img)
        out = out_dir / src.name
        white.convert("RGB").save(out)
    print(len(sys.argv) - 2)


if __name__ == "__main__":
    main()
