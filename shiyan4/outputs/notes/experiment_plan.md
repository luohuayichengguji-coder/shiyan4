# 阶段8：实验规划

## 1. 实验目标

验证“低质量感知增强 + 眼底专用 SAM 适配 + 小病灶/边界约束 + 轻量化蒸馏”是否能够提升眼底糖尿病视网膜病变病灶分割效果，特别关注微动脉瘤、出血等小病灶的召回率和边界稳定性。

## 2. 数据集选择

| 数据集 | 用途 | 说明 |
|---|---|---|
| IDRiD | 主训练/验证/测试 | 包含 MA、HE、EX、SE 像素级标注，适合多病灶分割主实验 |
| DDR | 外部验证或联合训练 | 数据规模更大，但需确认 segmentation split 和类别映射 |
| FGADR | 外部泛化/补充训练 | 细粒度 DR 标注，可补充病灶多样性 |
| APTOS / EyePACS | 预训练或辅助任务 | 图像级 DR 标签，可用于质量评估、分类辅助或自监督，不直接作为分割主训练 |
| Messidor / Messidor-2 | 外部筛查/质量泛化 | 适合分类/筛查和图像质量分析，不作为像素级分割主数据 |

## 3. 数据预处理

1. 眼底圆形视野检测与裁剪，去除黑边。
2. 统一分辨率，例如 1024×1024 或在显存有限时 512×512。
3. 颜色标准化：RGB 归一化、CLAHE 作为传统增强 baseline。
4. 病灶类别统一：MA、HE、EX、SE；类别名和颜色映射固定。
5. 低质量模拟：随机模糊、低照度、噪声、JPEG 压缩、过曝/欠曝，用于训练质量增强模块。
6. 数据增强：水平/垂直翻转、旋转、尺度缩放、颜色扰动、CutMix/Copy-Paste 小病灶增强。

## 4. 模型设置

### Baseline

- U-Net / U-Net++。
- DeepLabv3+。
- HEDNet+cGAN 或 RTNet 思路复现。
- SAM zero-shot with boxes/points。
- MedSAM 或 SAM-Med2D 冻结主干 + adapter。

### 拟提出模型

LQ-Fundus-SAM：

- QEM：质量感知增强模块。
- FSA：眼底专用 SAM adapter/LoRA。
- MPP：医学先验 prompt 生成器。
- SBC：小病灶/边界约束。
- LSD：轻量化蒸馏学生模型。

## 5. 训练设置

| 项目 | 建议设置 |
|---|---|
| 输入尺寸 | 512×512 起步；主实验可尝试 1024×1024 |
| Optimizer | AdamW |
| 学习率 | adapter/head: 1e-4；decoder/增强模块: 1e-4 到 3e-4；冻结 SAM 主干 |
| Batch size | 由显存决定，建议 2-8 |
| Epoch | 100-200 或 early stopping |
| Loss | Dice + Focal/Tversky + Boundary + Quality + Distillation |
| 类别权重 | 按病灶像素频率或 effective number weighting |
| Prompt 训练 | 随机点、病灶框、自动候选框、类别文本 prompt 混合 |
| 复现实验 | 固定 random seed，记录硬件、输入尺寸、预处理和 split |

## 6. 评价指标

| 指标 | 用途 |
|---|---|
| Dice / IoU | 总体分割重叠 |
| per-class Dice / IoU | 分类别评估 MA、HE、EX、SE |
| AUPR / AP | 稀疏小病灶更敏感 |
| Sensitivity / Recall | 重点检查漏检 |
| Specificity / Precision / F1 | 控制假阳性 |
| Boundary F1 / Hausdorff distance | 边界质量 |
| PSNR / SSIM / LPIPS | 增强模块质量 |
| FPS / 参数量 / FLOPs / 显存 | 轻量化部署 |

## 7. 对比实验

1. 与传统分割网络比较：U-Net、DeepLabv3+、RTNet。
2. 与基础模型比较：SAM、MedSAM、SAM-Med2D、Medical SAM Adapter。
3. 与眼底 prompt 方法比较：GlanceSeg、TP-DRSeg 思路。
4. 与增强方法比较：CLAHE、Retinex、SAT-Net 或简化结构感知增强。
5. 与轻量化方法比较：MobileSAM、EfficientSAM、EdgeSAM、KD-SAM。

## 8. 消融实验

| 消融项 | 对照设置 | 观察指标 |
|---|---|---|
| 去掉 QEM | 原图直接分割 | 低质量子集 Dice/AUPR、MA recall |
| 去掉 adapter | 只用冻结 SAM/MedSAM | 领域适配收益 |
| 去掉文本/类别 prompt | 只用点/框 prompt | 类别混淆和多病灶 Dice |
| 去掉结构先验 | 不用血管/边缘辅助 | HE/MA 误检和边界 F1 |
| 去掉小病灶损失 | 只用 Dice/Focal | MA/SE recall |
| 去掉蒸馏 | 大模型直接推理 | FPS/参数量/性能权衡 |

## 9. 可视化分析

1. 原图、增强图、ground truth、baseline 预测、拟提出模型预测并排展示。
2. 单独展示低质量样本、微小病灶样本和边界复杂样本。
3. 绘制 PR 曲线、类别 Dice 柱状图、效率-精度散点图。
4. 可视化 prompt 点/框、文本先验响应、adapter attention 或病灶热图。
5. 错误案例分析：漏检、误检、类别混淆、增强伪影。

## 10. 风险与备选方案

| 风险 | 影响 | 备选方案 |
|---|---|---|
| SAM/MedSAM 显存不足 | 无法 1024×1024 训练 | 冻结主干、使用 adapter、降低输入尺寸、梯度累积 |
| 分割标注太少 | 过拟合、泛化差 | 联合 DDR/FGADR、Copy-Paste 小病灶增强、自监督预训练 |
| 低质量增强改变病灶纹理 | 分割指标下降 | 联合分割损失、保留原图分支、只做轻量增强 |
| 文本 prompt 不稳定 | 类别先验无法有效注入 | 退化为类别 embedding/token 或病灶候选热图 |
| 蒸馏损失小病灶细节 | 学生模型漏检 | 增加边界蒸馏、小病灶响应蒸馏和 hard sample replay |
| 数据集许可/下载受限 | 不能完整复现 | 以 IDRiD 为主，报告中标注外部数据为计划验证 |

## 11. 阶段性实验产物

- `configs/`：训练配置和数据 split。
- `checkpoints/`：baseline、teacher、student 权重。
- `results/metrics.csv`：每类指标。
- `results/figures/`：PR 曲线、混淆/错误可视化、低质量案例。
- `results/ablation.csv`：消融实验表。
- `README_experiment.md`：运行命令与环境。

本次课程交付以调研和规划为主，不编造训练数值。若后续真正训练模型，以上规划可直接转化为实验执行清单。
