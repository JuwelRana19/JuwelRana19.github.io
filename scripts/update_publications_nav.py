"""Update Publications submenu across juwelrana.com HTML pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"E:\OneDrive - SAIST Foundation\Education\Higher Studies\JuwelRana19.github.io")

DROPDOWN_RE = re.compile(
    r'(<li class="has-dropdown">\s*<a href="publications\.html">Publications</a>\s*<ul class="dropdown">)(.*?)(</ul>\s*</li>)',
    re.DOTALL,
)

FOOTER_OLD = re.compile(
    r'<li><a href="publications\.html">Publications</a></li>\s*'
    r'<li><a href="software\.html">Software &amp; Tools</a></li>',
    re.DOTALL,
)

AIR_MAP = "Criteria-Air-Pollutants-in-Bangladesh/district.html"
LIPID_SHINY = "https://jrana.shinyapps.io/lipidr/"
R_PACKAGE = "https://juwelrana.com/tvcQGComp/"

FOOTER_NEW = f"""<li><a href="publications.html">Peer-Reviewed Publications</a></li>
              <li><a href="{R_PACKAGE}" target="_blank" rel="noopener">R Package</a></li>
              <li><a href="{LIPID_SHINY}" target="_blank" rel="noopener">Lipid Profile Shiny</a></li>
              <li><a href="{AIR_MAP}">Air Exposure Surfaces</a></li>"""


def dropdown_items(current: str | None) -> str:
    def link(href: str, label: str, key: str, external: bool = False) -> str:
        cur = ' aria-current="page"' if current == key else ""
        extra = ' target="_blank" rel="noopener"' if external else ""
        return f'              <li><a href="{href}"{extra}{cur}>{label}</a></li>'

    return "\n".join(
        [
            link("publications.html", "Peer-Reviewed Publications", "publications"),
            link(R_PACKAGE, "R Package", "r-package", external=True),
            link(LIPID_SHINY, "Shiny/Web Apps for Lipid Profile", "lipid", external=True),
            link(
                AIR_MAP,
                "Air Pollution Exposure Surface Development",
                "air",
            ),
        ]
    )


PAGE_CURRENT = {
    "publications.html": "publications",
}


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    current = PAGE_CURRENT.get(path.name)

    if DROPDOWN_RE.search(text):
        text = DROPDOWN_RE.sub(
            lambda m: m.group(1) + "\n" + dropdown_items(current) + "\n            " + m.group(3),
            text,
            count=1,
        )

    if FOOTER_OLD.search(text):
        text = FOOTER_OLD.sub(FOOTER_NEW, text, count=1)

    if path.name == "publications.html":
        text = text.replace(
            "<h1 class=\"site-banner-title\">Publications</h1>",
            "<h1 class=\"site-banner-title\">Peer-Reviewed Publications</h1>",
        )
        text = text.replace("<title>Publications — Juwel Rana</title>", "<title>Peer-Reviewed Publications — Juwel Rana</title>")
        text = text.replace('content="Publications — Juwel Rana"', 'content="Peer-Reviewed Publications — Juwel Rana"')

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for path in sorted(ROOT.glob("*.html")):
        if patch_file(path):
            changed.append(path.name)
    print("Updated:", ", ".join(changed) if changed else "(none)")


if __name__ == "__main__":
    main()
