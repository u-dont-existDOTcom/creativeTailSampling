#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from analysis.retrieval_ensemble.deep_research import (
    CASES,
    build_prompt,
    find_run_id,
    result_is_complete,
)

ROOT = Path(__file__).resolve().parents[1]
DEEP_ROOT = ROOT / "analysis/retrieval_ensemble/results/round-001/deep"
PROCESSOR = "pro"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def _parse_json_stdout(stdout: str) -> Any:
    text = stdout.strip()
    if not text:
        raise ValueError("Parallel CLI returned empty stdout")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Defensive fallback for a CLI notice printed before/after JSON.
        first_obj = text.find("{")
        last_obj = text.rfind("}")
        first_arr = text.find("[")
        last_arr = text.rfind("]")
        candidates = []
        if first_obj >= 0 and last_obj > first_obj:
            candidates.append(text[first_obj : last_obj + 1])
        if first_arr >= 0 and last_arr > first_arr:
            candidates.append(text[first_arr : last_arr + 1])
        for candidate in candidates:
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                pass
        raise


def _launch_path(case_id: str) -> Path:
    return DEEP_ROOT / case_id / "launch.json"


def _result_path(case_id: str) -> Path:
    return DEEP_ROOT / case_id / "result.json"


def _existing_run_id(case_id: str) -> str | None:
    path = _launch_path(case_id)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if payload.get("status") != "ok":
        return None
    run_id = payload.get("run_id")
    return run_id if isinstance(run_id, str) and run_id.startswith("trun_") else None


def launch_all() -> int:
    failures = 0
    launched = 0
    reused = 0

    print("Parallel deep escalation: 5 frozen cases, processor=pro")
    print("List price at current published rates: $0.10/run, maximum new spend for all five = $0.50 before credits.")

    for case_id, case in CASES.items():
        result_path = _result_path(case_id)
        if result_is_complete(result_path):
            print(f"{case_id}: result already complete")
            reused += 1
            continue

        existing = _existing_run_id(case_id)
        if existing:
            print(f"{case_id}: existing run {existing}; not relaunching")
            reused += 1
            continue

        case_dir = DEEP_ROOT / case_id
        case_dir.mkdir(parents=True, exist_ok=True)
        prompt_path = case_dir / "prompt.txt"
        prompt_path.write_text(build_prompt(case_id, case), encoding="utf-8")

        command = [
            "parallel-cli",
            "research",
            "run",
            "-f",
            str(prompt_path),
            "--processor",
            PROCESSOR,
            "--no-wait",
            "--json",
        ]
        started_at = _now()
        proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        envelope: dict[str, Any] = {
            "case_id": case_id,
            "processor": PROCESSOR,
            "started_at": started_at,
            "finished_at": _now(),
            "exit_code": proc.returncode,
        }
        if proc.returncode != 0:
            envelope.update({"status": "error", "stderr": proc.stderr[-4000:], "stdout": proc.stdout[-4000:]})
            _write_json(_launch_path(case_id), envelope)
            print(f"{case_id}: launch FAILED (exit {proc.returncode})", file=sys.stderr)
            failures += 1
            # An auth/API failure is likely shared by all cases. Stop rather than
            # hammering the endpoint or producing five identical failures.
            break

        try:
            parsed = _parse_json_stdout(proc.stdout)
            run_id = find_run_id(parsed)
        except Exception as exc:
            envelope.update({"status": "error", "parse_error": f"{type(exc).__name__}: {exc}", "stdout": proc.stdout[-8000:]})
            _write_json(_launch_path(case_id), envelope)
            print(f"{case_id}: launch returned no parsable run_id", file=sys.stderr)
            failures += 1
            break

        envelope.update({"status": "ok", "run_id": run_id, "response": parsed})
        _write_json(_launch_path(case_id), envelope)
        print(f"{case_id}: launched {run_id}")
        launched += 1

    print(f"launch summary: new={launched} existing_or_complete={reused} failures={failures}")
    return 0 if failures == 0 else 1


def poll_all() -> int:
    failures = 0
    complete = 0

    for case_id in CASES:
        result_path = _result_path(case_id)
        if result_is_complete(result_path):
            print(f"{case_id}: result already complete")
            complete += 1
            continue

        run_id = _existing_run_id(case_id)
        if not run_id:
            print(f"{case_id}: no launched run_id; cannot poll", file=sys.stderr)
            failures += 1
            continue

        print(f"{case_id}: polling {run_id}")
        started_at = _now()
        proc = subprocess.run(
            ["parallel-cli", "research", "poll", run_id, "--json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        envelope: dict[str, Any] = {
            "case_id": case_id,
            "processor": PROCESSOR,
            "run_id": run_id,
            "started_at": started_at,
            "finished_at": _now(),
            "exit_code": proc.returncode,
        }
        if proc.returncode != 0:
            envelope.update({"status": "error", "stderr": proc.stderr[-4000:], "stdout": proc.stdout[-4000:]})
            _write_json(result_path, envelope)
            print(f"{case_id}: poll FAILED (exit {proc.returncode}); same run will be polled on resume", file=sys.stderr)
            failures += 1
            continue

        try:
            parsed = _parse_json_stdout(proc.stdout)
        except Exception as exc:
            envelope.update({"status": "error", "parse_error": f"{type(exc).__name__}: {exc}", "stdout": proc.stdout[-12000:]})
            _write_json(result_path, envelope)
            print(f"{case_id}: completed CLI call but JSON parse failed", file=sys.stderr)
            failures += 1
            continue

        envelope.update({"status": "ok", "result": parsed})
        _write_json(result_path, envelope)
        print(f"{case_id}: result saved")
        complete += 1

    print(f"poll summary: complete={complete}/{len(CASES)} failures={failures}")
    return 0 if complete == len(CASES) and failures == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("launch", "poll", "all"), default="all")
    args = parser.parse_args()

    if args.phase == "launch":
        return launch_all()
    if args.phase == "poll":
        return poll_all()

    rc = launch_all()
    if rc:
        return rc
    return poll_all()


if __name__ == "__main__":
    raise SystemExit(main())
