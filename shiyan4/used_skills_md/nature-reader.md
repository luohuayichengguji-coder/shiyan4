# nature-reader

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/skills/nature-reader/SKILL.md`

## 本项目使用阶段

- 阶段3：本地重点论文阅读、结构化解读。

## 原始 skill 关键信息

```yaml
name: nature-reader
description: Build full-paper Chinese-English side-by-side, figure/table-aware,
source-grounded Markdown readers for journal or conference papers from PDF, DOI,
arXiv, publisher HTML, or pasted text.
```

## 关键原则

nature-reader 要求：

- 保留论文结构、原文位置和证据来源。
- 建立 source map 或稳定定位。
- 处理图表、标题、摘要、方法、实验、结论等关键部分。
- 不把论文阅读降级成无来源摘要。

## 本项目实际使用

本项目目标是技术调研，而不是全文翻译，因此没有生成逐段中英对照全文；而是借鉴 nature-reader 的“源文件定位 + 结构化阅读”方法，对本地重点论文生成题名、本地文件路径、arXiv/DOI、摘要/方法/实验/结论片段、数据集线索、指标线索和后续人工分析入口。

## 重点阅读论文示例

- SAM。
- MedSAM。
- Medical SAM Adapter。
- SAM-Med2D。
- SAM2。
- RTNet。
- GlanceSeg。
- SAT-Net。
- KD-SAM。
- EdgeSAM。

## 对应产物

- `outputs/notes/key_paper_reader_notes.md`
- `outputs/notes/key_paper_reader_notes.json`
- `outputs/notes/key_paper_analysis.md`
