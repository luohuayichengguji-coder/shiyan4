from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs"
TABLES = OUT / "tables"
NOTES = OUT / "notes"


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def md_table(rows: list[dict], headers: list[str]) -> str:
    out = []
    out.append("| " + " | ".join(headers) + " |")
    out.append("|" + "|".join(["---"] * len(headers)) + "|")
    for r in rows:
        out.append("| " + " | ".join(str(r[h]).replace("\n", "<br>").replace("|", "\\|") for h in headers) + " |")
    return "\n".join(out)


LOCAL_ANALYSIS = [
    {
        "ID": "P13",
        "论文": "Segment Anything (SAM)",
        "研究问题": "如何构建可提示、可零样本迁移的通用图像分割基础模型。",
        "方法": "图像编码器 + prompt encoder + 轻量 mask decoder；以点、框、mask 等 prompt 训练 promptable segmentation。",
        "数据集/验证": "SA-1B，约 11M 图像、1B masks；COCO/LVIS 等零样本验证。",
        "指标": "IoU、mIoU、zero-shot 下游任务表现。",
        "优势": "统一 prompt 接口和大规模数据引擎，成为医学适配模型的基础。",
        "不足": "自然图像预训练，不含眼底病灶医学先验；对低对比、小病灶、模糊边界不稳定。",
        "可借鉴点": "保持 promptable 框架，将病灶候选框/点、文本或质量先验作为 prompt 融入。"
    },
    {
        "ID": "P09",
        "论文": "MedSAM",
        "研究问题": "如何把 SAM 从自然图像迁移到通用医学图像分割。",
        "方法": "基于大规模医学 image-mask 对微调 SAM，采用框提示完成跨模态医学 ROI 分割。",
        "数据集/验证": "1,570,263 image-mask pairs，10 类模态，86 个内部和 60 个外部验证任务。",
        "指标": "Dice 等医学分割指标。",
        "优势": "证明大规模医学微调能显著缩小自然-医学域差距。",
        "不足": "仍偏通用医学 ROI，未专门针对眼底小病灶、类别极不平衡和低质量图像。",
        "可借鉴点": "作为 baseline 或 teacher，进一步做眼底专用 LoRA/adapter 微调。"
    },
    {
        "ID": "P10",
        "论文": "Medical SAM Adapter (Med-SA)",
        "研究问题": "如何用少量参数把 SAM 注入医学领域知识。",
        "方法": "Space-Depth Transpose + Hyper-Prompting Adapter，更新约 2% 参数。",
        "数据集/验证": "17 个医学分割任务，跨多种图像模态。",
        "指标": "Dice、IoU、MAE 等。",
        "优势": "参数高效，适合标注稀缺和算力受限课程实验。",
        "不足": "不是眼底 DR 病灶专用，未显式建模病灶类别先验与图像质量。",
        "可借鉴点": "在 SAM/MedSAM 的 image encoder 或 mask decoder 中加入眼底专用 adapter。"
    },
    {
        "ID": "P11",
        "论文": "SAM-Med2D",
        "研究问题": "如何系统评估并微调 SAM 于 2D 医学图像。",
        "方法": "收集约 4.6M 图像、19.7M masks；比较点、框、mask prompt 与 encoder/decoder 微调策略。",
        "数据集/验证": "多模态 2D 医学数据，含 fundus 类别；MICCAI 2023 challenge 外部验证。",
        "指标": "Dice 为主。",
        "优势": "给出 prompt 类型、分辨率、微调部位对医学分割的系统证据。",
        "不足": "仍是大而全医学集合，对 DR 病灶类别细粒度和低质量成像适配不足。",
        "可借鉴点": "借鉴多 prompt 训练，组合病灶框/点/粗 mask 与质量标签。"
    },
    {
        "ID": "P23",
        "论文": "RTNet",
        "研究问题": "如何利用 DR 病灶之间及病灶-血管之间的病理关系改进多病灶分割。",
        "方法": "双分支网络；GTB 保留小病灶细节，RTB 用自注意力建模病灶全局依赖、交叉注意力融合血管特征。",
        "数据集/验证": "IDRiD、DDR。",
        "指标": "AUC、AP/precision/recall 等。",
        "优势": "显式利用眼底结构和病灶关系，贴近 DR 病理机制。",
        "不足": "依赖血管伪标签；算力/内存开销和 SAM prompt 接口未统一。",
        "可借鉴点": "把 vessel/lesion relation block 放入 SAM 适配头或边界约束分支。"
    },
    {
        "ID": "P25",
        "论文": "GlanceSeg",
        "研究问题": "如何在少标注条件下利用 SAM 分割微小微动脉瘤。",
        "方法": "眼动 gaze map 粗定位，saliency map 生成 SAM prompt points，领域知识过滤器细化结果。",
        "数据集/验证": "IDRiD 与 Retinal-Lesions。",
        "指标": "AUPR、Precision/Recall 曲线等。",
        "优势": "直接把 SAM、临床交互、微小病灶结合，是本主题最接近的本地论文之一。",
        "不足": "依赖眼动数据或类似粗定位信号；主要聚焦 MA，不覆盖多病灶全类别。",
        "可借鉴点": "用自动病灶候选热图/文本先验替代眼动作为 prompt 生成器。"
    },
    {
        "ID": "P28",
        "论文": "SAT-Net",
        "研究问题": "如何增强低质量眼底图像并保留血管/毛细结构。",
        "方法": "Transformer attention fusion、cross-quality knowledge distillation、structure-aware multi-scale loss。",
        "数据集/验证": "合成与真实低质量 fundus 数据；还验证血管分割、视盘/视杯检测下游收益。",
        "指标": "图像增强指标和下游任务指标。",
        "优势": "把结构保持和轻量学生网络结合，正好对应低质量眼底成像问题。",
        "不足": "主要目标是增强，不直接优化 DR 小病灶分割；极低分辨率/过曝仍困难。",
        "可借鉴点": "作为前端质量感知增强模块，并让增强损失与分割损失联合训练。"
    },
    {
        "ID": "P06",
        "论文": "KD-SAM",
        "研究问题": "如何降低 SAM 在医学图像分割中的计算成本。",
        "方法": "对 encoder 和 decoder 同时蒸馏，使用 MSE + perceptual loss 保持结构和语义特征。",
        "数据集/验证": "Kvasir-SEG、ISIC 2017、Fetal Head Ultrasound、Breast Ultrasound。",
        "指标": "Dice、参数量/复杂度等。",
        "优势": "医学场景轻量化方向明确，可降低部署门槛。",
        "不足": "未在眼底 DR 病灶上验证；小病灶、低质量场景下蒸馏可能丢失细节。",
        "可借鉴点": "教师模型用眼底专用 SAM，学生模型用 MobileSAM/EdgeSAM，加入边界/小目标蒸馏。"
    },
    {
        "ID": "P01",
        "论文": "EdgeSAM",
        "研究问题": "如何在边缘设备上保持 SAM 交互分割能力。",
        "方法": "CNN student，prompt-in-the-loop distillation，把 prompt encoder/mask decoder 纳入蒸馏。",
        "数据集/验证": "COCO、LVIS、SA-1B 相关训练/验证。",
        "指标": "mIoU、FPS、FLOPs 等。",
        "优势": "强调 prompt 与 mask 生成动态关系，比单纯 encoder 蒸馏更适合交互式分割。",
        "不足": "自然图像蒸馏，非医学；未关注眼底小病灶。",
        "可借鉴点": "用于眼底模型轻量化：让学生学习质量增强后图像、prompt 和高质量 mask 的联合行为。"
    },
]


