"""Build a single API documentation tree with optional RGON extension layers."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


HEADING = re.compile(r"(?m)^### (?P<name>.+)$")
SIGNATURE = re.compile(r"(?m)^(#### .+?)(\s*\{:\s*[^\n]+\})?$")
API_NAME = re.compile(r"^(?P<name>.+?\(\))(?:\s|$)")
MALFORMED_ATTR = re.compile(r"\{\s*:\s*(?=\.)")
BADGES = {
    "rgon": "[ ](#){: .rgon .tooltip .badge }",
    "rgonplus": "[ ](#){: .rgonplus .tooltip .badge }",
    "rgonorplus": "[ ](#){: .rgonorplus .tooltip .badge }",
}


def _normalize_attributes(text: str) -> str:
    return MALFORMED_ATTR.sub("{: ", text)


def _canonical_section_key(name: str) -> str:
    """Ignore visual word separators when matching the same API callable."""
    return re.sub(r"[·\s]+", "", name).casefold()


def _heading_parts(heading: str) -> tuple[str, str, str]:
    """Return a stable merge key, an API-only heading, and localized suffix prose."""
    before_attr, marker, attributes = heading.partition("{:")
    heading_text = before_attr.strip()
    match = API_NAME.match(heading_text)
    if match:
        api_name = match.group("name")
        suffix = heading_text[match.end() :].strip()
        key = _canonical_section_key(api_name)
    else:
        api_name = heading_text
        suffix = ""
        key = _canonical_section_key(api_name)
    attr_text = f" {{:{attributes}" if marker else ""
    return key, f"{api_name}{attr_text}", suffix


def _sections(text: str) -> tuple[str, dict[str, str], list[str]]:
    text = _normalize_attributes(text)
    matches = list(HEADING.finditer(text))
    if not matches:
        return text, {}, []
    preamble = text[: matches[0].start()]
    sections: dict[str, str] = {}
    order: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        key, _, _ = _heading_parts(match.group("name"))
        if key not in sections:
            order.append(key)
        sections[key] = text[match.start() : end].rstrip() + "\n"
    return preamble, sections, order


def _clean_section(section: str) -> str:
    match = HEADING.search(section)
    if not match:
        return section.rstrip() + "\n"
    _, clean_heading, suffix = _heading_parts(match.group("name"))
    section = section[: match.start()] + f"### {clean_heading}" + section[match.end() :]
    signature = SIGNATURE.search(section)
    if suffix and suffix not in section:
        insertion = signature.end() if signature else match.end()
        section = section[:insertion] + f"\n\n{suffix}" + section[insertion:]
    return section.rstrip() + "\n"


def _with_badge(section: str, badge: str) -> str:
    def add_badge(match: re.Match[str]) -> str:
        return f"{match.group(1)} {BADGES[badge]}{match.group(2) or ''}"

    return SIGNATURE.sub(add_badge, _clean_section(section))


def wrap_extension(section: str, kind: str) -> str:
    return f'<div class="{kind}" markdown="1">\n\n{section.rstrip()}\n\n</div>\n'


def _badge_for(key: str, rgon: dict[str, str], plus: dict[str, str]) -> str:
    if key in rgon and key in plus:
        return "rgonorplus"
    return "rgon" if key in rgon else "rgonplus"


def _preferred_section(
    key: str,
    base: dict[str, str],
    rgon: dict[str, str],
    plus: dict[str, str],
    language: str,
) -> str:
    sources = (plus, base, rgon) if language == "en" else (rgon, base, plus)
    return next((source[key] for source in sources if key in source), "")


def _document_body(text: str) -> str:
    """Remove front matter and a page title before nesting extension prose."""
    text = _normalize_attributes(text).lstrip()
    if text.startswith("---\n"):
        _, _, text = text.partition("\n---\n")
    title = re.search(r"(?m)^# [^\n]+\n", text)
    return (text[title.end() :] if title else text).strip()


def _render_enum_page(base_text: str, rgon_text: str, plus_text: str, language: str) -> str:
    if not (rgon_text or plus_text):
        return _normalize_attributes(base_text).rstrip() + "\n"
    _, rgon, _ = _sections(rgon_text)
    _, plus, _ = _sections(plus_text)
    badge = "rgonorplus" if rgon_text and plus_text else "rgon" if rgon_text else "rgonplus"
    sources = (plus_text, rgon_text, base_text) if language == "en" else (rgon_text, plus_text, base_text)
    extension_text = next((text for text in sources if text), "")
    extension = f"{BADGES[badge]}\n\n## RGON additions\n\n{_document_body(extension_text)}"
    if not base_text:
        title = re.search(r"(?m)^# [^\n]+", extension_text)
        preamble = title.group(0) if title else "# RGON enumeration"
        return f"{preamble}\n\n{wrap_extension(extension, 'rgon-only')}"
    return f"{_normalize_attributes(base_text).rstrip()}\n\n{wrap_extension(extension, 'rgon-extension')}"


def _render_page(
    base_text: str,
    rgon_text: str,
    plus_text: str,
    language: str,
    *,
    is_enum: bool,
) -> str:
    if is_enum:
        return _render_enum_page(base_text, rgon_text, plus_text, language)
    base_preamble, base, base_order = _sections(base_text)
    rgon_preamble, rgon, rgon_order = _sections(rgon_text)
    plus_preamble, plus, plus_order = _sections(plus_text)
    preamble = base_preamble or (plus_preamble if language == "en" else rgon_preamble) or rgon_preamble or plus_preamble
    rendered = [preamble.rstrip(), ""]
    extension_keys = set(rgon) | set(plus)
    for key in base_order:
        rendered.extend([_clean_section(base[key]).rstrip(), ""])
        if key in extension_keys:
            extension = _preferred_section(key, base, rgon, plus, language)
            rendered.extend([wrap_extension(_with_badge(extension, _badge_for(key, rgon, plus)), "rgon-extension").rstrip(), ""])
    extension_order = rgon_order + [key for key in plus_order if key not in rgon]
    rgon_only = [key for key in extension_order if key not in base]
    if rgon_only:
        appended = []
        for key in rgon_only:
            section = _preferred_section(key, base, rgon, plus, language)
            appended.append(_with_badge(section, _badge_for(key, rgon, plus)).rstrip())
        rendered.extend([wrap_extension("\n\n".join(appended), "rgon-only").rstrip(), ""])
    return "\n".join(rendered).rstrip() + "\n"


def _copy_source_tree(source_docs: Path | None, base_en: Path, base_zh: Path, output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    if source_docs:
        shutil.copytree(
            source_docs,
            output,
            ignore=shutil.ignore_patterns("rgon", "rgon-plus", "superpowers", "__pycache__"),
        )
        return
    output.mkdir(parents=True)
    shutil.copytree(base_en, output / "en")
    shutil.copytree(base_zh, output / "zh")


def build_overlay_documents(
    base_en: Path,
    base_zh: Path,
    rgon_zh: Path,
    rgon_plus_en: Path,
    output: Path,
    *,
    source_docs: Path | None = None,
) -> None:
    """Write bilingual Original pages decorated with RGON extension blocks."""
    _copy_source_tree(source_docs, base_en, base_zh, output)
    page_paths = (
        {path.relative_to(base_en) for path in base_en.rglob("*.md")}
        | {path.relative_to(base_zh) for path in base_zh.rglob("*.md")}
        | {path.relative_to(rgon_zh) for path in rgon_zh.rglob("*.md")}
        | {path.relative_to(rgon_plus_en) for path in rgon_plus_en.rglob("*.md")}
    )
    for page in sorted(page_paths):
        rgon_path = rgon_zh / page
        plus_path = rgon_plus_en / page
        rgon_text = rgon_path.read_text(encoding="utf-8") if rgon_path.exists() else ""
        plus_text = plus_path.read_text(encoding="utf-8") if plus_path.exists() else ""
        for language, base_root in (("en", base_en), ("zh", base_zh)):
            base_path = base_root / page
            base_text = base_path.read_text(encoding="utf-8") if base_path.exists() else ""
            target = output / language / page
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(
                _render_page(
                    base_text,
                    rgon_text,
                    plus_text,
                    language,
                    is_enum=page.parts and page.parts[0] == "enums",
                ),
                encoding="utf-8",
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-en", type=Path, required=True)
    parser.add_argument("--base-zh", type=Path, required=True)
    parser.add_argument("--rgon-zh", type=Path, required=True)
    parser.add_argument("--rgon-plus-en", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-docs", type=Path)
    args = parser.parse_args()
    build_overlay_documents(
        args.base_en,
        args.base_zh,
        args.rgon_zh,
        args.rgon_plus_en,
        args.output,
        source_docs=args.source_docs,
    )


if __name__ == "__main__":
    main()
