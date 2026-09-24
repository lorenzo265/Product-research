#!/bin/bash
# Garante as dependências Python do harness em sessões do Claude Code na web.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
python3 -m pip install --quiet --disable-pip-version-check --root-user-action=ignore -r requirements.txt
