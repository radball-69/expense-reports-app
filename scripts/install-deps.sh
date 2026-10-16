#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${REPO_ROOT}/.venv"
VENV_PYTHON="${VENV_DIR}/bin/python"

if command -v python3 >/dev/null 2>&1; then
  SYSTEM_PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
  SYSTEM_PYTHON="python"
else
  echo "No Python interpreter found. Install Python 3.11+ and retry." >&2
  exit 1
fi

if [[ ! -x "${VENV_PYTHON}" ]]; then
  echo "Creating virtual environment in .venv..."
  "${SYSTEM_PYTHON}" -m venv "${VENV_DIR}"
fi

if ! "${VENV_PYTHON}" -c "import pytest,ruff,black,slack_bolt" >/dev/null 2>&1; then
  echo "Installing project dependencies..."
  "${VENV_PYTHON}" -m pip install --upgrade pip
  "${VENV_PYTHON}" -m pip install -e "${REPO_ROOT}[dev]"
fi
