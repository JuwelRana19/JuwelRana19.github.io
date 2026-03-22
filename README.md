# JuwelRana19.github.io (user site)

Personal academic site for **Juwel Rana** (static HTML + CSS).

## Public URL (no subpath)

**[https://juwelrana19.github.io/](https://juwelrana19.github.io/)**

That address only works after the GitHub repository is named **`JuwelRana19.github.io`** (same spelling as username **`JuwelRana19`**).

## One-time setup on GitHub (you must do this in the browser)

### 1. Rename the repository

1. Open **[Repository settings → General](https://github.com/JuwelRana19/juwelrana.github.io/settings)**.
2. Under **Repository name**, change **`juwelrana.github.io`** → **`JuwelRana19.github.io`**.
3. Click **Rename**.

GitHub will redirect old links from `juwelrana.github.io` to the new name.

### 2. GitHub Pages

1. Open **[Settings → Pages](https://github.com/JuwelRana19/JuwelRana19.github.io/settings/pages)** (use the new repo URL after rename).
2. **Source**: Deploy from a branch.
3. **Branch**: **`main`**, folder **`/ (root)`** — not `gh-pages`.
4. Save. Wait 1–2 minutes, then open **https://juwelrana19.github.io/**

Optional: delete the **`gh-pages`** branch if you no longer need the old Jekyll placeholder.

### 3. Update this folder’s git remote (after rename)

```powershell
git remote set-url origin https://github.com/JuwelRana19/JuwelRana19.github.io.git
git push origin main
```

## Repo layout

| Path | Purpose |
|------|---------|
| `index.html` | Home page |
| `research.html` | Selected publications |
| `css/style.css` | Styles |
| `doc/` | Add `CV.pdf` for a downloadable CV |
| `.nojekyll` | Serve plain HTML (no Jekyll) |

## Clone URL (after rename)

```text
https://github.com/JuwelRana19/JuwelRana19.github.io.git
```

Branch: **`main`**.
