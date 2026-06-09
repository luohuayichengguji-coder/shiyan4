# AI开发技术-实验4.1 交付物清单

## 任务依据

本项目已首先读取当前目录任务指导文件：

`AI技术-实验4.1-实验要求-医学图像技术调研.txt`

该文件作为全过程最高优先级本地任务依据。报告结构、PPT结构、过程记录、合规矩阵和最终交付物均对齐其中的实验目的、实验内容、实验步骤、实验要求和相关资料。

## 最终交付物

| 文件 | 用途 |
|---|---|
| `outputs/AI开发技术-实验4.1-医学图像技术调研报告.docx` | 最终 Word 技术调研报告，可直接提交 |
| `outputs/AI开发技术-实验4.1-医学图像技术调研汇报.pptx` | 最终调研汇报 PPTX，可直接展示 |
| `outputs/AI开发技术-实验4.1-医学图像技术调研报告.md` | 报告 Markdown 中间稿，便于检查和复用 |
| `outputs/compliance_matrix.md` | 对照任务指导文件的逐条合规矩阵 |
| `outputs/AI_environment_and_skill_trace.md` | AI 环境配置、命令、Skill/Agent 调用轨迹和降级处理记录 |
| `used_skills_md/` | 本次使用或参考的 skills 原始 Markdown 与审批摘要，便于老师审核 |

## 阶段性记录

| 文件 | 用途 |
|---|---|
| `outputs/notes/stage1_task_understanding_and_compliance.md` | 阶段1任务理解、阶段计划、交付物清单和合规矩阵草案 |
| `outputs/notes/local_pdf_extracted_snippets.md` | 本地 PDF 自动抽取摘要/引言片段 |
| `outputs/notes/key_paper_reader_notes.md` | 重点论文结构化阅读笔记 |
| `outputs/notes/key_paper_analysis.md` | 每篇重点论文的研究问题、方法、数据集、指标、优势、不足和可借鉴点 |
| `outputs/notes/literature_search_record.md` | 2024-2026 在线文献检索记录、检索式、来源、筛选理由 |
| `outputs/notes/sota_datasets_metrics.md` | SOTA 方法、数据集和评价指标对比 |
| `outputs/notes/research_problem_solution.md` | 研究不足分析和 LQ-Fundus-SAM 研究方案 |
| `outputs/notes/experiment_plan.md` | 数据集、预处理、训练、对比、消融、可视化、风险和备选方案 |

## 表格数据

| 文件 | 用途 |
|---|---|
| `outputs/tables/local_paper_index.csv` / `.md` / `.json` | 本地 29 篇 PDF 论文索引表 |
| `outputs/tables/key_paper_analysis.csv` | 重点论文人工分析表 |
| `outputs/tables/literature_search_record.csv` | 在线检索记录表 |
| `outputs/tables/sota_method_comparison.csv` | SOTA 方法族对比 |
| `outputs/tables/dataset_comparison.csv` | 数据集对比 |
| `outputs/tables/metrics_comparison.csv` | 评价指标对比 |

## 图表

图表均提供新版 PNG/PDF 版本，位于 `outputs/figures/`。旧版 SVG 因存在箭头与文字重叠、缩放后可读性不足等问题，已归档到 `outputs/figures/old_svg_backup/`，提交和报告引用请使用新版 PNG/PDF。

| 图 | 用途 |
|---|---|
| `technical_roadmap.png` / `.pdf` | LQ-Fundus-SAM 技术路线图 |
| `problem_solution_map.png` / `.pdf` | 研究不足与方案模块映射图 |
| `experiment_flow.png` / `.pdf` | 实验规划流程图 |
| `sota_method_map.png` / `.pdf` | SOTA 方法族地图 |
| `dataset_metric_matrix.png` / `.pdf` | 数据集与指标选择逻辑 |

## 脚本

| 文件 | 用途 |
|---|---|
| `outputs/scripts/extract_local_papers.py` | 扫描本地 PDF 并生成论文索引 |
| `outputs/scripts/extract_key_paper_notes.py` | 生成重点论文结构化阅读笔记 |
| `outputs/scripts/build_research_artifacts.py` | 生成检索记录、重点论文分析、SOTA/数据集/指标表 |
| `outputs/scripts/make_figures.py` | 生成报告和 PPT 使用的技术图 |
| `outputs/scripts/build_report_and_ppt.py` | 生成最终 Markdown、DOCX 和 PPTX |
| `outputs/scripts/render_office_with_fitz.py` | 用 LibreOffice 转 PDF，再用 PyMuPDF 渲染 PNG 做版式 QA |

## 渲染与打开性检查

已完成以下检查：

1. `python-docx` 打开新版 Word：201 段、7 个表格、5 张内嵌图。
2. `python-pptx` 打开 PPT：12 页幻灯片。
3. Word 报告图表修正后使用 Microsoft Word 导出 PDF 并转白底 PNG 预览：
   - Word 导出为 13 页：`outputs/render_checks/docx_figfix_word/white_contact_sheet.png`
   - 已重点检查包含图表的第 5、8、9、10、11 页，确认新版图表无箭头压字、文字重叠或配色过浅问题。
4. LibreOffice + PyMuPDF 早期渲染检查仍保留：
   - Word 旧版渲染为 9 页：`outputs/render_checks/docx/docx_contact_sheet.png`
   - PPT 渲染为 12 页：`outputs/render_checks/pptx/pptx_contact_sheet.png`
5. PPT 首轮发现封面长标题和第2页长 Skill 列表溢出，已修复并重新渲染确认。

备注：当前 macOS 环境缺少 LibreOffice/`soffice`，documents 官方 `render_docx.py` 不能直接渲染新版 Word；本轮改用已安装的 Microsoft Word 导出 PDF，再拆页转 PNG 做视觉检查。PyMuPDF 渲染早期 LibreOffice 生成的 tagged PDF 时曾打印 `No common ancestor in structure tree` 结构提示，但 PDF/PNG 页面成功生成，不影响可视化检查。
