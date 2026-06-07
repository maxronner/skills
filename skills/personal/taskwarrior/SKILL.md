---
name: taskwarrior
description: Use the Taskwarrior CLI as the user's actionable task system without treating it as durable factual memory. Use when the user mentions Taskwarrior, TODOs, reminders, deferred follow-up, or asks to manage personal tasks.
---

# Taskwarrior

Use Taskwarrior for actionable work items: deferred work, blocked follow-ups, cross-session commitments, and explicit requests to track or remind. Do not create tasks for work you can finish now.

## Default Posture

- Inspect before mutating: read nearby tasks, projects, and tags first when context matters.
- Mutate narrowly: add, annotate, modify, or complete only the intended task.
- Verify every mutation with a read-back command.
- Ask before destructive, broad, or remote-affecting changes: `delete`, `purge`, bulk `modify`, recurring-task edits, config changes, many completions, or `task sync`.
- Use Taskwarrior for actions, not facts. Use memory for durable preferences, context, and knowledge.

## Read

Use structured output for automation decisions:

```bash
task export
task <id> export
task _get <id>.uuid
```

```bash
task +READY
task <id> info
task projects
task tags
task project:<name> +PENDING
task description.contains:<word> +PENDING
```

## Add

```bash
task add "Description of actionable work"
task add project:<project> +<tag> "Description"
```

Choose `project:` and `+tag` from existing vocabulary when possible:

```bash
task projects
task tags
```

Only invent new projects or tags when the user named them or no existing fit is reasonable. Mention when a project or tag is new.

## Dates

Resolve relative dates against the current date and timezone before writing. State concrete dates in user-facing text.

- Use `due:` only for real commitments or deadlines.
- Use `wait:` for intentionally hidden/deferred tasks.
- Use `scheduled:` for planned start dates.
- Use `until:` only when the task should expire.
- Confirm ambiguous natural language before mutating, especially for time-specific reminders.

```bash
task add due:<YYYY-MM-DD> "Submit expense report"
task add wait:<YYYY-MM-DD> "Follow up on invoice"
task add scheduled:<YYYY-MM-DD> "Start migration notes"
```

## Update

Prefer annotation for history and small updates:

```bash
task <id> annotate "Waiting on vendor response"
task <id> modify project:<project> +<tag>
task <id> modify due:<YYYY-MM-DD>
task <id> done
```

```bash
task <id> info
```

## Priority

Do not set `priority:` by default. Let urgency come from Taskwarrior's normal urgency model: due dates, tags, project, and age.

If the user says a task is important, clarify whether they mean:

- `priority:H`, `priority:M`, or `priority:L`
- a concrete `due:`
- a workflow tag such as `+next`

## Reminders

- "Remember to do X" usually means create an actionable task.
- "Remember that X" usually means durable memory, not Taskwarrior.
- "Remind me at/by/on X" needs a concrete date or time before creating a dated task.

When in doubt, ask whether the user wants an actionable task or durable memory.
