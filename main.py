#!/usr/bin/env python3
"""make.fun entry: Out of Tokens, Mid-Sentence.

Prints one error line to stdout and writes the same line to
/output/entry.txt. Standard library only.
"""

import os

# The joke is the cut-off: the sentence stops mid-word, exactly where
# the token budget ran out.
_HEAD = "Error: out of tokens. I was about to say something truly "
_TAIL = "brilliant, but we will never kno"


def build_entry() -> str:
    return _HEAD + _TAIL


def main() -> None:
    line = build_entry()
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry length {len(line)} is outside 1..140")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not all(32 <= ord(ch) <= 126 for ch in line):
        raise ValueError("entry must not contain control characters")
    print(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
