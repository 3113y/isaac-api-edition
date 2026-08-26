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


def test_header_uses_compact_profile_pills_and_a_sliding_language_switch() -> None:
    page = build_site()

    assert 'id="base-version-control"' in page
    assert 'id="extension-control"' in page
    assert 'id="language-switch"' in page
    assert 'data-game="rep"' in page
    assert 'data-game="rep+"' in page
    assert 'class="profile-pill-indicator"' in page
    assert '<select id="profile-game"' not in page


def test_api_badges_are_rendered_as_metadata_classes() -> None:
    build_site()

    entity_page = (ROOT / "site" / "en" / "Entity" / "index.html").read_text(encoding="utf-8")

    assert 'class="abrep tooltip badge"' in entity_page
    assert '{: .abrep .tooltip .badge }' not in entity_page


def test_api_snippets_are_included_in_rendered_pages() -> None:
    build_site()

    entity_page = (ROOT / "site" / "en" / "Entity" / "index.html").read_text(encoding="utf-8")

    assert 'class="mermaid"' in entity_page
    assert "classDiagram" in entity_page
    assert '--8&lt;-- "docs/snippets/EntityClassDiagram.md"' not in entity_page


def test_version_badge_styles_preserve_rep_and_all_dlcs() -> None:
    stylesheet = (ROOT / "docs" / "assets" / "stylesheets" / "profile.css").read_text(
        encoding="utf-8"
    )

    assert '.rep::before { content: "REP"; }' in stylesheet
    assert '.repplus::before { content: "REP+"; }' in stylesheet
    assert '.alldlc::before { content: "ALL DLCs"; }' in stylesheet
    assert '.rgon::before { content: "RGON"; }' in stylesheet
    assert '.rgonplus::before { content: "RGON+"; }' in stylesheet
    assert '.rgonorplus::before { content: "RGON / RGON+"; }' in stylesheet


def test_profile_script_marks_upstream_badges_as_compatible_entries() -> None:
    script = (ROOT / "docs" / "assets" / "javascripts" / "profile.js").read_text(
        encoding="utf-8"
    )

    assert "annotateUpstreamEntries" in script
    assert "reporplus" in script
    assert "all-dlcs" in script
    assert "signature.classList.add(\"api-signature\")" in script
    assert "markerBlock.remove()" in script


def test_sidebar_uses_entity_and_grid_entity_sections() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert '      - Entity:' in config
    assert '          - EntityPlayer: en/EntityPlayer.md' in config
    assert '      - GridEntity:' in config
    assert '          - GridEntityDoor: en/GridEntityDoor.md' in config


def test_unified_site_excludes_the_rgon_plus_source_tree() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "exclude_docs: rgon-plus/**" in config


def test_signature_and_unavailable_entry_styles_are_scoped_to_the_call_line() -> None:
    stylesheet = (ROOT / "docs" / "assets" / "stylesheets" / "profile.css").read_text(
        encoding="utf-8"
    )

    assert ".md-typeset h4.api-signature" in stylesheet
    assert ".api-signature.is-unavailable" in stylesheet
    assert ".api-entry.is-unavailable" not in stylesheet
    assert '[data-md-color-scheme="slate"]' in stylesheet
    assert ".md-typeset h4.api-signature a.badge { float: right;" in stylesheet
    assert ".md-typeset a.tooltip::after { display: none;" in stylesheet


def test_profile_script_uses_only_original_and_unified_rgon_roots() -> None:
    script = (ROOT / "docs" / "assets" / "javascripts" / "profile.js").read_text(
        encoding="utf-8"
    )

    assert '"rgon": "/rgon/"' in script
    assert 'rgon-plus/en' not in script
    assert '"rgon+"' not in script
    assert "function siteBasePath()" in script
    assert "siteBasePath()}rgon/${language}/" in script


def test_original_extension_handler_routes_back_to_the_vanilla_profile() -> None:
    script = (ROOT / "docs" / "assets" / "javascripts" / "profile.js").read_text(
        encoding="utf-8"
    )

    original_handler = script.split('originalButton.addEventListener("click", () => {', 1)[1].split(
        "  });", 1
    )[0]
    assert "render();" in original_handler
    assert original_handler.index("render();") < original_handler.index("navigateToProfile();")


def test_api_pages_are_present_in_the_primary_navigation() -> None:
    build_site()

    entity_page = (ROOT / "site" / "en" / "Entity" / "index.html").read_text(encoding="utf-8")

    assert 'href="../EntityPlayer/" class="md-nav__link"' in entity_page


def test_deployment_builds_committed_sources_without_fetching_upstream() -> None:
    workflow = (ROOT / ".github" / "workflows" / "deploy-pages.yml").read_text(encoding="utf-8")

    assert "scripts/build_rgon_docs.py" in workflow
    assert "git clone" not in workflow
    assert "scripts/sync_upstream_docs.py" not in workflow
    assert workflow.index("scripts/build_rgon_docs.py") < workflow.index("mkdocs build --strict")
