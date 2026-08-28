from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = ("statutes", "regulations", "policies", "legislation")
IGNORED_DIRS = {".git", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__"}
ALLOWED_ROOT_DIRS = {".axiom", ".github", "bulk", "data", "programs", "tests", "no"}
ALLOWED_ROOT_FILES = {
    ".gitignore", "CLAUDE.md", "README.md", "corpus-manifest-skeleton.yaml",
    "engine-currency-seed.diff", "known-missing-money-atoms.yaml",
    "known-validation-gaps.yaml", "oracle-coverage-pending.yaml", "variables.toml",
}


def rulespec_files() -> list[Path]:
    return sorted(path for bucket in CONTENT_DIRS for path in (ROOT / "no" / bucket).rglob("*.yaml") if not path.name.endswith(".test.yaml"))


def test_only_no_namespace_present() -> None:
    names = {child.name for child in ROOT.iterdir() if child.is_dir() and re.fullmatch(r"[a-z]{2}(?:-[a-z0-9-]+)*", child.name) and any((child / marker).is_dir() for marker in CONTENT_DIRS)}
    assert names <= {"no"}


def test_no_content_buckets_exist() -> None:
    for marker in ("statutes", "regulations", "policies"):
        assert (ROOT / "no" / marker).is_dir()


def test_root_inventory_is_allowed() -> None:
    directories = {child.name for child in ROOT.iterdir() if child.is_dir() and child.name not in IGNORED_DIRS and not child.name.startswith(("_", "."))}
    files = {child.name for child in ROOT.iterdir() if child.is_file() and child.name != ".git"}
    assert not directories - ALLOWED_ROOT_DIRS
    assert not files - ALLOWED_ROOT_FILES


def test_every_rulespec_has_companion_test() -> None:
    for path in rulespec_files():
        assert path.with_name(path.stem + ".test.yaml").exists()


def test_empty_ratchets_have_current_shapes() -> None:
    assert yaml.safe_load((ROOT / "known-validation-gaps.yaml").read_text()) == {"validate_failures": {}}
    assert yaml.safe_load((ROOT / "known-missing-money-atoms.yaml").read_text()) == {"total_allowed": 0}
    pending = yaml.safe_load((ROOT / "oracle-coverage-pending.yaml").read_text())
    assert pending["ceiling"] == 0 and pending["entries"] == []


def test_scoped_indexes() -> None:
    for relative in ("data/oracles/oracle-index.json", "data/coverage/tax-benefit-source-map.json"):
        assert json.loads((ROOT / relative).read_text())["jurisdiction"] == "no"


def test_toolchain_declares_non_validating_placeholder() -> None:
    text = (ROOT / ".axiom/toolchain.toml").read_text()
    payload = tomllib.loads(text)
    assert payload == {"toolchain": {}}
    assert "NON-VALIDATING PLACEHOLDER" in text
    for key in ("axiom_corpus_release", "axiom_corpus_release_content_sha256", "validation_waiver_set_sha256"):
        assert key in text
