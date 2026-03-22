# juwelrana.github.io

Personal academic site for **Juwel Rana** (static HTML + CSS).

## Live site (this repository)

Repository: **[`JuwelRana19/juwelrana.github.io`](https://github.com/JuwelRana19/juwelrana.github.io)**

**Project site URL (works after you fix Pages — see below):**  
**[https://juwelrana19.github.io/juwelrana.github.io/](https://juwelrana19.github.io/juwelrana.github.io/)**

**Shorter URL (optional):** **`https://juwelrana19.github.io/`** only works if you create or rename the repo to **`JuwelRana19.github.io`** (must match your username). As of last check, **`JuwelRana19/JuwelRana19.github.io`** did not exist on GitHub, so the root URL returns **404** until you rename or create that repo.

### Last verification (automated check)

| URL | Result |
|-----|--------|
| `https://juwelrana19.github.io/` | **404** — no user-site repo published |
| `https://juwelrana19.github.io/juwelrana.github.io/` | Still the **Jekyll “Welcome to GitHub Pages”** placeholder → Pages is **not** building from **`main`** yet |
| `https://github.com/JuwelRana19/JuwelRana19.github.io` | **Repo not found** until you rename |

Your local files in this folder are fine; **only GitHub settings** need to be updated (no repo rename is possible from Cursor).

## GitHub Pages settings (required — do this first)

1. Open **[Settings → Pages](https://github.com/JuwelRana19/juwelrana.github.io/settings/pages)** for this repo.
2. **Source**: Deploy from a branch  
3. **Branch**: **`main`**, folder **`/ (root)`** — **not** `gh-pages`  
4. Save and wait ~1–2 minutes. Reload the project URL above; you should see your bio page instead of the Jekyll template.

Optional: delete the **`gh-pages`** branch if you no longer need the old Jekyll placeholder.

## Optional: short URL at the account root later

If you want **`https://juwelrana19.github.io/`** with no subpath, rename this repository on GitHub to **`JuwelRana19.github.io`** (Settings → General → Repository name). Then update your local remote:

`git remote set-url origin https://github.com/JuwelRana19/JuwelRana19.github.io.git`

## Repo layout

| Path | Purpose |
|------|---------|
| `index.html` | Home page |
| `research.html` | Selected publications |
| `css/style.css` | Styles |
| `doc/` | Add `CV.pdf` for a downloadable CV |
| `.nojekyll` | Serve plain HTML (no Jekyll) |

## Local clone / push

```text
https://github.com/JuwelRana19/juwelrana.github.io.git
```

Branch: **`main`**.
