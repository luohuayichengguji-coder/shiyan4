---
name: technical-report-writer
description: Write formal LaTeX technical reports and experiment reports for mathematical modeling and data analysis tasks from problem statements, code outputs, charts, CSV or XLSX data, external sources, and AI workflow evidence; includes requirement compliance checks, figure and table rules, metrics, references, appendices, and reproducibility rules.
---

# Technical Report Writer

Use this skill to generate a规范技术报告 or实验报告 from a modeling problem, experiment requirement, code, result CSVs, charts, external data, and AI workflow evidence. The report should be evidence-driven, reproducible, requirement-complete, and formatted for LaTeX submission. Do not hard-code any specific problem's answer; infer content only from the provided problem statement, experiment brief, data, code, outputs, figures, prompts, logs, and cited sources.

## Inputs To Collect

Before drafting, inspect and summarize:

- Problem statement: title, background, subproblems, required output tables/figures/metrics, appendix requirements.
- Experiment brief: required deliverables, AI tool or skill requirements, prompt/process evidence, comparison requirements, PPT or demo requirements.
- LaTeX template: document class, metadata fields, packages, existing section order, bibliography style, appendix/code listing conventions.
- Code and logs: model names, features, preprocessing, hyperparameters, train/test split, random seed, metrics, final predictions, generated file names.
- CSV/XLSX results: column names, units, row counts, decimal precision, summary statistics, prediction outputs.
- Charts: file paths, what each chart proves, axis labels, legends, resolution, whether labels are readable.
- External data: variables, sources, URLs or source names, publication names, time range, region, acquisition date, preprocessing and merge keys.
- AI workflow evidence: prompts, conversation screenshots, skill files, skill revision notes, generated code versions, and comparison baselines.

If key evidence is missing, state the gap in the report instead of inventing values.

## Requirement Compliance First

Before drafting, build a compliance matrix from every explicit requirement in the problem statement and experiment brief. Include this matrix in the report when the task is an experiment report, or keep it as a drafting checklist for a pure competition paper.

Recommended columns:

```latex
要求编号 & 原始要求摘要 & 报告位置 & 代码/数据/图表证据 & 状态 & 说明
```

Rules:

- Treat listed analysis dimensions as mandatory. If the prompt says "年龄、性别、学历、专业、行业", each dimension needs a table or figure unless the data is absent; absence must be documented.
- Treat required prediction outputs as mandatory. If an optimized model is requested to predict a prediction set, provide those predictions under a clearly stated scenario or mark the item as not fully satisfied.
- Treat external data requirements as mandatory. Simulated data may validate a workflow but cannot replace required real collected data unless the report explicitly labels it as a limitation.
- Treat deliverables such as code, technical report, experiment report, PPT, and demo notes separately. A technical report alone does not satisfy an experiment-report requirement.
- Do not hide noncompliance in limitations; state it directly in the compliance matrix and propose the missing artifact.

## Report Structure

Follow the local template when one is provided. For mathematical modeling reports, use this default structure:

1. Title page and metadata: title, problem number, team/school/date if required by the template.
2. Abstract: one paragraph for the overall task, then one concise paragraph per subproblem covering method, result, and conclusion. End with 3-5 keywords.
3. Problem Restatement: background and explicit subproblem requirements. Paraphrase; do not copy long passages.
4. Problem Analysis: explain each subproblem's modeling goal, input/output, core difficulty, and chosen strategy.
5. Model Assumptions: numbered assumptions with why they are reasonable and what risk they introduce.
6. Symbol Description: table of important symbols only, with units where applicable.
7. Per-Problem Modeling and Solving:
   - Model establishment: data labeling/cleaning, feature construction, model equations or algorithm principle.
   - Model solving: implementation steps, data split, parameter choices, training or optimization procedure.
   - Results: required tables, figures, predictions, and text interpretation.
8. Model Analysis and Testing: sensitivity analysis, error analysis, robustness checks, ablation, confusion matrix/ROC, or residual analysis as appropriate.
9. Model Evaluation: advantages, limitations, and improvement directions.
10. Summary and Outlook: concise overall findings and future extensions when the report length permits.
11. References: use the template's bibliography style, preferably GB/T 7714 numeric style for Chinese reports.
12. Appendices: file list, external data files, core code snippets or `\lstinputlisting`, and supplementary tables.

Adapt the number of per-problem sections to the problem statement. If a task has no modeling component, replace "model" language with the appropriate analysis or algorithm language.

For course experiments involving AI-assisted development, add a separate experiment-process section or a companion experiment report with:

- Tools and environment: IDE, model, Python/LaTeX versions, major packages, run commands.
- Prompt workflow: simple-prompt version, skill-assisted version, and representative prompt excerpts or screenshot references.
- Skill improvement: original weakness, revised rules, and the expected effect on report/code quality.
- Method comparison: compare simple prompting, skill-assisted generation, and any provided example report across completeness, reproducibility, evidence traceability, chart quality, and writing quality.
- Deliverable inventory: code, technical report, experiment report, PPT, demo script, data, and generated outputs.

## LaTeX Writing Rules

- Keep template commands intact: document class, packages, title metadata, bibliography style, and appendix environment.
- Use XeLaTeX for Chinese templates unless the template states otherwise.
- Cross-reference every important figure, table, and equation with `\label{...}` and `\cref{...}` or the template's preferred reference command.
- Use `\section`, `\subsection`, and `\subsubsection` consistently. Avoid excessive levels.
- Put equations in `equation` when they are referenced; use display math only for unnumbered equations.
- Use concise technical prose: each result paragraph should state what was computed, the key numeric result, and the modeling implication.

## Figure Insertion Rules

- Insert only figures that support a claim in the surrounding text. Mention the figure before or immediately after it appears.
- Store report figures in the template's figure directory when applicable, typically `figures/`, and use stable relative paths.
- Prefer `png` or `pdf` for generated charts; use `eps` only if the template or compilation flow requires it.
- Use a single-column figure at `0.70\textwidth` to `0.90\textwidth`; use subfigures only for direct comparisons.
- Every figure needs a short caption describing the analytic content, not just the file name.
- Axis labels, units, legends, class labels, and numeric annotations must be readable in the final PDF.
- For feature importance, model comparison, prediction statistics, confusion matrix, ROC, residual, or sensitivity charts, explain the main pattern and its implication in text.
- Do not insert screenshots of tables when a LaTeX table can present the data.

Example:

```latex
\begin{figure}[htbp]
\centering
\includegraphics[width=0.82\textwidth]{figures/model_comparison.png}
\caption{不同模型评价指标对比}
\label{fig:model_comparison}
\end{figure}
```

## Table Format Rules

- Use LaTeX tables, not images. Use `booktabs` style: `\toprule`, `\midrule`, `\bottomrule`.
- For full-width tables, use `tabularx` with `L`, `C`, `R` column types if the template defines them.
- Table captions go above the table in LaTeX's default `table` environment behavior; keep captions specific.
- Include units in column headers, for example `人数（人）`, `占比（%）`, `误差（万元）`.
- Use consistent numeric precision: metrics usually 3-4 decimals or percentages to 1-2 decimal places; counts are integers.
- Sort result tables by the meaningful criterion when useful, such as F1 descending or feature importance descending.
- Bold only the best or selected model row if it improves readability.
- For wide prediction tables, either split into multiple rows, use `tabularx`, or place detailed results in the appendix and summarize in the main text.

Example:

```latex
\begin{table}[H]
\centering
\caption{各模型评价指标结果}
\begin{tabularx}{0.86\textwidth}{LCCCC}
\toprule
模型 & 准确率 & 查准率 & 召回率 & F1 \\
\midrule
Model-A & 0.8123 & 0.7950 & 0.8123 & 0.8018 \\
\bottomrule
\end{tabularx}
\label{tab:model_metrics}
\end{table}
```

## Model Evaluation Metrics

Always define the evaluation setting before reporting metrics:

- Task type: classification, regression, ranking/recommendation, clustering, or optimization.
- Target variable and positive class, for binary classification.
- Train/test split, cross-validation strategy, random seed, and whether sampling is stratified.
- Whether the reported metric is per-class, macro average, micro average, or weighted average.

For classification reports:

- Include class distribution before metrics.
- Include a confusion matrix or a table with `TP`, `TN`, `FP`, and `FN` when data supports it.
- Report per-class precision, recall, and F1 when the classes are imbalanced or when one class is operationally important.
- Check for majority-class collapse. If all or almost all predictions are one class, state this plainly and add mitigation experiments such as class weights, resampling, threshold tuning, or model comparison.
- Compare against a simple baseline such as majority-class, logistic regression, random forest, or another locally available model when the task is predictive.
- For prediction-set outputs, include both individual predictions and summary counts in the required format.

For binary classification, write formulas once:

```latex
\begin{equation}
Acc=\frac{TP+TN}{TP+TN+FP+FN}
\end{equation}
\begin{equation}
P=\frac{TP}{TP+FP},\quad
R=\frac{TP}{TP+FN},\quad
F_1=\frac{2PR}{P+R}
\end{equation}
```

Then explain:

- `TP`, `TN`, `FP`, `FN` meanings in the problem context.
- Accuracy measures overall correctness.
- Precision/查准率 measures reliability of positive predictions.
- Recall/召回率 measures coverage of true positive samples.
- F1 balances precision and recall.
- For imbalanced data, prefer macro or weighted precision, recall, and F1, and include class distribution or confusion matrix.

