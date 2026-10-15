# IIT Bombay iGEM 2026: dry-lab wiki (draft)

Built on the iGEM template `wiki-frozen-flask-markdown` (Flask + Python-Markdown + Frozen-Flask).
Only dry-lab pages are included. Pages are Markdown in `docs/`; layout in `wiki/`.

## Pages (in reading order)
Home -> Model (sequence, FAS interaction, bridge, metabolism, trust, process) -> Results ->
Engineering -> Software -> Contribution -> Sustainability.

## Run locally
    python -m venv venv
    venv\Scripts\activate        # Windows;  source venv/bin/activate on Linux/macOS
    pip install -r dependencies.txt
    python app.py                # http://127.0.0.1:8080

## Images: read this before deploying
iGEM requires images to live on static.igem.wiki, not in this repository.
- `static/figures/` holds the figures for **local preview only** and is git-ignored.
- Upload the files with the iGEM uploads tool, then run
  `python tools/set_image_base.py https://static.igem.wiki/teams/<ID>/wiki/<folder>/`
  to rewrite the image links.
- `tools/make_figures.py` redraws the four generated figures. Every number in it is copied
  from a team document (source in the comments).
- `lca_summary.jpg` and `lca_boundary.jpg` are cropped from the LCA report.

## Honesty rules this draft follows
Nothing here is validated against wet-lab data and the pages say so. Every claim carries
[computed] / [literature] / [hypothesis] / [pending]. Search the docs for `TODO` and `[pending]`
before publishing. Do not fabricate results, data or citations (see `.claude/RESPONSIBLE_AI_USE.md`).

## Before the freeze
- Replace the footer repository link with your team's gitlab.igem.org repository (keep the licence text).
- Fill team name, SDG text, attributions; confirm model versions and numbers across analyses.
- Wiki requirements, file-size limits and the freeze date were not readable when this was built:
  check https://teams.igem.org/go/deliverables/wiki and the competition calendar.

## This repository (Cloudflare Pages preview)
A copy of the draft wiki for **preview hosting on Cloudflare Pages**, not the official iGEM repo.
- Figures in `static/figures/` ARE committed here so the preview shows images. In the official
  iGEM repository they must instead be uploaded to static.igem.wiki (see above).
- Cloudflare build: `pip install -r dependencies.txt && python tools/build_static.py`,
  output directory `public`, Python 3.12.
- Every push to `main` is a production deploy; other branches get preview URLs.
- The footer still links the template repository. Do not use this repo as the final wiki.
