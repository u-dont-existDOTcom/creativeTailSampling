from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
ROUND_ROOT = ROOT / "analysis/retrieval_ensemble/results/round-001"
RAW_ROOT = ROUND_ROOT / "raw"
MANIFEST = ROUND_ROOT / "query_manifest.json"
OUT_ROOT = ROUND_ROOT / "compact"

MAX_EXCERPT = 900


def _trim(text: str, limit: int = MAX_EXCERPT) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:limit]


def _content_texts(envelope: dict[str, Any]) -> list[str]:
    response = envelope.get("response") or {}
    content = response.get("content") or []
    return [item.get("text", "") for item in content if isinstance(item, dict) and item.get("text")]


def _parse_exa(text: str, family: str) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    for part in re.split(r"\n---\n", text):
        title = re.search(r"^Title:\s*(.+)$", part, re.MULTILINE)
        url = re.search(r"^URL:\s*(\S+)$", part, re.MULTILINE)
        if not title or not url:
            continue
        published = re.search(r"^Published:\s*(.+)$", part, re.MULTILINE)
        highlights = re.search(r"^Highlights:\s*\n?(.*)$", part, re.MULTILINE | re.DOTALL)
        sources.append(
            {
                "title": title.group(1).strip(),
                "url": url.group(1).strip(),
                "publish_date": published.group(1).strip() if published else "",
                "excerpt": _trim(highlights.group(1) if highlights else ""),
                "family": family,
            }
        )
    return sources


def _parse_parallel(text: str, family: str) -> list[dict[str, Any]]:
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return []

    sources: list[dict[str, Any]] = []
    for result in payload.get("results") or []:
        if not isinstance(result, dict) or not result.get("url"):
            continue
        excerpts = result.get("excerpts") or []
        if isinstance(excerpts, str):
            excerpts = [excerpts]
        sources.append(
            {
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "publish_date": result.get("publish_date") or "",
                "excerpt": _trim(" ".join(str(x) for x in excerpts)),
                "family": family,
            }
        )
    return sources


def extract_sources(envelope: dict[str, Any]) -> list[dict[str, Any]]:
    if envelope.get("status") != "ok":
        return []
    provider = envelope.get("provider")
    family = envelope.get("query_family", "")
    parsed: list[dict[str, Any]] = []
    for text in _content_texts(envelope):
        if provider == "exa":
            parsed.extend(_parse_exa(text, family))
        elif provider == "parallel":
            parsed.extend(_parse_parallel(text, family))
    return parsed


def _aggregate_provider(provider_dir: Path, max_sources: int) -> list[dict[str, Any]]:
    by_url: dict[str, dict[str, Any]] = {}
    if not provider_dir.exists():
        return []

    for path in sorted(provider_dir.glob("*.json")):
        try:
            envelope = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for source in extract_sources(envelope):
            url = source["url"].strip()
            if not url:
                continue
            current = by_url.setdefault(
                url,
                {
                    "title": source["title"],
                    "url": url,
                    "publish_date": source["publish_date"],
                    "excerpt": source["excerpt"],
                    "families": set(),
                },
            )
            current["families"].add(source["family"])
            if len(source["excerpt"]) > len(current.get("excerpt", "")):
                current["excerpt"] = source["excerpt"]
            if not current.get("publish_date") and source.get("publish_date"):
                current["publish_date"] = source["publish_date"]
            if not current.get("title") and source.get("title"):
                current["title"] = source["title"]

    rows: list[dict[str, Any]] = []
    for item in by_url.values():
        families = sorted(item.pop("families"))
        item["families"] = families
        item["family_count"] = len(families)
        rows.append(item)

    rows.sort(key=lambda x: (-x["family_count"], x["title"].lower(), x["url"]))
    return rows[:max_sources]


def compact_case(raw_root: Path, case_id: str, max_sources: int = 10) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "exa": _aggregate_provider(raw_root / "exa" / case_id, max_sources),
        "parallel": _aggregate_provider(raw_root / "parallel" / case_id, max_sources),
    }


def _markdown(case: dict[str, Any], candidate_text: str) -> str:
    lines = [f"# {case['case_id']}", "", f"**Candidate:** {candidate_text}", ""]
    for provider in ("exa", "parallel"):
        lines.extend([f"## {provider.title()}", ""])
        rows = case[provider]
        if not rows:
            lines.extend(["No parsed sources.", ""])
            continue
        for idx, source in enumerate(rows, 1):
            lines.append(f"### {idx}. {source['title'] or '(untitled)'}")
            lines.append(f"- URL: {source['url']}")
            if source.get("publish_date"):
                lines.append(f"- Published: {source['publish_date']}")
            lines.append(f"- Query families: {', '.join(source['families'])}")
            if source.get("excerpt"):
                lines.append(f"- Excerpt: {source['excerpt']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_compact_bundle(round_root: Path = ROUND_ROOT, max_sources: int = 10) -> dict[str, Any]:
    manifest = json.loads((round_root / "query_manifest.json").read_text(encoding="utf-8"))
    raw_root = round_root / "raw"
    out_root = round_root / "compact"
    out_root.mkdir(parents=True, exist_ok=True)

    index: dict[str, Any] = {"round": round_root.name, "cases": {}}
    for item in manifest["cases"]:
        case_id = item["case_id"]
        compact = compact_case(raw_root, case_id, max_sources=max_sources)
        md_path = out_root / f"{case_id}.md"
        md_path.write_text(_markdown(compact, item["candidate_text"]), encoding="utf-8")
        index["cases"][case_id] = {
            "exa_sources": len(compact["exa"]),
            "parallel_sources": len(compact["parallel"]),
            "file": str(md_path.relative_to(round_root)),
        }

    (out_root / "index.json").write_text(
        json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return index


if __name__ == "__main__":
    build_compact_bundle()