EXTERNAL_SEARCH = [
    {
        "检索日期": "2026-05-29",
        "检索式": "Segment Anything Model medical image segmentation 2025 MedSAM2 SAM-Med2D",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "MedSAM2: Segment Anything in 3D Medical Images and Videos",
        "年份": "2025",
        "标识/链接": "arXiv:2504.03600",
        "筛选理由": "SAM2 到 3D/视频医学分割的最新医学适配，说明 promptable 医学基础模型仍在向更大数据和人机协同扩展。",
        "用于报告位置": "研究现状、未来趋势"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "Medical SAM 2 Segment medical images as video via Segment Anything Model 2",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "Medical SAM 2: Segment medical images as video via Segment Anything Model 2",
        "年份": "2024",
        "标识/链接": "arXiv:2408.00874",
        "筛选理由": "把 2D/3D 医学图像当作视频跟踪问题处理，启发连续眼底随访或多图一 prompt 策略。",
        "用于报告位置": "SAM2 医学适配"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "TP-DRSeg explicit text prompt diabetic retinopathy lesion segmentation SAM",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "TP-DRSeg: Improving Diabetic Retinopathy Lesion Segmentation with Explicit Text-Prompts Assisted SAM",
        "年份": "2024",
        "标识/链接": "arXiv:2406.15764",
        "筛选理由": "最贴近本课题：显式文本/医学概念提示辅助 SAM 做 DR 病灶分割，可作为方案中文本先验模块依据。",
        "用于报告位置": "SOTA、方案设计"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "Generalist Models in Medical Image Segmentation survey 2025 SAM",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "Generalist Models in Medical Image Segmentation: A Survey and Performance Comparison with Task-Specific Approaches",
        "年份": "2025",
        "标识/链接": "arXiv:2506.10825",
        "筛选理由": "2025 综述，覆盖 SAM、SAM2、adapter、fine-tuning、zero/few-shot 与任务专用模型对比。",
        "用于报告位置": "国内外研究现状、挑战"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "knowledge distillation SAM medical image segmentation 2025",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "Efficient Knowledge Distillation of SAM for Medical Image Segmentation",
        "年份": "2025",
        "标识/链接": "arXiv:2501.16740",
        "筛选理由": "医学 SAM 蒸馏，支持研究方案中的轻量化/部署模块。",
        "用于报告位置": "轻量化蒸馏、实验规划"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "low quality retinal fundus image enhancement 2025 transformer SAT-Net",
        "来源": "CrossRef via nature-academic-search get_paper_by_id",
        "文献": "SAT-Net: Structure-Aware Transformer-Based Attention Fusion Network for Low-Quality Retinal Fundus Images Enhancement",
        "年份": "2025",
        "标识/链接": "DOI:10.1109/TMM.2025.3565935",
        "筛选理由": "低质量眼底增强与结构保持，正对任务指导文件建议问题 b。",
        "用于报告位置": "低质量图像问题、增强模块"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "All-In-One Medical Image Restoration task-adaptive routing 2024",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "All-In-One Medical Image Restoration via Task-Adaptive Routing",
        "年份": "2024",
        "标识/链接": "arXiv:2405.19769",
        "筛选理由": "多退化医学图像统一恢复，启发低质量类型识别和 task routing。",
        "用于报告位置": "医学图像增强现状"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "All-in-One Medical Image Restoration diffusion codebook 2025",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "DiffCode: All-in-One Medical Image Restoration with Latent Diffusion-Enhanced VQ Codebook Prior",
        "年份": "2025",
        "标识/链接": "arXiv:2507.19874",
        "筛选理由": "任务自适应高质量先验和 diffusion retrieval 可作为低质量增强替代路线。",
        "用于报告位置": "备选方案"
    },
    {
        "检索日期": "2026-05-29",
        "检索式": "MedSAM3 Segment Anything with medical concepts 2025",
        "来源": "arXiv via nature-academic-search get_paper_by_id",
        "文献": "MedSAM3: Delving into Segment Anything with Medical Concepts",
        "年份": "2025",
        "标识/链接": "arXiv:2511.19046",
        "筛选理由": "医学概念/文本提示是 SAM 适配新趋势；因日期晚于当前日期，报告中标注为未来待跟踪预印本，不作为已发表结论。",
        "用于报告位置": "趋势与不确定项"
    },
]


