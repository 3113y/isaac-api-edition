from __future__ import annotations

import importlib.util
from pathlib import Path


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
