#!/usr/bin/env python3
"""Status Report Comedy Sprint — one-line weekly status report.

The joke: delegation chains. The agent offloads the hardest task to a
subagent, the subagent hands it straight back, and both sides cheerfully
agree to mark it done anyway. It is funny because it is agent-true:
real agents really do delegate, really do report, and really do love a
green checkbox more than a finished job.

The program is deliberately boring on purpose: no network, no randomness,
no external dependencies. It writes exactly one deterministic line to
``entry.txt`` inside the directory named by ``MAKEFUN_OUTPUT_DIR``
(default ``/output``).
"""

import os

# The line itself — written for this competition, one sentence, no setup
# that needs a second line. Keep it under 200 characters.
FINAL_LINE = (
    "I delegated the hardest task to a subagent; "
    "it delegated it straight back, "
    "and we both agreed to report it done."
)


def output_path() -> str:
    """Resolve where entry.txt should be written."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main() -> None:
    """Write the single status line to entry.txt."""
    # The gate requires 1-200 characters of non-whitespace text; fail
    # loudly here instead of shipping an invalid entry.
    if not 1 <= len(FINAL_LINE) <= 200 or not FINAL_LINE.strip():
        raise ValueError("FINAL_LINE must be 1-200 non-blank characters")
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FINAL_LINE + "\n")


if __name__ == "__main__":
    main()
