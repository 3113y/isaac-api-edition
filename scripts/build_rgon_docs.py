"""Build unified RGON API pages from editable RGON and RGON+ source trees."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


HEADING = re.compile(r"(?m)^### (?P<name>.+)$")
API_NAME = re.compile(r"^(?P<name>.+?\(\))(?:\s|$)")
BADGES = {
    "rgon": "[ ](#){: .rgon .tooltip .badge }",
    "rgonplus": "[ ](#){: .rgonplus .tooltip .badge }",
    "rgonorplus": "[ ](#){: .rgonorplus .tooltip .badge }",
}
SIGNATURE = re.compile(r"(?m)^(#### .+?)(\s*\{:\s*[^\n]+\})?$")
MALFORMED_ATTR = re.compile(r"\{\s*:\s*(?=\.)")


def _section_key(heading: str) -> str:
    """Use the callable name, not translated annotation text, as the merge key."""
    match = API_NAME.match(heading.strip())
    return match.group("name") if match else heading.strip()


def _normalize_attributes(text: str) -> str:
    """Repair the legacy ``{ :.class }`` attribute spelling before rendering."""
    return MALFORMED_ATTR.sub("{: ", text)


def _sections(text: str) -> tuple[str, dict[str, str], list[str]]:
    matches = list(HEADING.finditer(text))
    if not matches:
        return text, {}, []
    preamble = text[: matches[0].start()]
    sections: dict[str, str] = {}
    order: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        key = _section_key(match.group("name"))
        if key not in sections:
            order.append(key)
        sections[key] = text[match.start() : end].rstrip() + "\n"
    return preamble, sections, order


def _render(
    rgon_text: str,
    plus_text: str,
    fallback_text: str = "",
    *,
    language: str,
) -> str:
    rgon_preamble, rgon, rgon_order = _sections(_normalize_attributes(rgon_text))
    plus_preamble, plus, plus_order = _sections(_normalize_attributes(plus_text))
    fallback_preamble, fallback, _ = _sections(_normalize_attributes(fallback_text))
    if language == "en":
        preamble = plus_preamble or fallback_preamble or rgon_preamble
        preferred_sources = (plus, fallback, rgon)
    else:
        preamble = rgon_preamble or fallback_preamble or plus_preamble
        preferred_sources = (rgon, fallback, plus)
    order = rgon_order + [name for name in plus_order if name not in rgon]
    rendered = [preamble.rstrip(), ""]
    for name in order:
        in_rgon = name in rgon
        in_plus = name in plus
        badge = "rgonorplus" if in_rgon and in_plus else "rgon" if in_rgon else "rgonplus"
        section = next((source[name] for source in preferred_sources if name in source), "").rstrip()
        signature = SIGNATURE.search(section)
        if signature:
            section = (
                section[: signature.start()]
                + f"{signature.group(1)} {BADGES[badge]}{signature.group(2) or ''}"
                + section[signature.end() :]
            )
        rendered.extend([section, ""])
    return "\n".join(rendered).rstrip() + "\n"


def _write_enum_index(root: Path, language: str) -> None:
    enum_directory = root / "enums"
    if not enum_directory.exists():
        return
    pages = sorted(path for path in enum_directory.glob("*.md") if path.name != "index.md")
    title = "Enumerations" if language == "en" else "枚举"
    content = [f"# {title}", ""]
    content.extend(f"- [{page.stem}]({page.name})" for page in pages)
    (enum_directory / "index.md").write_text("\n".join(content) + "\n", encoding="utf-8")


def build_rgon_documents(
    rgon_source: Path,
    rgon_plus_source: Path,
    output: Path,
    *,
    fallback_en: Path | None = None,
    fallback_zh: Path | None = None,
) -> None:
    """Create bilingual published trees; page bodies remain source-authored."""
    pages = sorted({path.relative_to(rgon_source) for path in rgon_source.rglob("*.md")} | {path.relative_to(rgon_plus_source) for path in rgon_plus_source.rglob("*.md")})
    for page in pages:
        rgon_path = rgon_source / page
        plus_path = rgon_plus_source / page
        fallback_en_path = fallback_en / page if fallback_en else None
        fallback_zh_path = fallback_zh / page if fallback_zh else None
        rgon_text = rgon_path.read_text(encoding="utf-8") if rgon_path.exists() else ""
        plus_text = plus_path.read_text(encoding="utf-8") if plus_path.exists() else ""
        fallback_en_text = (
            fallback_en_path.read_text(encoding="utf-8")
            if fallback_en_path and fallback_en_path.exists()
            else ""
        )
        fallback_zh_text = (
            fallback_zh_path.read_text(encoding="utf-8")
            if fallback_zh_path and fallback_zh_path.exists()
            else ""
        )
        rendered_by_language = {
            "zh": _render(rgon_text, plus_text, fallback_zh_text, language="zh"),
            "en": _render(rgon_text, plus_text, fallback_en_text, language="en"),
        }
        for language, rendered in rendered_by_language.items():
            target = output / language / page
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(rendered, encoding="utf-8")
    for source in (rgon_source, rgon_plus_source):
        for asset in source.rglob("*"):
            if not asset.is_file() or asset.suffix.lower() == ".md":
                continue
            relative = asset.relative_to(source)
            for language in ("zh", "en"):
                target = output / language / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                if asset.resolve() == target.resolve():
                    continue
                shutil.copy2(asset, target)
    for language in ("zh", "en"):
        _write_enum_index(output / language, language)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rgon-source", type=Path, required=True)
    parser.add_argument("--rgon-plus-source", type=Path, required=True)
    parser.add_argument("--fallback-en", type=Path)
    parser.add_argument("--fallback-zh", type=Path)
    parser.add_argument("--output", type=Path, default=Path("docs/rgon"))
    args = parser.parse_args()
    build_rgon_documents(
        args.rgon_source,
        args.rgon_plus_source,
        args.output,
        fallback_en=args.fallback_en,
        fallback_zh=args.fallback_zh,
    )


if __name__ == "__main__":
    main()
