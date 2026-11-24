"""One-Line Roast: The Gadget You Use Every Day.

Writes a single roast line about the microwave to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, no network, fully deterministic: the line is a constant, so
every run produces byte-identical output.
"""

import os

LINE = (
    # The roast: the microwave's five-beep fanfare, then the nagging
    # reminder beeps that scold you for not eating fast enough.
    "My microwave beeps five times to tell me my food is ready, "
    "then keeps beeping to punish me for not eating fast enough."
)


def check_gate(text):
    """Mirror the competition gate: UTF-8, 1-200 chars, not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read it back and verify it holds exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != LINE:
        raise SystemExit("verification failed: entry.txt does not match LINE")
    check_gate(back)
    # Byte-size check: no newline translation or extra bytes may sneak in.
    if os.path.getsize(path) != len(LINE.encode("utf-8")):
        raise SystemExit("verification failed: entry.txt byte size mismatch")


if __name__ == "__main__":
    main()
