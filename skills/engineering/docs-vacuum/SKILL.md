---
name: docs-vacuum
description: Audit repository documentation for stale, duplicate, contradictory, or orphaned content; propose keep/update/merge/delete actions before editing. Use when docs feel bloated, drifted, contradictory, costly for agents to read, or after large refactors.
---

# Docs Vacuum

Audit and prune repository documentation without destroying useful project memory.

Default posture: docs are part of the system. Do not broadly rewrite, delete, or reorganize them just because they are imperfect. First identify drift and duplication, then propose a small plan. Non-destructive updates may proceed if the user explicitly asked for direct edits; deletions, archives, merges, and moves still require explicit confirmation.

## Scope

Prioritize repo-local docs that future agents or contributors are likely to read:

- `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, and root-level project docs
- `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `.github/copilot-instructions.md`
- `CONTEXT.md`, `CONTEXT-MAP.md`, and domain glossaries
- `docs/`, especially `docs/adr/`, `docs/agents/`, architecture notes, runbooks, and setup docs
- issue/PRD files if the repo uses local markdown for planning

Treat generated docs, vendored docs, API references, and historical archives as out of scope unless the user asks. ADRs are in scope, but should usually be marked superseded or archived rather than deleted.

## Process

### 1. Inventory

Start by finding likely docs with targeted commands, then follow links, maps, and docs indexes deeper as needed:

```bash
find . -maxdepth 5 -type f \
  \( -name '*.md' -o -name '*.mdx' -o -name 'AGENTS.md' -o -name 'CLAUDE.md' \) \
  -not -path './node_modules/*' \
  -not -path './.git/*' \
  | sort
```

Also inspect likely doc entry points and maps before judging individual files:

- top-level `README.md`
- `CONTEXT.md` / `CONTEXT-MAP.md`
- `docs/README.md` if present
- `docs/adr/` index or newest ADRs
- `docs/agents/*.md` if present

### 2. Diagnose Doc Health

Classify findings into:

- **Keep** — current, unique, and useful.
- **Update** — useful but stale, incomplete, or wording no longer matches code/tooling.
- **Merge** — overlaps another doc; should be consolidated into one source of truth.
- **Delete** — orphaned, obsolete, misleading, or superseded by another artifact.
- **Archive** — historically useful but should not be presented as active guidance.

Look specifically for:

- stale commands, package names, install steps, paths, or branch names
- docs that contradict code, CI, package scripts, or agent instructions
- duplicate explanations across README, `docs/`, `CONTEXT.md`, ADRs, and issue docs
- orphan docs that nothing links to and no workflow references; do not delete a doc solely because it is unlinked
- docs that make agents do broad exploration, broad testing, or extra work unnecessarily
- ADRs that lack status or have been superseded without a pointer

### 3. Protect Project Memory

Do not delete or flatten useful history by default.

- Never delete ADRs just because they are old. Prefer adding status or supersession notes.
- Preserve domain language in `CONTEXT.md` unless it is demonstrably stale.
- Preserve setup/runbook details that are hard to rediscover from code.
- Prefer linking to one source of truth over copying the same explanation into multiple files.
- If a doc is obsolete but explains why a decision changed, archive or mark superseded instead of deleting.

### 4. Propose Before Editing

Before changing files, present a concise plan:

```markdown
## Docs vacuum plan

### Delete
- `path` — reason

### Merge
- `old path` → `source of truth path` — reason

### Update
- `path` — concrete stale/conflicting points to fix

### Keep
- `path` — why it remains useful

### Questions
- any uncertainty that changes whether to delete vs archive vs update
```

Ask for explicit confirmation before destructive edits: deletes, archives, merges, moves, or source-of-truth changes. If the user asked for a no-edit audit, stop after the plan.

### 5. Edit

When confirmed:

- make the smallest edits that remove drift or duplication
- update links when files move, merge, or are deleted
- add supersession notes to ADRs instead of deleting them
- keep `README.md` as the entry point, not the dumping ground
- keep `CONTEXT.md` focused on domain language, not implementation details
- keep `AGENTS.md` / `CLAUDE.md` focused on load-bearing agent instructions; use `improve-agents-md` if that file needs deeper tightening

### 6. Verify

Run the narrowest relevant verification:

- markdown formatter or lint if the repo has one
- link checker if available
- targeted grep/rg for deleted or renamed doc paths
- manually re-read changed docs for broken headings, stale links, and contradictions

For docs-only changes, do not run broad test suites unless the repo explicitly requires it.

### 7. Report

Summarize:

- docs deleted, merged, updated, archived, or kept
- source-of-truth decisions made
- what checks ran
- what was intentionally left alone
- any remaining stale-doc risk or unresolved question
