# documents

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/plugins/cache/openai-primary-runtime/documents/26.521.10419/skills/documents/SKILL.md`

## 本项目使用阶段

- 阶段9：生成最终 Word 技术报告。
- 最终检查：渲染 DOCX 并检查版式。

## 原始 skill 关键信息

```yaml
name: documents
description: Create, edit, redline, and comment on `.docx`, Word, and Google
Docs-targeted document artifacts inside the container, with a strict
render-and-verify workflow.
```

## 关键要求

documents skill 明确要求：

- 对 DOCX 使用 render → inspect PNGs → iterate 的检查流程。
- 对新建文档应选择设计 preset。
- 表格必须使用明确几何和可读格式。
- 最终交付前检查是否有文字重叠、溢出、表格拥挤、分页问题等。

## 本项目实际使用

本项目用 python-docx 生成 Word 报告，并尝试直接使用 `render_docx.py`。由于 `hj` 环境缺少 `pdf2image`，原 render 脚本无法继续转 PNG；随后采用等价替代流程：

1. LibreOffice/soffice 将 DOCX 转为 PDF。
2. PyMuPDF 将 PDF 渲染成 PNG。
3. Pillow 生成联系表。
4. 人工检查联系表和关键页面。

## 对应产物

- `outputs/AI开发技术-实验4.1-医学图像技术调研报告.docx`
- `outputs/render_checks/docx/docx_contact_sheet.png`
- `outputs/scripts/build_report_and_ppt.py`
- `outputs/scripts/render_office_with_fitz.py`

## QA 结果

- Word 可由 python-docx 打开。
- Word 渲染为 9 页 PDF/PNG。
- 联系表显示报告内容、表格和图片完整。
