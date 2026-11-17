# Dans agent skills

A personal collection of AI agent skills, collected and refined across different areas.

GitHub repository: [bottyBotz/dans-agent-skills](https://github.com/bottyBotz/dans-agent-skills).

## Catalogue

The entries below have not yet been exercised end to end from this repository.

| Skill | Category | Purpose | Requirements | Source | Licence | Tested status |
| --- | --- | --- | --- | --- | --- | --- |
| [step-by-step-instructions](skills/step-by-step-instructions/SKILL.md) | Guidance | Clear instructions with exact settings and checkpoints | Current product documentation when needed | Local collection | MIT | Experimental |
| [design-flow-auditor](skills/design-flow-auditor/SKILL.md) | Design | Review interface journeys against supplied requirements | Access to design artifacts; no specific design tool required | Generalized from local collection | MIT | Experimental |
| [goal-setter](skills/goal-setter/SKILL.md) | Agent workflows | Draft and validate clear Codex goals | Python 3.9+; native goal tools only for activation | Local collection | MIT | Experimental |
| [yeet](skills/yeet/SKILL.md) | Development | Stage, commit, push, and open a pull request when explicitly requested | Git, authenticated GitHub CLI; Avoid AI Writing for writing review | OpenAI skill, locally adapted | Apache-2.0 | Experimental |

## External skills

| Skill | Purpose | Source | Licence |
| --- | --- | --- | --- |
| Avoid AI Writing | Review and rewrite AI-writing patterns; referenced by `yeet` | [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) | MIT, per installed metadata |

Avoid AI Writing is linked rather than bundled. Follow its upstream installation instructions to make it available to your agent.

## Layout

```text
skills/
  skill-name/
    SKILL.md
    scripts/       # Optional reusable scripts
    references/    # Optional supporting documentation
    assets/        # Optional templates and resources
```

Keep each skill self-contained. Use lowercase, hyphenated folder names and relative paths within the skill.

## Adding a skill

Follow [CONTRIBUTING.md](CONTRIBUTING.md). Record third-party sources and modifications in [ATTRIBUTION.md](ATTRIBUTION.md), and preserve the applicable licence and copyright notices with each imported skill.

## Using a skill

Choose a skill from the catalogue, review its instructions and scripts, then follow the installation instructions for your agent. Requirements and supported environments belong in each skill's `SKILL.md`.

## Licence

Original contributions are licensed under the [MIT licence](LICENSE). Third-party material retains its own licence and notices; see the individual skill and [ATTRIBUTION.md](ATTRIBUTION.md). The root licence does not replace third-party terms.