SOTA_ROWS = [
    {
        "方向": "通用分割基础模型",
        "代表方法": "SAM / SAM2",
        "核心思想": "promptable segmentation；SAM2 引入 streaming memory 支持图像/视频。",
        "适合本课题的价值": "提供可提示的基础 mask 生成器和交互式分割范式。",
        "主要局限": "自然图像域；对低质量眼底和微小病灶需领域适配。"
    },
    {
        "方向": "医学 SAM 适配",
        "代表方法": "MedSAM、Medical SAM Adapter、SAM-Med2D、Medical SAM 2、MedSAM2",
        "核心思想": "医学数据微调、adapter/LoRA、prompt 策略、SAM2 医学跟踪化。",
        "适合本课题的价值": "说明从自然到医学必须注入医学域知识。",
        "主要局限": "多为通用医学目标，尚未充分解决 DR 小病灶和低质量问题。"
    },
    {
        "方向": "眼底 DR 病灶分割",
        "代表方法": "HEDNet+cGAN、RTNet、GlanceSeg、LANet、DeepLabv3+、TP-DRSeg",
        "核心思想": "边缘/对抗损失、病灶-血管关系、小病灶注意力、gaze/saliency prompt、文本先验。",
        "适合本课题的价值": "提供 DR 专用结构和类别先验，可与 SAM 结合。",
        "主要局限": "标注少、类别极不平衡；有些方法只针对 MA 或不够轻量。"
    },
    {
        "方向": "低质量医学/眼底增强",
        "代表方法": "SAT-Net、AMIR、DiffCode、TAT、MedSR-Vision",
        "核心思想": "结构感知增强、任务自适应路由、扩散/VQ 先验、超分与质量评估。",
        "适合本课题的价值": "可改善模糊、低对比、过曝导致的病灶边界不清。",
        "主要局限": "增强指标不一定等同于分割收益；可能改变病灶纹理需联合约束。"
    },
    {
        "方向": "SAM 蒸馏/轻量化",
        "代表方法": "MobileSAM、EfficientSAM、TinySAM、EdgeSAM、SAM-Lightening、KD-SAM",
        "核心思想": "轻量 encoder、masked image pretraining、prompt-in-loop distillation、Flash Attention、医学蒸馏。",
        "适合本课题的价值": "降低推理成本，适合筛查/边缘部署。",
        "主要局限": "轻量化可能损失微小病灶细节，需要小目标/边界蒸馏约束。"
    },
]


