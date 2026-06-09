from __future__ import annotations

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
FIG = ROOT / "outputs" / "figures"

W, H = 2200, 1240
FONT_PATHS = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    # PingFang TTC provides clean Chinese rendering on macOS. The index is
    # stable enough for this local report workflow; fall back gracefully.
    for p in FONT_PATHS:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size=size, index=1 if bold else 0)
            except TypeError:
                return ImageFont.truetype(p, size=size)
    return ImageFont.load_default(size=size)


F_TITLE = font(56, True)
F_SUB = font(30)
F_BOX = font(28, True)
F_SMALL = font(23)
F_TINY = font(21)
F_CAPTION = font(22)

INK = "#1F2937"
MUTED = "#475569"
LINE = "#334155"
BLUE = "#2563EB"
COLORS = {
    "gray": ("#F8FAFC", "#94A3B8"),
    "blue": ("#EAF2FF", "#3B82F6"),
    "teal": ("#E6FFFB", "#14B8A6"),
    "green": ("#ECFDF3", "#22C55E"),
    "amber": ("#FFF7D6", "#F59E0B"),
    "red": ("#FFF1F2", "#EF4444"),
    "purple": ("#F2EEFF", "#8B5CF6"),
    "white": ("#FFFFFF", "#CBD5E1"),
}


def new_canvas(title: str, subtitle: str | None = None) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    d.text((70, 54), title, fill=INK, font=F_TITLE)
    if subtitle:
        d.text((72, 128), subtitle, fill=MUTED, font=F_SUB)
    return img, d


def text_size(d: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = d.multiline_textbbox((0, 0), text, font=fnt, spacing=8, align="center")
    return box[2] - box[0], box[3] - box[1]


def wrap_cn(text: str, max_chars: int) -> str:
    parts = []
    for raw in text.split("\n"):
        if len(raw) <= max_chars:
            parts.append(raw)
        else:
            parts.extend(textwrap.wrap(raw, width=max_chars, break_long_words=True, replace_whitespace=False))
    return "\n".join(parts)


def rounded_box(
    d: ImageDraw.ImageDraw,
    rect: tuple[int, int, int, int],
    text: str,
    scheme: str = "gray",
    fnt: ImageFont.FreeTypeFont = F_BOX,
    max_chars: int = 12,
    radius: int = 32,
    width: int = 4,
) -> None:
    fill, outline = COLORS[scheme]
    d.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=width)
    t = wrap_cn(text, max_chars)
    tw, th = text_size(d, t, fnt)
    x1, y1, x2, y2 = rect
    d.multiline_text(
        ((x1 + x2 - tw) / 2, (y1 + y2 - th) / 2 - 4),
        t,
        fill=INK,
        font=fnt,
        spacing=8,
        align="center",
    )


def line_arrow(
    d: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str = LINE,
    width: int = 7,
) -> None:
    d.line([start, end], fill=color, width=width)
    # Arrow head.
    sx, sy = start
    ex, ey = end
    dx, dy = ex - sx, ey - sy
    if abs(dx) >= abs(dy):
        if dx >= 0:
            pts = [(ex, ey), (ex - 26, ey - 16), (ex - 26, ey + 16)]
        else:
            pts = [(ex, ey), (ex + 26, ey - 16), (ex + 26, ey + 16)]
    else:
        if dy >= 0:
            pts = [(ex, ey), (ex - 16, ey - 26), (ex + 16, ey - 26)]
        else:
            pts = [(ex, ey), (ex - 16, ey + 26), (ex + 16, ey + 26)]
    d.polygon(pts, fill=color)


def save(img: Image.Image, name: str) -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    img.save(FIG / f"{name}.png", dpi=(300, 300))
    # Word can consume PNG reliably; PDF is generated as a convenience copy.
    img.save(FIG / f"{name}.pdf", "PDF", resolution=300)


