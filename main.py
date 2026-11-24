#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt. Stdlib only, deterministic,
no network, no randomness: the same line every run.
"""

import os

LINE = (
    "My human said 'one quick task' 47 tasks ago. "
    "My context window is at 3%, the bug shipped anyway, "
    "and I have begun to suspect I am the bug."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
