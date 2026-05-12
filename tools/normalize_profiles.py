#!/usr/bin/env python3
"""Normalize local profile JSONL records into reviewed/ without changing source files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from profile_utils import build_normalized_profile, collect_jsonl_paths, iter_jsonl, repo_path, safe_write_text


def default_output_path(input_path: Path) -> Path:
    return repo_path("reviewed") / f"{input_path.stem}.normalized.jsonl"


def normalize_file(input_path: Path, output_path: Path) -> int:
    lines: list[str] = []
    count = 0
    for record in iter_jsonl(input_path):
        if record.json_error or record.data is None:
            raise ValueError(f"{record.path}:{record.line_number}: invalid JSONL: {record.json_error}")
        normalized = build_normalized_profile(record.data)
        lines.append(json.dumps(normalized, ensure_ascii=False, sort_keys=True))
        count += 1
    safe_write_text(output_path, "\n".join(lines) + ("\n" if lines else ""))
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Local .jsonl files or directories to normalize. Defaults to incoming/*.jsonl.")
    parser.add_argument("--output-dir", default="reviewed", help="Directory for normalized JSONL outputs. Must not overwrite existing files.")
    args = parser.parse_args()

    try:
        paths = collect_jsonl_paths(args.paths, default_dirs=("incoming",))
        output_dir = repo_path(args.output_dir)
        if not paths:
            print("No JSONL files found.")
            return 0
        total = 0
        for input_path in paths:
            output_path = output_dir / f"{input_path.stem}.normalized.jsonl"
            total += normalize_file(input_path, output_path)
    except (ValueError, FileExistsError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"Normalized {total} record(s) into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
