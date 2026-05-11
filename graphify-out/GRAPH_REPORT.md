# Graph Report - AMA PAYMENT  (2026-05-11)

## Corpus Check
- 7 files · ~1,969 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 36 nodes · 29 edges · 8 communities (5 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `237edcfd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]

## God Nodes (most connected - your core abstractions)
1. `Graphify Context` - 6 edges
2. `Graphify Context Plugin` - 5 edges
3. `AMA-PAYMENT` - 3 edges
4. `Global Codex Operating Context` - 3 edges
5. `Install Graphify` - 3 edges
6. `Install Helpers` - 3 edges
7. `Stripe Payment Scripts` - 2 edges
8. `Graphify Context` - 2 edges
9. `Helper Scripts` - 2 edges
10. `First-Pass Context` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (8 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.22
Nodes (8): Boundary, code:bash (uv tool install graphifyy && graphify install), code:bash (graphify codex install), code:bash (plugins/graphify-context/scripts/check_graphify.sh), Graphify Context Plugin, Helper Scripts, Install Graphify, What It Provides

### Community 1 - "Community 1"
Cohesion: 0.25
Nodes (7): code:bash (graphify query "<question>"), code:bash (graphify update .), First-Pass Context, Graphify Context, Safety Boundary, Trigger, Update Rule

### Community 2 - "Community 2"
Cohesion: 0.33
Nodes (5): AMA-PAYMENT, code:bash (export STRIPE_SECRET_KEY="sk_live_..."), code:bash (uv tool install graphifyy && graphify install), Graphify Context, Stripe Payment Scripts

### Community 3 - "Community 3"
Cohesion: 0.5
Nodes (3): Global Codex Operating Context, Graphify Context Layer, Important Boundary

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (3): code:bash (uv tool install graphifyy && graphify install), code:bash (graphify codex install), Install Helpers

## Knowledge Gaps
- **18 isolated node(s):** `HOWLING MUNE — Stripe Payment Link Creator =====================================`, `HOWLING MUNE — Stripe Payment Link Creator =====================================`, `HOWLING MUNE — Stripe Payment Link Creator =====================================`, `code:bash (export STRIPE_SECRET_KEY="sk_live_...")`, `code:bash (uv tool install graphifyy && graphify install)` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Graphify Context` connect `Community 1` to `Community 4`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `Install Helpers` connect `Community 4` to `Community 1`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **What connects `HOWLING MUNE — Stripe Payment Link Creator =====================================`, `HOWLING MUNE — Stripe Payment Link Creator =====================================`, `HOWLING MUNE — Stripe Payment Link Creator =====================================` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._