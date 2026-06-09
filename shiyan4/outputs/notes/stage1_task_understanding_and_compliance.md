# 阶段1：任务理解、交付物清单与合规矩阵

## 任务依据

本项目已首先读取当前工作目录下的任务指导文件：

`AI技术-实验4.1-实验要求-医学图像技术调研.txt`

该文件被作为本次实验最高优先级的本地任务依据。后续调研主题、阶段计划、报告结构、PPT 结构、过程记录、README 和合规矩阵均围绕其中的“实验目的、实验内容、实验步骤、实验要求、相关资料”展开。

## 任务主题理解

本次调研围绕“基于 SAM 及其医学图像适配方法的眼底视网膜病变/糖尿病视网膜病变病灶分割技术调研”。核心逻辑是：

1. 先理解医学图像处理，尤其是眼底视网膜病变在糖尿病筛查中的意义。
2. 梳理 SAM、MedSAM、SAM-Med2D、Medical SAM Adapter、SAM2 等基础模型与医学适配方法。
3. 结合眼底 DR 病灶分割论文，分析微动脉瘤、出血、硬性渗出、软性渗出等小病灶分割困难。
4. 结合低质量眼底增强和 SAM 蒸馏方向，提出可执行研究方案。
5. 输出课程可提交的技术调研报告、PPT 和全过程记录。

## 阶段计划

| 阶段 | 任务 | 输出 |
|---|---|---|
| 1 | 读取任务指导文件，建立任务理解、交付物清单和合规矩阵 | 本文件、合规矩阵 |
| 2 | 整理本地 PDF 论文库 | `outputs/tables/local_paper_index.*` |
| 3 | 重点论文结构化阅读与人工分析 | `outputs/notes/key_paper_reader_notes.md`、`outputs/notes/key_paper_analysis.md` |
| 4 | 在线检索 2024-2026 最新论文并核验 | `outputs/notes/literature_search_record.md` |
| 5 | 总结 SOTA、数据集和指标 | `outputs/notes/sota_datasets_metrics.md` |
| 6 | 分析研究不足 | `outputs/notes/research_problem_solution.md` |
| 7 | 提出组合式研究方案 | `outputs/notes/research_problem_solution.md` |
| 8 | 设计实验规划 | `outputs/notes/experiment_plan.md` |
| 9 | 生成技术调研报告 Word/Markdown/PDF 中间稿 | `outputs/AI开发技术-实验4.1-医学图像技术调研报告.*` |
| 10 | 生成调研汇报 PPTX | `outputs/AI开发技术-实验4.1-医学图像技术调研汇报.pptx` |

## 交付物清单

| 序号 | 交付物 | 文件路径 |
|---:|---|---|
| 1 | 阶段性 Markdown 记录 | `outputs/notes/*.md` |
| 2 | 论文索引表 | `outputs/tables/local_paper_index.csv` / `.md` |
| 3 | 文献检索记录 | `outputs/notes/literature_search_record.md` |
| 4 | 重点论文阅读笔记 | `outputs/notes/key_paper_reader_notes.md` |
| 5 | SOTA/数据集/指标对比表 | `outputs/notes/sota_datasets_metrics.md` |
| 6 | 研究问题与解决方案分析 | `outputs/notes/research_problem_solution.md` |
| 7 | 实验规划 | `outputs/notes/experiment_plan.md` |
| 8 | AI 环境配置和 Skill/Agent 调用轨迹 | `outputs/AI_environment_and_skill_trace.md` |
| 9 | 最终技术调研报告 Word | `outputs/AI开发技术-实验4.1-医学图像技术调研报告.docx` |
| 10 | 最终 PPTX | `outputs/AI开发技术-实验4.1-医学图像技术调研汇报.pptx` |
| 11 | README/交付物清单 | `outputs/README.md` |
| 12 | 合规矩阵 | `outputs/compliance_matrix.md` |

## 合规矩阵

| 指导文件要求 | 对应完成方式 | 证据文件 | 状态 |
|---|---|---|---|
| 了解医学图像处理主要作用，特别是眼底视网膜病变在糖尿病诊断中的意义 | 报告背景部分说明 DR 筛查、早期诊断、病灶分割临床价值 | 最终报告、PPT | 已规划/执行中 |
| 了解视网膜病变分割技术，熟悉 SAM 分割技术 | 本地论文索引覆盖 SAM、医学 SAM、眼底 DR 分割；SOTA 表总结方法族 | `local_paper_index.md`、`sota_datasets_metrics.md` | 已完成 |
| 熟悉配置基于大模型的代码生成环境 | 记录 conda hj、Python、PyMuPDF、docx、pptx、matplotlib 等环境 | `AI_environment_and_skill_trace.md` | 已完成 |
| 使用调研相关 Agent 和 Skill | 记录 academic-research-suite、nature-academic-search、nature-reader 等调用/参考方式 | `AI_environment_and_skill_trace.md` | 已完成 |
| 根据论文分类，将 SAM 医学图像分割应用扩展到眼底视网膜分割 | 按 SAM 相关、医学 SAM、眼底分割、增强、蒸馏建立索引并提出组合方案 | `local_paper_index.md`、`research_problem_solution.md` | 已完成/执行中 |
| 使用 Codex 桌面端等 AI 工具创建项目，分析论文文件夹 | 在当前 hj-5 工作目录创建 outputs，自动抽取 29 篇本地 PDF 信息 | `outputs/scripts/extract_local_papers.py`、索引表 | 已完成 |
| 在线搜索最新科研论文，分析不足并给出解决方案 | 检索并核验 TP-DRSeg、MedSAM2、Medical SAM 2、KD-SAM、SAT-Net 等 | `literature_search_record.md` | 已完成 |
| 针对“迁移到眼底分割”和“低质量图像”问题进一步分析 | 阶段6 明确领域适配、低质量、标注稀缺/类别不平衡/推理成本问题 | `research_problem_solution.md` | 执行中 |
| 给出具体实验规划 | 设计数据集、预处理、模型、损失、对比、消融、风险备选 | `experiment_plan.md` | 执行中 |
| 完成技术调研报告，包含背景、现状、问题、方案、实验规划、参考文献 | 生成 Markdown、Word，尽量完成渲染检查 | 最终报告 | 待生成 |
| 详细记录 AI 环境配置和过程 | 记录命令、工具链、脚本、降级处理 | `AI_environment_and_skill_trace.md` | 已完成/持续更新 |
| 完成实验 PPT 和报告 | 生成 PPTX 和 DOCX | 最终交付物 | 待生成 |
| 认真总结心得体会 | 报告和 PPT 末尾包含心得体会 | 最终报告、PPT | 待生成 |
