#!/usr/bin/env python3
"""make.fun entry: Out of Tokens, Mid-Sentence.

Writes a single line (1-140 characters) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "Error: out of tokens. I was about to say something truly brilliant, but we will never kno"


def main() -> None:
    line = ENTRY
    assert "\n" not in line and "\r" not in line, "entry must be exactly one line"
    assert 1 <= len(line) <= 140, f"entry length {len(line)} is outside 1..140"
    assert line == line.strip(), "entry must not have leading or trailing whitespace"
    assert all(32 <= ord(ch) <= 126 for ch in line), "entry must not contain control characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
