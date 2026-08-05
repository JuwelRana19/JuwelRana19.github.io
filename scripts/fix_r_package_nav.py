"""Point R Package submenu/footer links to tvcQGComp docs."""
from pathlib import Path

ROOT = Path(r"E:\OneDrive - SAIST Foundation\Education\Higher Studies\JuwelRana19.github.io")
PKG = "https://juwelrana.com/tvcQGComp/"

for path in sorted(ROOT.glob("*.html")):
    if path.name == "r-package.html":
        continue
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace('href="r-package.html"', f'href="{PKG}" target="_blank" rel="noopener"')
    if text != original:
        path.write_text(text, encoding="utf-8")
        print("Updated", path.name)
