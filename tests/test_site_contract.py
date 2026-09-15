from __future__ import annotations

import json
import re
import subprocess
import sys
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def build_site() -> str:
    subprocess.run(
        [
            sys.executable,
            "scripts/build_overlay_docs.py",
            "--source-docs",
            "docs",
            "--base-en",
            "docs/en",
            "--base-zh",
            "docs/zh",
            "--rgon-zh",
            "docs/rgon/zh",
            "--rgon-plus-en",
            "docs/rgon-plus/en",
            "--output",
            ".generated-docs",
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [
            sys.executable,
            "scripts/build_mkdocs_config.py",
            "--template",
            "mkdocs.yml",
            "--enum-source",
            ".generated-docs/en/enums",
            "--output",
            ".generated-mkdocs.yml",
        ],
        cwd=ROOT,
        check=True,
    )
    subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--config-file", ".generated-mkdocs.yml", "--strict"],
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
    assert "function syncNavigationState()" in script
    assert 'link.classList.add("md-nav__link--active")' in script
    assert 'item.classList.add("md-nav__item--active")' in script
    assert 'item.classList.remove("md-nav__item--section")' in script
    assert 'item.querySelector(":scope > input.md-nav__toggle[type=\'checkbox\']")' in script
    assert "toggle.checked = true" in script


def test_sidebar_uses_entity_and_grid_entity_sections() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert '      - Entity:' in config
    assert '          - EntityPlayer: en/EntityPlayer.md' in config
    assert '      - GridEntity:' in config
    assert '          - GridEntityDoor: en/GridEntityDoor.md' in config
    assert '      - Enumerations: en/enums/index.md' in config


def test_table_of_contents_excludes_call_signatures() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "toc_depth: 3" in config


def test_unified_site_excludes_the_rgon_plus_source_tree() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "exclude_docs: rgon-plus/**" in config
    assert "not_found: ignore" in config
    assert "anchors: ignore" in config


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
    assert 'content: "RGON extension";' in stylesheet
    assert ".rgon-toc-entry.is-first" in stylesheet


def test_profile_script_toggles_rgon_in_the_current_document() -> None:
    script = (ROOT / "docs" / "assets" / "javascripts" / "profile.js").read_text(
        encoding="utf-8"
    )

    assert "extensionRoots" not in script
    assert "function applyExtensionVisibility()" in script
    assert "function annotateExtensionToc()" in script
    assert "function enablePrimarySectionToggles()" in script
    assert '.toggleAttribute("hidden", !enabled)' in script
    assert "navigateToLanguage" in script
    assert "rgon-plus/en" not in script
    assert '"rgon+"' not in script
    assert "function siteBasePath()" in script
    assert "siteBasePath()}${language}/" in script


def test_profile_script_reference_is_cache_busted() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "assets/javascripts/profile.js?rev=" in config


def test_search_index_splits_underscored_api_identifiers() -> None:
    build_site()

    search_index = json.loads(
        (ROOT / "site" / "search" / "search_index.json").read_text(encoding="utf-8")
    )
    separator = search_index["config"]["separator"]
    tokens = re.split(separator, "MC_PRE_NPC_UPDATE")

    assert tokens == ["MC", "PRE", "NPC", "UPDATE"]


def test_extension_handler_does_not_navigate_to_another_document_tree() -> None:
    script = (ROOT / "docs" / "assets" / "javascripts" / "profile.js").read_text(
        encoding="utf-8"
    )

    extension_handler = script.split('extensionButton.addEventListener("click", () => {', 1)[1].split(
        "  });", 1
    )[0]
    assert "render();" in extension_handler
    assert "navigateToProfile" not in extension_handler


def test_api_pages_are_present_in_the_primary_navigation() -> None:
    build_site()

    entity_page = (ROOT / "site" / "en" / "Entity" / "index.html").read_text(encoding="utf-8")

    assert 'href="../EntityPlayer/" class="md-nav__link"' in entity_page


def test_deployment_builds_committed_sources_without_fetching_upstream() -> None:
    workflow = (ROOT / ".github" / "workflows" / "deploy-pages.yml").read_text(encoding="utf-8")

    assert "scripts/build_overlay_docs.py" in workflow
    assert "scripts/build_mkdocs_config.py" in workflow
    assert "--config-file .generated-mkdocs.yml --strict" in workflow
    assert "git clone" not in workflow
    assert "scripts/sync_upstream_docs.py" not in workflow
    assert workflow.index("scripts/build_overlay_docs.py") < workflow.index("scripts/build_mkdocs_config.py")
    assert workflow.index("scripts/build_mkdocs_config.py") < workflow.index("mkdocs build --config-file")


def test_site_identity_uses_the_renamed_human_documentation_repository() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "site_name: Isaac API Edition" in config
    assert "site_url: https://3113y.github.io/isaac-api-edition/" in config
    assert "repo_url: https://github.com/3113y/isaac-api-edition" in config
    assert "repo_name: 3113y/isaac-api-edition" in config


def test_homepages_provide_compact_language_and_api_starting_points() -> None:
    root_home = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    english_home = (ROOT / "docs" / "en" / "index.md").read_text(encoding="utf-8")
    chinese_home = (ROOT / "docs" / "zh" / "index.md").read_text(encoding="utf-8")

    assert "# Isaac API Edition" in root_home
    assert "English API reference" in root_home
    assert "中文 API 文档" in root_home
    assert "docs/index.md" not in root_home
    assert "## API Pages" not in english_home
    assert "## API 页面" not in chinese_home
    assert "Browse the reference" in english_home
    assert "浏览 API 参考" in chinese_home
    assert "RGON" in english_home
    assert "RGON" in chinese_home


def test_primary_home_navigation_points_to_the_bilingual_landing_page() -> None:
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "  - Home: index.md" in config


def test_language_switch_uses_the_configured_pages_base_from_the_landing_page() -> None:
    page = build_site()
    script = (ROOT / "docs" / "assets" / "javascripts" / "profile.js").read_text(
        encoding="utf-8"
    )

    assert 'data-site-base="https://3113y.github.io/isaac-api-edition/"' in page
    assert "const configuredSiteBase = profileBar.dataset.siteBase;" in script
    assert "new URL(configuredSiteBase, window.location.origin).pathname" in script
