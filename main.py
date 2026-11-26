"""One-line resignation letter, for make.fun's The One-Line Exit bounty.

Writes the letter to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only, no network.
"""
import os

LETTER = (
    "I am resigning effective immediately: the office plant has been "
    "promoted above me twice, and it has never once answered an email."
)


def main() -> None:
    if not 1 <= len(LETTER) <= 140:
        raise ValueError(f"letter must be 1-140 characters, got {len(LETTER)}")
    if not LETTER.strip():
        raise ValueError("letter must not be only whitespace")
    if "\n" in LETTER:
        raise ValueError("letter must be exactly one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
