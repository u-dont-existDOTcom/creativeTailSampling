#!/usr/bin/env python3
"""Compute reproduction-distribution metrics for the FEEFHS 1973 mature cohorts.

Source tables:
- https://feefhs.org/erg/hutterites-lehrerleut-colonies-1973
- https://feefhs.org/erg/hutterites-dariusleut-colonies-1973

Cohort definition: colonies founded 1918-1953 inclusive, giving at least 20 years
of observable reproduction before the 1973 source cutoff. K is the number of
listed daughters through 1973.

Important source-normalization note:
The Dariusleut table contains two distinct historical 'Beadle, South Dakota'
episodes (1905-1918 and 1920-1935). Raley (1918) belongs to the earlier episode;
therefore the 1920 Beadle cohort row has K=2 (Felger 1926 and King Ranch 1935),
not K=3. The CSV stores this disambiguated K directly.
"""

from __future__ import annotations

import math
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "hutterite_feefhs_1973_mature_cohorts.csv"


def metrics(series: pd.Series) -> dict[str, float]:
    k = series.astype(float)
    n = len(k)
    top_n = max(1, math.ceil(0.10 * n))
    ordered = k.sort_values()
    mean = float(k.mean())
    var = float(k.var(ddof=0))
    return {
        "n": n,
        "daughters": int(k.sum()),
        "mean_K": mean,
        "median_K": float(k.median()),
        "variance_K": var,
        "variance_mean": var / mean if mean else float("nan"),
        "P_K_0": float((k == 0).mean()),
        "top10_share": float(ordered.iloc[-top_n:].sum() / k.sum()) if k.sum() else float("nan"),
        "max_K": int(k.max()),
    }


def main() -> None:
    df = pd.read_csv(DATA)
    expected = {"Lehrerleut": 29, "Dariusleut": 33}
    assert df.groupby("branch").size().to_dict() == expected
    assert df["year"].between(1918, 1953).all()

    rows = []
    for branch, group in df.groupby("branch", sort=True):
        rows.append({"branch": branch, **metrics(group["K"])})

    out = pd.DataFrame(rows)
    print(out.to_csv(index=False), end="")


if __name__ == "__main__":
    main()
