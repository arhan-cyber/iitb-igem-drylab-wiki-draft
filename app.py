import json
import re
from html import escape
from os import path

import markdown
from flask import Flask, render_template
from flask_frozen import Freezer

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
# app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

# Markdown extensions enabled when converting docs/*.md to HTML.
# "extra" bundles tables, fenced code blocks, footnotes, attribute lists, etc.
# See https://python-markdown.github.io/extensions/
MARKDOWN_EXTENSIONS = ['extra', 'sane_lists', 'smarty', 'toc']


# Page titles where the slug does not title-case cleanly.
TITLES = {
    'fas-interaction': 'FAS Interaction',
    'life-cycle-assessment': 'Life Cycle Assessment',
}


# ---------------------------------------------------------------------------
# Citations. Authors write [@key] or [@key1, @key2] (optionally [@key|note]) in
# docs/<page>.md; docs/references.json holds the reference metadata. Numbers are
# assigned per page in order of first appearance, and a reference list and a
# source table are appended to the page.
# ---------------------------------------------------------------------------
CITE_RE = re.compile(r'\[@([A-Za-z0-9_\-]+(?:\s*[,;]\s*@?[A-Za-z0-9_\-]+)*)(?:\|([^\]]*))?\]')
HEADING_RE = re.compile(r'^(#{2,3})\s+(.*?)\s*(?:\{#([A-Za-z0-9_\-]+)\})?\s*$')


def load_references():
    with open('docs/references.json', encoding='utf-8') as ref_file:
        return {ref['key']: ref for ref in json.load(ref_file)}


def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower()).strip()
    return re.sub(r'[\s_-]+', '-', text)


def format_reference(ref):
    """Reference-list entry as an HTML string."""
    head = ' '.join(part for part in (
        escape(ref['authors']) if ref.get('authors') else '',
        f"({escape(str(ref['year']))})" if ref.get('year') else '') if part)
    out = f"{head}. {escape(ref['title'])}." if head else f"{escape(ref['title'])}."
    if ref.get('journal'):
        cite = f"<em>{escape(ref['journal'])}</em>"
        if ref.get('volume'):
            cite += f" {escape(str(ref['volume']))}"
            if ref.get('pages'):
                cite += f":{escape(str(ref['pages']))}"
        elif ref.get('pages'):
            cite += f", {escape(str(ref['pages']))}"
        out += f" {cite}."
    if ref.get('note'):
        out += f" {escape(ref['note'])}"
    if ref.get('doi'):
        doi = escape(ref['doi'])
        out += f' <a href="https://doi.org/{doi}">doi:{doi}</a>'
    elif ref.get('url'):
        url = escape(ref['url'])
        out += f' <a href="{url}">{url}</a>'
    if ref.get('accessed'):
        out += f" (accessed {escape(ref['accessed'])})"
    return out


def short_reference(ref):
    if ref.get('authors'):
        first = ref['authors'].split(',')[0].split(' and ')[0]
    else:
        first = ref['title']
    return f"{escape(first)} ({escape(str(ref['year']))})" if ref.get('year') else escape(first)


def apply_citations(text, references):
    """Replace [@key] macros by numbered superscripts.

    Returns the new text and the cited entries in order of first appearance:
    {'key', 'num', 'where': [(heading, anchor)], 'notes': [str]}.
    """
    cited = {}
    order = []
    state = {'heading': None, 'anchor': None}

    def repl(match):
        nums = []
        for key in re.findall(r'[A-Za-z0-9_\-]+', match.group(1)):
            if key not in references:
                raise KeyError(f'unknown reference key "{key}" in docs')
            if key not in cited:
                cited[key] = {'key': key, 'num': len(order) + 1, 'where': [], 'notes': []}
                order.append(cited[key])
            entry = cited[key]
            where = (state['heading'] or 'Introductory note', state['anchor'])
            if where not in entry['where']:
                entry['where'].append(where)
            note = (match.group(2) or '').strip()
            if note and note not in entry['notes']:
                entry['notes'].append(note)
            nums.append(entry['num'])
        links = ',&#8202;'.join(f'<a href="#ref-{n}">{n}</a>' for n in nums)
        return f'<sup class="r">{links}</sup>'

    in_fence = False
    out_lines = []
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
        if not in_fence:
            heading = HEADING_RE.match(line)
            if heading:
                title = re.sub(r'[*_`]', '', heading.group(2))
                state['heading'] = title
                state['anchor'] = heading.group(3) or slugify(title)
            line = CITE_RE.sub(repl, line)
        out_lines.append(line)
    return '\n'.join(out_lines), order


