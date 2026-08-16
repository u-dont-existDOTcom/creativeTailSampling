#!/usr/bin/env python3
import asyncio
import os
import sys
from contextlib import asynccontextmanager

ROOT_HINT = "Run: bash scripts/setup_direct_retrieval_runner.sh"


def _imports():
    try:
        import httpx2
        from mcp import ClientSession
        from mcp.client.streamable_http import streamable_http_client
    except ImportError as exc:
        raise RuntimeError(f"Direct MCP client dependency missing. {ROOT_HINT}") from exc
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


async def _check(name: str, url: str, expected: set[str], headers=None) -> bool:
    try:
        async with _session(url, headers) as session:
            result = await session.list_tools()
            names = {tool.name for tool in result.tools}
            missing = sorted(expected - names)
            if missing:
                print(f"{name}: connected, missing tools: {', '.join(missing)}")
                return False
            print(f"{name}: connected ({', '.join(sorted(expected))})")
            return True
    except Exception as exc:
        print(f"{name}: FAILED: {exc}")
        return False


async def main() -> int:
    from analysis.retrieval_ensemble.direct_mcp import (
        EXA_URL,
        PARALLEL_SEARCH_URL,
        PARALLEL_TASK_URL,
        parallel_headers,
    )

    key = os.environ.get("PARALLEL_API_KEY", "").strip()
    if not key:
        print("PARALLEL_API_KEY: missing (Search can be anonymous; Task cannot)")
        task_headers = None
    else:
        print("PARALLEL_API_KEY: set")
        task_headers = parallel_headers()

    search_headers = parallel_headers(required=False) if key else None
    checks = [
        await _check("exa", EXA_URL, {"web_search_exa", "web_fetch_exa"}),
        await _check("parallel-search", PARALLEL_SEARCH_URL, {"web_search", "web_fetch"}, search_headers),
    ]
    if task_headers:
        checks.append(
            await _check(
                "parallel-task",
                PARALLEL_TASK_URL,
                {"createDeepResearch", "getStatus", "getResultMarkdown"},
                task_headers,
            )
        )
    else:
        checks.append(False)
    return 0 if all(checks) else 1


if __name__ == "__main__":
    try:
        raise SystemExit(asyncio.run(main()))
    except RuntimeError as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(2)
