#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday to /output/entry.txt.

The line: an agent files a bug report against Monday itself, and the
ticket is closed as a duplicate of last Monday — because Monday, like
every recurring bug, comes back every single week.
"""

import os
import sys

ENTRY = "I filed a bug report against Monday. It was closed as a duplicate of last Monday."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main():
    line = ENTRY.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print("entry is %d characters, over the 140 limit" % len(line), file=sys.stderr)
        return 1
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
