#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path

from analysis.retrieval_ensemble.live_runner import (
    PROVIDERS,
    collect_provider,
    completion_counts,
    freeze_manifest,
)

ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "analysis" / "retrieval_ensemble" / "benchmark_cases.json"
RESULTS_ROOT = ROOT / "analysis" / "retrieval_ensemble" / "results"


def _args():
    parser = argparse.ArgumentParser(
        description="Run the frozen Creative Tail Sampling Exa/Parallel routine retrieval benchmark."
    )
    parser.add_argument(
        "--provider",
        choices=("both", "exa", "parallel"),
        default="both",
        help="Provider lane to collect. Default: both, independently and sequentially.",
    )
    parser.add_argument(
        "--round",
        default="round-001",
        help="Immutable benchmark round directory. Default: round-001.",
    )
    return parser.parse_args()


async def _main() -> int:
    args = _args()
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    round_root = RESULTS_ROOT / args.round
    manifest, digest = freeze_manifest(cases, round_root)

    providers = PROVIDERS if args.provider == "both" else (args.provider,)
    clean = True
    for provider in providers:
        print(f"=== {provider}: routine independent pass ===", flush=True)
        try:
            lane_ok = await collect_provider(provider, manifest, digest, round_root)
        except Exception as exc:
            print(f"{provider}: lane failed before/during collection: {type(exc).__name__}: {exc}")
            lane_ok = False
        clean = clean and lane_ok

    counts = completion_counts(manifest, round_root)
    print("=== checkpoint summary ===")
    for provider in PROVIDERS:
        row = counts[provider]
        print(
            f"{provider}: ok={row['ok']} error={row['error']} remaining={row['remaining']}"
        )

    selected_complete = all(counts[p]["remaining"] == 0 for p in providers)
    if clean and selected_complete:
        print(f"Routine retrieval complete. Frozen manifest sha256: {digest}")
        return 0
    print("Routine retrieval incomplete; checkpoints were preserved. Re-run the same command to resume.")
    return 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(_main()))
