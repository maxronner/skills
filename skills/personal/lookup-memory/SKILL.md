---
name: lookup-memory
description: Interact with the user's durable memory substrate without treating chat recall as truth. Use when prior decisions, preferences, cross-repo context, reusable procedures, or explicit save/curate/import requests could affect the work; ground in the current repo first, use available memory interfaces, and write only when asked.
---

# Lookup Memory

Use durable memory as a substrate: discover the available interface, follow its local rules, search/read selectively, and cite what influenced the answer.

## Default Order

1. Ground in the current repo first: instructions, docs, code, config, tests, and tooling.
2. Decide whether memory could change the answer. If not, skip memory.
3. Discover candidate memory interfaces from user-provided paths/tools, repo or home instructions, MCP/API tools, wrappers, and installed CLIs.
4. Load tool references only for tools that are both relevant and available; if absent, skip the reference.
5. Read local instructions for any substrate you use before reading or writing notes.
6. Prefer the substrate's normal interface (wrapper, MCP/API, index, `zk`, search tool) over raw file access.
7. Treat chat history and model recall as search hints only, never as source of truth.

If repo-local facts conflict with memory, prefer the repo and mention the conflict when it matters.

## Lookup Workflow

1. Locate the substrate and its local rules.
2. Search broadly, then narrow by title/tag/path/date/linkage when the interface supports it.
3. Read only the notes or records needed for the task.
4. When memory influenced the answer, cite the note title, id, tool result, or source path.
5. If no relevant memory is found, continue from repo facts rather than over-searching.

## Write Workflow

Write only when the user explicitly asks to save, curate, import, or process memory.

1. Search for duplicates first.
2. Follow local schema, taxonomy, linking, naming, and validation rules.
3. Use the substrate's creation/update workflow; do not invent paths or hand-roll metadata when a tool can create it.
4. Validate with the substrate's checker, index, or list/search command when available.
5. Report what was written and where.

## Boundaries

- Do not invent notebook taxonomy, schema, storage layout, or backlinks.
- Do not process inbox, raw, or import folders unless asked.
- Do not silently save project facts just because you learned them.
- Do not use memory as a substitute for repo-local grounding.
