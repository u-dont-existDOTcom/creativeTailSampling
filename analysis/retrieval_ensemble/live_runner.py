from __future__ import annotations

import hashlib
import json
import os
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from analysis.retrieval_ensemble.direct_mcp import (
    EXA_URL,
    PARALLEL_SEARCH_URL,
    build_parallel_search_args,
    parallel_headers,
)
from analysis.retrieval_ensemble.query_families import build_query_families

PROVIDERS = ("exa", "parallel")
FAMILIES = (
    "target_neighbor",
    "alternate_terminology",
    "source_domain",
    "falsification",
)


def build_manifest(cases: list[dict]) -> dict:
    frozen_cases = []
    for case in cases:
        families = build_query_families({"candidate_text": case["candidate_text"]})
        queries = {name: families[name][0] for name in FAMILIES}
        frozen_cases.append(
            {
                "case_id": case["case_id"],
                "candidate_text": case["candidate_text"],
                "queries": queries,
            }
        )
    return {"version": 1, "cases": frozen_cases}


def manifest_digest(manifest: dict) -> str:
    payload = json.dumps(
        manifest, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def result_path(root: Path, provider: str, case_id: str, family: str) -> Path:
    return root / "raw" / provider / case_id / f"{family}.json"


def should_skip(path: Path) -> bool:
    if not path.exists():
        return False
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("status") == "ok"
    except (OSError, json.JSONDecodeError):
        return False


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp.replace(path)


def freeze_manifest(cases: list[dict], round_root: Path) -> tuple[dict, str]:
    expected = build_manifest(cases)
    expected_digest = manifest_digest(expected)
    manifest_path = round_root / "query_manifest.json"
    digest_path = round_root / "query_manifest.sha256"

    if manifest_path.exists():
        existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        existing_digest = manifest_digest(existing)
        if existing_digest != expected_digest:
            raise RuntimeError(
                "Frozen query manifest differs from current benchmark fixtures. "
                "Preserve this round and start a new round instead of mutating it."
            )
        if digest_path.exists():
            recorded = digest_path.read_text(encoding="utf-8").strip().split()[0]
            if recorded != existing_digest:
                raise RuntimeError("query_manifest.sha256 does not match query_manifest.json")
        else:
            digest_path.write_text(existing_digest + "\n", encoding="utf-8")
        return existing, existing_digest

    round_root.mkdir(parents=True, exist_ok=True)
    _write_json(manifest_path, expected)
    digest_path.write_text(expected_digest + "\n", encoding="utf-8")
    return expected, expected_digest


def _jsonable(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(v) for v in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def _tool_schema(tool: Any) -> dict:
    schema = getattr(tool, "inputSchema", None)
    if schema is None:
        schema = getattr(tool, "input_schema", None)
    return schema or {}


def _exa_args(query: str, schema: dict) -> dict[str, Any]:
    properties = schema.get("properties", {}) if isinstance(schema, dict) else {}
    required = set(schema.get("required", [])) if isinstance(schema, dict) else set()
    if properties and "query" not in properties and "query" not in required:
        raise RuntimeError("Exa web_search_exa schema does not expose a query field")
    # Keep the request minimal. Exa's MCP search defaults to a useful result count.
    return {"query": query}


def _parallel_args(candidate_text: str, objective: str, schema: dict) -> dict[str, Any]:
    args = build_parallel_search_args(candidate_text, objective)
    properties = schema.get("properties", {}) if isinstance(schema, dict) else {}
    required = set(schema.get("required", [])) if isinstance(schema, dict) else set()
    for name in ("objective", "search_queries"):
        if properties and name not in properties and name not in required:
            raise RuntimeError(f"Parallel web_search schema does not expose {name}")
    return args


def _imports():
    try:
        import httpx2
        from mcp import ClientSession
        from mcp.client.streamable_http import streamable_http_client
    except ImportError as exc:
        raise RuntimeError(
            "Direct MCP dependencies missing. Run: bash scripts/setup_direct_retrieval_runner.sh"
        ) from exc
    return httpx2, ClientSession, streamable_http_client


@asynccontextmanager
async def _session(url: str, headers: dict[str, str] | None = None):
    httpx2, ClientSession, streamable_http_client = _imports()
    if headers:
        async with httpx2.AsyncClient(headers=headers, follow_redirects=True) as client:
            async with streamable_http_client(url, http_client=client) as streams:
                read, write = streams[0], streams[1]
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    yield session
    else:
        async with streamable_http_client(url) as streams:
            read, write = streams[0], streams[1]
            async with ClientSession(read, write) as session:
                await session.initialize()
                yield session


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _request_for(provider: str, candidate_text: str, objective: str, schema: dict):
    if provider == "exa":
        return "web_search_exa", _exa_args(objective, schema)
    if provider == "parallel":
        return "web_search", _parallel_args(candidate_text, objective, schema)
    raise ValueError(f"unknown provider: {provider}")


async def collect_provider(
    provider: str,
    manifest: dict,
    manifest_sha256: str,
    round_root: Path,
) -> bool:
    if provider == "exa":
        url = EXA_URL
        headers = None
        tool_name = "web_search_exa"
    elif provider == "parallel":
        url = PARALLEL_SEARCH_URL
        headers = parallel_headers(required=False) or None
        tool_name = "web_search"
    else:
        raise ValueError(f"unknown provider: {provider}")

    async with _session(url, headers) as session:
        listed = await session.list_tools()
        tools = {tool.name: tool for tool in listed.tools}
        if tool_name not in tools:
            raise RuntimeError(f"{provider} connected but {tool_name} is unavailable")
        schema = _tool_schema(tools[tool_name])
        _write_json(
            round_root / "schemas" / f"{provider}.json",
            {
                "provider": provider,
                "captured_at": _utc_now(),
                "tool": tool_name,
                "schema": schema,
            },
        )

        for case in manifest["cases"]:
            for family in FAMILIES:
                path = result_path(round_root, provider, case["case_id"], family)
                if should_skip(path):
                    continue
                objective = case["queries"][family]
                call_name, arguments = _request_for(
                    provider, case["candidate_text"], objective, schema
                )
                envelope = {
                    "status": "running",
                    "provider": provider,
                    "case_id": case["case_id"],
                    "query_family": family,
                    "manifest_sha256": manifest_sha256,
                    "request": {"tool": call_name, "arguments": arguments},
                    "started_at": _utc_now(),
                }
                _write_json(path, envelope)
                try:
                    result = await session.call_tool(call_name, arguments=arguments)
                except Exception as exc:
                    envelope.update(
                        {
                            "status": "error",
                            "finished_at": _utc_now(),
                            "error_type": type(exc).__name__,
                            "error": str(exc),
                        }
                    )
                    _write_json(path, envelope)
                    # Stop this provider lane after the first tool failure. The next
                    # invocation resumes from the last successful checkpoint rather
                    # than hammering a rate-limited or schema-changed server.
                    return False

                envelope.update(
                    {
                        "status": "ok",
                        "finished_at": _utc_now(),
                        "response": _jsonable(result),
                    }
                )
                _write_json(path, envelope)
    return True


def completion_counts(manifest: dict, round_root: Path) -> dict[str, dict[str, int]]:
    total = len(manifest["cases"]) * len(FAMILIES)
    counts: dict[str, dict[str, int]] = {}
    for provider in PROVIDERS:
        ok = error = 0
        for case in manifest["cases"]:
            for family in FAMILIES:
                path = result_path(round_root, provider, case["case_id"], family)
                if not path.exists():
                    continue
                try:
                    status = json.loads(path.read_text(encoding="utf-8")).get("status")
                except (OSError, json.JSONDecodeError):
                    continue
                ok += status == "ok"
                error += status == "error"
        counts[provider] = {"ok": ok, "error": error, "remaining": total - ok}
    return counts
