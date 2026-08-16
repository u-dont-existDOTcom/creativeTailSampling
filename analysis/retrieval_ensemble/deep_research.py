from __future__ import annotations

import json
from collections import OrderedDict
from pathlib import Path
from typing import Any

CASES = OrderedDict(
    [
        (
            "C015",
            {
                "candidate": "A governance right can exist in text yet be dead in a reachable institutional state, so governance should be verified for safety, liveness, and bounded liveness under realistic recusal, vacancy, quorum, deadline, delegation, and noncooperation states.",
                "target": "governance and institutional design",
            },
        ),
        (
            "C001",
            {
                "candidate": "Use high-information concrete cases to distinguish plausible constitutional or value interpretations, collect independent answers before deliberation, and preserve resolved cases as regression tests.",
                "target": "constitutional design, value interpretation, and deliberative governance",
            },
        ),
        (
            "C005",
            {
                "candidate": "Judge communal reproducibility by the parent-offspring distribution rather than total spread or mean daughters alone, including zero-offspring probability, median daughters, variance, and concentration in superstar parents.",
                "target": "intentional-community and organizational replication",
            },
        ),
        (
            "C006",
            {
                "candidate": "When evaluating communal success, prolific lineages mechanically contribute more extant observations, so analyses must state whether they sample founding attempts, lineages, extant communities, residents, or future movement contribution.",
                "target": "intentional-community and organizational-replication research",
            },
        ),
        (
            "C025",
            {
                "candidate": "A community should predefine how member-critical functions continue if the institution itself becomes nonviable, separating recovery of the organization from continuity of housing, care, food, records, transport, and other critical functions.",
                "target": "intentional communities, residential communities, nonprofits, and member-serving organizations",
            },
        ),
    ]
)


def build_prompt(case_id: str, case: dict[str, str]) -> str:
    return f"""Creative Tail Sampling precedent attack — {case_id}

Candidate proposition:
{case['candidate']}

Target domain:
{case['target']}

Research task:
Try to falsify the originality of the candidate. Find the strongest credible prior theory, research program, institutional practice, formal method, or documented proposal that substantially contains the same structural mechanism.

Search broadly across terminology and disciplines, but distinguish carefully between:
1. a mechanism that is merely familiar in a source domain; and
2. evidence that substantially the same structural transfer or operational architecture is already established in the target domain.

A familiar source-domain mechanism alone does not kill a cross-domain transfer. Find the strongest credible prior in the target domain or the closest documented transfer into it. Prefer primary literature, standards, official guidance, and original technical/historical sources. Do not infer originality from failure to find a precedent.

Return a cited research report with:
- strongest direct or near-direct precedents;
- exactly which parts of the candidate each precedent contains;
- what, if anything, remains as a narrower residual;
- a final disposition of DIRECT COLLISION, ROOT COLLISION + NARROW RESIDUAL, or NO TARGET-DOMAIN COLLISION FOUND;
- confidence and important search limitations.
"""


def find_run_id(value: Any) -> str:
    if isinstance(value, dict):
        for key in ("run_id", "id"):
            item = value.get(key)
            if isinstance(item, str) and item.startswith("trun_"):
                return item
        for item in value.values():
            try:
                return find_run_id(item)
            except ValueError:
                pass
    elif isinstance(value, list):
        for item in value:
            try:
                return find_run_id(item)
            except ValueError:
                pass
    raise ValueError("No Parallel task run_id found in CLI output")


def result_is_complete(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    if payload.get("status") == "ok":
        return bool(payload.get("result"))
    return payload.get("status") == "completed" and bool(payload.get("output"))
