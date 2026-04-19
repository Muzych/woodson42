from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_pelican_build_outputs_the_landing_page(tmp_path: Path) -> None:
    output_dir = tmp_path / "output"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pelican",
            "content",
            "--settings",
            "pelicanconf.py",
            "--output",
            str(output_dir),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr

    index_html = output_dir / "index.html"
    assert index_html.exists(), "Pelican did not generate index.html"

    html = index_html.read_text(encoding="utf-8")
    assert "Reality Is But An Illusion." in html
    assert "fonts.googleapis.com" in html
    assert "background: #000" in html or "background-color: #000" in html
    assert "clamp(" in html

    cname = output_dir / "CNAME"
    assert cname.exists(), "Pelican did not copy the custom domain file"
    assert cname.read_text(encoding="utf-8").strip() == "woodson42.com"
