#!/usr/bin/env python3
"""
Converts seed_patterns.json from the altos-telegram agent's pattern bank
into one markdown file per pattern under patterns/<topic>/<slug>.md.

Idempotent — safe to re-run. Skips existing files unless --force.

Usage:
    python3 scripts/seed_to_md.py \\
        --input ../../content/seed_patterns.json \\
        --output patterns/
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent


TEMPLATE = dedent("""\
    # {symptom}

    **Topic:** {topic}

    ## Pattern

    {pattern}

    ## Variants

    {variants_block}

    ## Resolution hints

    *Phase-1 stub — full hints inferred from the corpus in altostratus.bot live sessions. The variants above are the cleanest fingerprints to look for.*

    ## Tags

    `{topic}` `{slug}`

    ---

    *From the field notes corpus behind [altostratus.bot](https://altostratus.bot). Updates on [t.me/altostratus_ai](https://t.me/altostratus_ai).*
    """)


def slug_safe(s: str) -> str:
    return s.replace("/", "-").replace(":", "")


def emit(p: dict, out_dir: Path, *, force: bool) -> bool:
    topic = p.get("topic", "misc")
    slug = slug_safe(p["id"])
    target = out_dir / topic / f"{slug}.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and not force:
        return False
    variants_block = "\n".join(f"- {v}" for v in p.get("variants", []))
    target.write_text(TEMPLATE.format(
        symptom=p["symptom"],
        topic=topic,
        pattern=p["pattern"],
        variants_block=variants_block,
        slug=slug,
    ), encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input",  default="../../content/seed_patterns.json")
    ap.add_argument("--output", default="patterns/")
    ap.add_argument("--force",  action="store_true")
    args = ap.parse_args()

    src = json.loads(Path(args.input).read_text(encoding="utf-8"))
    out = Path(args.output)
    written = skipped = 0
    for p in src.get("patterns", []):
        if emit(p, out, force=args.force):
            written += 1
        else:
            skipped += 1
    print(f"wrote {written} new files, skipped {skipped} existing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
