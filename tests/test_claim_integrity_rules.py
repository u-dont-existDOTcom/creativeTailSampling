from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Exact wording pinned so the claim-integrity rules cannot be dropped from the
# runtime instructions unnoticed. Whitespace is normalized before matching.
PROTOCOL_ANCHORS = {
    "absence claims": "The claim covers only what was searched",
    "collision claims": "Saying that a tradition, theory, field, standard, or classification contains, includes, or excludes a mechanism",
    "source anchoring": "must rest on a specific passage that can be cited",
    "no invented backstory": "never add backstory, motives, or history that a person did not state",
    "quotation": "Put only a source's exact words inside quotation marks",
    "figures": "If a secondary figure does not match its own citation, use the primary figure",
    "recheck before conceding": "check the source before agreeing, just as before defending the claim",
    "say what was checked": "must name what was compared against which source or version",
    "consistency": "If they conflict, correct one and say so",
    "estimates": "Label estimates as estimates, and report a derived number at the resolution of its inputs",
    "key-condition check": "reads only the verdict text and names the key conditions it answers",
    "key-condition check never blocks": "this check never blocks promotion, demotion, or delivery",
}

WORKFLOW_ANCHORS = {
    "strongest reading": "state the strongest reading of the passage under which it is not a problem",
    "contradiction threshold": "Call something a contradiction only when both statements cannot be true under any reasonable reading",
    "no minimum": "There is no minimum number of flags",
    "recheck added facts": "check it against its source at that moment, even if it was checked during the discovery run",
    "attribution": "must not move the author's own characterization onto X",
}


def _normalized(relative_path):
    return " ".join((ROOT / relative_path).read_text().split())


def _missing(text, anchors):
    return sorted(name for name, phrase in anchors.items() if " ".join(phrase.split()) not in text)


def test_protocol_carries_claim_integrity_rules():
    assert _missing(_normalized("PROTOCOL.md"), PROTOCOL_ANCHORS) == []


def test_article_workflow_carries_review_and_recheck_rules():
    assert _missing(_normalized("docs/ARTICLE-IMPROVEMENT-TAIL-WORKFLOW.md"), WORKFLOW_ANCHORS) == []


def test_familiarity_veto_is_not_weakened():
    text = _normalized("PROTOCOL.md")
    assert "If the user immediately recognizes the proposition as common sense or a familiar theory, demote it" in text
    assert "The familiarity veto above needs no source check" in text


def test_key_condition_check_stays_experimental_and_out_of_conversation():
    text = _normalized("PROTOCOL.md")
    assert "**Experimental: key-condition check on written verdicts.**" in text
    assert "Never apply it to conversational or therapeutic replies." in text


def test_runtime_rules_are_self_contained():
    for relative_path in ("PROTOCOL.md", "docs/ARTICLE-IMPROVEMENT-TAIL-WORKFLOW.md"):
        text = (ROOT / relative_path).read_text()
        assert "universal-dev-architecture" not in text
        assert "claim-integrity pack" not in text.lower()
