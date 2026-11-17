# Adding and maintaining skills

## New skills

1. Create `skills/<skill-name>/SKILL.md`. Use lowercase letters, numbers, and single hyphens for the name.
2. Add YAML frontmatter with `name` matching the folder and a `description` explaining what the skill does and when to use it.
3. Write focused instructions covering required inputs, steps, expected output, and how to check the result.
4. Document required tools, plugins, credentials, operating systems, and network access. Include placeholders for configuration rather than personal values or credentials.
5. Bundle supporting scripts, references, and assets when needed. Use relative paths and avoid dependencies on files outside the skill folder.
6. Try the skill on a representative task. Record the date, agent/environment, outcome, and known limitations in a `## Verification` section. Label untested skills as experimental.
7. Update the README catalogue with the skill's category, requirements, source, licence, and tested status.

Minimum frontmatter:

```yaml
---
name: skill-name
description: Describe the task this skill handles and when to use it.
---
```

Format reference: [Agent Skills specification](https://agentskills.io/specification).

## Imported or adapted skills

- Check that the source terms allow redistribution and the intended modifications.
- Preserve the original licence, required notices, and author credits within the skill folder.
- Add the source URL, exact upstream revision, licence, and modifications to `ATTRIBUTION.md`.
- Keep upstream imports and local changes in separate commits where practical.
- For link-only recommendations, add a clearly labelled external link in the README rather than a copied skill folder.

## Before publishing

- Check that names and frontmatter match, referenced files exist, and scripts behave as described.
- Remove credentials, private examples, client material, personal paths, and generated output.
- Review all staged files and any existing Git history for sensitive information. `.gitignore` does not remove tracked files.
- Check that catalogue links and attribution entries are accurate.

## Updates

Describe meaningful behaviour changes in commit messages. Re-run a representative task after changing a skill's behaviour, and update its verification notes. Record upstream revision changes in `ATTRIBUTION.md` when refreshing imported skills.
