#!/usr/bin/env bash
set -euo pipefail

if ! command -v graphify >/dev/null 2>&1; then
  echo "graphify is not installed. Install with: uv tool install graphifyy && graphify install" >&2
  exit 1
fi

target="${1:-.}"
graphify update "$target"
