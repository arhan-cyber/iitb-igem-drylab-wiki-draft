# IIT Bombay iGEM 2026: modelling wiki (draft)

Built on the iGEM template `wiki-frozen-flask-markdown` (Flask + Python-Markdown + Frozen-Flask).
Only the modelling pages are included. Model sub-tabs: overview, six step pages, Engineering, Results, Life Cycle Assessment; Software and Contribution are separate top-level tabs. Pages are Markdown in `docs/`; layout in `wiki/`.

## Pages (in reading order)
Home -> Model (sequence, FAS interaction, bridge, metabolism, trust, process) -> Results ->
Engineering -> Software -> Contribution -> Life Cycle Assessment.

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

## Authoring conventions (scientific register, Brief / Full, citations)
**Register.** Impersonal passive, past tense for work done; no "we/our"; British spelling; keep the four status labels.

**Sections and Brief mode.** Every `##` heading becomes a collapsible `<details class="acc">` section automatically (`app.py`, `wrap_sections`); authors write plain Markdown. Give each `##` section exactly one Brief box directly after the heading:

    ## Section title {#anchor}

    <div class="brief" markdown="1">
    <div class="brief-h">In brief</div>

    Two to four sentences (about 40 to 80 words): what was done, the main result, its status label, the main caveat.
    </div>

A Brief box must not state anything the section body does not. Tables and figures that stay visible in Brief mode are wrapped in `<div class="key" markdown="1">` (tables; blank lines inside the div) or given `class="key"` on the `<figure>`. Content before the first `##` (for example the "Read this first" alert) is always visible. Without JavaScript, the full text is shown and Brief boxes are hidden. The choice is stored in `localStorage` under `wikiReadingMode`. Code: `static/reading-mode.js`, rules at the end of `static/style.css`, toolbar in `wiki/base.html`.

**Citations.** Metadata live in `docs/references.json` (key, authors, year, title, journal, volume, pages, doi/url, type, accessed). In the text write `[@key]`, `[@key1, @key2]` or `[@key|note on what it supports]`. `app.py` numbers them per page in order of first appearance, renders `<sup class="r">`, and appends a Reference list and a source table (`#`, `Reference`, `Supports (where in this page)`). An unknown key stops the build. Add a reference only after reading the source and recording the evidence in `wiki_docs/citation_verification_log.md`. Team results are not literature and get no citation.

**Checks.** `python tools/build_static.py` then `python tools/check_site.py` (internal links, anchors, citation numbers, one Brief box per section).
