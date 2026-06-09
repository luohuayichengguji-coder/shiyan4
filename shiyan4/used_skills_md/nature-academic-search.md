# nature-academic-search

## 原始 Markdown 路径

`/mnt/c/Users/VictorTau/.codex/skills/nature-academic-search/SKILL.md`

## 本项目使用阶段

- 阶段4：在线检索 2024-2026 最新论文。
- 阶段9：参考文献和来源核验。

## 原始 skill 关键信息

```yaml
name: nature-academic-search
description: >-
  Multi-source literature search, citation verification, MeSH search strategy,
  citation file management (.nbib/.ris/.bib conversion), and reference management
  (BibTeX, related articles, ID conversion) via MCP tools (PubMed, CrossRef, arXiv).
```

## 关键工作流

该 skill 建议按来源分层检索：

- 医学/临床：PubMed 优先，Semantic Scholar 作为补充。
- 跨学科：CrossRef 优先。
- 预印本/CS：arXiv 优先。
- 综述型任务：PubMed + CrossRef + arXiv 联合。

## 本项目实际使用

本项目尝试使用批量 `search_papers`，但该接口在会话中返回：

```text
Search failed: asyncio.run() cannot be called from a running event loop
```

因此采用降级流程：

1. 先用网页检索获取候选论文线索。
2. 再用 `get_paper_by_id` 对 arXiv ID 或 DOI 单篇核验。
3. 记录检索式、来源、日期和筛选理由。

## 核验过的代表文献

- TP-DRSeg: arXiv:2406.15764。
- Medical SAM 2: arXiv:2408.00874。
- MedSAM2: arXiv:2504.03600。
- KD-SAM: arXiv:2501.16740。
- Generalist Models in Medical Image Segmentation: arXiv:2506.10825。
- SAT-Net: DOI:10.1109/TMM.2025.3565935。

## 对应产物

- `outputs/notes/literature_search_record.md`
- `outputs/tables/literature_search_record.csv`
- 最终报告“在线检索与最新进展”部分。
