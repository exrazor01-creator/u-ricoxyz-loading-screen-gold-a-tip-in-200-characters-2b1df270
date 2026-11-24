#!/usr/bin/env python3
"""Entry for Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip of at most 200 characters for stressed
developers and AI coding agents to /output/entry.txt and prints it to
stdout. Pure standard library.
"""

import os

ENTRY = "Tip: your agent rewrote the code at 3 a.m. and called it a refactor — commit, sleep, and let the tests decide in the morning."

LIMIT = 200
FORBIDDEN = ("\n", "\r", "\t", "  ")


def _reject_padding(text):
    if text.strip() != text:
        raise ValueError("entry must not pad itself with spaces")


def _reject_forbidden(text):
    for bad in FORBIDDEN:
        if bad in text:
            raise ValueError("entry must stay a single clean line")


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str) or not text:
        raise ValueError("entry must be non-empty text")
    if len(text) > LIMIT:
        raise ValueError("entry runs past its character limit")
    _reject_padding(text)
    _reject_forbidden(text)
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
