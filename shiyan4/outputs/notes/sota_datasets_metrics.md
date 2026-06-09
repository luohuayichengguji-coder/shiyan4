# SOTA 方法、数据集与评价指标对比

## SOTA 方法族
| 方向 | 代表方法 | 核心思想 | 适合本课题的价值 | 主要局限 |
|---|---|---|---|---|
| 通用分割基础模型 | SAM / SAM2 | promptable segmentation；SAM2 引入 streaming memory 支持图像/视频。 | 提供可提示的基础 mask 生成器和交互式分割范式。 | 自然图像域；对低质量眼底和微小病灶需领域适配。 |
| 医学 SAM 适配 | MedSAM、Medical SAM Adapter、SAM-Med2D、Medical SAM 2、MedSAM2 | 医学数据微调、adapter/LoRA、prompt 策略、SAM2 医学跟踪化。 | 说明从自然到医学必须注入医学域知识。 | 多为通用医学目标，尚未充分解决 DR 小病灶和低质量问题。 |
| 眼底 DR 病灶分割 | HEDNet+cGAN、RTNet、GlanceSeg、LANet、DeepLabv3+、TP-DRSeg | 边缘/对抗损失、病灶-血管关系、小病灶注意力、gaze/saliency prompt、文本先验。 | 提供 DR 专用结构和类别先验，可与 SAM 结合。 | 标注少、类别极不平衡；有些方法只针对 MA 或不够轻量。 |
| 低质量医学/眼底增强 | SAT-Net、AMIR、DiffCode、TAT、MedSR-Vision | 结构感知增强、任务自适应路由、扩散/VQ 先验、超分与质量评估。 | 可改善模糊、低对比、过曝导致的病灶边界不清。 | 增强指标不一定等同于分割收益；可能改变病灶纹理需联合约束。 |
| SAM 蒸馏/轻量化 | MobileSAM、EfficientSAM、TinySAM、EdgeSAM、SAM-Lightening、KD-SAM | 轻量 encoder、masked image pretraining、prompt-in-loop distillation、Flash Attention、医学蒸馏。 | 降低推理成本，适合筛查/边缘部署。 | 轻量化可能损失微小病灶细节，需要小目标/边界蒸馏约束。 |

## 常用数据集
| 数据集 | 任务属性 | 规模/标注 | 适用性 | 注意事项 |
|---|---|---|---|---|
| IDRiD | DR 分级、病灶分割、视盘/中央凹定位 | 常用描述为 516 张眼底图，包含 MA、HE、EX、SE 像素级标注；训练/测试划分需按官方协议确认。 | 本课题首选分割数据集，覆盖四类典型 DR 病灶。 | 样本量小且类别不平衡，MA/SE 等小目标评估波动大。 |
| DDR | DR 检测、分级与病灶分割 | 公开资料常描述为 13,673 张眼底图，其中部分图像含像素级病灶标注。 | 适合外部验证和跨数据集泛化评估。 | 不同子集标注密度不同，需区分 classification 与 segmentation split。 |
| FGADR | 细粒度 DR 标注 | 常用描述为 1,842 张图像，提供多类别病灶/等级相关标注。 | 适合补充小病灶和细粒度病灶分析。 | 公开可得性和标注类别映射需在实验前核验。 |
| APTOS 2019 | DR 分级/分类 | Kaggle 竞赛数据，常用训练集约 3,662 张图像，标签为 0-4 级。 | 可用于预训练质量/病灶感知分类辅助，不适合作为像素级分割主数据。 | 无官方病灶分割 mask。 |
| EyePACS | DR 分级/筛查 | Kaggle/EyePACS 大规模眼底图像，常用于 DR classification。 | 可用于自监督预训练、质量评估或分类辅助。 | 主要是图像级标签，不是病灶分割数据集。 |
| Messidor / Messidor-2 | DR 分级、筛查评估 | Messidor 常用描述为 1,200 张彩色眼底图；Messidor-2 为更大筛查数据。 | 适合外部筛查/分类验证或图像质量/泛化分析。 | 通常无像素级 DR 病灶 mask，不能直接训练病灶分割。 |

## 常用评价指标
| 指标 | 定义/含义 | 适用场景 | 注意事项 |
|---|---|---|---|
| Dice | 2\|P∩G\|/(\|P\|+\|G\|)，衡量 mask 重叠；医学分割常用。 | 病灶/血管/器官分割 | 小病灶下对少量像素误差极敏感。 |
| IoU/Jaccard | \|P∩G\|/\|P∪G\|，重叠区域占并集比例。 | 通用分割、SAM 评估 | 比 Dice 更严格。 |
| AUC | ROC 曲线下面积，衡量阈值无关分类/检测能力。 | DR 筛查、病灶像素/图像级检测 | 类别极不平衡时应补充 AUPR。 |
| Sensitivity/Recall | TP/(TP+FN)，衡量漏检控制能力。 | 筛查、小病灶召回 | 本课题应优先关注 MA/HE 小病灶召回。 |
| Specificity | TN/(TN+FP)，衡量假阳性控制能力。 | 临床筛查/分类 | 需要与 sensitivity 同时报出。 |
| Precision/F1 | Precision=TP/(TP+FP)，F1=2PR/(P+R)。 | 病灶检测/分割二值化结果 | 病灶很稀疏时 F1/AUPR 比 accuracy 更有意义。 |
| AUPR/AP | Precision-Recall 曲线面积或平均精度。 | 微动脉瘤、出血等稀疏病灶 | 比 AUC 更能反映正类稀少场景。 |
| PSNR/SSIM/LPIPS | 图像增强/超分常用保真、结构相似和感知质量指标。 | 低质量眼底增强 | 需同时报告下游分割指标，避免“增强好看但分割变差”。 |
| FPS/参数量/FLOPs | 推理效率与模型复杂度。 | SAM 蒸馏/部署 | 应在固定输入大小、硬件和 batch 设置下比较。 |
