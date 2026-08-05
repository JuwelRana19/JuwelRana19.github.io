"""Point Lipid Profile submenu/footer links to the live Shiny app."""
from pathlib import Path

ROOT = Path(r"E:\OneDrive - SAIST Foundation\Education\Higher Studies\JuwelRana19.github.io")
SHINY = "https://jrana.shinyapps.io/lipidr/"

REPLACEMENTS = [
    ('href="lipid-profile-shiny.html">Shiny/Web Apps for Lipid Profile', f'href="{SHINY}" target="_blank" rel="noopener">Shiny/Web Apps for Lipid Profile'),
    ('href="lipid-profile-shiny.html" aria-current="page">Shiny/Web Apps for Lipid Profile', f'href="{SHINY}" target="_blank" rel="noopener">Shiny/Web Apps for Lipid Profile'),
    ('href="lipid-profile-shiny.html">Lipid Profile Shiny', f'href="{SHINY}" target="_blank" rel="noopener">Lipid Profile Shiny'),
]

for path in sorted(ROOT.glob("*.html")):
    if path.name == "lipid-profile-shiny.html":
        continue
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print("Updated", path.name)
