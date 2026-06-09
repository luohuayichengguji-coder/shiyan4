# 阶段6-7：研究不足分析与可执行研究方案

## 一、研究不足

### 1. SAM 从通用图像迁移到眼底 DR 病灶分割时领域适配不足

SAM 的核心优势是 promptable segmentation 和零样本迁移，但其训练源主要是自然图像。眼底 DR 病灶具有典型医学图像特征：低对比、病灶尺度小、边界模糊、类别间视觉差异细微、背景结构复杂。Medical SAM Adapter、MedSAM、SAM-Med2D 等本地论文和核验文献均指出，直接使用 SAM 做医学图像分割会受自然-医学域差距影响。TP-DRSeg 进一步说明，DR 病灶分割不仅需要空间提示，还需要病灶类别和医学概念先验。

具体表现：

- 微动脉瘤与小出血点在颜色、形状和尺度上接近，SAM 单靠点/框 prompt 容易产生错误粒度。
- 硬性渗出与反光、视盘边缘、低质量背景可能混淆。
- 通用 SAM 的 mask 质量不一定覆盖医学边界需求，HQ-SAM 类思路虽改善细节，但仍非眼底专用。
- 大规模通用医学微调能提升总体 Dice，却不一定最优处理 DR 小病灶。

### 2. 低质量眼底图像导致微小病灶、边界和细长结构分割不稳定

任务指导文件建议关注“待分割图像质量较低”。本地 SAT-Net、医学图像增强综述和 MedSR-Vision 等文献显示，真实临床眼底图像可能存在低对比、模糊、过曝、照明不均、低分辨率和伪影。低质量图像对 DR 分割的影响比普通分类更严重，因为分割需要像素级边界。

具体表现：

- 微动脉瘤只有少量像素，轻微模糊即可导致漏检。
- 出血和血管末梢、暗背景之间边界不清。
- 低质量增强若只优化 PSNR/SSIM，可能“抹平”病灶纹理或引入伪病灶。
- 血管、视盘、病灶之间存在结构关系，增强模块若破坏血管拓扑会影响后续分割。

### 3. 标注稀缺、类别不平衡、小病灶漏检与推理成本高

IDRiD、DDR、FGADR 等像素级 DR 分割数据集规模远小于自然图像分割数据。四类病灶面积占比差异明显，微动脉瘤和软性渗出通常更稀疏。SAM/MedSAM 这类模型又带来较高显存和推理成本，直接用于基层筛查或边缘设备部署不现实。

具体表现：

- 数据集小，模型容易过拟合具体成像设备和标注风格。
- 背景像素占绝大多数，普通交叉熵会偏向背景。
- 小病灶漏检在 Dice/IoU 上可能被整体指标掩盖，因此需要 AUPR、Sensitivity、lesion-level F1 等补充。
- 医学 SAM 模型若每张图需人工框/点 prompt，会增加临床流程负担。

## 二、拟提出研究方案

### 方案名称

LQ-Fundus-SAM：低质量感知增强 + 眼底专用 SAM 适配 + 小病灶/边界约束 + 轻量化蒸馏的 DR 病灶分割方案

### 核心目标

在 IDRiD、DDR 等眼底 DR 病灶分割数据集上，构建一个既能处理低质量眼底图像，又能利用 SAM/MedSAM 泛化能力的多病灶分割框架，重点提升 MA/HE 等小病灶召回、边界质量和跨数据集泛化，同时降低推理成本。

### Baseline

建议设置三类 baseline：

1. 传统专用分割模型：U-Net、DeepLabv3+、HEDNet+cGAN、RTNet。
2. 基础模型适配：SAM zero-shot、MedSAM、SAM-Med2D 或 Medical SAM Adapter。
3. DR-SAM 近邻方法：GlanceSeg、TP-DRSeg 思路的可复现实验或概念对比。

课程实验可优先选择 DeepLabv3+ + MedSAM/Medical SAM Adapter 作为可复现 baseline；若算力有限，使用冻结 SAM/MedSAM + 轻量 adapter。

### 模块设计

