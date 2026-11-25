#!/usr/bin/env python3
"""Write the one-line out-of-office reply entry to /output/entry.txt.

One out-of-office auto-reply, a single line, at most 140 characters,
that a real person would actually set. It opens like every out-of-office
ever written — "I'm out of the office until Monday" — then turns on a
surprise the reader does not see coming: if it is urgent, email twice,
because the second email proves you really mean it. The twist is the
whole joke, it lands on the last words, and nothing in the line could
be cut without losing the laugh. It is a filter disguised as a favour.
"""
import os

TEXT = "I'm out of the office until Monday. If it's urgent, email me twice — the second one proves you really mean it."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
