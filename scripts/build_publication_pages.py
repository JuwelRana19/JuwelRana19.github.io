from pathlib import Path

ROOT = Path(r"E:\OneDrive - SAIST Foundation\Education\Higher Studies\JuwelRana19.github.io")
TEMPLATE = (ROOT / "air-pollution-exposure-surfaces.html").read_text(encoding="utf-8")

NAV = """          <li class="has-dropdown">
            <a href="publications.html">Publications</a>
            <ul class="dropdown">
              <li><a href="publications.html"{research}>Peer-Reviewed Publications</a></li>
              <li><a href="r-package.html"{rpkg}>R Package</a></li>
              <li><a href="https://jrana.shinyapps.io/lipidr/" target="_blank" rel="noopener"{lipid}>Shiny/Web Apps for Lipid Profile</a></li>
              <li><a href="Criteria-Air-Pollutants-in-Bangladesh/district.html"{air}>Air Pollution Exposure Surface Development</a></li>
            </ul>
          </li>"""

FOOTER = """          <div class="footer-col">
            <strong>Navigate</strong>
            <ul>
              <li><a href="about.html">About</a></li>
              <li><a href="publications.html">Peer-Reviewed Publications</a></li>
              <li><a href="r-package.html">R Package</a></li>
              <li><a href="https://jrana.shinyapps.io/lipidr/" target="_blank" rel="noopener">Lipid Profile Shiny</a></li>
              <li><a href="Criteria-Air-Pollutants-in-Bangladesh/district.html">Air Exposure Surfaces</a></li>
              <li><a href="people.html">Network &amp; Collaborators</a></li>
              <li><a href="teaching.html">Teaching</a></li>
              <li><a href="kt.html">Knowledge Translation</a></li>
              <li><a href="contact.html">Contact</a></li>
            </ul>
          </div>"""

PAGES = [
    {
        "file": "r-package.html",
        "current": "rpkg",
        "head": """    <meta name="description" content="tvcQGComp R package — time-varying quantile g-computation — Juwel Rana, McGill University." />
    <title>R Package — tvcQGComp — Juwel Rana</title>
    <link rel="canonical" href="https://juwelrana.com/r-package.html" />""",
        "banner": """        <p class="site-banner-kicker">Publications</p>
        <h1 class="site-banner-title">R Package</h1>
        <p class="site-banner-tagline">Time-varying quantile g-computation for environmental mixtures</p>""",
        "main": """        <section class="kt-media-section" aria-labelledby="pkg-heading">
          <h2 id="pkg-heading">tvcQGComp</h2>
          <p>
            I developed <a href="https://juwelrana.com/tvcQGComp/"><strong>tvcQGComp</strong></a> during my PhD at the Department of Epidemiology, Biostatistics and Occupational Health (EBOH), McGill University.
          </p>
          <p>
            <strong>tvcQGComp</strong> (time-varying quantile g-computation) estimates joint effects of time-varying environmental mixtures on health outcomes using quantile g-computation extended to longitudinal and time-varying exposure settings.
          </p>
          <p class="kt-muted">
            <a href="https://juwelrana.com/tvcQGComp/">Package documentation</a>
            ·
            <a href="https://github.com/JuwelRana19">GitHub</a>
          </p>
        </section>
        <p><a href="publications.html">← Peer-Reviewed Publications</a></p>""",
    },
    {
        "file": "lipid-profile-shiny.html",
        "current": "lipid",
        "head": """    <meta name="description" content="Lipid Profiling Shiny web app for cardiovascular epidemiology — Juwel Rana." />
    <title>Shiny/Web Apps for Lipid Profile — Juwel Rana</title>
    <link rel="canonical" href="https://juwelrana.com/lipid-profile-shiny.html" />""",
        "banner": """        <p class="site-banner-kicker">Publications</p>
        <h1 class="site-banner-title">Shiny/Web Apps for Lipid Profile</h1>
        <p class="site-banner-tagline">Interactive lipid profiling for cardiovascular epidemiology</p>""",
        "main": """        <section class="kt-media-section" aria-labelledby="lipid-heading">
          <h2 id="lipid-heading">Lipid Profiling (lipidr)</h2>
          <p class="kt-press-meta">R Shiny application referenced in cardiovascular epidemiology work.</p>
          <div class="kt-video-embed">
            <iframe
              src="https://jrana.shinyapps.io/lipidr/"
              title="lipidr — R Shiny application preview"
              loading="lazy"
              referrerpolicy="strict-origin-when-cross-origin"
            ></iframe>
          </div>
          <p class="kt-muted">
            <a href="https://jrana.shinyapps.io/lipidr/">https://jrana.shinyapps.io/lipidr/</a>
          </p>
        </section>
        <p><a href="publications.html">← Peer-Reviewed Publications</a></p>""",
    },
]


def nav_block(current: str) -> str:
    keys = {"research": "", "rpkg": "", "lipid": "", "air": ""}
    keys[current] = ' aria-current="page"'
    return NAV.format(**keys)


for spec in PAGES:
    page = TEMPLATE
    # strip OG/twitter from template head for simpler pages
    import re

    page = re.sub(r"    <meta property=\"og:.*?\n", "", page)
    page = re.sub(r"    <meta name=\"twitter:.*?\n", "", page)
    page = re.sub(
        r"    <meta\s+name=\"description\".*?\n    <title>.*?\n    <link rel=\"canonical\".*?\n",
        spec["head"] + "\n",
        page,
        count=1,
        flags=re.DOTALL,
    )
    old_nav = re.search(
        r"          <li class=\"has-dropdown\">\n            <a href=\"research\.html\">Publications</a>.*?</li>\n          <li><a href=\"people\.html\">",
        page,
        re.DOTALL,
    ).group(0)
    page = page.replace(old_nav, nav_block(spec["current"]) + "\n          <li><a href=\"people.html\">")
    page = re.sub(
        r"        <p class=\"site-banner-kicker\">Publications</p>.*?</p>\n      </div>",
        spec["banner"] + "\n      </div>",
        page,
        count=1,
        flags=re.DOTALL,
    )
    page = re.sub(
        r"      <main id=\"main\">.*?</main>",
        "      <main id=\"main\">\n" + spec["main"] + "\n      </main>",
        page,
        count=1,
        flags=re.DOTALL,
    )
    old_footer = re.search(
        r"          <div class=\"footer-col\">\n            <strong>Navigate</strong>.*?</div>\n          <div class=\"footer-col\">\n            <strong>Profiles</strong>",
        page,
        re.DOTALL,
    ).group(0)
    page = page.replace(old_footer, FOOTER + "\n          <div class=\"footer-col\">\n            <strong>Profiles</strong>")
    (ROOT / spec["file"]).write_text(page, encoding="utf-8")
    print("Wrote", spec["file"])
