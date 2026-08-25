from __future__ import annotations

import importlib.util
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_polished_docs.py"


def validate_document(original: str, polished: str) -> list[str]:
    """Load the validator when it exists, keeping the first test run executable."""
    if not VALIDATOR_PATH.exists():
        return ["validator unavailable"]
    spec = importlib.util.spec_from_file_location("validate_polished_docs", VALIDATOR_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate_document(original, polished)


def test_allows_prose_only_edits() -> None:
    original = """---
title: Example
---

# Entity

This action adds an effect to the room.

#### `Entity:AddEffect(effect, amount)`

See [the guide](guide.md#effects).
"""
    polished = """---
title: Example
---

# Entity

Adds the specified effect to the current room.

#### `Entity:AddEffect(effect, amount)`

See [the guide](guide.md#effects).
"""

    assert validate_document(original, polished) == []


def test_reports_signature_and_link_target_changes() -> None:
    original = """#### `Entity:AddEffect(effect, amount)`

See [the guide](guide.md#effects).
"""
    polished = """#### `Entity:AddEffect(effect, duration)`

See [the guide](reference.md#effects).
"""

    violations = validate_document(original, polished)

    assert "signature changed" in violations
    assert "link changed" in violations


def test_reports_fenced_code_contents_changes() -> None:
    original = """# Example

```lua
entity:AddEffect(effect, amount)
```
"""
    polished = """# Example

```lua
entity:AddEffect(effect, duration)
```
"""

    assert "fenced code changed" in validate_document(original, polished)


def test_reports_inline_code_changes() -> None:
    original = "Use `Entity:AddEffect(effect, amount)` to add an effect."
    polished = "Use `Entity:AddEffect(effect, duration)` to add an effect."

    assert "inline code changed" in validate_document(original, polished)


def test_reports_double_backtick_inline_code_changes() -> None:
    original = "Use ``Share`` to duplicate the value."
    polished = "Use ``Clone`` to duplicate the value."

    assert "inline code changed" in validate_document(original, polished)


def test_reports_indented_fenced_code_contents_changes() -> None:
    original = """    ```lua
    entity:AddEffect(effect, amount)
    ```
"""
    polished = """    ```lua
    entity:AddEffect(effect, duration)
    ```
"""

    assert "fenced code changed" in validate_document(original, polished)


def test_reports_real_api_signature_heading_change() -> None:
    original = "#### void AddBurn ( [EntityRef](EntityRef.md) integer Duration ) {: .copyable }"
    polished = "#### void AddBurn ( [EntityRef](EntityRef.md) integer Frames ) {: .copyable }"

    assert validate_document(original, polished) == ["signature changed"]


def test_reports_non_signature_heading_change_in_api_document() -> None:
    original = """## Notes

#### void AddBurn ( [EntityRef](EntityRef.md) integer Duration ) {: .copyable }
"""
    polished = """## Details

#### void AddBurn ( [EntityRef](EntityRef.md) integer Duration ) {: .copyable }
"""

    violations = validate_document(original, polished)

    assert "heading changed" in violations
    assert "signature changed" not in violations


def test_reports_front_matter_badge_and_html_tag_changes() -> None:
    original = """---
title: Example
---

[DLC](#){: .badge }

<span class="api">Example</span>
"""
    polished = """---
title: Renamed
---

[DLC](#){: .tag }

<em class="api">Example</em>
"""

    assert validate_document(original, polished) == [
        "front matter changed",
        "badge changed",
        "HTML tag changed",
    ]


def test_cli_validates_matching_document_trees(tmp_path: Path) -> None:
    original = tmp_path / "original"
    polished = tmp_path / "polished"
    original.mkdir()
    polished.mkdir()
    source = "#### void AddBurn ( [EntityRef](EntityRef.md) integer Duration ) {: .copyable }\n\nAdds fire.\n"
    (original / "Entity.md").write_text(source, encoding="utf-8")
    (polished / "Entity.md").write_text(
        source.replace("Adds fire.", "Adds a burning effect."), encoding="utf-8"
    )

    safe = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--original",
            str(original),
            "--polished",
            str(polished),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert safe.returncode == 0
    (polished / "Entity.md").write_text(
        source.replace("Duration", "Frames"), encoding="utf-8"
    )
    broken = subprocess.run(
        [
            sys.executable,
            str(VALIDATOR_PATH),
            "--original",
            str(original),
            "--polished",
            str(polished),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert broken.returncode != 0
    assert "Entity.md: signature changed" in broken.stdout
