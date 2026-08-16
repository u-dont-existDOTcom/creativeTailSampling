_ALLOWED = {"direct", "root_plus_residual", "corroboration", "ambiguous", "no_collision"}


def adjudicate(records: list[dict]) -> dict:
    strengths = [record.get("collision_strength", "no_collision") for record in records]
    invalid = [strength for strength in strengths if strength not in _ALLOWED]
    if invalid:
        raise ValueError(f"invalid collision_strength: {invalid[0]}")
    if "direct" in strengths:
        return {"action": "reject", "reason": "at least one credible direct collision"}
    if "root_plus_residual" in strengths:
        return {"action": "narrow", "reason": "known root with a potentially additive residual"}
    if "ambiguous" in strengths:
        return {"action": "escalate", "reason": "unresolved plausible collision"}
    return {"action": "no_collision_found", "reason": "no substantive collision established"}
