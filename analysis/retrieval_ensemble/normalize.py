_ALLOWED_STRENGTHS = {"direct", "root_plus_residual", "corroboration", "ambiguous", "no_collision"}
_REQUIRED = {"provider", "query_family", "collision_strength"}


def normalize_result(raw: dict) -> dict:
    missing = sorted(_REQUIRED - raw.keys())
    if missing:
        raise ValueError(f"missing required field: {missing[0]}")
    strength = raw["collision_strength"]
    if strength not in _ALLOWED_STRENGTHS:
        raise ValueError(f"invalid collision_strength: {strength}")
    return {
        "provider": raw["provider"],
        "query_family": raw["query_family"],
        "title": raw.get("title", ""),
        "url": raw.get("url", ""),
        "date": raw.get("date", ""),
        "precedent_claim": raw.get("precedent_claim", ""),
        "collision_strength": strength,
        "source_quality": raw.get("source_quality", "unknown"),
        "unique_to_provider": bool(raw.get("unique_to_provider", False)),
        "rationale": raw.get("rationale", ""),
    }
