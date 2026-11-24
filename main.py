"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy to /output/entry.txt.
Deterministic: the same line on every run. Python standard library only.
"""

import os

ENTRY = (
    "Upload failed: your Wi-Fi gave up five minutes ago and didn't tell anyone. "
    "Your file is safe. Your internet is not."
)


def main() -> None:
    # Gate self-check: one line, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
