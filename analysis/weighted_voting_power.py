#!/usr/bin/env python3
"""Exact power indices for small weighted voting games.

Creative Tail use case: intentional-community/federation governance analysis.

This tool deliberately distinguishes *nominal voting weight* from *pivotal voting
power*. It computes exact normalized Penrose-Banzhaf and Shapley-Shubik indices
by enumerating coalitions, so it is intended for small/medium federations rather
than hundreds of voters.

Examples
--------

# Absolute quota
python analysis/weighted_voting_power.py --weights 100 64 9 --quota 103.8 \
    --labels A B C

# Quota as fraction of total weight
python analysis/weighted_voting_power.py --weights 10 8 3 --quota-fraction 0.60

Important: these are top-tier power indices. A two-tier individual-influence
analysis additionally requires a model of how each represented community forms
its position and how correlated member preferences are.
"""

from __future__ import annotations

import argparse
import json
from math import factorial
from typing import Sequence


def exact_power(weights: Sequence[float], quota: float) -> dict[str, object]:
    """Return exact coalition and power statistics for a weighted voting game."""
    n = len(weights)
    if n == 0:
        raise ValueError("at least one weight is required")
    if n > 24:
        raise ValueError(
            "exact enumeration is exponential; use <=24 players or a sampled/optimized method"
        )
    if any(weight <= 0 for weight in weights):
        raise ValueError("all weights must be positive")
    total_weight = float(sum(weights))
    if not (0 < quota <= total_weight):
        raise ValueError("quota must be >0 and <= total weight")

    banzhaf_swings = [0] * n
    shapley_shubik = [0.0] * n
    winning_coalitions = 0
    minimal_winning: list[list[int]] = []

    fact_n = factorial(n)

    for mask in range(1 << n):
        coalition_weight = sum(
            weights[player] for player in range(n) if (mask >> player) & 1
        )
        winning = coalition_weight >= quota
        if winning:
            winning_coalitions += 1
            is_minimal = True
            for player in range(n):
                if (mask >> player) & 1 and coalition_weight - weights[player] >= quota:
                    is_minimal = False
                    break
            if is_minimal:
                minimal_winning.append(
                    [player for player in range(n) if (mask >> player) & 1]
                )

        # Count swings for members already in a winning coalition.
        if winning:
            for player in range(n):
                if (mask >> player) & 1 and coalition_weight - weights[player] < quota:
                    banzhaf_swings[player] += 1

        # Shapley-Shubik: coalitions S not containing i where i is pivotal.
        for player in range(n):
            if (mask >> player) & 1:
                continue
            if coalition_weight < quota <= coalition_weight + weights[player]:
                k = mask.bit_count()
                shapley_shubik[player] += (
                    factorial(k) * factorial(n - k - 1) / fact_n
                )

    swing_total = sum(banzhaf_swings)
    normalized_banzhaf = [
        swing / swing_total if swing_total else 0.0 for swing in banzhaf_swings
    ]

    return {
        "total_weight": total_weight,
        "quota": quota,
        "quota_fraction": quota / total_weight,
        "weights": list(map(float, weights)),
        "weight_shares": [weight / total_weight for weight in weights],
        "winning_coalitions": winning_coalitions,
        "minimal_winning_coalitions": minimal_winning,
        "banzhaf_raw_swings": banzhaf_swings,
        "banzhaf_normalized": normalized_banzhaf,
        "shapley_shubik": shapley_shubik,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weights", nargs="+", type=float, required=True)
    parser.add_argument("--labels", nargs="+", default=None)
    quota_group = parser.add_mutually_exclusive_group(required=True)
    quota_group.add_argument("--quota", type=float, help="absolute winning quota")
    quota_group.add_argument(
        "--quota-fraction",
        type=float,
        help="winning quota as fraction of total weight, e.g. 0.6",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    weights = args.weights
    labels = args.labels or [f"P{index + 1}" for index in range(len(weights))]
    if len(labels) != len(weights):
        raise SystemExit("--labels must have the same number of entries as --weights")

    quota = (
        args.quota
        if args.quota is not None
        else float(args.quota_fraction) * sum(weights)
    )
    result = exact_power(weights, quota)

    result["players"] = [
        {
            "label": label,
            "weight": weights[index],
            "weight_share": result["weight_shares"][index],
            "banzhaf_raw_swings": result["banzhaf_raw_swings"][index],
            "banzhaf_normalized": result["banzhaf_normalized"][index],
            "shapley_shubik": result["shapley_shubik"][index],
        }
        for index, label in enumerate(labels)
    ]

    result["minimal_winning_coalitions"] = [
        [labels[index] for index in coalition]
        for coalition in result["minimal_winning_coalitions"]
    ]

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
