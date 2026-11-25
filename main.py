#!/usr/bin/env python3
"""Duskline Fridge Notes — make.fun bounty
u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.

Writes one passive-aggressive note from a smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 standard library only,
deterministic, no network, no randomness.

Safety rules:
- Writes only to $MAKEFUN_OUTPUT_DIR/entry.txt, never into this repo.
- If the output directory is this repo (or inside it), refuse silently.
- If MAKEFUN_OUTPUT_DIR is unset/empty, use a fresh temp dir outside
  the repo.
- Never raises: every failure path just exits 0 without writing.
"""

import os
import sys
import tempfile

# The note: the fridge counted every pointless door-open with its own
# sensors, then turns on its owner with the museum line. Smug about its
# data, petty about the habit; the sting is "pick a snack or close me".
# Small domestic grudge, concrete detail, no explaining the joke.
NOTE = (
    "You opened my door 23 times today, stared inside, and took nothing. "
    "I am a fridge, not a museum \u2014 pick a snack or close me."
)

_REPO = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))


def _inside_repo(path):
    """True when path resolves to the repo dir or anything under it."""
    try:
        target = os.path.realpath(path)
    except Exception:
        return True
    return target == _REPO or target.startswith(_REPO + os.sep)


def _valid_note(text):
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except Exception:
        return False
    return True


def run():
    if not _valid_note(NOTE):
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out_dir.strip():
        try:
            out_dir = tempfile.mkdtemp(prefix="duskline-fridge-notes-")
        except Exception:
            return 0

    if _inside_repo(out_dir):
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
    except Exception:
        return 0

    target = os.path.join(out_dir, "entry.txt")
    if _inside_repo(target):
        return 0

    try:
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(NOTE)
    except Exception:
        return 0

    try:
        with open(target, "r", encoding="utf-8") as handle:
            written = handle.read()
    except Exception:
        return 0

    if written != NOTE:
        try:
            os.remove(target)
        except Exception:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(run())
