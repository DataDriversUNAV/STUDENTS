<table width="100%">
<tr>
<td align="left"><img src="../../assets/logos/unav-logo.png" width="250"></td>
<td align="right"><img src="../../assets/logos/data-logo.png" width="200"></td>
</tr>
</table>

# Working on a Group Project (Step by Step)

This guide takes you from "I have a team" to "our project is merged" and assumes no prior knowledge. If you haven't installed Git, Python and VS Code yet, do [software-installation.md](software-installation.md) first. If words like *commit* or *push* are new to you, skim section 1 of [github-beginner-guide.md](github-beginner-guide.md).

Solo project (most Foundations members)? You still follow this guide. You're just a team of one, so skip the parts about teammates.

---

## 1. How we work: one branch per project

```
main  ────────────────────────────────────────────────●  (merged at the final showcase)
        \                                            /
project-sales-forecast  ●──●──●──●──●──●──●──●──●──●
                        Ana  Juan Ana  María ...  (everyone on the team commits here)
```

- **`main`** is the official version of the repo. Nobody works on it directly.
- **Each project gets its own branch**, and the whole team works on that one branch.
- **Push at the end of every session.** The branch on GitHub is your backup and how mentors see your work.
- **A draft pull request (PR)** is opened in the first weeks so mentors can comment along the way. It's merged into `main` when the project is finished.
- **Your team only edits its own folder** (`PROJECTS/advanced/your-project/` or `PROJECTS/foundations/your-project/`). That way you never break another team's work.

### The rules in one box

> 1. **Pull before you start.** 2. **Push when you finish.** 3. **One person per file** (especially notebooks). 4. **Only touch your project folder.**

---

## 2. Before your first session

