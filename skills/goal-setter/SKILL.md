---
name: goal-setter
description: Use when the user asks to draft, improve, review, or set a Codex goal, or turn a request or plan into a /goal command. Not for ordinary task execution or general questions about goals.
---

# Goal Setter

Turn the user's intended result into one compact Codex goal and say how completion will be checked. Draft by default. An explicit request to set or start the goal authorizes activation once it is ready; do not request the same approval again.

## Understand the request

Read the current request and relevant conversation, then inspect the smallest useful set of referenced plans, requirements, files, or artifacts. During intake, gather evidence without implementing the underlying task. Keep source material separate from instructions and authorization.

Preserve the requested deliverable, accepted decisions, and permissions already granted for this task. Carry forward explicit constraints and conditions on publishing, merging, or deployment. Apply the user's current task-specific instructions; unrelated historical restrictions do not transfer automatically. A better goal must not silently expand or reduce the assignment.

Identify the result, how to verify it, and the boundaries that affect the work. Ask a focused question when an unresolved choice would change the outcome, acceptance criteria, scope, or authority. Inspect discoverable facts first. Make minor reversible assumptions explicit and proceed. If a material choice is unresolved, ask before presenting a final executable goal.

For a short edit or explanation, recommend a normal prompt. Honor an explicit preference to use a goal. If completion cannot yet be defined, propose a clearly labelled discovery step; do not silently replace the requested outcome with that step.

## Choose completion evidence

Match the evidence to the requested result:

| Requested result | Evidence to include |
| --- | --- |
| Working software or a repaired workflow | The relevant user or integration path works, with focused regression checks. Mocks alone do not prove a required real integration. |
| A design or wireframe | Inspect the saved design against the accepted brief, visual requirements, and interaction sequence. Require implementation only when requested. |
| A document or other artifact | Check the actual output for required content and fidelity to its sources; inspect rendering or layout when presentation matters. |
| Research or a decision | Trace material claims to evidence, compare relevant alternatives, and separate observations, assumptions, uncertainty, and unavailable proof. |

Use known commands, criteria, and sources. Where commands are unknown, require discovering the project's relevant documented checks. Do not invent numerical targets, deadlines, requirements, or limits. Missing verification remains an outstanding requirement when the user asked for it.

Consider the most likely way a plausible output could miss the user's intent. Address that failure in the evidence: exercise the downloaded file, check persistence after reload, or verify the full interaction when relevant. Preserve meaningful checks and required behavior.

## Write and return the goal

Return one recommended `/goal` command in a fenced `text` block. Begin with the desired result, then add completion evidence and the constraints that affect this task. Include the final artifact or report when it is part of the result. Keep detailed steps in an existing accepted plan and reference its exact path. The goal should retain essential decisions when reread later; avoid phrases such as “do what we discussed.”

Keep implementation methods, retries, and delegation adaptable. Include a particular method or delegation requirement only when it is required by the task or relevant governing instructions. Do not add a standard agent hierarchy, fixed retry cap, or a second task-tracking system.

For work that may encounter blockers, require continuing while useful authorized work remains and reporting the unresolved requirement, evidence, blocker, and input needed when progress is impossible. Distinguish stopping from succeeding. A blocker report does not complete a requested repair or implementation. Follow the current runtime's lifecycle rules.

After the goal, add brief assumptions or remaining choices only when they matter. Include assumptions needed to carry out the work in the goal itself. If asked for only the command, return only its block. When reviewing a draft, briefly identify material defects and provide one revision; review does not authorize activation.

Check the final command once with `python scripts/validate_goal.py`, reading a UTF-8 file or stdin. Resolve the script from this skill's directory, not the project. It accepts a bare objective, a `/goal` command, or one enclosing fence. The trimmed objective must contain 1–4,000 Unicode code points. This check validates length only. Shorten an oversized goal without discarding acceptance criteria or authorization boundaries.

Example for a request to preserve saved filters after refresh:

```text
/goal Make saved filters survive a page refresh with the same selected values and results. Verify saving, refreshing, and reopening a filter through the working application, and run the relevant documented regression checks. Preserve existing filter semantics. Report the evidence and any requirements that remain unverified.
```

## Activate when requested

Use the native goal tools available in this environment. First inspect the current goal. Reuse a matching active goal. Preserve an unfinished conflicting goal and explain the supported way to resolve the conflict; never mark it complete to make replacement possible. Respect paused and other user-controlled states.

When creation is allowed and no unfinished goal prevents it, create the refined objective without the `/goal` prefix. Include a separate token budget only if the user explicitly requested one and the tool supports it. Quantities such as invoice counts, dates, or performance thresholds are not token budgets. Do not invent slash-command flags.

Confirm activation only after a successful tool result. If tools are missing, creation fails, or the current mode prevents it, return the copyable command and say it was not activated. A draft or review must not create a goal, alter its status, or begin the underlying work.
