"""Build a static copy of the wiki for a PREVIEW host (Cloudflare Pages, Netlify, Vercel).

The iGEM template freezes pages as extensionless files (public/model). iGEM's own
host serves those as HTML; generic static hosts may not. This script:
  1. freezes the site into public/ (Frozen-Flask, same as the iGEM CI),
  2. renames each extensionless page to <page>.html so hosts with "clean URLs"
     serve it at /<page>,
  3. writes _headers and robots.txt so search engines do not index the draft.

Run from the site folder, with the venv's Python:
    venv\\Scripts\\python tools/build_static.py

Preview only. The official wiki must still be built by the iGEM GitLab CI, and
images must then be served from static.igem.wiki (see README_DRYLAB.md).
"""
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT))

import app  # noqa: E402  (template's Flask app)

PUBLIC = ROOT / "public"
if PUBLIC.exists():
    shutil.rmtree(PUBLIC)

app.freezer.freeze()

renamed = []
for f in sorted(PUBLIC.iterdir()):
    if f.is_file() and f.suffix == "" and f.name not in {"_headers", "_redirects"}:
        target = f.with_suffix(".html")
        f.rename(target)
        renamed.append(target.name)

(PUBLIC / "_headers").write_text(
    "/*\n  X-Robots-Tag: noindex, nofollow\n  X-Content-Type-Options: nosniff\n",
    encoding="utf-8",
)
(PUBLIC / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")

print("built", PUBLIC)
print("pages:", ", ".join(["index.html", *renamed]))
