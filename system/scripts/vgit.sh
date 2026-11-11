#!/usr/bin/env bash
# Git for this vault, with the history kept OUTSIDE iCloud (iCloud corrupts .git folders).
# Usage:  bash system/scripts/vgit.sh init                    create the history folder (once)
#         bash system/scripts/vgit.sh <any git command>        e.g. vgit.sh log --oneline -20
#         bash system/scripts/vgit.sh snapshot <tool> "<message>"   commit everything changed, e.g. snapshot claude "save chat Best carbs"
set -euo pipefail
WT="$(cd "$(dirname "$0")/../.." && pwd)"
# History folder: $VAULT_GIT_DIR if set, else "<vault folder name> history.git" next to the vault.
GD="${VAULT_GIT_DIR:-$(dirname "$WT")/$(basename "$WT") history.git}"
if [ ! -d "$GD" ]; then
  if [ "${1:-}" = "init" ]; then git init -q --bare "$GD"; echo "Created $GD"; exit 0; fi
  echo "Vault history folder not found: $GD (run: bash system/scripts/vgit.sh init, or set VAULT_GIT_DIR)" >&2; exit 1
fi
g() { git -c safe.directory='*' -c core.quotepath=off --git-dir="$GD" --work-tree="$WT" "$@"; }
if [ "${1:-}" = "snapshot" ]; then
  tool="${2:?tool name}"; msg="${3:?message}"
  g add -A
  if g diff --cached --quiet; then echo "Nothing to commit."; exit 0; fi
  gone="$(g diff --cached --name-status -- keepers/ | grep -E '^(D|R)' || true)"
  if [ -n "$gone" ] && [ "${KEEPERS_OK:-}" != "1" ]; then
    g reset -q
    echo "STOP: keepers were deleted or renamed. Only the owner may do this. Ask the owner to confirm, then rerun with KEEPERS_OK=1." >&2
    echo "$gone" >&2
    exit 2
  fi
  g -c user.name="$tool" -c user.email="$tool@distill.local" commit -q -m "$tool: $msg"
  g log --oneline -1; g show --stat --format= HEAD | tail -1
else
  g "$@"
fi
