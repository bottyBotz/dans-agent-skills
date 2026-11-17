---
name: "yeet"
description: "Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`)."
license: Apache-2.0
---

## Prerequisites

- Require GitHub CLI `gh`. Check `gh --version`. If missing, ask the user to install `gh` and stop.
- Require authenticated `gh` session. Run `gh auth status`. If not authenticated, ask the user to run `gh auth login` (and re-run `gh auth status`) before continuing.

## Writing dependency

Use the `avoid-ai-writing` skill to review human-facing commit messages, PR titles,
and PR descriptions before publishing them. Resolve it from the installed skill
catalogue and follow its instructions. Its upstream source is
[Avoid AI Writing](https://github.com/conorbronsdon/avoid-ai-writing).
If it is unavailable, disclose that the writing pass was skipped and apply a
manual plain-language review. Preserve technical facts, commands, links, and
verification evidence during editing.

## Naming conventions

- Branch: `codex/{description}` when starting from main/master/default.
- Commit: `{description}` (terse).
- PR title: `[codex] {description}` summarizing the full diff.

## Workflow

- If on main/master/default, create a branch: `git checkout -b "codex/{description}"`
- Otherwise stay on the current branch.
- Inspect status and the diff. Stage only the files belonging to the requested change; do not include unrelated work or sensitive files.
- Commit tersely with the description: `git commit -m "{description}"`
- Run checks if not already. If checks fail due to missing deps/tools, install dependencies and rerun once.
- Push with tracking: `git push -u origin $(git branch --show-current)`
- If push fails, inspect the reported error. Do not pull an arbitrary branch, rewrite history, or change authentication settings as a generic retry. Report any unresolved access requirement.
- Open a PR ready for review and edit title/body to reflect the description and the deltas: `GH_PROMPT_DISABLED=1 GIT_TERMINAL_PROMPT=0 gh pr create --fill --head $(git branch --show-current)`
- Ready for review is the default. Use `--draft` only when the user explicitly requests a draft. If this flow continues an existing draft PR, mark it ready with `gh pr ready` after the changes and checks are complete, unless the user requests keeping it as a draft.
- Write the PR description to a temporary file with real newlines, then pass its path to `gh pr create --body-file` or `gh pr edit --body-file`. Do not execute the body file. Keep it outside the staged changes.
- Describe the problem, resulting behaviour, and relevant validation in plain prose. Scale detail to the change and follow any repository template. Do not invent causes, test results, or user impact.
