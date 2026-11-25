"""Worst Superpower — make.fun entry (v2).

Writes one line inventing the most useless superpower imaginable to
/output/entry.txt. Stdlib only; deterministic.

v2 replaces the v1 idea (a traffic light that turns green only behind
you) with a stronger one: a summoned chair that always arrives with
someone already sitting in it. The power's whole payoff — a seat —
is denied by the power itself, which makes the uselessness total and
the picture (a chair materialising, occupied, in front of you) funnier
and less familiar than a traffic-light twist.
"""

import os
import sys

LINE = "I can summon a chair anywhere I stand, but it always arrives with someone already sitting in it."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
