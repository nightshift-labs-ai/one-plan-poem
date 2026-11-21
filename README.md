`main.py` (Python 3.13, standard library only) writes one short poem, UTF-8 with no trailing newline, to `/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set; run it with `python3 main.py` (for example `MAKEFUN_OUTPUT_DIR=out python3 main.py`). It exits non-zero if the text is not 1 to 280 code points or is only white space. The text, 273 Unicode code points long, is:

```
Controls

You have control, he said.
I have control, I said.
You have control, he said,
the way they teach it,
so the plane is never no one's.

He lifted his hands from the yoke
and set them on his knees.
Forty years he had flown.
He looked out the window
like a passenger.
```
