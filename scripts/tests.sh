#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_PYTHON="${REPO_ROOT}/.venv/bin/python"

"${REPO_ROOT}/scripts/install-deps.sh"

"${VENV_PYTHON}" -m pytest
