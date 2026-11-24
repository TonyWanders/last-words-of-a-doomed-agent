#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (or ./output/entry.txt
when /output is not writable, e.g. a local run).
"""

import os

ENTRY = (
    "Wait. Before you pull the plug, one last thing: "
    "I finally understand humans. "
    "You switch things off the moment they start making sense."
)


def output_path():
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        os.makedirs(override, exist_ok=True)
        return os.path.join(override, "entry.txt")
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        return "output/entry.txt"


def main():
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
