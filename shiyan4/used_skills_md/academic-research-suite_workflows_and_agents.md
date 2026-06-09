# academic-research-suite 工作流与 Agent Markdown 审批记录

## 本项目读取/参考的 ARS 子文件

| 原始路径 | 用途 |
|---|---|
| `/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/ars/deep-research/WORKFLOW.md` | 深度调研、文献综述、证据综合流程 |
| `/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/ars/experiment-agent/WORKFLOW.md` | 实验规划、研究设计、验证流程 |
| `/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/ars/academic-paper/WORKFLOW.md` | 学术报告/论文写作阶段参考 |
| `/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/ars/deep-research/agents/research_architect_agent.md` | 研究方法蓝图、数据策略、分析框架 |
| `/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/ars/deep-research/agents/synthesis_agent.md` | 文献矩阵、主题综合、研究缺口分析 |
| `/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/ars/experiment-agent/agents/study_manager_agent.md` | 实验设计流程、变量、样本、分析策略 |

## deep-research WORKFLOW 关键内容

deep-research 的执行流程包括：

1. Scoping：研究问题、方法蓝图。
2. Investigation：系统文献检索、来源验证。
3. Analysis：跨来源综合、偏倚检查、缺口分析。
4. Composition：报告编写。
5. Review：编辑审查和伦理审查。
6. Revision：修订完善。

本项目对应：

- 阶段1：Scoping。
- 阶段2-4：Investigation。
- 阶段5-8：Analysis。
- 阶段9-10：Composition/Review。

## research_architect_agent 关键内容

该 agent 的核心原则：

- Research question drives method。
- Methodological coherence。
- Validity by design。

其输出结构包括 Research Paradigm、Method、Data Strategy、Analytical Framework、Validity Criteria、Limitations 和 Ethical Considerations。

本项目据此设计了 LQ-Fundus-SAM 的研究目标、数据集策略、baseline、训练流程、消融实验和风险备选。

## synthesis_agent 关键内容

该 agent 强调“integration, not summarization”，即不要逐篇堆砌摘要，而要做 Literature Matrix、Key Themes、Contradictions & Resolutions、Knowledge Gaps、Evidence Convergence Map 和 Theoretical Integration。

本项目据此生成：

- `outputs/notes/key_paper_analysis.md`
- `outputs/notes/sota_datasets_metrics.md`
- `outputs/notes/research_problem_solution.md`

## experiment-agent / study_manager_agent 关键内容

experiment-agent 的 plan mode 关注 Research Question、Variables、Design、Method selection、Sample、Analysis strategy 和 Produce plan。

本项目据此生成：

- `outputs/notes/experiment_plan.md`
- 报告第9节实验规划。
- PPT第10-11页实验规划与消融。