| 模块 | 设计 | 解决问题 |
|---|---|---|
| 质量感知增强模块 QEM | 输入眼底图先估计质量/退化类型，再用轻量结构感知增强网络恢复对比度、边界和血管细节；借鉴 SAT-Net 的 attention fusion、cross-quality distillation 和 structure-aware loss | 低质量图像、小病灶不可见、边界模糊 |
| 眼底专用 SAM 适配模块 FSA | 冻结 SAM/MedSAM 主干，在 image encoder 中插入 LoRA/adapter，在 mask decoder 中加入 lesion-aware token 或 prompt-conditioned adapter | 通用 SAM 缺少眼底/病灶先验 |
| 医学先验 prompt 模块 MPP | 自动生成病灶候选点/框：由低分辨率病灶热图、血管/视盘结构先验和文本类别提示共同产生；参考 GlanceSeg 和 TP-DRSeg | 人工 prompt 成本高、类别细粒度差异小 |
| 小病灶/边界约束模块 SBC | 使用 Dice + Focal/Tversky + Boundary/Hausdorff + 小目标重加权；为 MA/HE 设计 lesion-level recall loss 或 hard example mining | 类别不平衡、漏检、边界不稳定 |
| 轻量化蒸馏模块 LSD | 教师为 LQ-Fundus-SAM 大模型，学生为 MobileSAM/EdgeSAM/KD-SAM 风格轻量模型；蒸馏 image embedding、prompt-conditioned mask、边界特征和小病灶响应图 | 推理成本高、部署困难 |

### 训练流程

1. 数据准备：IDRiD 为主训练集，DDR/FGADR 作扩展或外部验证；统一病灶类别映射为 MA、HE、EX、SE。
2. 预处理：眼底圆形视野裁剪、黑边去除、尺寸归一化、颜色标准化；保留原图与增强图双分支。
3. 质量感知增强预训练：用合成退化或真实低质量/高质量对训练 QEM，损失包括 L1/SSIM/感知损失和结构边缘损失。
4. SAM 适配训练：冻结主干大部分参数，只训练 adapter/LoRA、病灶 token、prompt 生成器和 mask head。
5. 联合微调：以分割指标为主目标，增强模块不只追求视觉质量，而要通过分割损失约束病灶保真。
6. 蒸馏训练：用大模型教师生成软 mask、边界响应、embedding，训练轻量学生模型。

### 损失函数

总损失可写为：

`L = L_seg + λ1 L_boundary + λ2 L_small + λ3 L_quality + λ4 L_distill`

其中：

- `L_seg`：Dice loss + Focal loss 或 Tversky loss，缓解前景稀疏。
- `L_boundary`：Boundary loss / Hausdorff loss / edge Dice，约束边界。
- `L_small`：小病灶重加权、lesion-level recall 或 hard pixel mining。
- `L_quality`：增强模块 L1 + SSIM + structure-aware loss，保留血管和病灶纹理。
- `L_distill`：MSE embedding 蒸馏 + perceptual loss + mask KL/Dice 蒸馏。

### 消融实验

| 实验编号 | 设置 | 验证问题 |
|---|---|---|
| A0 | DeepLabv3+ 或 U-Net baseline | 基础专用模型性能 |
| A1 | SAM/MedSAM zero-shot 或冻结主干 + 线性头 | 基础模型直接迁移效果 |
| A2 | A1 + 眼底 adapter/LoRA | 领域适配是否有效 |
| A3 | A2 + 医学先验 prompt | 文本/候选点/框 prompt 是否提升类别识别 |
| A4 | A3 + 质量感知增强 | 低质量图像处理是否提升分割 |
| A5 | A4 + 小病灶/边界损失 | MA/HE recall 和边界质量是否提升 |
| A6 | A5 蒸馏为轻量学生 | 性能-效率权衡 |
| A7 | 去除血管/视盘结构先验 | 结构先验对误检/漏检的影响 |

### 预期创新点

1. 从“通用医学 SAM”进一步细化到“眼底 DR 病灶 SAM”，把病灶类别、血管结构和低质量成像共同建模。
2. 增强模块以分割收益为目标，避免单纯追求视觉增强指标。
3. 利用显式医学概念/文本 prompt 与自动候选 prompt，降低人工交互成本。
4. 针对小病灶设计边界和召回约束，弥补普通 Dice/IoU 的不足。
5. 通过 prompt-aware/medical-aware 蒸馏降低推理成本，面向基层筛查部署。

### 不确定性说明

本方案为技术调研后的实验蓝图，尚未实际训练模型。报告中不编造实验结果，所有“预期提升”仅作为假设，需要后续实验验证。
