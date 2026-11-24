#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Deterministic: the same single line, every run, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

EXCUSE = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted the deadline, the ticket, and, briefly, you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
