#!/usr/bin/env python3
"""Shared helpers for local router recovery profile tools."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schema" / "recovery_profile.schema.json"
ENUMS_PATH = REPO_ROOT / "schema" / "enums.md"
DEFAULT_SCAN_DIRS = ("incoming", "reviewed")
DERIVED_FIELDS = {"normalized_brand", "normalized_model", "dedupe_key"}
QUALITY_FIELDS = {"source_evidence"}


@dataclass(frozen=True)
class ProfileRecord:
    path: Path
    line_number: int
    data: dict[str, Any] | None
    raw: str
    json_error: str | None = None


def repo_path(path: str | Path) -> Path:
    candidate = Path(path).expanduser()
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    return candidate.resolve()


def load_schema() -> dict[str, Any]:
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_enums() -> dict[str, set[str]]:
    enums: dict[str, set[str]] = {}
    current: str | None = None
    heading_re = re.compile(r"^##\s+\d+\.\s+([a-zA-Z0-9_]+)\s*$")
    value_re = re.compile(r"^\|\s*`([^`]+)`\s*\|")

    for line in ENUMS_PATH.read_text(encoding="utf-8").splitlines():
        heading = heading_re.match(line)
        if heading:
            current = heading.group(1)
            enums[current] = set()
            continue
        if current is None:
            continue
        value = value_re.match(line)
        if value and value.group(1) != "Value":
            enums[current].add(value.group(1))

    return enums


def iter_jsonl(path: Path) -> Iterable[ProfileRecord]:
    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            raw = raw_line.rstrip("\n")
            if not raw.strip():
                continue
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as exc:
                yield ProfileRecord(path, line_number, None, raw, str(exc))
                continue
            if not isinstance(data, dict):
                yield ProfileRecord(path, line_number, None, raw, "line must be a JSON object")
                continue
            yield ProfileRecord(path, line_number, data, raw)


def collect_jsonl_paths(paths: list[str], default_dirs: tuple[str, ...] = DEFAULT_SCAN_DIRS) -> list[Path]:
    if paths:
        candidates = [repo_path(path) for path in paths]
    else:
        candidates = []
        for directory in default_dirs:
            candidates.extend(sorted((REPO_ROOT / directory).glob("*.jsonl")))

    files: list[Path] = []
    for candidate in candidates:
        if candidate.is_dir():
            files.extend(sorted(candidate.glob("*.jsonl")))
        elif candidate.suffix == ".jsonl":
            files.append(candidate)
        else:
            raise ValueError(f"not a JSONL file or directory: {candidate}")

    return sorted(dict.fromkeys(files))


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value)).strip().lower()
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"[^a-z0-9.-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def normalized_identity(profile: dict[str, Any]) -> tuple[str, str, str]:
    brand = normalize_text(profile.get("vendor"))
    model = normalize_text(profile.get("model"))
    firmware = normalize_text(profile.get("firmware_version")) or "all"
    return brand, model, firmware


def dedupe_key(profile: dict[str, Any]) -> str:
    return "::".join(normalized_identity(profile))


def build_normalized_profile(profile: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(profile)
    brand, model, _firmware = normalized_identity(profile)
    normalized.setdefault("normalized_brand", brand)
    normalized.setdefault("normalized_model", model)
    normalized.setdefault("dedupe_key", dedupe_key(profile))
    return normalized


def safe_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def add_common_path_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "paths",
        nargs="*",
        help="Local .jsonl files or directories to process. Defaults to incoming/*.jsonl and reviewed/*.jsonl.",
    )
