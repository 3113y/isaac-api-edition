from pathlib import Path

from scripts.build_mkdocs_config import write_mkdocs_config


def test_generated_navigation_expands_enumerations(tmp_path: Path) -> None:
    template = tmp_path / "mkdocs.yml"
    enum_source = tmp_path / "enums"
    output = tmp_path / "generated.yml"
    template.write_text(
        "nav:\n  - API reference:\n      - Enumerations: en/enums/index.md\n",
        encoding="utf-8",
    )
    enum_source.mkdir()
    (enum_source / "ActionTriggers.md").write_text("# ActionTriggers\n", encoding="utf-8")
    (enum_source / "BombVariant.md").write_text("# BombVariant\n", encoding="utf-8")

    write_mkdocs_config(template, enum_source, output)

    config = output.read_text(encoding="utf-8")
    assert "      - Enumerations:" in config
    assert "          - ActionTriggers: en/enums/ActionTriggers.md" in config
    assert "          - BombVariant: en/enums/BombVariant.md" in config
    assert "index.md" not in config
