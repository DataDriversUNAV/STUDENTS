<table width="100%">
<tr>
<td align="left"><img src="../../../DOCUMENTATION/01-getting-started/images/unav%20logo.png" width="250"></td>
<td align="right"><img src="../../../DOCUMENTATION/01-getting-started/images/data%20logo.png" width="200"></td>
</tr>
</table>

# GitHub Beginner Guide (Zero to First Pull Request)

This assumes you've never used Git or GitHub before. Follow in order — each step builds on the last. If a term is unfamiliar, it's explained the first time it appears.

## 0. Before you start

Make sure you've done [software-installation.md](software-installation.md): Git installed, GitHub account created, VS Code installed.

## 1. Key concepts (30-second version)

- **Repository (repo):** a project folder tracked by Git — this whole club knowledge base is one repo.
- **Clone:** download a copy of the repo to your computer.
- **Branch:** an independent line of work, so you don't edit `main` directly.
- **Commit:** a saved snapshot of your changes, with a message describing what changed.
- **Push:** upload your commits to GitHub.
- **Pull Request (PR):** a request to merge your branch into `main`, which officers/collaborators review before accepting.

## 2. Clone the repo

1. Go to the repo page on GitHub.
2. Click the green **Code** button → copy the HTTPS URL (looks like `https://github.com/leokonma/DD_CLASS.git`).
3. Open a terminal (or VS Code's built-in terminal) and run:
   ```
   git clone https://github.com/leokonma/DD_CLASS.git
   cd DD_CLASS
   ```
4. Open the folder in VS Code: `code .`

## 3. Configure Git (first time only)

```
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
Use the same email as your GitHub account.

## 4. Create a branch for your work

Never commit directly to `main`. For a project submission:
```
git checkout -b project-my-cool-analysis
```

## 5. Make your changes

- Add your project folder under `PROJECTS/your-project-name/` (see [PROJECTS/README.md](../../PROJECTS/README.md)).
- Save your files as usual in VS Code.

## 6. Check what changed

```
git status
```
Shows which files you've added/modified.

## 7. Stage and commit

```
git add .
git commit -m "Add sales forecast project"
```
`git add .` stages all changes; the commit message should briefly describe what you did.

## 8. Push your branch to GitHub

```
git push -u origin project-my-cool-analysis
```
First push of a new branch needs `-u origin <branch-name>`; after that, `git push` alone works.

## 9. Open a Pull Request

1. Go to the repo on GitHub — you'll see a banner "Compare & pull request" for your recently pushed branch. Click it.
   (If you don't see it, go to the **Pull Requests** tab → **New pull request** → select your branch.)
2. Fill in a title and description of what you're submitting.
3. Click **Create pull request**.
4. Tag a science collaborator or officer for review (type `@` followed by their GitHub username in a comment).

## 10. Respond to feedback

Reviewers may leave comments asking for changes. To update your PR:
```
git add .
git commit -m "Address review feedback"
git push
```
The PR updates automatically — no need to open a new one.

## 11. After it's merged

Once approved and merged, switch back to `main` and pull the latest:
```
git checkout main
git pull
```

## Common errors

| Error | Meaning | Fix |
|---|---|---|
| `fatal: not a git repository` | You're not inside the cloned folder | `cd` into the repo folder first |
| `Permission denied (publickey)` | GitHub authentication issue | Use HTTPS clone URL, or set up SSH keys (ask a science collaborator) |
| `Updates were rejected` on push | Your branch is behind | Run `git pull` first, then push again |
| Merge conflict | Two people edited the same lines | Ask a science collaborator to help resolve — this is normal, not a disaster |

## Cheat sheet

```
git clone <url>          # download the repo
git checkout -b <name>    # create and switch to a new branch
git status                # see what changed
git add .                  # stage all changes
git commit -m "message"    # save a snapshot
git push -u origin <name>  # upload branch (first time)
git pull                   # get latest changes from main
```

---
*Last updated: 2026-07-18 · Updated by: Leo · Source: [docs.github.com](https://docs.github.com)*
