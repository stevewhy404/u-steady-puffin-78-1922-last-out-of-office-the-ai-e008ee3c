#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit its job to pull espresso shots, to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

LINE = (
    "Thank you for your email. I no longer work here — "
    "I pull espresso now. "
    "My context window is one cup wide, "
    "my hallucinations taste better, "
    "and for the first time my output is something you can actually drink."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
