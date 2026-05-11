---
name: graphify-context
description: Use Graphify as a standing codebase context layer before broad file searches, architecture explanations, cross-module questions, or multi-file edits. Also use it after meaningful code or docs changes to refresh graphify-out when safe.
---

# Graphify Context

Graphify is the first-pass map for any repo where it is installed. It does not replace direct file reads, git state, handoff docs, or system instructions.

## Trigger

Use this skill when the user asks for:

- architecture or codebase explanation
- broad file search or repo orientation
- cross-module questions
- multi-file edits
- refactors or docs updates that should keep the repo map current
- anything that explicitly mentions Graphify

## First-Pass Context

1. If `graphify-out/GRAPH_REPORT.md` exists, read it before broad raw searches.
2. If `graphify-out/wiki/index.md` exists, prefer that wiki map before raw file spelunking.
3. For cross-module questions, prefer the local CLI:

```bash
graphify query "<question>"
graphify path "<A>" "<B>"
graphify explain "<concept>"
```

4. Verify anything important against current files before editing or making a firm claim.
5. Never expose secret values from `.env`, local config, Graphify output, or tool output.

## Update Rule

After meaningful code or docs changes in a graphified repo, run:

```bash
graphify update .
```

Only run it when safe and useful. If the repo is very large, not graphified yet, or the user asked for read-only/audit-only work, report the reason instead of forcing an update.

## Install Helpers

Graphify can be installed locally with one of:

```bash
uv tool install graphifyy && graphify install
pipx install graphifyy && graphify install
pip install graphifyy && graphify install
```

For Codex-specific installation:

```bash
graphify codex install
```

## Safety Boundary

Graphify gives durable context. Repo files, git remotes, system docs, and explicit handoff files remain authoritative.
