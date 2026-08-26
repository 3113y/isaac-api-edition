from pathlib import Path

from scripts.build_rgon_docs import build_rgon_documents
from scripts.build_overlay_docs import build_overlay_documents


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


def test_overlay_retains_original_method_and_appends_rgon_variant(tmp_path: Path) -> None:
    base_en, base_zh, rgon_zh, plus_en, output = (
        tmp_path / "en",
        tmp_path / "zh",
        tmp_path / "rgon-zh",
        tmp_path / "rgon-plus-en",
        tmp_path / "generated",
    )
    for root, text in (
        (base_en, "# Entity\n\n### AddKnockback ()\n\n#### void AddKnockback ( int Duration )\n\nBase description.\n"),
        (base_zh, "# Entity\n\n### AddKnockback ()\n\n#### void AddKnockback ( int Duration )\n\n原版说明。\n"),
        (rgon_zh, "# Entity\n\n### AddKnockback () 添加击退效果\n\n#### void AddKnockback ( int Duration, boolean TakeImpactDamage )\n\nRGON 中文说明。\n\n### AddBaited ()\n\n#### void AddBaited ( )\n\n仅 RGON。\n"),
        (plus_en, "# Entity\n\n### AddKnockback ()\n\n#### void AddKnockback ( int Duration, boolean TakeImpactDamage )\n\nRGON English description.\n"),
    ):
        root.mkdir()
        (root / "Entity.md").write_text(text, encoding="utf-8")

    build_overlay_documents(base_en, base_zh, rgon_zh, plus_en, output)

    english = (output / "en" / "Entity.md").read_text(encoding="utf-8")
    chinese = (output / "zh" / "Entity.md").read_text(encoding="utf-8")
    assert "#### void AddKnockback ( int Duration )" in english
    assert '<div class="rgon-extension" markdown="1">' in english
    assert "#### void AddKnockback ( int Duration, boolean TakeImpactDamage )" in english
    assert "RGON English description." in english
    assert english.index("### AddKnockback ()") < english.index('<div class="rgon-only"')
    assert "### AddBaited ()" in english
    assert "### AddKnockback () 添加击退效果" not in chinese
    assert "添加击退效果" in chinese.split("#### void AddKnockback", 1)[1]
    assert ".rgonorplus" in english


def test_overlay_uses_original_english_when_rgon_has_no_english_source(tmp_path: Path) -> None:
    base_en, base_zh, rgon_zh, plus_en, output = (
        tmp_path / "en",
        tmp_path / "zh",
        tmp_path / "rgon-zh",
        tmp_path / "rgon-plus-en",
        tmp_path / "generated",
    )
    for root, text in (
        (base_en, "# Entity\n\n### Shared ()\n\n#### void Shared ( )\n\nOriginal English.\n"),
        (base_zh, "# Entity\n\n### Shared ()\n\n#### void Shared ( )\n\n原版中文。\n"),
        (rgon_zh, "# Entity\n\n### Shared ()\n\n#### void Shared ( )\n\nRGON 中文。\n"),
        (plus_en, "# Entity\n"),
    ):
        root.mkdir()
        (root / "Entity.md").write_text(text, encoding="utf-8")

    build_overlay_documents(base_en, base_zh, rgon_zh, plus_en, output)

    english = (output / "en" / "Entity.md").read_text(encoding="utf-8")
    assert "Original English." in english
    assert "RGON 中文。" not in english


def test_overlay_appends_rgon_enum_table_to_the_original_enum(tmp_path: Path) -> None:
    base_en, base_zh, rgon_zh, plus_en, output = (
        tmp_path / "en",
        tmp_path / "zh",
        tmp_path / "rgon-zh",
        tmp_path / "rgon-plus-en",
        tmp_path / "generated",
    )
    for root, text in (
        (base_en, '# Enum "Status"\n\n|Value|Enumerator|\n|:--|:--|\n|0|BASE|\n'),
        (base_zh, '# 枚举 "Status"\n\n|值|枚举|\n|:--|:--|\n|0|BASE|\n'),
        (rgon_zh, '# 枚举 "Status"\n\n|值|枚举|\n|:--|:--|\n|1|RGON|\n'),
        (plus_en, '# Enum "Status"\n\n|Value|Enumerator|\n|:--|:--|\n|2|RGON_PLUS|\n'),
    ):
        (root / "enums").mkdir(parents=True)
        (root / "enums" / "Status.md").write_text(text, encoding="utf-8")

    build_overlay_documents(base_en, base_zh, rgon_zh, plus_en, output)

    english = (output / "en" / "enums" / "Status.md").read_text(encoding="utf-8")
    assert "|0|BASE|" in english
    assert '<div class="rgon-extension" markdown="1">' in english
    assert "|2|RGON_PLUS|" in english
    assert ".rgonorplus" in english


def test_overlay_matches_decorated_original_callable_names(tmp_path: Path) -> None:
    base_en, base_zh, rgon_zh, plus_en, output = (
        tmp_path / "en",
        tmp_path / "zh",
        tmp_path / "rgon-zh",
        tmp_path / "rgon-plus-en",
        tmp_path / "generated",
    )
    for root, text in (
        (base_en, "# Isaac\n\n### Find·By·Type ()\n\n#### table FindByType ( )\n\nOriginal.\n\n### Next ()\n\n#### void Next ( )\n"),
        (base_zh, "# Isaac\n\n### Find·By·Type ()\n\n#### table FindByType ( )\n\n原版。\n"),
        (rgon_zh, "# Isaac\n\n### FindByType ()\n\n#### Entity[] FindByType ( )\n\nRGON 中文。\n"),
        (plus_en, "# Isaac\n\n### FindByType ()\n\n#### Entity[] FindByType ( )\n\nRGON English.\n"),
    ):
        root.mkdir()
        (root / "Isaac.md").write_text(text, encoding="utf-8")

    build_overlay_documents(base_en, base_zh, rgon_zh, plus_en, output)

    page = (output / "en" / "Isaac.md").read_text(encoding="utf-8")
    extension = page.index('<div class="rgon-extension"')
    assert page.index("### Find·By·Type ()") < extension < page.index("### Next ()")
    assert '<div class="rgon-only"' not in page