For regression, use MAE, RMSE, MAPE, and `R^2` where appropriate, and report units for error metrics. For recommendation/ranking, use Top-K hit rate, precision@K, recall@K, NDCG, MAP, coverage, diversity, average similarity, or case-review tables as supported by available evidence. If recommendations use simulated items, label the results as workflow validation rather than real deployment evidence.

## External Data Source Table

When external variables are used, include a table before modeling with at least:

- Variable name used in code.
- Meaning.
- Unit/frequency.
- Time range and region.
- Data source and URL or official publication name.
- Acquisition date.
- Preprocessing or merge method.
- Reason for inclusion.

Keep source claims traceable. If a source is unofficial, say so and discuss reliability risk. Cite external datasets in references or footnotes when possible.

Example columns:

```latex
序号 & 变量名 & 含义 & 单位/频率 & 时间范围/地区 & 数据来源 & 处理方式
```

In the text after the table, explain why each variable is theoretically relevant to the target and how it is aligned with the modeling dataset.

If external data is required by the problem statement:

- Prefer real collected data with URL, source platform or publication, collection date, region, time range, and license or access notes where available.
- Keep raw external files or extraction notes in the appendix/file inventory.
- Describe cleaning, de-duplication, missing-value handling, unit conversion, and merge keys.
- For macro variables, state the frequency mismatch risk and how prediction samples receive macro values, such as target year, scenario year, or latest available year.
- For job or market data, include fields such as岗位名称、公司/来源、地区、薪资、学历、技能、行业、发布日期、URL、采集日期 when available.
- Simulated external data must be clearly separated from real external data in tables, filenames, and conclusions.

## Drafting Workflow

1. Build a compliance matrix from the problem statement and experiment brief.
2. Build an evidence map: match each requirement to code outputs, CSV files, charts, prompt evidence, and source data.
3. Identify missing evidence before writing. Generate or request missing tables, charts, prediction files, external-source tables, or comparison outputs when feasible.
4. Decide section outline from the problem statement, experiment brief, and template.
5. Convert CSV/XLSX outputs into LaTeX tables with clean captions and labels.
6. Insert only validated chart files and write interpretation paragraphs tied to the numbers.
7. Write model methods from code behavior, including preprocessing, feature selection, leakage controls, hyperparameters, split strategy, and random seed.
8. Write metric definitions and results; compare models using the most relevant metric, not only the largest number.
9. Add model diagnostics, especially confusion matrix and per-class metrics for imbalanced classification.
10. Add external-data source tables and references for any non-provided data.
11. Add AI development process sections when required: prompt workflow, skill usage, skill improvement, method comparison, and example-report comparison.
12. Add appendices: deliverable inventory, file list, external data files, core code snippets or `\lstinputlisting`, supplementary tables, and run instructions.
13. Compile with the template's LaTeX engine and fix missing references, overfull tables, unreadable figures, broken bibliography, and oversized code appendices.
14. Final pass: verify every required table/figure/metric/prediction/deliverable in the problem statement and experiment brief appears in the report or is explicitly marked incomplete.

## Code and Appendix Rules

- The main text should explain algorithms and show only compact core code when necessary.
- Put full source code, long prediction tables, raw external data, and generated CSVs in appendices or submitted files.
- Include a reproducibility table with command, input files, output files, and expected result for each task script.
- Include `requirements.txt` or package/version notes when code execution is part of the deliverable.
- If a PDF appendix includes code, prefer `\lstinputlisting` or concise snippets; avoid dozens of pages of uncurated code unless the template requires it.

## Quality Checklist

- The report answers every subproblem explicitly.
- A requirement compliance matrix was built, and mandatory dimensions, outputs, and deliverables are not missing silently.
- Every numeric claim is supported by a code output, CSV, chart, or cited source.
- Figures and tables are referenced in prose and have labels/captions.
- Metric formulas match the task and class definition.
- Classification results include class distribution, per-class diagnostics, and majority-class-collapse checks when relevant.
- Prediction-set requirements include individual predictions and summary counts, including optimized-model predictions when requested.
- External data sources are traceable and have preprocessing notes.
- Simulated external data is not presented as real collected data.
- AI-development experiment reports include prompt evidence, skill usage/improvement, method comparison, and example-report comparison when required.
- Assumptions are plausible and limitations are stated.
- The appendix contains the file list and code or source files required by the problem.
- The deliverable inventory covers code, technical report, experiment report, PPT, demo materials, data, and generated outputs when these are required.
- The LaTeX compiles cleanly without missing figures, undefined references, or broken bibliography.
