"""Build unified RGON API pages from editable RGON and RGON+ source trees."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


HEADING = re.compile(r"(?m)^### (?P<name>.+)$")
BADGES = {
    "rgon": "[ ](#){: .rgon .tooltip .badge }",
    "rgonplus": "[ ](#){: .rgonplus .tooltip .badge }",
    "rgonorplus": "[ ](#){: .rgonorplus .tooltip .badge }",
}
SIGNATURE = re.compile(r"(?m)^(#### .+?)(\s*\{:\s*[^\n]+\})?$")


def _sections(text: str) -> tuple[str, dict[str, str], list[str]]:
    matches = list(HEADING.finditer(text))
    if not matches:
        return text, {}, []
    preamble = text[: matches[0].start()]
    sections: dict[str, str] = {}
    order: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        key = match.group("name").strip()
        sections[key] = text[match.start() : end].rstrip() + "\n"
        order.append(key)
    return preamble, sections, order


def _render(rgon_text: str, plus_text: str) -> str:
    preamble, rgon, rgon_order = _sections(rgon_text)
    plus_preamble, plus, plus_order = _sections(plus_text)
    if not preamble:
        preamble = plus_preamble
    order = rgon_order + [name for name in plus_order if name not in rgon]
    rendered = [preamble.rstrip(), ""]
    for name in order:
        in_rgon = name in rgon
        in_plus = name in plus
        badge = "rgonorplus" if in_rgon and in_plus else "rgon" if in_rgon else "rgonplus"
        section = rgon.get(name, plus.get(name, "")).rstrip()
        signature = SIGNATURE.search(section)
        if signature:
            section = (
                section[: signature.start()]
                + f"{signature.group(1)} {BADGES[badge]}{signature.group(2) or ''}"
                + section[signature.end() :]
            )
        rendered.extend([section, ""])
    return "\n".join(rendered).rstrip() + "\n"


def build_rgon_documents(rgon_source: Path, rgon_plus_source: Path, output: Path) -> None:
    """Create bilingual published trees; page bodies remain source-authored."""
    pages = sorted({path.relative_to(rgon_source) for path in rgon_source.rglob("*.md")} | {path.relative_to(rgon_plus_source) for path in rgon_plus_source.rglob("*.md")})
    for page in pages:
        rgon_path = rgon_source / page
        plus_path = rgon_plus_source / page
        rgon_text = rgon_path.read_text(encoding="utf-8") if rgon_path.exists() else ""
        plus_text = plus_path.read_text(encoding="utf-8") if plus_path.exists() else ""
        rendered = _render(rgon_text, plus_text)
        for language in ("zh", "en"):
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rgon-source", type=Path, required=True)
    parser.add_argument("--rgon-plus-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("docs/rgon"))
    args = parser.parse_args()
    build_rgon_documents(args.rgon_source, args.rgon_plus_source, args.output)


if __name__ == "__main__":
    main()
