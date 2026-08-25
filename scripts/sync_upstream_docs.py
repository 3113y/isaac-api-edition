"""Copy paired upstream Markdown documents into the static-site tree."""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import dataclass
from pathlib import Path


EXCLUDED_PARTS = {"customData", "css", "js", "images"}
EXCLUDED_NAMES = {"PLACEHOLDER.md", "tags.md"}


@dataclass(frozen=True)
class SyncSummary:
    page_count: int


def _pages(source: Path) -> set[Path]:
    return {
        path.relative_to(source)
        for path in source.rglob("*.md")
        if path.name not in EXCLUDED_NAMES
        and not any(part in EXCLUDED_PARTS for part in path.relative_to(source).parts)
    }


def _copy_assets(source: Path, destination: Path) -> None:
    for path in source.rglob("*"):
        if not path.is_file() or path.suffix.lower() == ".md":
            continue
        relative = path.relative_to(source)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def _copy_page(source: Path, destination: Path, language: str) -> None:
    content = source.read_text(encoding="utf-8")
    content = content.replace(
        '--8<-- "docs/snippets/', f'--8<-- "{language}/snippets/'
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def _write_index(destination: Path, language: str, pages: list[Path]) -> None:
    title = "Isaac API Documentation" if language == "en" else "以撒 API 文档"
    intro = (
        "Generated from pinned upstream documentation snapshots."
        if language == "en"
        else "由固定版本的上游文档快照自动生成。"
    )
    links = [f"- [{path.stem}]({path.as_posix()})" for path in pages if path.name != "index.md"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        f"# {title}\n\n{intro}\n\n## API Pages\n\n" + "\n".join(links) + "\n",
        encoding="utf-8",
    )


def _read_manifest(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    content = json.loads(path.read_text(encoding="utf-8"))
    return content if isinstance(content, dict) else {}


def sync_documents(
    english_source: Path,
    chinese_source: Path,
    output_docs: Path,
    english_revision: str,
    chinese_revision: str,
) -> SyncSummary:
    """Write only source files that have a page in both language snapshots."""
    english_pages = _pages(english_source)
    chinese_pages = _pages(chinese_source)
    paired_pages = sorted(english_pages.intersection(chinese_pages))

    for language, source in (("en", english_source), ("zh", chinese_source)):
        language_root = output_docs / language
        if language_root.exists():
            shutil.rmtree(language_root)
        _copy_assets(source, language_root)
        for relative in paired_pages:
            if relative.name == "index.md":
                continue
            destination = language_root / relative
            _copy_page(source / relative, destination, language)
        _write_index(language_root / "index.md", language, paired_pages)

    assets = output_docs / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    page_count = len([page for page in paired_pages if page.name != "index.md"])
    manifest_path = assets / "source-release.json"
    manifest = _read_manifest(manifest_path)
    manifest.update(
        {
            "english_revision": english_revision,
            "chinese_revision": chinese_revision,
            "page_count": page_count,
        }
    )
    manifest_path.write_text(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return SyncSummary(page_count=page_count)


def sync_extension_documents(
    source: Path,
    output: Path,
    extension: str,
    language: str,
    revision: str,
) -> SyncSummary:
    """Write an independent, pinned extension documentation snapshot."""
    pages = sorted(_pages(source))
    language_root = output / extension / language
    if language_root.exists():
        shutil.rmtree(language_root)
    _copy_assets(source, language_root)
    for relative in pages:
        _copy_page(source / relative, language_root / relative, f"{extension}/{language}")
    _write_index(language_root / "index.md", language, pages)

    assets = output / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    manifest_path = assets / "source-release.json"
    manifest = _read_manifest(manifest_path)
    extensions = manifest.setdefault("extensions", {})
    if not isinstance(extensions, dict):
        raise ValueError("source-release manifest extensions must be an object")
    extensions[extension] = {"revision": revision, "page_count": len(pages)}
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return SyncSummary(page_count=len(pages))


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize paired upstream API Markdown")
    parser.add_argument("--english-source", type=Path, required=True)
    parser.add_argument("--chinese-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("docs"))
    parser.add_argument("--english-revision", required=True)
    parser.add_argument("--chinese-revision", required=True)
    args = parser.parse_args()
    sync_documents(
        args.english_source,
        args.chinese_source,
        args.output,
        args.english_revision,
        args.chinese_revision,
    )


if __name__ == "__main__":
    main()
