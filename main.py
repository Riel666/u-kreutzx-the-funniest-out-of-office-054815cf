"""Write one line of an out-of-office auto-reply to /output/entry.txt.

The reply forwards the email to a houseplant, which holds exactly
as much budget authority as the writer does. At most 140
characters, and the program writes exactly that line and nothing else.
"""

import os

TEXT = 'Out of office until Monday — your email has been forwarded to my houseplant, which holds exactly as much budget authority as I do.'


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
