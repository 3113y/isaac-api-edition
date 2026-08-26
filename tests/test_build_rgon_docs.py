from pathlib import Path

from scripts.build_rgon_docs import build_rgon_documents


def test_build_marks_shared_and_version_specific_api_entries(tmp_path: Path) -> None:
    rgon = tmp_path / "rgon"
    rgon_plus = tmp_path / "rgon-plus"
    output = tmp_path / "output"
    for root, text in (
        (rgon / "zh", "# Entity\n\n### Shared ()\n\n中文。\n\n### RgonOnly ()\n\n仅 RGON。\n"),
        (rgon_plus / "en", "# Entity\n\n### Shared ()\n\nEnglish.\n\n### RgonPlusOnly ()\n\nRGON+ only.\n"),
    ):
        root.mkdir(parents=True)
        (root / "Entity.md").write_text(text, encoding="utf-8")
    (rgon / "zh" / "img").mkdir()
    (rgon / "zh" / "img" / "guide.png").write_bytes(b"image")

    build_rgon_documents(rgon / "zh", rgon_plus / "en", output)

    zh = (output / "zh" / "Entity.md").read_text(encoding="utf-8")
    en = (output / "en" / "Entity.md").read_text(encoding="utf-8")
    for rendered_language, rendered in (("zh", zh), ("en", en)):
        assert "[ ](#){: .rgonorplus .tooltip .badge }\n### Shared ()" in rendered
        assert "[ ](#){: .rgon .tooltip .badge }\n### RgonOnly ()" in rendered
        assert "[ ](#){: .rgonplus .tooltip .badge }\n### RgonPlusOnly ()" in rendered
        assert (output / rendered_language / "img" / "guide.png").read_bytes() == b"image"


def test_build_allows_output_to_contain_the_rgon_source_tree(tmp_path: Path) -> None:
    docs = tmp_path / "docs"
    rgon = docs / "rgon" / "zh"
    plus = docs / "rgon-plus" / "en"
    rgon.mkdir(parents=True)
    plus.mkdir(parents=True)
    (rgon / "Entity.md").write_text("# Entity\n", encoding="utf-8")
    (rgon / "img").mkdir()
    (rgon / "img" / "guide.png").write_bytes(b"image")
    (plus / "Entity.md").write_text("# Entity\n", encoding="utf-8")

    build_rgon_documents(rgon, plus, docs / "rgon")

    assert (docs / "rgon" / "zh" / "img" / "guide.png").read_bytes() == b"image"
