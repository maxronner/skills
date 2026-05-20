---
name: improve-agents-md
description: Tighten repository AGENTS.md or CLAUDE.md instructions down to minimal, repo-specific requirements that help future coding agents without adding unnecessary exploration or cost. Use when the user asks to improve, audit, tighten, refactor, or create agent instructions, AGENTS.md, CLAUDE.md, or repo-local AI coding guidance.
---

# Improve AGENTS.md

Audit and improve repo-local agent instructions. The goal is a short set of load-bearing requirements a future agent must know to work safely and verify correctly in this repository.

Default posture: less instruction is usually better. Context files can make agents spend more effort exploring, testing, and reasoning; unnecessary requirements can make tasks harder. Add or keep a rule only when it changes behavior in this repo.

## Process

### 1. Explore The Repo

Read existing instruction files and likely workflow entry points before editing:

- `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `.github/copilot-instructions.md`
- `README.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/adr/`
- `justfile`, `Makefile`, `flake.nix`, `shell.nix`, `package.json`, `Cargo.toml`, `pyproject.toml`, `go.mod`
- CI config under `.github/workflows/`, `.gitlab-ci.yml`, or similar

Use the existing files to infer concrete repo behavior, but do not turn every fact into an instruction:

- setup and development shell
- formatting, linting, tests, builds, and narrow verification commands
- generated files or codegen steps
- dependency and lockfile policy
- deployment, database, infrastructure, or secret handling boundaries
- monorepo ownership, nested instruction files, and domain docs

If the repo provides a setup skill such as `setup-agent-skills`, read its generated `docs/agents/*.md` files as additional context.

### 2. Diagnose Instruction Quality

Look for:

- **Missing load-bearing facts** — commands or conventions future agents are likely to get wrong without an explicit rule.
- **Generic filler** — broad advice that applies to every repository and does not change agent behavior here.
- **Stale or contradictory guidance** — instructions that conflict with tooling, docs, CI, or nested agent files.
- **Unsafe ambiguity** — deploys, migrations, destructive git, secrets, or production operations without approval boundaries.
- **Verification gaps** — no clear narrow command for common edits, or commands that require untracked files to be staged first.
- **Cost multipliers** — rules that force broad exploration, broad testing, or extra reporting when a narrow task would not need it.

Treat nested instruction files as scoped overrides. Do not collapse them into the root file unless the same rule truly belongs at the root.

### 3. Edit Principles

Prefer deletion and compression before adding text:

- Preserve specific existing guidance unless it is wrong or obsolete.
- Replace vague imperatives with concrete commands, file paths, or decision rules.
- Delete generic policy that the harness, system prompt, or normal engineering judgment already covers.
- Avoid adding rules that future agents cannot verify locally.
- Avoid duplicating harness or system-level behavior unless the repo needs a concrete local implication.
- Avoid requiring broad scans, full test suites, or exhaustive summaries by default.

Apply the instruction deletion test to every paragraph:

- Would a competent agent probably do this anyway?
- Is this already enforced by tooling or the harness?
- Does this rule apply to almost every repo?
- Could it cause extra exploration, tests, or thinking on small tasks?

If the answer is yes, delete or shorten it unless this repo has a concrete reason to keep it.

Use clear sections only when they carry real content. Most files should need only:

1. Workflow
2. Verification
3. Safety boundaries
4. Repo-specific conventions

### 4. Suggested Content Patterns

For commands, prefer exact examples:

```markdown
Run `just test` for broad verification. For QML-only changes, run `just qml-lint`.
```

For Nix repos, include the flake visibility rule when relevant:

```markdown
Git-add newly created source files before `nix build`, `nix flake check`, or `nix fmt`; flake evaluation cannot see untracked paths.
```

For generated files:

```markdown
After editing route definitions, run `npm run generate:routes` and include generated output in the same change.
```

For safety:

```markdown
Ask before deploys, database migrations, secret rotation, destructive filesystem operations, or destructive git operations.
```

For reporting:

```markdown
Before handoff, state what changed and what was checked. Mention skipped checks only when they are relevant.
```

Avoid broad or decorative content:

```markdown
<!-- Too broad -->
Always understand the entire architecture before changing code.

<!-- Better -->
For changes under `nix/modules/system/`, run `just nix-check` before handoff.
```

### 5. Verify

Run the narrowest relevant verification:

- For instruction-only edits, run a markdown formatter or repo-local lint if one exists.
- If the repo uses Nix and the instruction file is packaged or linked through Nix, run the narrowest build/check that evaluates it.
- If no relevant command exists, read the final file and check headings, links, and command names manually.

When verification is skipped, say exactly why and name the command that would be useful if it existed.

### 6. Report

Summarize:

- which instruction files changed
- what text was deleted or compressed
- what behavior future agents will now follow that they might otherwise miss
- what verification ran
- any remaining uncertainty, especially commands inferred from docs rather than CI
