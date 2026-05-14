#!/usr/bin/env bash
set -euo pipefail

# Links all skills in the repository to ~/.claude/skills, so that
# they can be used by the local Claude CLI.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/link-skills-core.sh"

DEST="${HOME}/.claude/skills"
link_skills_cli "$DEST" "Claude CLI" "$@"
