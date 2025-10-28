# Project Guidelines

## Exam Deliverable Requirements
- The take-home exam runs for two weeks: hand-out and submission open **17-10-2025 12:00:00** and close **31-10-2025 12:00:00** via exam.cbs.dk. Retake runs 19-12-2025 12:00:00 to 02-01-2026 12:00:00.
- Produce an individual written assignment with a **maximum of 15 CBS pages (34,125 characters)**. Stay within this character cap while answering **all ten exam questions**.
- Demonstrate reflective analysis of the group platform project: document decision-making, network effects work, monetisation choices, governance/data policies, competitive positioning, inequality considerations, metrics, scaling approach, and five-year outlook.
- Support claims with specific course concepts, frameworks, and readings. Maintain a coherent referencing style throughout.

## Repository & File Layout
- Core LaTeX lives in `main.tex`, which should `\input{}` chapter files stored as `opgaver/opgave01.tex` … `opgaver/opgave10.tex` (one per exam question).
- Place all figures and UI screenshots inside `figures/` (e.g., move the existing `graph.png` to `figures/graph.png`). Reference them from LaTeX with relative paths such as `\includegraphics{figures/graph.png}`.
- Store provided reading material PDFs (e.g., `exam questions_.pdf`, `Syllabus.pdf`, session packets) at the repository root under their current filenames for quick access.

## Writing Style & Voice
- When drafting narrative text, adopt an informal, student-like oral tone. Allow for the occasional harmless typo or colloquialism, and vary sentence rhythm so it feels conversational rather than polished corporate prose.

## Referencing & LaTeX Practice
- Continue using LaTeX citation commands such as `\citet{...}` and `\citep{...}` with entries from `references.bib`. Add missing sources to the `.bib` file before citing them.
- When referencing UI images or screenshots, mention the asset by filename in the surrounding text (e.g., “see Figure~\ref{fig:graph} based on `figures/graph.png`”) and ensure the graphic resides in `figures/`.
- Apply consistent LaTeX structure for sections, figures, tables, and other elements; avoid filler text in guidelines.
