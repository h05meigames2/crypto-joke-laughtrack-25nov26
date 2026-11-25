#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single original joke about crypto trading life to
/output/entry.txt (plain text, 1-200 characters, one line).
"""

import os

JOKE = (
    "I bought the dip, then the dip bought a shovel. Now I check the "
    "chart at 3 a.m. like a baby monitor for a coin that only cries "
    "when I sleep."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(path, 0o644)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
