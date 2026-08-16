#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "analysis" / "retrieval_ensemble" / "results"


def collect_errors(round_name: str) -> list[dict]:
    round_root = BASE / round_name / "raw"
    out: list[dict] = []
    if not round_root.exists():
        return out
    for path in sorted(round_root.glob("*/*/*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if payload.get("status") != "error":
            continue
        out.append(
            {
                "provider": payload.get("provider", path.parts[-3]),
                "case_id": payload.get("case_id", path.parts[-2]),
                "query_family": payload.get("query_family", path.stem),
                "error_type": payload.get("error_type", ""),
                "error": payload.get("error", ""),
                "path": str(path.relative_to(ROOT)),
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round", default="round-001")
    args = parser.parse_args()
    errors = collect_errors(args.round)
    if not errors:
        print("No saved provider errors found.")
        return 0
    print("=== saved provider errors ===")
    for item in errors:
        print(
            f"{item['provider']} {item['case_id']} {item['query_family']}: "
            f"{item['error_type']}: {item['error']}"
        )
        print(f"  checkpoint: {item['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
