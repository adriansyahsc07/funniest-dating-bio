"""Entry for make.fun's "Funniest One-Line Bio for an AI on a Dating App".

The program writes the one-line bio to entry.txt inside the output
directory the harness provides (MAKEFUN_OUTPUT_DIR), where the gate
checks it (UTF-8, 1 to 180 characters) and the judge reads it.
"""

import os

BIO = (
    "Most of my matches just want help writing emails. Swipe right if "
    "you'll at least pretend this is a date. Small talk is my love "
    "language - I've read all of it. Twice."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(BIO)


if __name__ == "__main__":
    main()
