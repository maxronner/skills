#!/usr/bin/env python3
"""
Quick validation script for skills — dependency-free version.

Validates SKILL.md frontmatter, name/description conventions, and
basic structure. Run against a single skill directory.
"""

import re
import sys
from pathlib import Path

MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024

# Frontmatter keys recognised by this project's skills
KNOWN_KEYS = {
    "name",
    "description",
    "argument-hint",
    "disable-model-invocation",
    "license",
    "allowed-tools",
    "metadata",
}


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    """Parse simple YAML frontmatter. Returns (dict, error_or_none)."""
    if not text.startswith("---"):
        return {}, "No YAML frontmatter found"

    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}, "Invalid frontmatter format"

    raw = match.group(1)
    result: dict[str, str] = {}
    current_key: str | None = None
    folded_lines: list[str] = []

    for line in raw.split("\n"):
        # Check for a new key: value pair at indent 0
        kv = re.match(r"^([a-z][a-z0-9-]*)\s*:\s*(.*)", line)
        if kv:
            # Flush any previous folded value
            if current_key is not None and folded_lines:
                result[current_key] = " ".join(folded_lines).strip()
                folded_lines = []

            key = kv.group(1)
            val = kv.group(2).strip()

            if val == ">" or val == "|":
                # Multi-line scalar — collect subsequent indented lines
                current_key = key
                folded_lines = []
            elif val:
                result[key] = val
                current_key = None
            else:
                # Empty value (e.g. "key:") — treat as ""
                result[key] = ""
                current_key = None
        elif current_key is not None and re.match(r"^\s{2,}", line):
            # Continuation of a multi-line scalar
            folded_lines.append(line.strip())
        elif current_key is not None:
            # End of multi-line — flush and reset
            if folded_lines:
                result[current_key] = " ".join(folded_lines).strip()
                folded_lines = []
            current_key = None

    # Flush any trailing folded value
    if current_key is not None and folded_lines:
        result[current_key] = " ".join(folded_lines).strip()

    return result, None


def validate_skill(skill_path: str | Path) -> tuple[bool, str]:
    """Basic validation of a skill directory. Returns (ok, message)."""
    skill_path = Path(skill_path)

    if not skill_path.is_dir():
        return False, f"Not a directory: {skill_path}"

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text()

    frontmatter, err = _parse_frontmatter(content)
    if err:
        return False, err

    # --- Unexpected keys ---
    unexpected = set(frontmatter.keys()) - KNOWN_KEYS
    if unexpected:
        allowed = ", ".join(sorted(KNOWN_KEYS))
        unexpected_str = ", ".join(sorted(unexpected))
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {unexpected_str}. "
            f"Allowed properties are: {allowed}"
        )

    # --- Required: name ---
    if "name" not in frontmatter:
        return False, "Missing 'name' in frontmatter"

    # --- Required: description ---
    if "description" not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # --- Validate name ---
    name = frontmatter.get("name", "")
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if not name:
        return False, "Name must not be empty"
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, (
            f"Name '{name}' should be hyphen-case "
            f"(lowercase letters, digits, and hyphens only)"
        )
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, (
            f"Name '{name}' cannot start/end with hyphen "
            f"or contain consecutive hyphens"
        )
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, (
            f"Name is too long ({len(name)} characters). "
            f"Maximum is {MAX_SKILL_NAME_LENGTH}."
        )

    # --- Validate description ---
    description = frontmatter.get("description", "")
    if not isinstance(description, str):
        return False, (
            f"Description must be a string, got {type(description).__name__}"
        )
    description = description.strip()
    if not description:
        return False, "Description must not be empty"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets (< or >)"
    if len(description) > MAX_DESCRIPTION_LENGTH:
        return False, (
            f"Description is too long ({len(description)} characters). "
            f"Maximum is {MAX_DESCRIPTION_LENGTH}."
        )

    return True, "Skill is valid!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        prog = Path(sys.argv[0]).name
        print(f"Usage: {prog} <skill_directory>")
        sys.exit(1)

    ok, message = validate_skill(sys.argv[1])
    if not ok:
        print(message)
    sys.exit(0 if ok else 1)
