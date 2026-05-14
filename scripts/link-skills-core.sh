#!/usr/bin/env bash
set -euo pipefail

link_skills_to() {
  local dest="$1"
  local quiet="${2:-0}"
  shift 2
  local -a include_buckets=("$@")
  local repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
  local src name target

  # If destination is a symlink into this repo, we'd end up writing the per-skill
  # symlinks back into the repo's own skills/ tree. Detect and bail out instead
  # of polluting the working copy.
  if [ -L "$dest" ]; then
    local resolved
    resolved="$(readlink -f "$dest")"
    case "$resolved" in
      "$repo"|"$repo"/*)
        echo "error: $dest is a symlink into this repo ($resolved)." >&2
        echo "Remove it (rm \"$dest\") and re-run; the script will recreate it as a real dir." >&2
        exit 1
        ;;
    esac
  fi

  mkdir -p "$dest"

  find "$repo/skills" -name SKILL.md -not -path '*/node_modules/*' -print0 |
  while IFS= read -r -d '' skill_md; do
    src="$(dirname "$skill_md")"
    name="$(basename "$src")"

    if ((${#include_buckets[@]} > 0)); then
      local matched=0
      local bucket
      for bucket in "${include_buckets[@]}"; do
        if [[ "$src" =~ (^|/)${bucket}/ ]]; then
          matched=1
          break
        fi
      done
      if [ "$matched" -eq 0 ]; then
        continue
      fi
    fi

    target="$dest/$name"

    if [ -e "$target" ] && [ ! -L "$target" ]; then
      rm -rf "$target"
    fi

    ln -sfn "$src" "$target"

    if [ "$quiet" -eq 0 ]; then
      echo "linked $name -> $src"
    fi
  done
}

link_skills_cli() {
  local dest="$1"
  local client="$2"
  local quiet=0
  local -a buckets=()
  local -a positional=()
  shift 2

  while (( "$#" > 0 )); do
    case "$1" in
      -q|--quiet)
        quiet=1
        ;;
      -m|--misc)
        buckets+=("misc")
        ;;
      -p|--productivity)
        buckets+=("productivity")
        ;;
      -d|--deprecated)
        buckets+=("deprecated")
        ;;
      -e|--engineering)
        buckets+=("engineering")
        ;;
      --personal)
        buckets+=("personal")
        ;;
      -h|--help)
        echo "Usage: $(basename "$0") [options] [destination]"
        echo ""
        echo "Link skills into your local $client installation."
        echo ""
        echo "Bucket filters (defaults to all):"
        echo "  -m, --misc"
        echo "  -p, --productivity"
        echo "  -d, --deprecated"
        echo "  -e, --engineering"
        echo "      --personal"
        echo ""
        echo "Other options:"
        echo "  -q, --quiet     Suppress per-skill output"
        echo "  -h, --help      Show this help"
        echo ""
        echo "A final positional argument can be used as destination."
        exit 0
        ;;
      --)
        shift
        positional+=("$@")
        break
        ;;
      -* )
        echo "error: unknown argument '$1'" >&2
        echo "Try --help for usage." >&2
        exit 1
        ;;
      *)
        positional+=("$1")
        ;;
    esac
    shift
  done

  if ((${#positional[@]} > 1)); then
    echo "error: too many positional arguments: ${positional[*]}" >&2
    exit 1
  elif ((${#positional[@]} == 1)); then
    dest="${positional[0]}"
  fi

  link_skills_to "$dest" "$quiet" "${buckets[@]}"
}
