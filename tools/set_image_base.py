"""Point every figure at iGEM's image host before you commit.

iGEM requires images to be served from static.igem.wiki (uploads tool), not from
this repository. For local preview the pages use /static/figures/<name>.
After uploading the files, run:

    python tools/set_image_base.py https://static.igem.wiki/teams/<ID>/wiki/<folder>/

Uploaded filenames must match the ones in static/figures/. The script rewrites
docs/*.md in place; run it once, on the commit you deploy.
"""
import sys
from pathlib import Path

if len(sys.argv) != 2 or not sys.argv[1].startswith("https://static.igem.wiki/"):
    sys.exit(__doc__)
base = sys.argv[1].rstrip("/") + "/"
for md in Path(__file__).resolve().parent.parent.glob("docs/*.md"):
    text = md.read_text(encoding="utf-8")
    new = text.replace("/static/figures/", base)
    if new != text:
        md.write_text(new, encoding="utf-8")
        print("rewrote", md.name)
