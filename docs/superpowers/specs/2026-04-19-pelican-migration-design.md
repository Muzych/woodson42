# Pelican Landing Page Migration Design

**Date:** 2026-04-19

**Goal**

Replace the current 11ty-based blog scaffold with a minimal Pelican site that builds a single full-screen landing page and deploys to GitHub Pages.

**Approved Direction**

Use the simplest Pelican setup possible:

- remove the 11ty source, config, and Node dependency files
- keep a Pelican configuration at the repository root
- generate a single `index.html` from a custom Pelican template
- copy `CNAME` into the build output so the custom domain keeps working
- deploy the Pelican output directory with GitHub Actions Pages

**Page Design**

- black background across the full viewport
- one centered line of white text
- wording: `Reality Is But An Illusion.`
- elegant bold serif typeface loaded from Google Fonts
- responsive sizing using `clamp(...)` so the line fills the screen without becoming oversized

**Non-Goals**

- no example posts
- no article index
- no fallback blog theme
- no migration of the previous 11ty content model

**Build and Deployment**

- local and CI builds run through Pelican with a Python dependency set
- the generated site lives in `output/`
- GitHub Pages uploads `output/` and deploys on pushes to `main`
