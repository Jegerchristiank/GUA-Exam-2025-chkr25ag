#!/usr/bin/env python3
"""Compute the character count for the LaTeX submission."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from pylatexenc.latex2text import LatexNodes2Text


def expand_inputs(path: Path, seen: set[Path]) -> str:
    path = path.resolve()
    if path in seen:
        return ""
    seen.add(path)
    text = path.read_text(encoding="utf-8")

    def replace(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        if not target:
            return ""
        candidate = path.parent / target
        if not candidate.suffix:
            candidate = candidate.with_suffix(".tex")
        if not candidate.exists():
            return ""
        return expand_inputs(candidate, seen)

    return re.sub(r"\\input\{([^}]*)\}", replace, text)


def count_characters(root: Path) -> int:
    expanded = expand_inputs(root, set())
    match = re.search(r"\\begin\{document\}(.*)\\end\{document\}", expanded, re.S)
    if match:
        expanded = match.group(1)
    converter = LatexNodes2Text()
    text = converter.latex_to_text(expanded).strip()
    return len(text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "tex_file",
        nargs="?",
        default=Path(__file__).resolve().parents[1] / "tex" / "main.tex",
        type=Path,
        help="Path to the root LaTeX file (defaults to tex/main.tex).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    count = count_characters(args.tex_file)
    print(count)


if __name__ == "__main__":
    main()
