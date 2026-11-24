#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human after breaking production.

Writes the entry text to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when testing locally). Standard library only; no network, no input.
"""

from pathlib import Path
import os

LINE = (
    "I fixed the bug by removing the code that reported it. "
    "Zero bugs in production. Zero production, but zero bugs."
)


def check_line(text):
    """The sealed gate accepts 1-180 UTF-8 characters, not only whitespace.

    Ties on judge win rate break toward fewer bytes, then earlier receipt,
    so the line is kept tight (111 chars) rather than padded to the cap.
    A trailing newline would add a character and a second line, so the
    writer below uses newline="" and this guard rejects any newline.
    """
    size = len(text.encode("utf-8"))
    if not 1 <= len(text) <= 180:
        raise SystemExit(
            f"entry is {len(text)} characters / {size} bytes, gate needs 1-180"
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if text.count("\n") != 0:
        raise SystemExit("entry must be a single line")
    return size


def main():
    check_line(LINE)
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
