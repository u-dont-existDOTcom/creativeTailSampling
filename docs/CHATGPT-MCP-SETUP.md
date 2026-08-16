# ChatGPT MCP Exposure for Creative Tail Sampling

Date: 2026-08-16

## Purpose

Expose the routine retrieval adversaries directly to ChatGPT so Creative Tail Sampling can run Exa and Parallel Search inside the conversation instead of using the user's laptop as an execution relay.

The repository's direct MCP runner remains canonical and reproducible. ChatGPT exposure is an additional interactive surface, not a replacement for the repo runner.

## Current ChatGPT plan boundary

OpenAI currently documents that ChatGPT Pro users can connect custom MCP apps in Developer Mode with read/fetch permissions. Full write/modify MCP support is currently limited to Business and Enterprise/Edu.

Therefore:

1. **Parallel Search MCP — first ChatGPT compatibility target.** Parallel publishes explicit ChatGPT setup instructions.
2. **Exa Search MCP — second target.** Exa supports generic remote MCP clients but does not currently publish a ChatGPT-specific setup recipe in its MCP documentation.
3. **Parallel Task MCP — keep direct/repo-side as the durable default.** Parallel documents ChatGPT setup, but Pro's read/fetch boundary and the Task MCP's task-creation surface make it nonessential for the interactive path.

## ChatGPT custom app setup

Enable Developer Mode in ChatGPT web, then create a custom app from Settings → Apps/Connectors → Create. ChatGPT custom MCP support is experimental; vendor docs explicitly warn that it may not work reliably.

### Parallel Search — use the vendor's ChatGPT-specific endpoint

Name: `Parallel Search MCP`

Use exactly the endpoint Parallel currently documents for ChatGPT:

```text
https://search-mcp.parallel.ai/mcp
```

Authentication: **OAuth**.

Expected tools:

- `web_search`
- `web_fetch`

Do not substitute the generic programmatic endpoint or the `/mcp-oauth` endpoint when testing ChatGPT compatibility. Those are valid Parallel MCP endpoints in other clients, but Parallel's ChatGPT installation page currently specifies `search-mcp.parallel.ai/mcp` + OAuth.

### Exa — simplified compatibility attempt

Name: `Exa Search`

Start with the bare remote endpoint rather than a tool-filtered query-string URL:

```text
https://mcp.exa.ai/mcp
```

Authentication: none for the free tier.

Expected default tools:

- `web_search_exa`
- `web_fetch_exa`

Only after the bare endpoint scans successfully should the optional advanced tool be enabled with the `tools=` query parameter.

### Parallel Task — optional later test

Parallel's current ChatGPT instructions specify:

```text
https://task-mcp.parallel.ai/mcp
```

Authentication: OAuth.

Because the repository already has a verified direct Task MCP connection, ChatGPT Task exposure is not required for Creative Tail Sampling to function.

## Interpreting ChatGPT `Unknown error`

A successful connection from the repository's standard MCP client proves the remote server and credentials are working, but does not prove ChatGPT's custom-app scanner accepts the server. ChatGPT performs its own tool scan/authentication flow and custom MCP support remains experimental.

When ChatGPT shows only `Unknown error`:

1. test **Parallel Search first** using the exact vendor-documented ChatGPT endpoint and OAuth;
2. if that fails, treat it as a ChatGPT/Parallel custom-app compatibility problem rather than changing the working repo runner;
3. test Exa separately with the bare URL and no auth;
4. do not block the Creative Tail Sampling workflow on ChatGPT exposure—the direct runner remains authoritative.

## Verification

After creating a custom app:

1. Click **Scan Tools** and verify the expected tool names.
2. Create the app.
3. Open a fresh chat.
4. Select the custom app from the tools/app menu.
5. Ask ChatGPT to make one clearly identified search.
6. Confirm the custom tool executes rather than generic web search.

## Source references

- OpenAI Developer Mode / MCP apps: https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta
- Exa MCP: https://exa.ai/docs/reference/exa-mcp
- Parallel Search MCP, including ChatGPT setup: https://docs.parallel.ai/integrations/mcp/search-mcp
- Parallel Task MCP, including ChatGPT setup: https://docs.parallel.ai/integrations/mcp/task-mcp
- Parallel programmatic/auth details: https://docs.parallel.ai/integrations/mcp/programmatic-use
