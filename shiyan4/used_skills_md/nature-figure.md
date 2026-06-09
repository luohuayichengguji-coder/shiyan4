# nature-figure

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/skills/nature-figure/SKILL.md`

## 本项目使用阶段

- 阶段9：生成报告中的技术路线图、方法对比图、实验流程图。
- 阶段10：将图表用于 PPT。

## 原始 skill 关键信息

```yaml
name: nature-figure
description: Submission-grade Nature/high-impact journal figure workflow for
Python or R.
```

## 关键要求

nature-figure 要求先建立 figure contract：

1. Core conclusion。
2. Evidence chain。
3. Archetype。
4. Backend。
5. Journal/export contract。

该 skill 还要求在用户未选择 Python 或 R 时先询问。本项目用户已明确要求优先使用 conda 环境 `hj` 和 Python 脚本，因此本项目将 Python/matplotlib 作为制图后端，并在过程记录中说明。

## 本项目生成的图

位于 `outputs/figures/`：

- `technical_roadmap.*`
- `problem_solution_map.*`
- `experiment_flow.*`
- `sota_method_map.*`
- `dataset_metric_matrix.*`

## 对应脚本

- `outputs/scripts/make_figures.py`

## QA 记录

首次制图时发现中文字体缺失警告，随后显式加载 Windows 中文字体 `NotoSansSC-VF.ttf` 重新生成，解决中文图表显示问题。
