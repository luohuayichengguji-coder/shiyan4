# presentations

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/plugins/cache/openai-primary-runtime/presentations/26.521.10419/skills/presentations/SKILL.md`

## 本项目使用阶段

- 阶段10：最终 PPTX 生成和版式检查。

## 原始 skill 关键信息

```yaml
name: Presentations
description: Build PowerPoint PPTX decks with artifact-tool presentation JSX
```

## 关键要求摘要

presentations skill 强调：

- PPT 不应只是“干净”，而应有清晰故事线、证据对象和视觉节奏。
- 需要确认 task mode、source story、claim spine、design system、contact sheet。
- 最终 PPTX 应经过渲染预览和 QA。
- 避免全 deck 使用同一种模板化布局。

## 本项目实际使用

本项目没有现成模板，因此采用 create 模式思想，以课程技术调研为内容源，使用 python-pptx 生成可编辑 PPTX，并使用 LibreOffice + PyMuPDF 渲染为 PNG 联系表进行 QA。

## 对应产物

- `outputs/AI开发技术-实验4.1-医学图像技术调研汇报.pptx`
- `outputs/render_checks/pptx/pptx_contact_sheet.png`
- `outputs/scripts/build_report_and_ppt.py`
- `outputs/scripts/render_office_with_fitz.py`
