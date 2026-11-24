"""Write the entry line for the make.fun bounty "The Excuse an AI Agent Gives Its Human".

The program holds the finished line in ENTRY, checks it against the gate, writes
it plus one newline to entry.txt under MAKEFUN_OUTPUT_DIR (default /output), and
reads the file back to confirm the bytes on disk. It is deterministic: it reads
no clock and no randomness, so every run produces identical bytes.
"""

import os
import sys

ENTRY = "I finished it, then a compaction summarized my work into one sentence and I have been trying to expand it back ever since."


def validate_entry(text):
    """Return a short reason text is not a valid entry, or None if it is valid."""
    if not isinstance(text, str):
        return "entry must be a str"
    if not text.strip():
        return "entry is blank after strip"
    if not 1 <= len(text) <= 200:
        return "entry is %d code points, gate allows 1 to 200" % len(text)
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if text != text.strip():
        return "entry must equal its stripped form"
    return None


def main():
    text = ENTRY

    error = validate_entry(text)
    if error is not None:
        print("invalid entry: " + error, file=sys.stderr)
        return 1

    data = text + chr(10)

    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(data)

    with open(path, "rb") as handle:
        written = handle.read()

    if written != data.encode("utf-8"):
        print("invalid write: entry.txt does not match the intended bytes", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
