"""Reproduce the Manitoba Hutterite direct-daughter summary used in Batch 09.

Input scope is deliberately narrow: the MHS table's `Manitoba Daughter(s)`
field. It does NOT count daughters founded outside Manitoba and therefore must
not be interpreted as a complete North-American lifetime offspring count.

Run from repository root:
    python analysis/hutterite_reproduction_metrics.py
"""
from __future__ import annotations

import math
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "hutterite_manitoba_mature_lineage_reconstruction.csv"


def summarize(frame: pd.DataFrame, cutoff: int) -> dict[str, float | int]:
    d = frame[frame["year"] <= cutoff].copy()
    k = d["manitoba_daughters_count"]
    top_n = max(1, math.ceil(len(d) * 0.10))
    top_share = k.nlargest(top_n).sum() / k.sum() if k.sum() else float("nan")
    mean = float(k.mean())
    variance = float(k.var(ddof=0))
    return {
        "cutoff": cutoff,
        "n": int(len(d)),
        "mean_K": mean,
        "median_K": float(k.median()),
        "P_K_0": float((k == 0).mean()),
        "variance_K": variance,
        "variance_to_mean": variance / mean if mean else float("nan"),
        "top_10pct_share": float(top_share),
        "total_recorded_MB_daughters": int(k.sum()),
    }


def main() -> None:
    df = pd.read_csv(DATA)
    for cutoff in (1960, 1970, 1975, 1980, 1985, 1986):
        print(summarize(df, cutoff))

    pre = df[df["year"] <= 1970]
    post = df[(df["year"] >= 1971) & (df["year"] <= 1985)]
    print({
        "cohort": "1918-1970",
        "n": len(pre),
        "zero_MB_daughters": int((pre.manitoba_daughters_count == 0).sum()),
    })
    print({
        "cohort": "1971-1985",
        "n": len(post),
        "zero_MB_daughters": int((post.manitoba_daughters_count == 0).sum()),
    })


if __name__ == "__main__":
    main()
