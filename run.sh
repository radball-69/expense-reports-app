#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPT="${REPO_ROOT}/scripts/${1:-}.sh"

if [[ -z "${1:-}" || ! -x "${SCRIPT}" ]]; then
  echo "Usage: ./run.sh <script> [args...]" >&2
  echo "Available scripts:" >&2
  for f in "${REPO_ROOT}"/scripts/*.sh; do
    basename "${f}" .sh >&2
  done
  exit 1
fi

shift
exec "${SCRIPT}" "$@"
