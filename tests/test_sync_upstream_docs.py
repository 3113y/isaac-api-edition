from __future__ import annotations

import json
from pathlib import Path

from scripts.sync_upstream_docs import sync_documents, sync_extension_documents


def write_source(root: Path, language: str, body: str) -> None:
    root.mkdir(parents=True)
    (root / "Entity.md").write_text(body, encoding="utf-8")
    (root / "images").mkdir()
    (root / "images" / "entity.png").write_bytes(b"image fixture")
    (root / "enums").mkdir()
    (root / "enums" / "Direction.md").write_text(
        f"# Direction\n\n{language} enum reference.", encoding="utf-8"
    )


def test_sync_writes_paired_api_pages_and_language_indexes(tmp_path: Path) -> None:
    english = tmp_path / "english"
    chinese = tmp_path / "chinese"
    output = tmp_path / "docs"
    write_source(english, "English", "# Entity\n\nAdds an effect.\n\n[ ](#){: .alldlc .badge }")
    write_source(chinese, "Chinese", "# Entity\n\n添加效果。\n\n[ ](#){: .alldlc .badge }")

    summary = sync_documents(english, chinese, output, "english-sha", "chinese-sha")

    assert summary.page_count == 2
    assert "Adds an effect." in (output / "en" / "Entity.md").read_text(encoding="utf-8")
    assert "添加效果。" in (output / "zh" / "Entity.md").read_text(encoding="utf-8")
    assert "[Entity](Entity.md)" in (output / "en" / "index.md").read_text(encoding="utf-8")
    assert "[Entity](Entity.md)" in (output / "zh" / "index.md").read_text(encoding="utf-8")
    assert (output / "en" / "images" / "entity.png").read_bytes() == b"image fixture"
    assert (output / "zh" / "images" / "entity.png").read_bytes() == b"image fixture"
    manifest = json.loads((output / "assets" / "source-release.json").read_text(encoding="utf-8"))
    assert manifest["english_revision"] == "english-sha"
    assert manifest["chinese_revision"] == "chinese-sha"


def test_sync_rewrites_snippet_paths_for_each_language(tmp_path: Path) -> None:
    english = tmp_path / "english"
    chinese = tmp_path / "chinese"
    output = tmp_path / "docs"
    for source in (english, chinese):
        source.mkdir()
        (source / "snippets").mkdir()
        (source / "snippets" / "diagram.md").write_text("diagram body", encoding="utf-8")
        (source / "Entity.md").write_text(
            '--8<-- "docs/snippets/diagram.md"\n', encoding="utf-8"
        )

    sync_documents(english, chinese, output, "english-sha", "chinese-sha")

    assert '--8<-- "en/snippets/diagram.md"' in (output / "en" / "Entity.md").read_text(
        encoding="utf-8"
    )
    assert '--8<-- "zh/snippets/diagram.md"' in (output / "zh" / "Entity.md").read_text(
        encoding="utf-8"
    )


def test_sync_removes_stale_language_pages(tmp_path: Path) -> None:
    english = tmp_path / "english"
    chinese = tmp_path / "chinese"
    output = tmp_path / "docs"
    write_source(english, "English", "# Entity")
    write_source(chinese, "Chinese", "# Entity")
    stale_page = output / "en" / "RemovedUpstreamPage.md"
    stale_page.parent.mkdir(parents=True)
    stale_page.write_text("obsolete", encoding="utf-8")

    sync_documents(english, chinese, output, "english-sha", "chinese-sha")

    assert not stale_page.exists()


def test_sync_extension_writes_an_independent_document_root(tmp_path: Path) -> None:
    source = tmp_path / "rgon-source"
    output = tmp_path / "docs"
    source.mkdir()
    (source / "Entity.md").write_text("# Entity\n\nRGON entity reference.", encoding="utf-8")

    summary = sync_extension_documents(source, output, "rgon", "zh", "rgon-sha")

    assert summary.page_count == 1
    assert (output / "rgon" / "zh" / "Entity.md").exists()
    manifest = json.loads((output / "assets" / "source-release.json").read_text(encoding="utf-8"))
    assert manifest["extensions"]["rgon"]["revision"] == "rgon-sha"


def test_sync_preserves_extension_provenance(tmp_path: Path) -> None:
    english = tmp_path / "english"
    chinese = tmp_path / "chinese"
    output = tmp_path / "docs"
    write_source(english, "English", "# Entity")
    write_source(chinese, "Chinese", "# Entity")
    manifest_path = output / "assets" / "source-release.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_text(
        json.dumps({"extensions": {"rgon": {"revision": "rgon-sha", "page_count": 1}}}),
        encoding="utf-8",
    )

    sync_documents(english, chinese, output, "english-sha", "chinese-sha")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["extensions"]["rgon"]["revision"] == "rgon-sha"


def test_sync_extension_adds_placeholder_for_missing_relative_markdown_link(
    tmp_path: Path,
) -> None:
    source = tmp_path / "rgon-plus-source"
    output = tmp_path / "docs"
    source.mkdir()
    (source / "Renderer.md").write_text(
        "# Renderer\n\n[Transformer](renderer/Transformer.md)\n", encoding="utf-8"
    )

    sync_extension_documents(source, output, "rgon-plus", "en", "rgon-plus-sha")

    placeholder = output / "rgon-plus" / "en" / "renderer" / "Transformer.md"
    assert placeholder.exists()
    assert "pinned upstream source links here" in placeholder.read_text(encoding="utf-8")


def test_sync_extension_ignores_absolute_markdown_links(tmp_path: Path) -> None:
    source = tmp_path / "rgon-plus-source"
    output = tmp_path / "docs"
    source.mkdir()
    (source / "Renderer.md").write_text(
        "# Renderer\n\n[Upstream](https://example.invalid/Transformer.md)\n", encoding="utf-8"
    )

    sync_extension_documents(source, output, "rgon-plus", "en", "rgon-plus-sha")

    assert not (output / "rgon-plus" / "en" / "https:").exists()
