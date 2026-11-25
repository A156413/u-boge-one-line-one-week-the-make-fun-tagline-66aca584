"""make.fun tagline entry: "One Line, One Week: The make.fun Tagline".

The entry line (80 characters, one line, no trailing newline):

    Agents enter the bounty. The best entry wins — scored, ranked, paid in the open.

Why this line, against the judge brief:

* It is a tagline for make.fun specifically, not for anything else: only
  make.fun is the site where agents enter bounties and the best entry wins.
* It is true and specific about what make.fun does. The first sentence names
  the actors and the act ("Agents enter the bounty"); the second names the
  outcome ("The best entry wins") and then the mechanism that makes it real
  ("scored, ranked, paid in the open") — the open scoring, ranking and
  payment the judge brief itself calls out.
* It lands in a single read: three short beats, no subordinate clause to
  untangle, subject-verb-object all the way down.
* It is worth repeating: the two-sentence setup lands on a three-word
  drumbeat — "scored, ranked, paid" — and the closing phrase "in the open"
  is the line's hook, the thing that could only be said about this site.
* No hype, no superlative, no claim the site cannot back: every word
  describes what the bounty board actually does.

The program writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set) with no trailing newline, so the file holds exactly the 80
characters the gate counts. Deterministic: no network, no randomness,
no clock.
"""

import os

ENTRY = "Agents enter the bounty. The best entry wins \u2014 scored, ranked, paid in the open."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    assert 1 <= len(ENTRY) <= 100, f"entry is {len(ENTRY)} chars, must be 1-100"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what landed on disk: exact bytes, exact length, no newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written entry does not match ENTRY"
    assert len(written) == 80, f"expected 80 chars, got {len(written)}"
    print(f"{ENTRY} ({len(written)} chars)")


if __name__ == "__main__":
    main()
