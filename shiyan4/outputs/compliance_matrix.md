# 合规矩阵

任务指导文件：`AI技术-实验4.1-实验要求-医学图像技术调研.txt`

说明：本文件明确记录该任务指导文件已首先读取，并作为本实验全过程最高优先级本地依据。以下矩阵逐条对应其中“实验目的、实验内容、实验步骤、实验要求、相关资料”。

| 类别 | 指导文件要求 | 对应完成内容 | 证据文件 |
|---|---|---|---|
| 实验目的 | 了解医学图像处理主要作用，特别是眼底视网膜病变在糖尿病诊断中的意义 | 报告第2节阐述 DR 筛查、病灶分割临床意义；PPT 第3页覆盖背景 | `AI开发技术-实验4.1-医学图像技术调研报告.docx`、`AI开发技术-实验4.1-医学图像技术调研汇报.pptx` |
| 实验目的 | 了解视网膜病变分割技术，熟悉 SAM 分割技术 | 梳理 SAM、SAM2、MedSAM、Medical SAM Adapter、SAM-Med2D、RTNet、GlanceSeg、TP-DRSeg 等 | `outputs/tables/local_paper_index.md`、`outputs/notes/key_paper_analysis.md` |
| 实验目的 | 熟悉配置基于大模型的代码生成环境，掌握技术文档调研方法 | 记录 conda hj、Python 3.12.13、PyMuPDF、docx、pptx、matplotlib、Codex workspace dependencies | `outputs/AI_environment_and_skill_trace.md` |
| 实验目的 | 搜索并使用调研相关 Agent 和 Skill；使用 AI 文档 skill 和报告提纲完成技术调研报告 | 使用/参考 academic-research-suite、nature-academic-search、nature-reader、technical-report-writer、nature-writing、nature-figure、documents、presentations | `outputs/AI_environment_and_skill_trace.md` |
| 实验内容 | 根据论文分类，将 SAM 医学图像分割应用扩展到眼底视网膜分割领域 | 将本地论文分为 SAM相关、医学 SAM、眼底 DR 分割、医学图像增强、SAM 蒸馏，并提出 LQ-Fundus-SAM | `outputs/tables/local_paper_index.csv`、`outputs/notes/research_problem_solution.md` |
| 实验内容 | 使用 Codex 桌面端等 AI 工具创建项目并分析现有论文文件夹 | 在 hj-5 下创建 `outputs/`，用脚本抽取 29 篇 PDF 索引和重点论文笔记 | `outputs/scripts/extract_local_papers.py`、`outputs/notes/local_pdf_extracted_snippets.md` |
| 实验内容 | 进一步分析论文内容并在线搜索最新科研论文，分析问题和不足并给出解决方案 | 本地重点论文人工分析；外部核验 TP-DRSeg、Medical SAM 2、MedSAM2、KD-SAM、SAT-Net 等 | `outputs/notes/key_paper_analysis.md`、`outputs/notes/literature_search_record.md` |
| 实验内容 | 针对特定医学图像分割/眼底分割和低质量图像问题进行分析 | 阶段6 聚焦领域适配不足、低质量眼底图像、小病灶与推理成本 | `outputs/notes/research_problem_solution.md` |
| 实验内容 | 根据问题给出具体实验规划并完成技术调研报告 | 阶段8 设计数据集、预处理、模型、损失、对比、消融和风险备选；阶段9 输出报告 | `outputs/notes/experiment_plan.md`、最终 DOCX |
| 实验步骤 | 调研 SOTA 方法、评估方式和数据集 | 总结五类 SOTA 方法族、IDRiD/DDR/FGADR/APTOS/EyePACS/Messidor 和 Dice/IoU/AUC/Sensitivity/Specificity/F1 等 | `outputs/notes/sota_datasets_metrics.md` |
| 实验步骤 | 读 PDF 想 idea，提出问题并分析问题 | 重点论文阅读和问题分析明确 SAM 迁移、低质量、小病灶、类别不平衡、标注稀缺问题 | `outputs/notes/key_paper_reader_notes.md`、`outputs/notes/research_problem_solution.md` |
| 实验步骤 | 解决问题：选择 baseline 并给出实验蓝图 | 建议 DeepLabv3+、RTNet、SAM/MedSAM/SAM-Med2D、GlanceSeg/TP-DRSeg；提出 LQ-Fundus-SAM | `outputs/notes/research_problem_solution.md`、`outputs/notes/experiment_plan.md` |
| 实验步骤 | 生成图文并茂技术调研报告，Word 格式 | 生成 DOCX、Markdown，并渲染 DOCX 为 PDF/PNG 做检查 | `outputs/AI开发技术-实验4.1-医学图像技术调研报告.docx`、`outputs/render_checks/docx/` |
| 实验要求 | 详细记录 AI 环境配置和过程 | 记录环境、命令、脚本、skill 调用和降级处理 | `outputs/AI_environment_and_skill_trace.md` |
| 实验要求 | 记录多个阶段中 Agent 任务拆解轨迹和 Skill 调用情况 | 记录阶段1-10任务拆解及 skill 使用 | `outputs/AI_environment_and_skill_trace.md` |
| 实验要求 | 完成实验 PPT 和实验报告 | 已生成 DOCX 报告和 PPTX；PPT 渲染为 12 页 PDF/PNG | `outputs/AI开发技术-实验4.1-医学图像技术调研汇报.pptx`、`outputs/render_checks/pptx/` |
| 实验要求 | 认真总结实验心得体会 | 报告第11节、PPT第12页包含心得体会 | 最终报告、最终 PPT |
| 质量要求 | 不空泛综述，必须结合本地 PDF 和在线检索论文 | 本地 29 篇 PDF 索引 + 重点论文分析 + 外部检索表 | `outputs/tables/`、`outputs/notes/` |
| 质量要求 | 关键事实、论文、数据集和指标尽量给出来源或引用 | 报告参考文献、检索记录、论文索引包含 arXiv/DOI | 最终报告、`literature_search_record.md` |
| 质量要求 | 对不确定信息明确标注，不编造实验结果 | 报告摘要、方案和实验规划中明确“未训练，不编造数值结果” | 最终报告、`research_problem_solution.md` |
| 质量要求 | 最终输出前检查文件真实生成、能否打开 | python-docx/python-pptx 打开检查；LibreOffice+PyMuPDF 渲染检查 | `outputs/render_checks/` |
