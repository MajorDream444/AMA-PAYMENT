# Global Codex Operating Context

## Graphify Context Layer

Graphify is a standing context layer for this workspace.

When working inside any repo or project:

1. If `graphify-out/GRAPH_REPORT.md` exists, read it before broad file searches, codebase explanations, architecture answers, or multi-file edits.
2. If `graphify-out/wiki/index.md` exists, prefer the wiki map before raw file spelunking.
3. For cross-module questions, prefer:
   - `graphify query "<question>"`
   - `graphify path "<A>" "<B>"`
   - `graphify explain "<concept>"`
4. Use Graphify as the context map, then verify current code with direct file reads before editing.
5. After meaningful code or docs changes in a graphified repo, run `graphify update .` when it is safe and useful so the graph stays current.

Graphify should provide durable context, not replace repo truth. GitHub, local files, system docs, and handoff files remain authoritative.

## Important Boundary

Do not expose secrets while using Graphify or any local context tool.
