# juwelrana.github.io

Personal academic site for **Juwel Rana** (static HTML + CSS). Live site is published with [GitHub Pages](https://pages.github.com/).

## What’s in this repo

| Path | Purpose |
|------|---------|
| `index.html` | Home page (bio, links, contact) |
| `research.html` | Selected publications |
| `css/style.css` | Styles |
| `doc/` | Add `CV.pdf` here if you want a downloadable CV |
| `.nojekyll` | Tells GitHub Pages not to run Jekyll (plain static files) |

## Publish the site

1. Push these files to the **`master`** or **`main`** branch (repo root: `index.html` at top level).
2. On GitHub: **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**, branch **`main`** or **`master`**, folder **`/ (root)`**, then **Save**.

After a minute or two, the site URL shown at the top of the Pages settings should load.

### User site URL (important)

For a **user** site at `https://<username>.github.io`, the repository name must be **`<username>.github.io`** (same spelling as your GitHub username).

- If your username is **`JuwelRana19`**, rename this repository to **`JuwelRana19.github.io`** so the site is served at **`https://juwelrana19.github.io`** (GitHub treats username case as case-insensitive for this URL).

If you keep the name **`juwelrana.github.io`** without matching the username, Pages may treat it as a **project** site instead, with a URL like `https://<username>.github.io/juwelrana.github.io/`. Check the exact URL in **Settings → Pages** after the first successful deploy.

## Optional

- Delete any stray files from early experiments (for example an odd `.html` filename) so only the intended pages remain in the root.
- Add `doc/CV.pdf` and the home page CV link will work.
