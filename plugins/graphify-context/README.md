# Graphify Context Plugin

This local Codex plugin makes Graphify a standing context layer for repository work.

## What It Provides

- A `graphify-context` skill that tells Codex to read `graphify-out/GRAPH_REPORT.md` and `graphify-out/wiki/index.md` before broad repo work.
- A repo-local marketplace entry with `policy.installation` set to `INSTALLED_BY_DEFAULT`.
- Helper scripts for checking Graphify availability and refreshing `graphify-out`.

## Install Graphify

Use one of:

```bash
uv tool install graphifyy && graphify install
pipx install graphifyy && graphify install
pip install graphifyy && graphify install
```

For Codex-specific install support:

```bash
graphify codex install
```

## Helper Scripts

```bash
plugins/graphify-context/scripts/check_graphify.sh
plugins/graphify-context/scripts/update_graphify.sh .
```

## Boundary

Graphify is context, not authority. Always verify important claims against current local files before editing.
