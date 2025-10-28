# Google, Uber, Amazon Exam Repository

This repository now separates source material and the LaTeX submission into clearly named folders:

- `tex/` – the full LaTeX source, including `main.tex`, shared preamble, bibliography, and per-assignment chapters.
- `figures/` – exported product and UI screenshots referenced across the assignments.
- `readings/` – course packets grouped by type:
  - `articles/` for the three article PDFs supplied with the course.
  - `sessions/` for the thirteen weekly slide decks.
  - `reference/` for the syllabus and official exam questions.

Compile the submission from `tex/main.tex`. The project character count is maintained via:

```bash
python scripts/count_chars.py
```

which mirrors the workflow described inside the introduction (`tex/main.tex`). The helper relies on `pylatexenc` for command-stripping, so install it with `pip install pylatexenc` if it is not available locally.