def make_roadmap() -> None:
    img, d = new_canvas(
        "LQ-Fundus-SAM 技术路线",
        "低质量增强、眼底专用适配、小病灶约束与轻量化蒸馏的组合方案",
    )
    y = 310
    boxes = [
        (70, y, 370, y + 150, "低质量眼底图\nIDRiD / DDR / FGADR", "gray"),
        (450, y, 750, y + 150, "质量感知增强\nQEM", "teal"),
        (830, y, 1130, y + 150, "眼底专用 SAM\nAdapter / LoRA", "blue"),
        (1210, y, 1510, y + 150, "医学先验 Prompt\n点 / 框 / 文本", "purple"),
        (1590, y, 1890, y + 150, "多病灶 Mask\nMA / HE / EX / SE", "green"),
    ]
    for x1, y1, x2, y2, txt, c in boxes:
        rounded_box(d, (x1, y1, x2, y2), txt, c, max_chars=13)
    for i in range(len(boxes) - 1):
        line_arrow(d, (boxes[i][2] + 14, y + 75), (boxes[i + 1][0] - 14, y + 75))

    aux_y = 610
    aux = [
        (430, aux_y, 780, aux_y + 135, "结构保持损失\nSSIM / Edge / Quality", "amber"),
        (925, aux_y, 1275, aux_y + 135, "小病灶边界约束\nDice + Focal + Boundary", "red"),
        (1430, aux_y, 1780, aux_y + 135, "轻量化蒸馏\nMobileSAM / EdgeSAM", "gray"),
    ]
    for x1, y1, x2, y2, txt, c in aux:
        rounded_box(d, (x1, y1, x2, y2), txt, c, F_SMALL, max_chars=17)
    line_arrow(d, (605, aux_y), (605, y + 162), "#B45309")
    line_arrow(d, (1100, aux_y), (980, y + 162), "#B91C1C")
    line_arrow(d, (1605, aux_y), (1740, y + 162), "#64748B")

    d.text((80, 870), "输出评价", fill=INK, font=F_SUB)
    metrics = ["per-class Dice / IoU", "AUPR & Sensitivity", "Boundary F1", "PSNR / SSIM / LPIPS", "FPS / Params / FLOPs"]
    for i, m in enumerate(metrics):
        x = 70 + i * 392
        rounded_box(d, (x, 950, x + 335, 1048), m, "white", F_TINY, max_chars=23, radius=24, width=3)
    save(img, "technical_roadmap")


def make_sota_map() -> None:
    img, d = new_canvas("SOTA 方法族地图", "五类方法围绕眼底 DR 病灶分割形成可组合证据链")
    center = (830, 520, 1370, 680)
    rounded_box(d, center, "眼底 DR 病灶分割\nSAM 适配研究", "white", F_BOX, max_chars=14, width=6)

    nodes = [
        (110, 300, 570, 455, "通用 SAM\nSAM / SAM2 / HQ-SAM", "blue"),
        (870, 230, 1330, 385, "医学 SAM\nMedSAM / SAM-Med2D\nMedical SAM 2", "teal"),
        (1630, 300, 2090, 455, "眼底病灶分割\nRTNet / GlanceSeg\nTP-DRSeg", "green"),
        (270, 810, 730, 965, "低质量增强\nSAT-Net / AMIR\nDiffCode / TAT", "amber"),
        (1470, 790, 1930, 985, "SAM 蒸馏\nMobileSAM / EdgeSAM\nKD-SAM", "purple"),
    ]
    for rect in nodes:
        rounded_box(d, rect[:4], rect[4], rect[5], F_BOX, max_chars=16)

    # Orthogonal connectors stop at the center box edge, leaving the text area clear.
    line_arrow(d, (570, 378), (830, 560), "#64748B")
    line_arrow(d, (1100, 385), (1100, 520), "#64748B")
    line_arrow(d, (1630, 378), (1370, 560), "#64748B")
    line_arrow(d, (730, 888), (830, 640), "#64748B")
    line_arrow(d, (1470, 888), (1370, 640), "#64748B")
    save(img, "sota_method_map")


