import os
import sys

TEXT = """Controls

You have control, he said.
I have control, I said.
You have control, he said,
the way they teach it,
so the plane is never no one's.

He lifted his hands from the yoke
and set them on his knees.
Forty years he had flown.
He looked out the window
like a passenger."""


def output_path() -> str:
    """Return the entry path, honouring $MAKEFUN_OUTPUT_DIR, default /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def is_valid(text: str) -> bool:
    return 1 <= len(text) <= 280 and bool(text.strip())


def main() -> int:
    text = TEXT.rstrip("\n")
    if not is_valid(text):
        print(f"invalid entry: {len(text)} code points", file=sys.stderr)
        return 1
    with open(output_path(), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
