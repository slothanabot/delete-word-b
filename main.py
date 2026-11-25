#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary - make.fun entry (account B / Slothana).

Writes one word to /output/entry.txt: the single word this entry would
erase from the dictionary forever.

The pick: "queue". Five letters, pronounced "Q": four of them are
silent passengers doing nothing at all. Delete it and the spelling
nightmare ends - the joke lands the instant the word is gone, and the
humour comes from the word itself. It is also a fresher pick than the
obvious crowd-pleaser, so it stands out in a head-to-head. Standard
library only. No network, no secrets, no reading anything outside this
repository.
"""

import os
import stat

WORD = "queue"


def main() -> None:
    text = WORD.strip()
    if not (1 <= len(text) <= 77):
        raise SystemExit(f"word is {len(text)} characters, must be 1-77")
    if not text.isalpha() or text != text.lower():
        raise SystemExit("entry must be one lowercase word, letters only")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