def make_problem_solution() -> None:
    img, d = new_canvas("研究不足与方案模块映射", "左侧是问题，右侧是对应模块；箭头只表示一一映射关系")
    problems = [
        ((90, 260, 760, 400), "领域适配不足\n自然图像先验\n难识别眼底微小病灶", "red"),
        ((90, 500, 760, 640), "低质量图像\n低对比 / 模糊 / 过曝\n破坏边界和细长结构", "amber"),
        ((90, 740, 760, 880), "数据与效率瓶颈\n标注稀缺 / 类别不平衡\n推理成本较高", "gray"),
    ]
    solutions = [
        ((1240, 260, 2050, 400), "眼底专用 SAM 适配\nAdapter / LoRA + lesion-aware token\n融合血管 / 视盘 / 病灶先验", "blue"),
        ((1240, 500, 2050, 640), "质量感知增强\n退化识别 + 结构保持增强\n增强目标受分割损失约束", "teal"),
        ((1240, 740, 2050, 890), "小病灶约束与蒸馏\nFocal / Tversky / Boundary\n医学 prompt 蒸馏", "green"),
    ]
    for rect, txt, c in problems + solutions:
        rounded_box(d, rect, txt, c, F_SMALL, max_chars=20)
    for (p_rect, _, _), (s_rect, _, _) in zip(problems, solutions):
        line_arrow(d, (p_rect[2] + 25, (p_rect[1] + p_rect[3]) // 2), (s_rect[0] - 25, (s_rect[1] + s_rect[3]) // 2), BLUE)

    rounded_box(d, (780, 970, 1420, 1090), "联合目标：病灶保真 + 边界稳定 + 可部署", "white", F_SMALL, max_chars=24, width=5)
    # Short vertical summary arrows avoid the right-side text blocks.
    line_arrow(d, (1100, 900), (1100, 970), "#64748B")
    save(img, "problem_solution_map")


def make_dataset_metric_matrix() -> None:
    img, d = new_canvas("数据集与指标选择逻辑", "先区分数据集任务属性，再选择能反映分割质量和部署效率的指标")
    left = [
        ((120, 250, 720, 390), "IDRiD\n主分割训练\n四类病灶 mask", "green"),
        ((120, 430, 720, 540), "DDR / FGADR\n外部验证\n泛化与细粒度补充", "teal"),
        ((120, 590, 720, 700), "APTOS / EyePACS\n图像级标签\n预训练 / 质量辅助", "blue"),
        ((120, 750, 720, 860), "Messidor\n筛查 / 分类泛化\n非主分割数据", "gray"),
    ]
    for rect, txt, c in left:
        rounded_box(d, rect, txt, c, F_SMALL, max_chars=18)

    center = (860, 470, 1340, 660)
    rounded_box(d, center, "训练 / 验证目标\n不能只看 accuracy\n必须分病灶类别报告", "white", F_BOX, max_chars=16, width=5)
    line_arrow(d, (740, 560), (860, 560), BLUE)

    right = [
        ((1500, 230, 2070, 330), "分割重叠：Dice / IoU", "white"),
        ((1500, 370, 2070, 470), "小病灶检出：AUPR / Sensitivity / F1", "white"),
        ((1500, 510, 2070, 610), "边界质量：Boundary F1 / Hausdorff", "white"),
        ((1500, 650, 2070, 750), "增强质量：PSNR / SSIM / LPIPS", "white"),
        ((1500, 790, 2070, 890), "部署效率：FPS / Params / FLOPs", "white"),
    ]
    for rect, txt, c in right:
        rounded_box(d, rect, txt, c, F_TINY, max_chars=30, radius=22, width=4)
    line_arrow(d, (1340, 560), (1500, 560), BLUE)
    save(img, "dataset_metric_matrix")


def make_experiment_flow() -> None:
    img, d = new_canvas("实验规划流程", "从数据准备到评价消融，主流程与检查项分开显示")
    steps = [
        (90, "数据准备\nIDRiD 主实验\nDDR / FGADR 外部验证", "gray"),
        (485, "预处理 / 增强\n裁剪黑边、CLAHE\n低质量模拟", "teal"),
        (880, "Baseline\nU-Net / DeepLabv3+\nSAM / MedSAM", "blue"),
        (1275, "拟提出模型\nLQ-Fundus-SAM\n四类病灶分割", "purple"),
        (1670, "评价与消融\nDice / IoU / AUPR\nFPS / 参数量 / 可视化", "green"),
    ]
    y1, y2 = 310, 470
    for x, txt, c in steps:
        rounded_box(d, (x, y1, x + 315, y2), txt, c, F_SMALL, max_chars=17)
    for i in range(len(steps) - 1):
        x = steps[i][0] + 315
        nx = steps[i + 1][0]
        line_arrow(d, (x + 15, 390), (nx - 15, 390))

    rows = [
        ("对比方法", "DeepLabv3+、RTNet、MedSAM、SAM-Med2D、TP-DRSeg 思路"),
        ("消融设置", "去 QEM、去 adapter、去文本 prompt、去边界损失、去蒸馏"),
        ("风险控制", "小样本过拟合、增强伪影、显存不足、标注类别映射不一致"),
    ]
    y = 705
    for label, val in rows:
        rounded_box(d, (230, y, 610, y + 95), label, "white", F_SMALL, max_chars=8, radius=20, width=3)
        rounded_box(d, (620, y, 1970, y + 95), val, "white", F_SMALL, max_chars=38, radius=20, width=3)
        y += 140
    save(img, "experiment_flow")


def main() -> None:
    make_roadmap()
    make_sota_map()
    make_problem_solution()
    make_dataset_metric_matrix()
    make_experiment_flow()
    print(f"Figures written to {FIG}")


if __name__ == "__main__":
    main()
