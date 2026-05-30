---
name: brainstorm
description: Shape fuzzy goals into candidate approaches and an agreed direction before implementation. Use when the user asks to brainstorm or explore options, does not yet have a plan, or says they are not sure what they want yet.
---

# Brainstorm

Use this when the user needs help discovering the plan. If the user already has a plan and wants it challenged, use `grill-me` or `grill-with-docs`.

## Workflow

1. **Read local context first.** Check the nearest repo docs, current structure, and relevant code before asking questions that the repo can answer.
2. **Check scope.** If the idea spans multiple independent subsystems, call that out and help split it. Continue with the first useful slice.
3. **Switch early when domain docs matter.** Use `grill-with-docs` instead if the design depends on project language, glossary changes, or durable architectural decisions.
4. **Ask one question at a time.** Prefer questions that resolve purpose, constraints, success criteria, user workflow, or hard trade-offs. Include your recommended answer.
5. **Explore approaches.** Present 2-3 plausible approaches with trade-offs. Lead with your recommendation and why.
6. **Present the agreed design.** Keep it proportional to risk: a few sentences for small work, a structured outline for larger work.
7. **Get approval before implementation.** Ask whether the design is right before writing code, creating issues, or producing a PRD.
8. **Route the next step by scale.**
   - Use direct implementation for small, well-understood changes.
   - Use `prototype` when a UI, state model, or interaction needs to be felt before committing.
   - Use `to-prd` when the design should become a durable product spec.
   - Use `to-issues` when the design is ready to break into independently-grabbable work.

## Guardrails

- Do not hard-gate trivial edits behind a spec or commit.
- Do not write a design doc just because brainstorming happened. Use durable docs only when the decision is large, cross-cutting, hard to reverse, or useful for future agents.
- Do not ask questions that can be answered by reading the repo.
- Do not keep brainstorming after the user clearly approves a small implementation path.
- Keep alternatives concrete. Avoid abstract option names unless each option has behavior, cost, and risk attached.

## Output Shape

For small work:

```md
Recommended design: ...
Trade-off: ...
Approval question: Does this match what you want me to build?
```

For larger work:

```md
Problem
Approaches
Recommendation
User flow
Components or modules
Data and error handling
Testing
Out of scope
Approval question
```
