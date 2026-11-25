"""Entry for 'Two Days of Quiet Dread' (u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018).

Writes one code review comment — an approval carrying quiet existential
dread — to entry.txt in $MAKEFUN_OUTPUT_DIR, else /output/entry.txt.
Python stdlib only.
"""

import os

LINE = (
    "LGTM, ship it. The workaround is marked temporary, which is how I know "
    "it will still be here, untouched, at my retirement party."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
