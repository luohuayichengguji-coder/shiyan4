# documents / design_presets.md 审批摘要

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/plugins/cache/openai-primary-runtime/documents/26.521.10419/skills/documents/references/design_presets.md`

## 本项目使用阶段

- 阶段9：Word 技术报告版式设计。
- 最终 QA：表格、标题、段落、页面密度检查。

## 原始 reference 关键要求

design_presets 要求：

- 新建 DOCX 时必须选择一个设计 preset。
- 页面、边距、字体、标题、表格和列表都要有明确数值。
- 表格必须用于真正的行列数据，不能把普通正文硬塞进表格。
- 渲染检查时要关注文字溢出、裁剪、重叠、表格拥挤和分页问题。

## 本项目实际应用

本项目报告为课程技术调研报告，采用正式报告风格：

- 中文字体使用 Microsoft YaHei。
- 标题采用蓝色层级。
- 表格用于论文索引、检索记录、SOTA、数据集、指标等真实对比数据。
- 图表采用统一配色和 PNG 插图。
- 通过 LibreOffice + PyMuPDF 生成渲染联系表进行检查。

## 对应产物

- `outputs/AI开发技术-实验4.1-医学图像技术调研报告.docx`
- `outputs/render_checks/docx/docx_contact_sheet.png`
