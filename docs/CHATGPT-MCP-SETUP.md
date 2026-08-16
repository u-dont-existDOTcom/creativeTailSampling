# ChatGPT MCP Exposure for Creative Tail Sampling

Date: 2026-08-16

## Purpose

Expose the routine retrieval adversaries directly to ChatGPT so Creative Tail Sampling can run Exa and Parallel Search inside the conversation instead of using the user's laptop as an execution relay.

The repository's direct MCP runner remains canonical and reproducible. ChatGPT exposure is an additional interactive surface, not a replacement for the repo runner.

## Current ChatGPT plan boundary

OpenAI currently documents that ChatGPT Pro users can connect custom MCP apps in Developer Mode with read/fetch permissions. Full write/modify MCP support is currently limited to Business and Enterprise/Edu.

Therefore:

1. **Exa Search MCP — expose to ChatGPT now.** Read/search/fetch only.
2. **Parallel Search MCP — expose to ChatGPT now.** Read/search/fetch only.
3. **Parallel Task MCP — keep direct/repo-side by default.** Test in ChatGPT only if the tool scanner/permission model explicitly accepts its deep-research tools under Pro's read/fetch boundary. Do not rely on it in ChatGPT until verified.

## ChatGPT custom app setup

Enable Developer Mode in ChatGPT web, then create a custom app from Settings → Apps → Create.

### Exa

Name: `Exa Search`

Remote MCP endpoint:

```text
https://mcp.exa.ai/mcp?tools=web_search_exa,web_fetch_exa,web_search_advanced_exa
```

Authentication: none for the free tier. Add an Exa key later only if rate limits justify it.

Expected tools:

- `web_search_exa`
- `web_fetch_exa`
- `web_search_advanced_exa`

### Parallel Search

Name: `Parallel Search`

Preferred ChatGPT endpoint:

```text
https://search.parallel.ai/mcp-oauth
```

Authentication: OAuth. This avoids embedding a literal Parallel API key into app configuration and uses Parallel's auth-enforced Search MCP endpoint.

Expected tools:

- `web_search`
- `web_fetch`

If OAuth is unavailable in the ChatGPT setup UI, use the standard endpoint with Bearer API-key authentication if the UI explicitly supports secret/header authentication:

```text
https://search.parallel.ai/mcp
```

Never paste the Parallel API key into conversation text or commit it to GitHub.

### Parallel Task — provisional

Endpoint:

```text
https://task-mcp.parallel.ai/mcp
```

Authentication: OAuth or Bearer key is required.

Expected tools currently include:

- `createDeepResearch`
- `getStatus`
- `getResultMarkdown`

Because ChatGPT Pro currently permits custom MCPs only within the read/fetch permission boundary, do not make Parallel Task a required ChatGPT dependency. The repository's direct Task MCP connection remains canonical for deep-research escalation.

## Verification

After creating Exa and Parallel Search apps:

1. Click **Scan Tools** during app creation and verify the expected tool names.
2. Create the apps.
3. Open a fresh chat.
4. Select both custom apps from the tools/app menu.
5. Ask ChatGPT to make one clearly identified Exa search and one clearly identified Parallel search for the same harmless query.
6. Confirm both tools execute independently rather than falling back to generic web search.

## Source references

- OpenAI Developer Mode / MCP apps: https://help.openai.com/en/articles/12584461-developer-mode-apps-and-full-mcp-connectors-in-chatgpt-beta
- Exa MCP: https://exa.ai/docs/reference/exa-mcp
- Parallel MCP quickstart: https://docs.parallel.ai/integrations/mcp/quickstart
- Parallel programmatic/auth details: https://docs.parallel.ai/integrations/mcp/programmatic-use
