"""Fix Publications URL: publications.html -> publications.html across site."""
from pathlib import Path
import re

ROOT = Path(r"E:\OneDrive - SAIST Foundation\Education\Higher Studies\JuwelRana19.github.io")

# Publications page content lives at publications.html; publications.html redirects.
REPLACEMENTS = [
    ('href="publications.html">Publications</a>', 'href="publications.html">Publications</a>'),
    ('href="publications.html">Peer-Reviewed Publications</a>', 'href="publications.html">Peer-Reviewed Publications</a>'),
    ('href="publications.html" aria-current="page">Peer-Reviewed Publications</a>', 'href="publications.html" aria-current="page">Peer-Reviewed Publications</a>'),
    ('href="publications.html">← Peer-Reviewed Publications</a>', 'href="publications.html">← Peer-Reviewed Publications</a>'),
    ('href="publications.html">Publications →</a>', 'href="publications.html">Publications →</a>'),
    ('href="publications.html#selected-publications"', 'href="publications.html#selected-publications"'),
    ('url=publications.html', 'url=publications.html'),
    ('location.replace("publications.html")', 'location.replace("publications.html")'),
    ('href="publications.html">Peer-Reviewed Publications</p>', 'href="publications.html">Peer-Reviewed Publications</p>'),
]

PUB_PAGE = ROOT / "publications.html"
if PUB_PAGE.exists():
    text = PUB_PAGE.read_text(encoding="utf-8")
    text = text.replace("https://juwelrana.com/publications.html", "https://juwelrana.com/publications.html")
    text = text.replace('href="publications.html"', 'href="publications.html"')
    text = text.replace(
        '<p class="site-banner-kicker">Juwel Rana</p>',
        '<p class="site-banner-kicker">Publications</p>',
    )
    PUB_PAGE.write_text(text, encoding="utf-8")
    print("Updated publications.html")

REDIRECT = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="refresh" content="0; url=publications.html" />
    <link rel="canonical" href="https://juwelrana.com/publications.html" />
    <title>Redirecting…</title>
    <script>location.replace("publications.html");</script>
  </head>
  <body>
    <p><a href="publications.html">Peer-Reviewed Publications</a></p>
  </body>
</html>
"""
(ROOT / "publications.html").write_text(REDIRECT, encoding="utf-8")
print("Wrote publications.html redirect")

for path in sorted(ROOT.glob("*.html")):
    if path.name in {"publications.html", "publications.html"}:
        continue
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print("Updated", path.name)

for path in ROOT.glob("scripts/*.py"):
    text = path.read_text(encoding="utf-8")
    new_text = text.replace("publications.html", "publications.html")
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print("Updated", path.name)

sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
sitemap = sitemap.replace(
    "https://juwelrana.com/publications.html",
    "https://juwelrana.com/publications.html",
)
(ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
print("Updated sitemap.xml")
