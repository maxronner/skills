#!/usr/bin/env bash
set -euo pipefail

# Links all skills in the repository to ~/.pi/agent/skills, so that
# they can be used by the local pi CLI.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/link-skills-core.sh"

DEST="${PI_SKILLS_DIR:-$HOME/.pi/agent/skills}"
link_skills_cli "$DEST" "pi CLI" "$@"