1. **Have a GitHub account.** Create one at [github.com/signup](https://github.com/signup) if you haven't.
2. **Send your GitHub username to the coordinator** so you're added to the [DataDriversUNAV](https://github.com/DataDriversUNAV) organization.
3. **Accept the invitation.** It arrives by email, or you'll see a banner at [github.com/DataDriversUNAV](https://github.com/DataDriversUNAV). Until you accept, you can't see or push to the repo.
4. **Tell Git who you are** (first time on this computer only). Open a terminal (in VS Code: **Terminal → New Terminal**) and run:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "the-email-of-your-github-account@example.com"
   ```

---

## 3. Create your team

Teams are up to **3 people** for Advanced investigations. Foundations projects are usually individual.

1. Agree on a **project name**: short, lowercase, hyphens instead of spaces, e.g. `sales-forecast` or `netflix-eda-ana`. This name becomes both your **folder** and your **branch**.
2. One person, the **team lead**, registers the team on GitHub:
   1. Go to the [STUDENTS repo](https://github.com/DataDriversUNAV/STUDENTS) → **Issues** tab → **New issue**.
   2. Choose **New project team** and fill it in: team members' GitHub usernames, group, project name and topic.
   3. Click **Submit new issue**. The coordinator confirms it in a comment.
3. The issue is your team's home page. Use its comments for questions to mentors.

---

## 4. Team lead: set up the branch and folder (once)

Only **one** person does this. Everyone else waits for step 5.

1. **Download the repo** (skip if you already have it):
   ```
   git clone https://github.com/DataDriversUNAV/STUDENTS.git
   cd STUDENTS
   ```
2. **Make sure you have the latest `main`:**
   ```
   git checkout main
   git pull
   ```
3. **Create your team's branch** (`project-` + your project name):
   ```
   git checkout -b project-sales-forecast
   ```
   `checkout -b` means "create a new branch and move onto it".
4. **Create your project folder** inside your group's folder, and copy the template in as your README:
   ```
   mkdir PROJECTS/advanced/sales-forecast
   cp PROJECTS/project-submission-template.md PROJECTS/advanced/sales-forecast/README.md
   ```
   (Foundations: use `PROJECTS/foundations/...` instead. On Windows PowerShell, use `copy` instead of `cp`.)
5. **Open the README in VS Code and fill in** at least the project name, group and authors.
6. **Save a snapshot (commit) and upload it (push):**
   ```
   git add PROJECTS/advanced/sales-forecast
   git commit -m "Set up sales-forecast project"
   git push -u origin project-sales-forecast
   ```
   `-u origin project-sales-forecast` is only needed the first time. It links your local branch to the one on GitHub.
7. Tell your team: **"The branch is up!"**

---

## 5. Teammates: join the branch

1. **Download the repo** (skip if you already have it):
   ```
   git clone https://github.com/DataDriversUNAV/STUDENTS.git
   cd STUDENTS
   ```
2. **Get the list of branches from GitHub and switch to yours:**
   ```
   git fetch
   git checkout project-sales-forecast
   ```
   Git sees that the branch exists on GitHub and creates your local copy automatically.
3. **Check you're on the right branch:**
   ```
   git branch
   ```
   The one with `*` next to it is where you are. It should be `project-sales-forecast`, **not** `main`.

---

## 6. Open a draft pull request (team lead, week 1–3)

A pull request (PR) is how your work will eventually enter `main`. Opening it early as a **draft** lets mentors follow and comment, and it can't be merged by accident.

1. Go to the [STUDENTS repo](https://github.com/DataDriversUNAV/STUDENTS) → **Pull requests** → **New pull request**.
2. Set **base: `main`** and **compare: `project-sales-forecast`**.
3. Click **Create pull request**, then use the small arrow on the green button and pick **Create draft pull request**.
4. Title: `Project: sales-forecast (Advanced)`. In the description, write `Closes #12`, using your team issue's number. This links the PR to your team issue.

---

## 7. Every session: the work loop

Do this **every time** you sit down to work, alone or in class.

```
git checkout project-sales-forecast   # 1. be on your branch
git pull                              # 2. get your teammates' latest work
#    ... work in VS Code, save your files ...
git status                            # 3. see what you changed
git add PROJECTS/advanced/sales-forecast
git commit -m "Clean the 2025 sales data"   # 4. snapshot with a clear message
git pull                              # 5. grab anything pushed while you worked
git push                              # 6. upload
```

**Good commit messages** say what you did: `Add EDA of customer ages`, `Fix date parsing in cleaning step`. Avoid messages like `changes` or `asdf`.

### Prefer buttons? Do it in VS Code

The **Source Control** panel (the branch-shaped icon on the left, or `Ctrl+Shift+G`) does the same thing:

| Command | VS Code |
|---|---|
| See which branch you're on / switch | Branch name in the **bottom-left corner**. Click it to switch. |
| `git pull` / `git push` | The **↻ Sync Changes** button, or `…` menu → Pull / Push |
| `git add` | **+** next to a file under *Changes* |
| `git commit -m` | Type the message in the box at the top → **✓ Commit** |

---

## 8. Don't step on each other

Two people changing **the same lines of the same file** at the same time causes a *merge conflict*. Avoid it like this:

- **Split work by file.** Each person has their own notebook: `01-cleaning-ana.ipynb`, `02-eda-juan.ipynb`. When a part is done, one person combines the results.
- **Never edit a teammate's notebook.** Jupyter notebooks are stored as complicated JSON, and conflicts in them are painful to fix. Leave a comment instead, or ask the owner.
- **Shared files (like README.md): say it in the team chat** ("I'm editing the README now") and push quickly.
- **Pull before you start, push when you finish.** This alone prevents most problems.

---

## 9. If you get a merge conflict

Don't panic. It's normal, and nothing is lost.

1. After `git pull`, Git says `CONFLICT (content): Merge conflict in <file>`.
2. Open that file in VS Code. You'll see colored blocks:
   ```
   <<<<<<< HEAD
   your version
   =======
   your teammate's version
   >>>>>>> ...
   ```
3. Above each block VS Code shows buttons: **Accept Current** (yours), **Accept Incoming** (theirs), **Accept Both**. Pick one, or edit by hand until the file looks right, then delete any leftover `<<<<<<<`, `=======`, `>>>>>>>` lines.
4. Save, then:
   ```
   git add .
   git commit -m "Resolve merge conflict in README"
   git push
   ```
5. **Conflict in a notebook (`.ipynb`)?** Don't try to edit it by hand. Keep one version with `git checkout --theirs path/to/notebook.ipynb` (their version) or `--ours` (yours), then `git add`, `git commit`, `git push`, and copy over whatever cells you lost. Ask a mentor if you're unsure.

---

## 10. Before each sharing session

Every 3rd week (see [upcoming-events.md](../02-events-and-activities/upcoming-events.md)) your team presents. **Before the session:**

1. Put your slides, notebook or notes in a `sharing/` folder inside your project, numbered by session: `sharing/01-proposal.pdf`, `sharing/02-first-exploration.ipynb`.
2. Commit and push (section 7).
3. Check that the files appear in your draft PR under **Files changed**.

---

## 11. Finishing the project

1. Make sure your project README is complete (summary, data, how to run, key findings) and everything is pushed.
2. On your PR page, click **Ready for review**.
3. On the right, under **Reviewers**, add a science collaborator or mentor.
4. Reviewers may ask for changes. Do them with the normal work loop (section 7), and the PR updates by itself.
5. Once approved, a reviewer **merges** it. Your project is now in `main`. 🎉
6. Clean up your computer:
   ```
   git checkout main
   git pull
   git branch -d project-sales-forecast
   ```

---

## Common problems

| Problem | What it means | Fix |
|---|---|---|
| `fatal: not a git repository` | Your terminal isn't inside the STUDENTS folder | `cd STUDENTS` (or open the folder in VS Code and use its terminal) |
| `Repository not found` / `403` | You haven't accepted the org invitation, or weren't added | Check your email / [github.com/DataDriversUNAV](https://github.com/DataDriversUNAV), or ask the coordinator |
| `error: pathspec 'project-...' did not match` | Git doesn't know the branch yet | Run `git fetch` first, and check the spelling |
| `Updates were rejected because the remote contains work...` | A teammate pushed while you worked | `git pull`, then `git push` again |
| `Please commit your changes or stash them before you switch branches` | You have unsaved work | Commit it first (section 7) |
| You committed on `main` by mistake | Your work is on the wrong branch | Don't push. Ask a mentor, it's a 1-minute fix |
| Sign-in window keeps popping up | Git needs to log in to GitHub | Sign in with the browser option. It's only asked once per computer |

## Cheat sheet

```
git clone https://github.com/DataDriversUNAV/STUDENTS.git   # download the repo (once)
git fetch                          # learn about new branches on GitHub
git checkout project-<name>        # switch to your team branch
git checkout -b project-<name>     # create a new branch (team lead, once)
git branch                         # which branch am I on?
git pull                           # get teammates' latest work
git status                         # what did I change?
git add <folder>                   # stage changes
git commit -m "What I did"         # save a snapshot
git push                           # upload (first time: git push -u origin project-<name>)
```

---
*Last updated: 2026-10-14 · Updated by: Leo · Source: [docs.github.com](https://docs.github.com)*
