#!/usr/bin/env python3
"""Write one short office joke to entry.txt.

Deterministic: the joke is a constant below, no network, no input files.
The grader runs this program and reads <output>/entry.txt.
"""
import os

JOKE = "I told my manager I was taking a long lunch. The elevator ride was the long part."

assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert "\n" not in JOKE, "joke must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
