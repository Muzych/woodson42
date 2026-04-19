# Pelican Landing Page Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the 11ty site with a minimal Pelican-powered landing page and deploy it through GitHub Pages.

**Architecture:** Keep the repository root as the Pelican project. Use one custom template for the generated home page, keep `CNAME` as a copied static asset, and verify the output with a build test that checks the rendered HTML and copied domain file.

**Tech Stack:** Pelican, pytest, GitHub Actions Pages, Google Fonts

---

### Task 1: Define the migration contract

**Files:**
- Create: `requirements.txt`
- Create: `tests/test_site_build.py`
- Modify: `.gitignore`

- [ ] **Step 1: Write the failing test**

Create a pytest case that builds the Pelican site into a temporary directory and asserts:

- `index.html` exists
- the page contains `Reality Is But An Illusion.`
- the output contains a Google Fonts stylesheet reference
- `CNAME` exists in the output root with `woodson42.com`

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/bin/python -m pytest tests/test_site_build.py -q`
Expected: FAIL because the Pelican project files do not exist yet.

- [ ] **Step 3: Write minimal implementation scaffolding**

Add the Python dependency list and ignore local Python build artifacts.

- [ ] **Step 4: Run test to keep the failure signal honest**

Run: `.venv/bin/python -m pytest tests/test_site_build.py -q`
Expected: still FAIL for missing Pelican configuration or templates.

### Task 2: Replace 11ty with Pelican

**Files:**
- Create: `pelicanconf.py`
- Create: `content/extra/CNAME`
- Create: `theme/templates/index.html`
- Delete: `eleventy.config.js`
- Delete: `package.json`
- Delete: `package-lock.json`
- Delete: `src/index.njk`
- Delete: `src/CNAME`
- Delete: `src/posts/hello-world.md`
- Delete: `src/_includes/layout.njk`

- [ ] **Step 1: Create the Pelican configuration**

Configure:

- site metadata
- `THEME` to the local theme directory
- `DIRECT_TEMPLATES = ["index"]`
- `ARTICLE_PATHS = []`
- `PAGE_PATHS = []`
- static copy rules for `content/extra/CNAME`
- `output/` as the generated site directory

- [ ] **Step 2: Create the single landing page template**

Render a centered heading with black background, white text, bold elegant serif typography, and responsive sizing.

- [ ] **Step 3: Move the custom domain file into Pelican's static content**

Add `content/extra/CNAME` with `woodson42.com`.

- [ ] **Step 4: Delete the obsolete 11ty files**

Remove the old 11ty config, templates, and Node package manifests.

- [ ] **Step 5: Run the focused test**

Run: `.venv/bin/python -m pytest tests/test_site_build.py -q`
Expected: PASS.

### Task 3: Update deployment and clean generated artifacts

**Files:**
- Modify: `.github/workflows/deploy-pages.yml`

- [ ] **Step 1: Rewrite the GitHub Pages workflow for Python**

Use:

- `actions/setup-python`
- `python -m pip install -r requirements.txt`
- `python -m pelican content -s pelicanconf.py`
- `output/` as the uploaded artifact path

- [ ] **Step 2: Remove obsolete generated directories from the working tree**

Delete the local `node_modules/` and `_site/` directories inside this repository only.

- [ ] **Step 3: Run the full local verification**

Run:

- `.venv/bin/python -m pytest tests/test_site_build.py -q`
- `.venv/bin/python -m pelican content -s pelicanconf.py`

Expected: both commands PASS and `output/index.html` exists.

### Task 4: Publish

**Files:**
- Modify: tracked files from Tasks 1-3

- [ ] **Step 1: Inspect the final diff**

Run: `git status -sb`

- [ ] **Step 2: Commit the migration**

Run:

```bash
git add .gitignore requirements.txt pelicanconf.py content theme tests docs .github/workflows/deploy-pages.yml
git commit -m "migrate site from 11ty to pelican"
```

- [ ] **Step 3: Push to GitHub**

Run: `git push origin main`

- [ ] **Step 4: Confirm the deployment trigger**

Check that the push updated the remote branch and that the GitHub Pages workflow started for that commit.
