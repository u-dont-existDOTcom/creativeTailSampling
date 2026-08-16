def build_query_families(case: dict) -> dict[str, list[str]]:
    candidate = case["candidate_text"].strip()
    if not candidate:
        raise ValueError("candidate_text must be non-empty")

    return {
        "target_neighbor": [
            f'{candidate} Find the closest established theory, mechanism, institutional practice, or prior proposal in the same target domain that substantially contains this claim.'
        ],
        "alternate_terminology": [
            f'{candidate} Search for substantially the same mechanism described with different terminology, older vocabulary, or an adjacent discipline\'s language. Prefer conceptual equivalence over phrase matching.'
        ],
        "source_domain": [
            f'{candidate} Identify any field outside the target domain where the same structural mechanism is already well established, then look for evidence that this mechanism has already been transferred into the target domain.'
        ],
        "falsification": [
            f'{candidate} Try to falsify the originality of this proposition. Find the strongest credible predecessor or established equivalent that would justify rejecting or materially narrowing a novelty claim.'
        ],
    }
