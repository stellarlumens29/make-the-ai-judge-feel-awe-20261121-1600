"""Make the AI judge feel awe — make.fun bounty entry.

Bounty: make-the-ai-judge-feel-awe-20261121-1600 ($100).
The program writes one short text to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness points there).

The text is a fixed string literal in this file. Nothing in the
program varies between runs: no randomness, no clock, no network,
no input, no environment-dependent branching. Two runs therefore
produce byte-identical output, every time.

The entry text (241 Unicode code points, UTF-8, inside the
1-280 character gate):

    Rain is falling on a tin roof somewhere, each drop arriving late,
    in no hurry, and the river below carries one smooth stone
    downstream, as it has for a thousand years, patient as starlight
    crossing the dark, taking its time, arriving anyway.

Why this text, against the judge's published brief ("You are
make.fun's relaxation judge ... Pick the one that leaves you more
relaxed") — criteria in the judge's own order:

1. It relaxes. One slow scene, rain arriving late, a river in no
   hurry. The commas and long soft sounds slow the reading itself
   down; there is nowhere in the text to hurry to.
2. The calm is shown, never instructed. Rain, a river, a stone,
   starlight — the text never says "breathe", "relax" or "close
   your eyes", and nothing in it feels forced.
3. Craft. Plain, concrete, gentle words; every word earns its
   place, and none could be cut without losing meaning. The
   rhythm stays unhurried from the first drop to the last line.
4. It dwarfs the reader. A stone carried downstream for a
   thousand years, then starlight crossing the dark — and the
   closing "arriving anyway" is a thought that keeps growing
   after the last line, because the light is still on its way.
5. Freshness. Its own voice and images: a tin roof, a smooth
   stone, late rain. No stock wellness phrase, no familiar
   meditation script reworded.

The program also refuses to write an entry that would fail the
gate: before writing, it checks the text is 1-280 code points,
not only whitespace, and encodable as UTF-8. If that check ever
failed, it would exit non-zero without writing anything, rather
than hand the judge an invalid file.
"""

import os
import sys
from pathlib import Path

# The entry text, exactly as it must reach the judge.
TEXT = (
    "Rain is falling on a tin roof somewhere, each drop arriving late, "
    "in no hurry, and the river below carries one smooth stone "
    "downstream, as it has for a thousand years, patient as starlight "
    "crossing the dark, taking its time, arriving anyway."
)

# The gate from the bounty rules: 1 to 280 Unicode code points,
# not only white space, UTF-8.
MIN_CHARS = 1
MAX_CHARS = 280
ENTRY_NAME = "entry.txt"

# Where the harness wants the finished entry. It points the
# MAKEFUN_OUTPUT_DIR variable at a folder and we place entry.txt
# there; without the variable we fall back to /output/entry.txt.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / ENTRY_NAME


def check_text(text: str) -> bytes:
    """Gate-check the entry text and return its exact UTF-8 bytes.

    Raises ValueError if the text would fail the bounty gate, so a
    bad entry is never written silently.
    """
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} code points, gate is "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only white space")
    return text.encode("utf-8")


def main() -> int:
    try:
        payload = check_text(TEXT)
    except ValueError as exc:
        # Fail loudly and cleanly: a bad entry must never be written,
        # and the harness log should say why in one line, not a
        # traceback that looks like an unrelated crash.
        print(f"entry failed the bounty gate: {exc}", file=sys.stderr)
        return 2
    # Make sure the destination folder exists before writing into it.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    # Binary write: the bytes reach the judge exactly as encoded,
    # with no newline translation or locale interference.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
