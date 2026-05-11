# AMA-PAYMENT

Payment-link helper scripts and local Codex context tooling for this workspace.

## Stripe Payment Scripts

The payment scripts create HOWLING MUNE Stripe Payment Links. They do not store Stripe secrets in source code.

Before running a script, set the key in your shell:

```bash
export STRIPE_SECRET_KEY="sk_live_..."
python3 create_payment_links.py
```

Do not commit `.env` files or pasted Stripe keys.

## Graphify Context

This repo includes a local `graphify-context` Codex plugin:

- [AGENTS.md](AGENTS.md) defines Graphify as the standing context layer.
- [plugins/graphify-context](plugins/graphify-context) contains the plugin manifest, skill, and helper scripts.
- [graphify-out/GRAPH_REPORT.md](graphify-out/GRAPH_REPORT.md) is the current repo map.

Install or refresh Graphify with:

```bash
uv tool install graphifyy && graphify install
graphify update .
```
