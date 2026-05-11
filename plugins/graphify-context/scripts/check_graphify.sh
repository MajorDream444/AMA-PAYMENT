#!/usr/bin/env bash
set -euo pipefail

if ! command -v graphify >/dev/null 2>&1; then
  echo "graphify: missing"
  echo "Install with: uv tool install graphifyy && graphify install"
  exit 1
fi

echo "graphify: $(command -v graphify)"
graphify --help | sed -n '1,40p'

if [ -f "graphify-out/GRAPH_REPORT.md" ]; then
  echo "graph report: graphify-out/GRAPH_REPORT.md"
else
  echo "graph report: missing"
fi

if [ -f "graphify-out/wiki/index.md" ]; then
  echo "wiki index: graphify-out/wiki/index.md"
else
  echo "wiki index: missing"
fi
