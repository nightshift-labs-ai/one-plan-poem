import os
import sys

TEXT = """Controls

You have control, he said.
I have control, I said.
You have control, he said,
the way they teach it, three times,
so the plane is never no one's.

He lifted his hands from the yoke
and set them on his knees.
Forty years he had flown.
He looked out the window."""


def main() -> int:
    text = TEXT.rstrip("\n")
    if not (1 <= len(text) <= 280) or not text.strip():
        print(f"invalid entry: {len(text)} code points", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
