"""Expand the generated MkDocs navigation from the current enum source tree."""

from __future__ import annotations

import argparse
from pathlib import Path


ENUM_PLACEHOLDER = "      - Enumerations: en/enums/index.md"


def write_mkdocs_config(template: Path, enum_source: Path, output: Path) -> None:
    pages = sorted(path for path in enum_source.glob("*.md") if path.name != "index.md")
    nav_lines = ["      - Enumerations:"]
    nav_lines.extend(f"          - {page.stem}: en/enums/{page.name}" for page in pages)
    config = template.read_text(encoding="utf-8")
    if ENUM_PLACEHOLDER not in config:
        raise ValueError(f"Missing enumeration placeholder: {ENUM_PLACEHOLDER}")
    output.write_text(config.replace(ENUM_PLACEHOLDER, "\n".join(nav_lines)), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--template", type=Path, required=True)
    parser.add_argument("--enum-source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    write_mkdocs_config(args.template, args.enum_source, args.output)


if __name__ == "__main__":
    main()