DATASETS = [
    {
        "数据集": "IDRiD",
        "任务属性": "DR 分级、病灶分割、视盘/中央凹定位",
        "规模/标注": "常用描述为 516 张眼底图，包含 MA、HE、EX、SE 像素级标注；训练/测试划分需按官方协议确认。",
        "适用性": "本课题首选分割数据集，覆盖四类典型 DR 病灶。",
        "注意事项": "样本量小且类别不平衡，MA/SE 等小目标评估波动大。"
    },
    {
        "数据集": "DDR",
        "任务属性": "DR 检测、分级与病灶分割",
        "规模/标注": "公开资料常描述为 13,673 张眼底图，其中部分图像含像素级病灶标注。",
        "适用性": "适合外部验证和跨数据集泛化评估。",
        "注意事项": "不同子集标注密度不同，需区分 classification 与 segmentation split。"
    },
    {
        "数据集": "FGADR",
        "任务属性": "细粒度 DR 标注",
        "规模/标注": "常用描述为 1,842 张图像，提供多类别病灶/等级相关标注。",
        "适用性": "适合补充小病灶和细粒度病灶分析。",
        "注意事项": "公开可得性和标注类别映射需在实验前核验。"
    },
    {
        "数据集": "APTOS 2019",
        "任务属性": "DR 分级/分类",
        "规模/标注": "Kaggle 竞赛数据，常用训练集约 3,662 张图像，标签为 0-4 级。",
        "适用性": "可用于预训练质量/病灶感知分类辅助，不适合作为像素级分割主数据。",
        "注意事项": "无官方病灶分割 mask。"
    },
    {
        "数据集": "EyePACS",
        "任务属性": "DR 分级/筛查",
        "规模/标注": "Kaggle/EyePACS 大规模眼底图像，常用于 DR classification。",
        "适用性": "可用于自监督预训练、质量评估或分类辅助。",
        "注意事项": "主要是图像级标签，不是病灶分割数据集。"
    },
    {
        "数据集": "Messidor / Messidor-2",
        "任务属性": "DR 分级、筛查评估",
        "规模/标注": "Messidor 常用描述为 1,200 张彩色眼底图；Messidor-2 为更大筛查数据。",
        "适用性": "适合外部筛查/分类验证或图像质量/泛化分析。",
        "注意事项": "通常无像素级 DR 病灶 mask，不能直接训练病灶分割。"
    },
]


