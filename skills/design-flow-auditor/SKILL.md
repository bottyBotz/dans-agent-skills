---
name: design-flow-auditor
description: "Use when reviewing wireframes or multi-step interface flows for task completeness, navigation clarity, state continuity, accessibility, and shared-component consistency, or iterating on explicitly authorized design fixes."
---

# Design Flow Auditor

Help the designer catch concrete problems the owner would otherwise need to
point out. Assess whether a person can understand and complete the journey,
not whether a screenshot looks polished. An audit pass means ready for owner
review, never owner approval or proof of real-world usability.

## Establish the review contract

Read the supplied brief, accepted decisions, component inventory and any
project review criteria provided for the task. Recover relevant owner feedback from the conversation.
Distinguish explicit requirements, tentative proposals and reviewer preferences.
Use current artifacts; do not treat archived alternatives as the current design.

Identify the task, actor, scoped flows, fidelity and available evidence. Keep
project-specific rules in the project's own documentation, outside this skill.
Do not assume a particular domain, data model, tool, layout or interaction style.
If project documentation conflicts with a newer explicit instruction, follow the
instruction and flag the stale documentation for correction.

Use the mode authorized by the request:

- **Audit only:** inspect and report; do not change the artifact.
- **Design and iterate:** the designer may make authorized fixes and seek another
  audit. An auditor subagent remains read-only unless explicitly assigned edits.

Preserve the requested tool, fidelity and scope. This skill does not authorize
publishing, messaging others, product implementation, or redesigning other areas.
Avoid routine permission requests for already-authorized reversible refinement.

## Audit the journey

Trace the task from a credible starting state to an understandable result.
For each transition, identify the visible action, target, resulting state and
return/recovery route when relevant. Do not assume an invisible click or an
undocumented state reset.

Use these questions where they affect the task:

| Lens | Questions to answer from the artifact |
| --- | --- |
| Entry and scope | Where do I start? What task or item am I working on? Is the scope of each action clear? |
| Controls and meaning | Does this control belong at this scope and for this type? Can I understand its value and effect without the designer explaining it? |
| Transitions and return | What happens after this click? Can I change my mind, return to the parent, close and reopen? Do selection and panel state stay coherent? |
| Result and persistence | Is the requested change visible? Are drafts, proposals, applied changes and publication distinguishable where relevant? Does the design imply an unapproved save or overwrite policy? |
| Continuity | Do inputs, edits and selection survive transitions as intended? Is the user asked to repeat supplied information? |
| Structure and geometry | Do labels, controls and groups follow shared layout rules? Are scope boundaries clear? Is anything clipped, crowded, misaligned or unreadable at the intended size? |
| Components | Is repeated UI actually linked? Was a shared defect fixed at its source? Are overrides necessary, and have affected uses been checked? |
| Economy and accessibility | Does each label, hint, badge and confirmation help someone decide or act? Are actionable elements visibly actionable? Are requiredness, focus/keyboard intent and meaning conveyed appropriately for this fidelity? |
| Boundaries | Does the journey stay in its assigned area and use the agreed terminology/data model? Are genuinely undecided product choices visibly identified as candidates in review notes? |

Inspect the actual visual artifact at a useful scale, plus native structure or
runtime evidence when available. A node/text dump cannot establish visual quality.
Screenshots cannot prove click behavior, keyboard access, persistence or component
inheritance. Mark unavailable evidence as unverified, not passed. Use the tool's
native inspection/editing guidance; do not infer unsupported interactions.
Before reporting a material visual defect, recheck the original image at a
readable scale or inspect the relevant region. Do not mistake a thumbnail,
cropped tool result or stale export for missing UI. If evidence conflicts,
resolve which artifact and revision was viewed before prescribing a redesign.

Show only states that establish meaningful behavior. Reuse shared recovery flows
when the behavior is identical. Do not demand an arbitrary screen count or repeat
every failure state for every type. Where multiple routes serve the same task,
check that their outcomes are consistent with the supplied requirements.

## Give actionable findings

Each finding must identify a specific problem and consequence. Use a compact
ledger with stable IDs:

`ID | Flow/state/node | Severity | Evidence and consequence | Smallest correction | Status`

- **High:** breaks the task, loses work, changes the wrong scope, contradicts an
  accepted rule, or misleadingly represents a consequential action.
- **Medium:** creates material ambiguity, an undiscoverable required route, or
  inconsistent behavior likely to require owner correction.
- **Low:** nonblocking clarity or visual refinement with a concrete benefit.

Ground findings in the artifact and a stated requirement, owner decision or
reasoned usability concern. Do not describe subjective taste as a requirement.
Separate **defects**, **owner decisions** and **evidence gaps**. Missing product
policy is not permission to invent it; a coherent, labelled candidate may still
be ready for owner review. Avoid generic comments such as "make this cleaner."
Consolidate repeated defects under their shared component with affected uses.

## Iterate to a reviewable result

For authorized design-and-iterate work:

1. Map the journey and create/refine the scoped artifact using existing patterns.
2. Have an independent reviewer inspect the brief, accepted profile and raw
   artifacts when delegation is available. Do not prime the first audit with the
   designer's desired verdict or suspected defects. Keep canvas writes with one
   owner unless editing areas are explicitly separated.
3. Fix substantiated findings at their owning component or flow. Explain any
   rejected finding using the contract and evidence. A designer cannot dismiss a
   material finding merely to reach completion.
4. Re-audit corrected transitions and affected component instances. Verify the
   actual revision; a promised fix is not closure. Keep prior findings available
   for retesting, while checking for new regressions.
5. Review the entire scoped set once the individual flows converge, including
   shared navigation, terminology, content and regression effects.

If delegation is unavailable, perform a separate audit pass and disclose that it
was self-review. Keep a resumable coverage/finding ledger in the project's normal
work record for substantial work. Keep repeated review chatter out of product UI.

Ready for owner review requires complete scoped coverage, no unresolved high or
medium defects, checked shared-component effects, and evidence appropriate to
the requested fidelity. Record low-priority items and explicitly labelled
candidate decisions; do not bury them in a blanket "passed."

Avoid endless polishing. After three unsuccessful attempts at the same correction,
seek a fresh diagnosis and change approach rather than repeating it. Continue
while meaningful progress is possible. Only a genuine missing decision, evidence
or access should leave that scope unfinished; continue independent flows and
report the specific gap. Do not relabel a defect as an owner decision to pass the
audit. Routine visual choices belong to the designer; policy choices stay with
the owner.

## Handoff

Report the review status, flow coverage, material fixes, evidence and remaining
decisions or limitations. Link the reviewable artifact and keep the summary short.
Use **Ready for owner review**, **Needs revision** or **Needs owner decision** as
appropriate per flow; a labelled proposal may be ready to review while awaiting
its policy decision. Never claim working interactions, testing or approval that
did not occur.
