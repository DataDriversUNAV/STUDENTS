<table width="100%">
<tr>
<td align="left"><img src="assets/logos/unav-logo.png" width="250"></td>
<td align="right"><img src="assets/logos/data-logo.png" width="200"></td>
</tr>
</table>

# Contributing

Everything goes through a pull request (PR) — nobody pushes directly to `main`.

If you've never used Git or GitHub, read [DOCUMENTATION/01-getting-started/github-beginner-guide.md](DOCUMENTATION/01-getting-started/github-beginner-guide.md) first. For projects, follow the step-by-step [group-project-collaboration.md](DOCUMENTATION/01-getting-started/group-project-collaboration.md).

## Projects: one branch per project

Every project, whether a team or solo, lives on **its own branch** for the whole year and is merged into `main` at the end.

1. **Register your team:** open an issue with the **New project team** template.
2. **Team lead creates the branch** `project-<project-name>` and the folder `PROJECTS/<foundations|advanced>/<project-name>/`, with the template copied in as `README.md`.
3. **Teammates join the branch** with `git fetch` and `git checkout project-<project-name>`.
4. **Open a draft pull request** against `main` in the first weeks, so mentors can follow and comment.
5. **Work loop, every session:** `git pull` → work → `git add` / `git commit` → `git pull` → `git push`.
6. **Before each sharing session,** push your materials to `sharing/` inside your project folder.
7. **When finished,** mark the PR **Ready for review**, add a science collaborator as reviewer, and they merge once approved.

Rules: only edit your own project folder, one person per notebook, and push at the end of every session.

## Editing documentation

1. Create a branch, e.g. `git checkout -b update-setup-guide`.
2. Make your edits.
3. Commit and push.
4. Open a PR describing what changed and why.
5. A science collaborator or officer reviews and merges.

## Branch naming

Use short, descriptive branch names: `project-<project-name>` (same as your project folder), `docs-<topic>`, `fix-<thing>`.

## Questions

Not sure where something belongs? Open an issue, or ask a science collaborator before starting — better to check early than redo it.
