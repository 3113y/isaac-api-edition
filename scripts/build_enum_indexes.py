"""Generate the human-browsable enumeration index pages from source files."""

from __future__ import annotations

import argparse
from pathlib import Path


def write_enum_index(source: Path, title: str) -> None:
    enum_directory = source / "enums"
    pages = sorted(path for path in enum_directory.glob("*.md") if path.name != "index.md")
    lines = [f"# {title}", ""]
    lines.extend(f"- [{page.stem}]({page.name})" for page in pages)
    (enum_directory / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--english-source", type=Path, required=True)
    parser.add_argument("--chinese-source", type=Path, required=True)
    args = parser.parse_args()
    write_enum_index(args.english_source, "Enumerations")
    write_enum_index(args.chinese_source, "枚举")


if __name__ == "__main__":
    main()
