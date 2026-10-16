"""Check the built site in public/: internal links, anchors, citations and Brief-mode structure.

Run after tools/build_static.py:
    venv\\Scripts\\python tools/check_site.py
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / "public"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.hrefs, self.sups = set(), [], []
        self.sections, self.briefs_per_section = 0, []
        self._stack = []
        self._cur_brief = None
        self._in_sup = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href") is not None:
            self.hrefs.append(a["href"])
            if self._in_sup and a["href"].startswith("#ref-"):
                self.sups.append(a["href"][1:])
        if tag == "sup" and "r" in (a.get("class") or "").split():
            self._in_sup = True
        if tag == "details" and "acc" in (a.get("class") or "").split():
            self.sections += 1
            self.briefs_per_section.append([0, "refs" in a["class"].split()])
        if tag == "div" and "brief" in (a.get("class") or "").split() and self.briefs_per_section:
            self.briefs_per_section[-1][0] += 1

    def handle_endtag(self, tag):
        if tag == "sup":
            self._in_sup = False


def main():
    pages = {}
    for f in sorted(PUBLIC.glob("*.html")):
        p = Page()
        p.feed(f.read_text(encoding="utf-8"))
        pages[f.stem] = p
    errors = []
    for name, p in pages.items():
        label = name
        for href in p.hrefs:
            if re.match(r"(https?:|mailto:)", href):
                continue
            target, _, frag = href.partition("#")
            target = target.strip("/").removesuffix(".html")
            if target.startswith("static") or target.startswith("."):
                continue
            tpage = pages.get(target or "index") if target else p
            if tpage is None:
                errors.append(f"{label}: link to missing page {href}")
            elif frag and frag not in tpage.ids:
                errors.append(f"{label}: missing anchor {href}")
        for ref in p.sups:
            if ref not in p.ids:
                errors.append(f"{label}: citation {ref} has no reference entry")
        for count, is_refs in p.briefs_per_section:
            if not is_refs and count != 1:
                errors.append(f"{label}: a section has {count} brief boxes (expected 1)")
        print(f"{label:24s} sections={p.sections:2d} citations={len(set(p.sups)):2d}")
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
