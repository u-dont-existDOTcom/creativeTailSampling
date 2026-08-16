# Exa + Parallel retrieval setup

This project uses Exa and Parallel only after retrieval-free candidate generation and the active-project corpus collision gate.

**Codex is not required.** The canonical benchmark runner connects directly to the providers' Streamable HTTP MCP endpoints using the official Python MCP client. Codex, Claude Code, Cursor, or another MCP host may still be used interactively, but they are not part of the benchmark architecture.

## Servers

- Exa Search MCP: `https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa`
- Parallel Search MCP: `https://search.parallel.ai/mcp`
- Parallel Task MCP: `https://task-mcp.parallel.ai/mcp`

Exa Search MCP can run without an Exa key. Parallel Search MCP can run anonymously at lower rate limits. Parallel Task MCP always requires authentication.

Official references:
- Exa MCP: https://exa.ai/docs/reference/exa-mcp
- Parallel MCP quickstart: https://docs.parallel.ai/integrations/mcp/quickstart
- Parallel programmatic MCP use: https://docs.parallel.ai/integrations/mcp/programmatic-use
- Parallel Task MCP: https://docs.parallel.ai/integrations/mcp/task-mcp
- MCP Python SDK: https://github.com/modelcontextprotocol/python-sdk

## Give the direct runner the Parallel key without exposing it

Do not paste the key into chat and do not put a literal key in repository files.

In the terminal where you will run the benchmark:

```bash
read -rsp 'Paste Parallel API key: ' PARALLEL_API_KEY; echo
export PARALLEL_API_KEY
```

The prompt is silent, so the key does not appear on screen or in shell history. Confirm only that the variable is populated:

```bash
[[ -n "${PARALLEL_API_KEY:-}" ]] && echo 'Parallel key is set' || echo 'Parallel key is missing'
```

## Install the direct MCP runner

From the repository root:

```bash
bash scripts/setup_direct_retrieval_runner.sh
source .venv-retrieval/bin/activate
```

This installs the official Python MCP client in a project-local virtual environment. It does not alter any Codex configuration.

## Verify direct provider connectivity

```bash
bash scripts/check_retrieval_capabilities.sh
```

The check opens MCP sessions itself and verifies the provider tool surfaces:

- Exa: `web_search_exa`, `web_fetch_exa`
- Parallel Search: `web_search`, `web_fetch`
- Parallel Task: `createDeepResearch`, `getStatus`, `getResultMarkdown`

The benchmark must not begin paid deep-research escalation until the Task MCP connection succeeds.

## Optional persistence across terminal restarts

If you prefer a local permission-restricted environment file rather than re-entering the key for each shell:

```bash
install -m 700 -d "$HOME/.config/creative-tail-sampling"
umask 077
printf 'export %s=%q\n' PARALLEL_API_KEY "$PARALLEL_API_KEY" > "$HOME/.config/creative-tail-sampling/parallel.env"
printf '%s\n' '[ -f "$HOME/.config/creative-tail-sampling/parallel.env" ] && . "$HOME/.config/creative-tail-sampling/parallel.env"' >> "$HOME/.bashrc"
. "$HOME/.config/creative-tail-sampling/parallel.env"
```

That file remains plaintext on your machine but is mode-restricted by `umask 077`. Do not place it inside the Git repository.

## Optional Parallel CLI

The CLI is useful for diagnostics or manual deep-research experiments, but it is not required by the canonical benchmark runner.

```bash
sudo apt install -y pipx
pipx ensurepath
pipx install 'parallel-web-tools[cli]' || pipx upgrade parallel-web-tools
parallel-cli auth
```

## Optional Codex configuration

`scripts/setup_retrieval_mcp_codex.sh` remains available only as a convenience if you want to call Exa/Parallel interactively from Codex. It is not used to execute or score the benchmark.
