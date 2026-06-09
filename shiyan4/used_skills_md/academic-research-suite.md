# academic-research-suite

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/skills/academic-research-suite/SKILL.md`

## 本项目使用阶段

- 阶段1：建立任务理解、阶段计划和合规矩阵。
- 阶段3-5：文献综述、重点论文分析、SOTA 归纳。
- 阶段6-8：研究问题拆解、研究方案和实验规划。

## 原始 skill 关键信息

```yaml
name: academic-research-suite
description: >
  Codex-native Academic Research Skills suite for deep research, academic paper
  writing, manuscript review, full research-to-paper pipelines, and experiment
  planning or validation.
```

## 关键使用规则摘录

该 skill 是 ARS suite 的 Codex 适配器。它要求：

- 不默认加载整个 suite，而是选择一个 workflow 后只读取当前阶段需要的 agent/reference/template。
- 深度研究、文献综述、事实核验、研究问题细化使用 `ars/deep-research/WORKFLOW.md`。
- 实验规划、研究方案设计使用 `ars/experiment-agent/WORKFLOW.md`。
- 学术报告/论文写作结构可参考 `ars/academic-paper/WORKFLOW.md`。

## 本项目实际引用方式

本项目没有把 ARS 当作自动“黑盒 agent”运行，而是读取其工作流和 agent Markdown，按其中的研究流程在当前会话内执行：

1. 使用 deep-research 的 scoping、investigation、analysis、composition 思路组织阶段1-5。
2. 使用 research_architect_agent 的 methodology blueprint 结构建立研究方案。
3. 使用 synthesis_agent 的 literature matrix、theme、gap analysis 思路整合本地和外部论文。
4. 使用 experiment-agent 的 plan mode 思路设计数据集、指标、消融和风险备选。

## 对应产物

- `outputs/notes/stage1_task_understanding_and_compliance.md`
- `outputs/notes/sota_datasets_metrics.md`
- `outputs/notes/research_problem_solution.md`
- `outputs/notes/experiment_plan.md`
