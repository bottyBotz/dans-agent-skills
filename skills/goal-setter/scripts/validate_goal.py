#!/usr/bin/env python3
"""Check a Codex objective's nonempty text and 4,000-code-point limit.

Accept raw objective text, a /goal command, or one enclosing Markdown fence.
Read UTF-8 from a named file, or stdin with no argument (or '-').
Exit 0 for valid input, 1 for invalid objective text, 2 for input/usage errors.
This checks mechanical validity only; it does not score goal quality.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_OBJECTIVE_CHARACTERS = 4000


def validate_goal(text: str) -> str:
    """Return the trimmed objective, raising ValueError for invalid input."""
    objective = text.strip()
    if objective.startswith("```"):
        lines = objective.splitlines()
        opening = re.fullmatch(r"(`{3,})(?:text|plaintext)?", lines[0].strip())
        if opening is None or len(lines) < 2 or lines[-1].strip() != opening.group(1):
            raise ValueError("expected one complete enclosing Markdown fence")
        if any(line.lstrip().startswith("```") for line in lines[1:-1]):
            raise ValueError("expected one goal, not multiple Markdown fences")
        objective = "\n".join(lines[1:-1]).strip()
    if objective == "/goal":
        objective = ""
    elif objective.startswith("/goal") and len(objective) > 5 and objective[5].isspace():
        objective = objective[5:].strip()
    count = len(objective)
    if not objective:
        raise ValueError("objective is empty (0 characters)")
    if count > MAX_OBJECTIVE_CHARACTERS:
        raise ValueError(f"objective has {count} characters; maximum is {MAX_OBJECTIVE_CHARACTERS}")
    return objective


def main(argv: list[str]) -> int:
    if argv in (["--help"], ["-h"]):
        print(__doc__)
        return 0
    if len(argv) > 1:
        print("Usage: python validate_goal.py [UTF8_FILE|-]", file=sys.stderr)
        return 2
    try:
        if argv and argv[0] != "-":
            text = Path(argv[0]).read_text(encoding="utf-8-sig")
        else:
            text = sys.stdin.buffer.read().decode("utf-8-sig")
    except (OSError, UnicodeError) as error:
        print(f"Input error: {error}", file=sys.stderr)
        return 2
    try:
        objective = validate_goal(text)
    except ValueError as error:
        print(f"INVALID: {error}", file=sys.stderr)
        return 1
    print(f"VALID: {len(objective)} characters (maximum {MAX_OBJECTIVE_CHARACTERS}); quality not assessed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
