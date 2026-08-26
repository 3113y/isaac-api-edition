from pathlib import Path

from scripts.build_rgon_docs import build_rgon_documents


def test_build_marks_shared_and_version_specific_api_entries(tmp_path: Path) -> None:
    rgon = tmp_path / "rgon"
    rgon_plus = tmp_path / "rgon-plus"
    output = tmp_path / "output"
    for root, text in (
        (
            rgon / "zh",
            "# Entity\n\n### Shared ()\n\n#### void Shared ( ) {: .copyable }\n\n中文。\n\n"
            "### RgonOnly ()\n\n#### void RgonOnly ( ) {: .copyable }\n\n仅 RGON。\n",
        ),
        (
            rgon_plus / "en",
            "# Entity\n\n### Shared ()\n\n#### void Shared ( ) {: .copyable }\n\nEnglish.\n\n"
            "### RgonPlusOnly ()\n\n#### void RgonPlusOnly ( ) {: .copyable }\n\nRGON+ only.\n",
        ),
    ):
        root.mkdir(parents=True)
        (root / "Entity.md").write_text(text, encoding="utf-8")
    (rgon / "zh" / "img").mkdir()
    (rgon / "zh" / "img" / "guide.png").write_bytes(b"image")

    build_rgon_documents(rgon / "zh", rgon_plus / "en", output)

    zh = (output / "zh" / "Entity.md").read_text(encoding="utf-8")
    en = (output / "en" / "Entity.md").read_text(encoding="utf-8")
    for rendered_language, rendered in (("zh", zh), ("en", en)):
        assert "#### void Shared ( ) [ ](#){: .rgonorplus .tooltip .badge } {: .copyable }" in rendered
        assert "#### void RgonOnly ( ) [ ](#){: .rgon .tooltip .badge } {: .copyable }" in rendered
        assert "#### void RgonPlusOnly ( ) [ ](#){: .rgonplus .tooltip .badge } {: .copyable }" in rendered
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


def test_build_normalizes_signatures_deduplicates_localized_names_and_falls_back_to_english(
    tmp_path: Path,
) -> None:
    rgon = tmp_path / "rgon" / "zh"
    rgon_plus = tmp_path / "rgon-plus" / "en"
    fallback_en = tmp_path / "en"
    output = tmp_path / "output"
    for root, text in (
        (
            rgon,
            "# Entity\n\n### AddKnockback () 添加击退效果\n\n"
            "#### void AddKnockback ( ) {: .copyable }\n\n中文说明。\n\n"
            "### RgonOnly ()\n\n#### void RgonOnly ( ) {: .copyable }\n\n仅 RGON。\n",
        ),
        (
            rgon_plus,
            "# Entity\n\n### AddKnockback ()\n\n#### void AddKnockback ( ) {: .copyable }\n\n"
            "English RGON+ description.\n\n### RNG ()\n\n"
            "#### RNG RNG ( ) { :.copyable }\n",
        ),
        (
            fallback_en,
            "# Entity\n\n### RgonOnly ()\n\n#### void RgonOnly ( ) {: .copyable }\n\n"
            "Original English fallback.\n",
        ),
    ):
        root.mkdir(parents=True)
        (root / "Entity.md").write_text(text, encoding="utf-8")

    build_rgon_documents(rgon, rgon_plus, output, fallback_en=fallback_en)

    english = (output / "en" / "Entity.md").read_text(encoding="utf-8")
    assert english.count("### AddKnockback ()") == 1
    assert "添加击退效果" not in english
    assert "English RGON+ description." in english
    assert "Original English fallback." in english
    assert "{ :.copyable" not in english
    assert "{: .copyable" in english


def test_build_creates_enum_indexes_for_both_published_languages(tmp_path: Path) -> None:
    rgon = tmp_path / "rgon" / "zh"
    rgon_plus = tmp_path / "rgon-plus" / "en"
    output = tmp_path / "output"
    for root in (rgon, rgon_plus):
        (root / "enums").mkdir(parents=True)
    (rgon / "enums" / "StatusEffect.md").write_text("# StatusEffect\n", encoding="utf-8")
    (rgon_plus / "enums" / "WeaponModifier.md").write_text("# WeaponModifier\n", encoding="utf-8")

    build_rgon_documents(rgon, rgon_plus, output)

    for language in ("zh", "en"):
        index = (output / language / "enums" / "index.md").read_text(encoding="utf-8")
        assert "StatusEffect" in index
        assert "WeaponModifier" in index
