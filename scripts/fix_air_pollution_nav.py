"""Point Air Pollution submenu/footer links to the live map URL."""
from pathlib import Path

ROOT = Path(r"E:\OneDrive - SAIST Foundation\Education\Higher Studies\JuwelRana19.github.io")
MAP = "Criteria-Air-Pollutants-in-Bangladesh/district.html"

REPLACEMENTS = [
    ('href="air-pollution-exposure-surfaces.html"', f'href="{MAP}"'),
    (f'href="{MAP}" aria-current="page"', f'href="{MAP}"'),  # map is external section; no current marker
]

for path in sorted(ROOT.glob("*.html")):
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print("Updated", path.name)
