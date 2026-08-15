"""Check whether coarse historical Hutterite period-growth variation makes
arithmetic vs geometric/log growth materially different.

Source values are transcribed from Table E-2 / E-3 of the historical Manitoba
Hutterite monograph. This is a descriptive check, NOT a fitted branching
process in random environment.
"""
from __future__ import annotations

import math
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "hutterite_manitoba_period_growth_1918_1975.csv"


def main() -> None:
    df = pd.read_csv(DATA)
    df["years"] = df.end_year - df.start_year
    df["annual_factor"] = 1 + df.reported_compound_annual_percent / 100

    years = df.years.sum()
    weighted_arithmetic = (df.annual_factor * df.years).sum() / years
    weighted_log = (df.annual_factor.map(math.log) * df.years).sum() / years
    weighted_geometric = math.exp(weighted_log)

    print(f"years={years}")
    print(f"weighted_arithmetic_factor={weighted_arithmetic:.9f}")
    print(f"weighted_geometric_factor={weighted_geometric:.9f}")
    print(f"difference_percentage_points={(weighted_arithmetic-weighted_geometric)*100:.6f}")
    print(f"annual_growth_range={df.reported_compound_annual_percent.min():.2f}%..{df.reported_compound_annual_percent.max():.2f}%")
    print(f"mean_fission_interval_range={df.reported_mean_division_interval_years.min():.1f}..{df.reported_mean_division_interval_years.max():.1f} years")


if __name__ == "__main__":
    main()
