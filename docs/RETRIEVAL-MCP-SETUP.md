# Exa + Parallel retrieval setup for Codex

This project uses Exa and Parallel only after retrieval-free candidate generation and the active-project corpus collision gate.

## Servers

- Exa Search MCP: `https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa`
- Parallel Search MCP: `https://search.parallel.ai/mcp`
- Parallel Task MCP: `https://task-mcp.parallel.ai/mcp`

Exa Search MCP can run without an Exa key. Parallel Search MCP can run anonymously at lower rate limits. Parallel Task MCP always requires authentication.

Official references:
- Exa MCP: https://exa.ai/docs/reference/exa-mcp
- Parallel Search MCP: https://docs.parallel.ai/integrations/mcp/search-mcp
- Parallel Task MCP: https://docs.parallel.ai/integrations/mcp/task-mcp
- Parallel CLI: https://docs.parallel.ai/integrations/cli

## Give Codex the Parallel key without exposing it

Do not paste the key into chat and do not put a literal key in repository files or `~/.codex/config.toml`.

In the terminal from which you will launch Codex, enter:

```bash
read -rsp 'Paste Parallel API key: ' PARALLEL_API_KEY; echo
export PARALLEL_API_KEY
```

The prompt is silent, so the key does not appear on screen or in shell history. Confirm only that the variable is populated:

```bash
[[ -n "${PARALLEL_API_KEY:-}" ]] && echo 'Parallel key is set' || echo 'Parallel key is missing'
```

Then configure all three MCP servers:

```bash
bash scripts/setup_retrieval_mcp_codex.sh
```

The setup uses Codex's `--bearer-token-env-var PARALLEL_API_KEY` option. Codex config therefore stores the variable name, not its value.

Restart Codex after setup. The active Codex process must inherit the variable; setting it in another terminal after Codex has already started is insufficient.

### Optional persistence across terminal restarts

If you prefer a local permission-restricted environment file rather than re-entering the key for each shell:

```bash
install -m 700 -d "$HOME/.config/creative-tail-sampling"
umask 077
printf 'export %s=%q\n' PARALLEL_API_KEY "$PARALLEL_API_KEY" > "$HOME/.config/creative-tail-sampling/parallel.env"
printf '%s\n' '[ -f "$HOME/.config/creative-tail-sampling/parallel.env" ] && . "$HOME/.config/creative-tail-sampling/parallel.env"' >> "$HOME/.bashrc"
. "$HOME/.config/creative-tail-sampling/parallel.env"
```

That file remains plaintext on your machine but is mode-restricted by `umask 077`. Do not place it inside the Git repository.

## Parallel CLI

The CLI is optional and is used only for deep-research escalation or diagnostics. On Ubuntu/Zorin:

```bash
sudo apt install -y pipx
pipx ensurepath
pipx install 'parallel-web-tools[cli]' || pipx upgrade parallel-web-tools
```

It uses the same `PARALLEL_API_KEY` environment variable. Verify authentication with:

```bash
parallel-cli auth
```

Parallel also supports interactive OAuth via `parallel-cli login` if you prefer not to use an API key for CLI calls.

## Verify configuration

```bash
bash scripts/check_retrieval_capabilities.sh
```

Then restart/open Codex and use `/mcp`. Confirm that Exa exposes `web_search_exa`, `web_fetch_exa`, and `web_search_advanced_exa`; Parallel Search exposes `web_search` and `web_fetch`; and Parallel Task exposes deep-research/task tools. The benchmark must not begin paid deep-research escalation until Parallel Task authentication is confirmed.