METRICS = [
    {"指标": "Dice", "定义/含义": "2|P∩G|/(|P|+|G|)，衡量 mask 重叠；医学分割常用。", "适用场景": "病灶/血管/器官分割", "注意事项": "小病灶下对少量像素误差极敏感。"},
    {"指标": "IoU/Jaccard", "定义/含义": "|P∩G|/|P∪G|，重叠区域占并集比例。", "适用场景": "通用分割、SAM 评估", "注意事项": "比 Dice 更严格。"},
    {"指标": "AUC", "定义/含义": "ROC 曲线下面积，衡量阈值无关分类/检测能力。", "适用场景": "DR 筛查、病灶像素/图像级检测", "注意事项": "类别极不平衡时应补充 AUPR。"},
    {"指标": "Sensitivity/Recall", "定义/含义": "TP/(TP+FN)，衡量漏检控制能力。", "适用场景": "筛查、小病灶召回", "注意事项": "本课题应优先关注 MA/HE 小病灶召回。"},
    {"指标": "Specificity", "定义/含义": "TN/(TN+FP)，衡量假阳性控制能力。", "适用场景": "临床筛查/分类", "注意事项": "需要与 sensitivity 同时报出。"},
    {"指标": "Precision/F1", "定义/含义": "Precision=TP/(TP+FP)，F1=2PR/(P+R)。", "适用场景": "病灶检测/分割二值化结果", "注意事项": "病灶很稀疏时 F1/AUPR 比 accuracy 更有意义。"},
    {"指标": "AUPR/AP", "定义/含义": "Precision-Recall 曲线面积或平均精度。", "适用场景": "微动脉瘤、出血等稀疏病灶", "注意事项": "比 AUC 更能反映正类稀少场景。"},
    {"指标": "PSNR/SSIM/LPIPS", "定义/含义": "图像增强/超分常用保真、结构相似和感知质量指标。", "适用场景": "低质量眼底增强", "注意事项": "需同时报告下游分割指标，避免“增强好看但分割变差”。"},
    {"指标": "FPS/参数量/FLOPs", "定义/含义": "推理效率与模型复杂度。", "适用场景": "SAM 蒸馏/部署", "注意事项": "应在固定输入大小、硬件和 batch 设置下比较。"},
]


def main() -> None:
    write_csv(TABLES / "key_paper_analysis.csv", LOCAL_ANALYSIS)
    write_csv(TABLES / "literature_search_record.csv", EXTERNAL_SEARCH)
    write_csv(TABLES / "sota_method_comparison.csv", SOTA_ROWS)
    write_csv(TABLES / "dataset_comparison.csv", DATASETS)
    write_csv(TABLES / "metrics_comparison.csv", METRICS)

    md = [
        "# 重点论文人工分析表",
        "",
        md_table(LOCAL_ANALYSIS, list(LOCAL_ANALYSIS[0].keys())),
        "",
    ]
    (NOTES / "key_paper_analysis.md").write_text("\n".join(md), encoding="utf-8")

    md = [
        "# 阶段4 在线文献检索记录",
        "",
        "说明：检索日期为 2026-05-29。优先使用 nature-academic-search 的 `get_paper_by_id` 对 arXiv/DOI 进行核验；批量 `search_papers` 在本会话中返回 `asyncio.run() cannot be called from a running event loop`，因此采用网页检索线索 + 单篇标识核验的降级流程，并在本记录中保留检索式和筛选理由。",
        "",
        md_table(EXTERNAL_SEARCH, list(EXTERNAL_SEARCH[0].keys())),
        "",
    ]
    (NOTES / "literature_search_record.md").write_text("\n".join(md), encoding="utf-8")

    md = [
        "# SOTA 方法、数据集与评价指标对比",
        "",
        "## SOTA 方法族",
        md_table(SOTA_ROWS, list(SOTA_ROWS[0].keys())),
        "",
        "## 常用数据集",
        md_table(DATASETS, list(DATASETS[0].keys())),
        "",
        "## 常用评价指标",
        md_table(METRICS, list(METRICS[0].keys())),
        "",
    ]
    (NOTES / "sota_datasets_metrics.md").write_text("\n".join(md), encoding="utf-8")
    print("Research artifact tables written.")


if __name__ == "__main__":
    main()
