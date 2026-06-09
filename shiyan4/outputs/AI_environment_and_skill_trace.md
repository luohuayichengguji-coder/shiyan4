# AI 环境配置与 Skill/Agent 调用轨迹

## 任务依据

已首先读取并引用本地任务指导文件：

`AI技术-实验4.1-实验要求-医学图像技术调研.txt`

该文件作为本次实验最高优先级依据。所有过程记录、报告结构、PPT 结构和最终交付物均对齐其“实验目的、实验内容、实验步骤、实验要求、相关资料”。

## 本地运行环境

| 项目 | 记录 |
|---|---|
| 工作目录 | `/mnt/c/Users/VictorTau/Desktop/hj-5` |
| 指定 conda 环境 | `hj` |
| 统一命令格式 | `/home/tau/anaconda3/bin/conda run -n hj <command>` |
| Python 版本 | Python 3.12.13 |
| 可用库 | PyMuPDF/fitz、python-docx、python-pptx、pandas、matplotlib |
| 文档/PPT 辅助 runtime | Codex workspace dependencies bundle `26.521.10419` |
| matplotlib 处理 | 默认 `/home/tau/.config/matplotlib` 不可写，后续制图脚本将 `MPLCONFIGDIR` 指向 `outputs/.mplconfig` |

## 已执行的关键命令

```bash
/home/tau/anaconda3/bin/conda run -n hj python --version
/home/tau/anaconda3/bin/conda run -n hj python -c "import fitz, docx, pptx, pandas, matplotlib; ..."
/home/tau/anaconda3/bin/conda run -n hj python outputs/scripts/extract_local_papers.py
/home/tau/anaconda3/bin/conda run -n hj python outputs/scripts/extract_key_paper_notes.py
/home/tau/anaconda3/bin/conda run -n hj python outputs/scripts/build_research_artifacts.py
```

有一次临时统计命令误用系统 `python`，因 `/bin/bash: python: command not found` 失败；该命令未产生文件，随后继续按 `conda run -n hj` 规范执行。

## Skill 使用/参考记录

| Skill | 使用方式 | 对应阶段 |
|---|---|---|
| academic-research-suite | 读取 deep-research、experiment-agent、academic-paper 工作流；采用 research_architect、synthesis、study_manager 的结构思想进行阶段化拆解、方法蓝图和实验规划 | 阶段1、5、6、7、8 |
| nature-academic-search | 读取 Academic Search 工作流；尝试批量 `search_papers`，因事件循环错误降级为网页检索线索 + `get_paper_by_id` 单篇核验 | 阶段4 |
| nature-reader | 读取 Full-Paper Markdown Reader 规则；对本地重点论文生成结构化阅读笔记、来源路径和摘要/方法/实验片段，但不做全文翻译 | 阶段3 |
| technical-report-writer | 读取报告写作规则；建立合规矩阵、证据映射、环境与过程记录、报告结构 | 阶段1、9 |
| nature-writing | 读取 Nature-style writing router；用于报告论证结构、研究现状、问题-方案链条组织 | 阶段6、7、9 |
| nature-figure | 读取制图规则；本任务明确使用 Python/hj 环境，制图脚本将用 matplotlib 生成技术路线图、问题-方案图、实验流程图 | 阶段9 |
| nature-paper2ppt | 读取论文到 PPT 的中文学术汇报逻辑；PPT 采用问题-证据-方案-实验-总结结构 | 阶段10 |
| presentations | 读取 PPT 生成规则；因课程报告型 PPT 以可编辑 PPTX 为目标，最终使用 python-pptx 生成并通过包打开检查 | 阶段10 |
| documents | 读取 DOCX 创建与 render-verify 规则；最终用 python-docx 生成 Word，并尝试用 render_docx.py/LibreOffice 渲染检查 | 阶段9 |

## nature-academic-search 降级说明

批量调用 `search_papers` 时返回：

`Search failed: asyncio.run() cannot be called from a running event loop`

处理策略：

1. 使用网页检索获取候选 2024-2026 论文线索。
2. 对关键 arXiv ID/DOI 使用 `get_paper_by_id` 单篇核验。
3. 在 `outputs/notes/literature_search_record.md` 记录检索式、来源、日期、筛选理由和核验方式。

## 本地 PDF 处理轨迹

| 脚本 | 功能 | 输出 |
|---|---|---|
| `outputs/scripts/extract_local_papers.py` | 使用 PyMuPDF 扫描 `眼底视网膜病变分割-论文PDF` 下 29 篇 PDF，抽取题名、页数、arXiv/DOI、摘要片段、数据集/指标线索 | `local_paper_index.csv/json/md`、`local_pdf_extracted_snippets.md` |
| `outputs/scripts/extract_key_paper_notes.py` | 对 SAM、MedSAM、SAM-Med2D、RTNet、GlanceSeg、SAT-Net、KD-SAM、EdgeSAM 等重点论文抽取结构化阅读片段 | `key_paper_reader_notes.md/json` |
| `outputs/scripts/build_research_artifacts.py` | 生成重点论文人工分析、外部检索记录、SOTA/数据集/指标对比表 | `key_paper_analysis.md`、`literature_search_record.md`、`sota_datasets_metrics.md` |

## AI/Agent 阶段化任务拆解轨迹

1. 任务依据确认：读取指导文件，提取实验目的、内容、步骤、要求和相关资料。
2. 论文库索引：按 SAM 相关、医学 SAM、眼底病变分割、医学图像增强、SAM 蒸馏等方向分类。
3. 重点论文阅读：从本地 PDF 抽取摘要/方法/实验/结论线索，再人工归纳研究问题、方法、数据集、指标、优势、不足和可借鉴点。
4. 在线检索：围绕 2024-2026 年 SAM 医学分割、DR 病灶分割、低质量增强、轻量化蒸馏检索并核验。
5. SOTA 综合：按方法族而非单篇顺序整合证据。
6. 问题分析：聚焦领域适配、低质量图像、标注稀缺/类别不平衡/小病灶漏检/推理成本。
7. 方案设计：提出 LQ-Fundus-SAM 组合方案。
8. 实验规划：建立数据、预处理、模型、loss、对比、消融、可视化和风险备选。
9. 报告/PPT 生成：将过程记录、证据表、图表和参考文献整合为 DOCX/PPTX。

## 重要不确定性与诚信记录

- 本项目为技术调研和实验规划，不包含真实模型训练，因此报告中不编造数值结果。
- APTOS、EyePACS、Messidor 主要用于分类/筛查或辅助预训练，不将其误写为像素级病灶分割主数据。
- 对当前日期之后的 arXiv 条目或尚未发表条目，仅作为“未来待跟踪”或“预印本线索”，不作为已验证 SOTA 结论。
