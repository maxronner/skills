#!/usr/bin/env bash
set -euo pipefail

# Links all skills in the repository to ~/.codex/skills, so that
# they can be used by the local Codex CLI.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/link-skills-core.sh"

DEST="${CODEX_SKILLS_DIR:-$HOME/.codex/skills}"
link_skills_cli "$DEST" "Codex CLI" "$@"
