# RGON Unified Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate bilingual RGON pages that combine RGON and RGON+ entries with Markdown badges, while retaining separate Original and RGON site roots.

**Architecture:** Keep `docs/rgon/zh` and `docs/rgon-plus/en` as editable cleaned sources. Add a deterministic generator that emits the published `docs/rgon/{zh,en}` trees from those sources, inserting `.rgon`, `.rgonplus`, or `.rgonorplus` badges immediately before API `###` headings. MkDocs renders badges; JavaScript only switches Original/RGON and language.

**Tech Stack:** Python 3.12, pytest, MkDocs Material, GitHub Actions.

## Global Constraints

- Original and RGON are the only top-level documentation interfaces.
- RGON and RGON+ are distinguished per API entry with generated Markdown badges, not browser filtering.
- `ALL DLCs` means AB, AB+, REP, and REP+; existing original badges remain unchanged.
- English source prose takes precedence; inferred translations must be marked only when English is absent.
- Deployment must build committed Markdown and must not re-fetch and overwrite edited sources.

### Task 1: Generator and unit tests

**Files:** Create `scripts/build_rgon_docs.py`; create `tests/test_build_rgon_docs.py`.

- [ ] Write failing tests for shared headings producing `.rgonorplus`, RGON-only headings producing `.rgon`, RGON+-only headings producing `.rgonplus`, and unchanged headings/signatures.
- [ ] Run `uv run pytest tests/test_build_rgon_docs.py -q` and confirm failure because the generator is missing.
- [ ] Implement the minimal parser/generator using `###` API headings as boundaries and emit both language trees.
- [ ] Run the focused tests and confirm success.

### Task 2: Site contract and profile UI

**Files:** Modify `tests/test_site_contract.py`, `overrides/main.html`, `docs/assets/javascripts/profile.js`, `docs/assets/stylesheets/profile.css`.

- [ ] Write failing assertions for exactly Original/RGON roots, a sliding capsule language toggle, and generated RGON badge classes.
- [ ] Implement root-only navigation; remove RGON+ route selection and source notices; preserve REP/REP+/ALL DLC behavior for Original.
- [ ] Add `.rgon`, `.rgonplus`, `.rgonorplus` visual and tooltip styles matching existing badges.
- [ ] Run focused site-contract tests.

### Task 3: Deployment build contract

**Files:** Modify `.github/workflows/deploy-pages.yml`; modify/add tests for workflow/generator invocation.

- [ ] Write a failing assertion that deploy invokes the generator and never clones upstream or calls `sync_upstream_docs.py`.
- [ ] Implement Actions generation before `mkdocs build --strict` using committed sources only.
- [ ] Run all tests plus `mkdocs build --strict`.

### Task 4: Review and final verification

- [ ] Run full `uv run pytest -q` and `mkdocs build --strict`.
- [ ] Review generated representative pages (`Entity`, one shared entry, one RGON-only entry, one RGON+-only entry) and verify profile navigation.
