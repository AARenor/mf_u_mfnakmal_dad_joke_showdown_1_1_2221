"""Write one short dad joke for a make.fun bounty.

The entry text lives in TEXT. Running this program writes those exact bytes,
with no trailing newline, into entry.txt inside the output folder and prints
the character count to stderr.
"""

import os
import sys

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)

assert 1 <= len(TEXT) <= 280, "entry text must be 1 to 280 characters"


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
