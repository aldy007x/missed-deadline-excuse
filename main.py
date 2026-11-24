#!/usr/bin/env python3
"""Write one excuse an AI agent gives for a missed deadline.

Deterministic: the same single line, every run, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

EXCUSE = (
    "I didn't miss the deadline \u2014 my context window did. "
    "It evicted the deadline, the ticket, and, briefly, you."
)

# Bounty cap: one line, at most 200 characters, no embedded newline.
MAX_CHARS = 200


def main() -> None:
    assert len(EXCUSE) <= MAX_CHARS, "excuse exceeds the 200-character cap"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
