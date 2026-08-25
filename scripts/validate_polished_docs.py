"""Validate that a documentation polish changed prose only."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FENCE_PATTERN = re.compile(
    r"(?ms)^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})[^\n]*\n.*?^(?P=indent)(?P=fence)[ \t]*$"
)
HEADING_PATTERN = re.compile(r"(?m)^#{1,6}[ \t]+.*$")
INLINE_CODE_PATTERN = re.compile(r"(?<!`)`[^`\n]+`")
LINK_PATTERN = re.compile(r"!?\[[^\]\n]*\]\([^\n)]*\)")
REFERENCE_LINK_PATTERN = re.compile(r"(?m)^\[[^\]\n]+\]:\s*\S+.*$")
BADGE_PATTERN = re.compile(r"(?mi)^.*\bbadge\b.*$")
HTML_TAG_PATTERN = re.compile(r"</?[A-Za-z][^>]*>")


def _front_matter(document: str) -> str | None:
    match = re.match(
        r"\A---[ \t]*\n.*?^---[ \t]*$(?:\n|\Z)", document, re.MULTILINE | re.DOTALL
    )
    return match.group(0) if match else None


def _matches(pattern: re.Pattern[str], document: str) -> list[str]:
    return [match.group(0) for match in pattern.finditer(document)]


def _without_fenced_code(document: str) -> str:
    return FENCE_PATTERN.sub("", document)


def _headings(document: str) -> list[str]:
    return _matches(HEADING_PATTERN, _without_fenced_code(document))


def _inline_code(document: str) -> list[str]:
    prose = HEADING_PATTERN.sub("", _without_fenced_code(document))
    return _matches(INLINE_CODE_PATTERN, prose)


def _links(document: str) -> list[str]:
    prose = _without_fenced_code(document)
    return _matches(LINK_PATTERN, prose) + _matches(REFERENCE_LINK_PATTERN, prose)


def validate_document(original: str, polished: str) -> list[str]:
    """Return violations when protected Markdown content differs."""
    violations: list[str] = []
    if _front_matter(original) != _front_matter(polished):
        violations.append("front matter changed")

    original_headings = _headings(original)
    polished_headings = _headings(polished)
    if original_headings != polished_headings:
        if any(heading.startswith("####") for heading in original_headings + polished_headings):
            violations.append("signature changed")
        else:
            violations.append("heading changed")

    if _matches(FENCE_PATTERN, original) != _matches(FENCE_PATTERN, polished):
        violations.append("fenced code changed")
    if _inline_code(original) != _inline_code(polished):
        violations.append("inline code changed")
    if _links(original) != _links(polished):
        violations.append("link changed")
    if _matches(BADGE_PATTERN, original) != _matches(BADGE_PATTERN, polished):
        violations.append("badge changed")
    if _matches(HTML_TAG_PATTERN, original) != _matches(HTML_TAG_PATTERN, polished):
        violations.append("HTML tag changed")
    return violations


def validate_directories(original_root: Path, polished_root: Path) -> list[str]:
    """Return path-qualified violations for Markdown documents in two trees."""
    violations: list[str] = []
    original_paths = {path.relative_to(original_root) for path in original_root.rglob("*.md")}
    polished_paths = {path.relative_to(polished_root) for path in polished_root.rglob("*.md")}
    for relative_path in sorted(original_paths):
        display_path = relative_path.as_posix()
        if relative_path not in polished_paths:
            violations.append(f"{display_path}: document missing")
            continue
        original = (original_root / relative_path).read_text(encoding="utf-8")
        polished = (polished_root / relative_path).read_text(encoding="utf-8")
        violations.extend(
            f"{display_path}: {violation}"
            for violation in validate_document(original, polished)
        )
    for relative_path in sorted(polished_paths - original_paths):
        violations.append(f"{relative_path.as_posix()}: unexpected document")
    return violations


def main(argv: list[str] | None = None) -> int:
    """Validate all polished Markdown files against their original counterparts."""
    parser = argparse.ArgumentParser(description="Validate prose-only Markdown polishing")
    parser.add_argument("--original", type=Path, required=True)
    parser.add_argument("--polished", type=Path, required=True)
    args = parser.parse_args(argv)
    violations = validate_directories(args.original, args.polished)
    for violation in violations:
        print(violation)
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
