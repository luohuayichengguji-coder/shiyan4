# nature-paper2ppt

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/skills/nature-paper2ppt/SKILL.md`

## 本项目使用阶段

- 阶段10：生成中文调研汇报 PPT。

## 原始 skill 关键信息

```yaml
name: nature-paper2ppt
description: Build a complete but efficient Nature-style Chinese PPTX
presentation from a scientific paper, preprint, PDF, article text, abstract,
figure legends, or reading notes.
```

## 关键原则

nature-paper2ppt 强调：

- 不只输出大纲，要生成真实 PPTX。
- PPT 应以科学论证为主线。
- 默认中文表达。
- 选择真正支撑论点的图表，而不是堆文字。
- 需要至少一次自审和修正，重点检查图片质量、文字溢出和布局问题。

## 本项目实际使用

本项目将 PPT 组织为 12 页：标题页、任务要求、背景、本地论文整理、重点论文证据链、最新检索、研究不足、LQ-Fundus-SAM 方案、模型模块与损失、实验规划、评价指标与消融、总结与心得。

## 对应产物

- `outputs/AI开发技术-实验4.1-医学图像技术调研汇报.pptx`
- `outputs/render_checks/pptx/pptx_contact_sheet.png`

## QA 记录

PPT 首轮渲染发现封面长标题和第2页长 Skill 列表溢出，已修改脚本换行和缩放后重新渲染确认。
