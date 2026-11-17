---
name: step-by-step-instructions
description: Give beginner-safe, click-by-click instructions with exact settings, checkpoints, and warnings. Use when the user asks for step-by-step, idiot-proof, highly explicit, or first-time guidance for a concrete task.
---

# Step-by-Step Instructions

Turn the user's chosen task into instructions they can follow without prior knowledge. Preserve their product, goal, scope, and authorization boundaries.

## Prepare

- Verify unstable product details against current authoritative documentation before giving UI paths, settings, prices, limits, or provider-specific advice.
- Inspect relevant existing state when read-only access is available and the result affects the instructions.
- Ask a question only when a missing choice would materially change the safe procedure. Otherwise, make a reasonable recommendation and label it.
- If the user asks only for instructions, do not make external changes. If they also ask Codex to act, perform only the authorized actions and explain any user-only steps.

## Write the instructions

1. Lead with the exact recommended outcome or configuration.
2. State prerequisites that must be ready before step 1.
3. Use a numbered sequence with one primary action per step.
4. Use the exact current UI labels, navigation paths, field names, commands, and literal values when known.
5. Visually distinguish literal values from placeholders. Never invent provider-generated values, DNS contents, tokens, IDs, or secrets.
6. Explain unfamiliar terms at the point where they appear, especially when similar-looking fields serve different purposes.
7. Put warnings immediately before the risky step. Name what must not be changed and the consequence.
8. At each important stage, include a checkpoint describing the expected screen, status, output, or observable result.
9. When multiple valid options exist, recommend one and explain the practical tradeoff. Clearly mark optional settings so the user does not mistake them for requirements.
10. End with the exact next action and what the user should report back if they want help continuing.

## Safety and clarity

- Never ask the user to paste passwords, API keys, recovery codes, or other secrets into chat. Direct them to enter secrets in the destination system and identify any seal, mask, or secret-storage control.
- Avoid destructive actions, unnecessary deployments, test sends, purchases, or production changes unless the user explicitly authorized them.
- Do not tell the user to copy example values when a provider generates account-specific values; tell them where to copy the exact generated value.
- Keep existing configuration unchanged unless a step explicitly requires and authorizes a change.
- Use plain language without talking down to the user. Interpret "idiot-proof" as beginner-safe and omission-resistant.
- Cite the authoritative source near any time-sensitive claim when web research was used.

## Formatting

- Prefer a compact settings summary before the numbered steps when several fields must be mapped exactly.
- Use short notes such as **Leave off**, **Leave unchanged**, or **Do not paste this into chat** beside the relevant field.
- Do not bury the recommended choice beneath alternatives or background explanation.
