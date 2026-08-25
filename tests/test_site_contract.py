from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def build_site() -> str:
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return (ROOT / "site" / "index.html").read_text(encoding="utf-8")


def test_header_uses_profile_pills_and_a_sliding_language_switch() -> None:
    page = build_site()

    assert 'id="base-version-control"' in page
    assert 'id="extension-control"' in page
    assert 'id="language-switch"' in page
    assert 'data-game="rep"' in page
    assert 'data-game="rep+"' in page
    assert '<select id="profile-game"' not in page
