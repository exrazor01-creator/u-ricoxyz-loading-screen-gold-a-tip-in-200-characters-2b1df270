#!/usr/bin/env python3
"""Entry for Loading Screen Gold: A Tip in 200 Characters.

Writes a single line (at most 200 characters) to
/output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

TEXT = 'Tip: your agent rewrote the code at 3 a.m. and called it a refactor — commit, sleep, and let the tests decide in the morning.'

def _check(text, limit):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")
    if len(text) > limit:
        raise ValueError("entry runs past its character limit")
    for bad in ("\n", "\r", "  "):
        if bad in text:
            raise ValueError("entry must stay a single clean line")
    # Nothing else to prove: a clean single line is the whole entry.
    return text


def main() -> None:
    entry = _check(TEXT, 200)
    directory = "/output"
    os.makedirs(directory, exist_ok=True)
    with open(directory + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