def references_html(order, references):
    """Reference list and source table for the cited entries (raw HTML)."""
    if not order:
        return ''
    items = ''.join(
        f'<li id="ref-{e["num"]}">{format_reference(references[e["key"]])}</li>' for e in order)
    rows = ''
    for e in order:
        ref = references[e['key']]
        places = '; '.join(f'<a href="#{escape(a)}">{escape(h)}</a>' if a else escape(h)
                           for h, a in e['where'])
        if e['notes']:
            places += (' &mdash; ' if places else '') + escape('; '.join(e['notes']))
        rows += (f'<tr><td>{e["num"]}</td><td>{short_reference(ref)}</td><td>{places}</td></tr>')
    return (
        '<h2 id="references">References</h2>\n'
        f'<ol class="ref-list">{items}</ol>\n'
        '<h3 id="source-table">Source table</h3>\n'
        '<table class="table table-sm ref-table"><thead><tr><th>#</th><th>Reference</th>'
        f'<th>Supports (where in this page)</th></tr></thead><tbody>{rows}</tbody></table>\n')


NAV_TAIL = re.compile(r'<hr />\s*<p>\s*<strong>(?:Previous|Next)', re.S)


def split_nav(html):
    """Separate a trailing "Previous / Next" block (after the last <hr />) from the body."""
    cut = html.rfind('<hr />')
    if cut != -1 and NAV_TAIL.match(html, cut):
        return html[:cut], html[cut:]
    return html, ''


def wrap_sections(html):
    """Wrap every <h2> section in <details class="acc" open>, heading inside <summary>."""
    pieces = re.split(r'(?m)^(?=<h2[ >])', html)
    head, sections = pieces[0], pieces[1:]
    wrapped = []
    for sec in sections:
        match = re.match(r'(<h2[^>]*>.*?</h2>)\s*', sec, re.S)
        heading, body = match.group(1), sec[match.end():]
        cls = 'acc refs' if 'id="references"' in heading else 'acc'
        wrapped.append(f'<details class="{cls}" open><summary>{heading}</summary>'
                       f'<div class="acc-body">\n{body}</div></details>\n')
    return head + ''.join(wrapped)


def render_markdown(page):
    """Read docs/<page>.md and convert it to an HTML fragment."""
    with open(f'docs/{page}.md', encoding='utf-8') as md_file:
        text = md_file.read()
    references = load_references()
    text, order = apply_citations(text, references)
    html = markdown.markdown(text, extensions=MARKDOWN_EXTENSIONS)
    body, nav = split_nav(html)
    refs = references_html(order, references)
    if refs:
        body += refs
    return wrap_sections(body) + nav


@app.cli.command()
def freeze():
    freezer.freeze()


@app.cli.command()
def serve():
    freezer.run()


@app.route('/')
def home():
    md_content = render_markdown('home')
    return render_template('base.html',
                           title='Home',
                           md_content=md_content)


@app.route('/<page>')
def pages(page):
    md_content = render_markdown(page.lower())
    return render_template('base.html',
                           title=TITLES.get(page.lower(), page.title().replace('-', ' ')),
                           md_content=md_content)


# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    app.run(port=8080)
