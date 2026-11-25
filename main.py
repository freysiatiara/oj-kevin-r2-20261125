#!/usr/bin/env python3
"""Round 2 entry for 'The Funniest Office Joke, Judged Head to Head'.

Writes a single one-line office joke to /output/entry.txt (or to the path
given by ENTRY_OUTPUT, defaulting to /output/entry.txt).

Stdlib only. No network, no tempfiles.
"""

import os

JOKE = (
    "I spent the whole call on mute, then unmuted to say 'sorry, I was on "
    "mute' \u2014 the most honest thing I've said at work all year."
)


def main() -> None:
    text = JOKE
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
