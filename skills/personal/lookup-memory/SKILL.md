---
name: lookup-memory
description: Use when a task may benefit from durable user or project memory after grounding in the current repository. Check repo-local instructions, docs, source, config, tests, and tooling first; search configured notebooks when prior decisions, preferences, cross-repo context, or reusable procedures could affect the answer. Write only when explicitly asked to save, curate, import, or process memory.
---

# Lookup Memory

Ground in the current repository first. Use durable notebook memory as additional context for prior decisions, preferences, cross-repo patterns, or reusable procedures.

## Source Order

1. Current repo instructions, docs, code, config, tests, and local tooling.
2. Notebook-local instructions for any memory source you use.
3. Notebook search, indexes, MCP/API, wrapper tools, or direct files when that is the notebook's normal interface.
4. Chat history or model recall only as hints, never as source of truth.

If repo-local facts conflict with memory, prefer the repo and mention the conflict when it matters.

## Lookup

1. Find the relevant notebook from local instructions, user-provided paths, environment, or available memory tools.
2. Read the notebook's local instructions before using it.
3. Prefer the notebook's own tools, wrappers, indexes, MCP/API, or search interface over ad hoc file access.
4. Search memory when repo grounding leaves relevant context unknown or when prior decisions, preferences, or cross-repo patterns could change the answer.
5. When memory influenced the answer, mention the note title, id, tool result, or source path.

## Write

Write only when the user asks to save, curate, import, or process memory.

1. Use the notebook's local creation workflow.
2. Search for duplicates first.
3. Follow local schema, taxonomy, linking, and validation rules.
4. Validate with the notebook's own checker when available.

## Boundaries

- Do not invent notebook taxonomy, schema, or storage layout.
- Do not process inbox, raw, or import folders unless asked.
- Do not hand-write notes when a local workflow exists.
- Do not treat chat history or model recall as a substitute for repo or notebook grounding.
