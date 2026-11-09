<table width="100%">
<tr>
<td align="left"><img src="../../assets/logos/unav-logo.png" width="250"></td>
<td align="right"><img src="../../assets/logos/data-logo.png" width="200"></td>
</tr>
</table>

# Working on a Group Project (Step by Step)

This guide takes you from "I have a group" to "our project is merged" and assumes no prior knowledge. If you haven't installed Git, Python and VS Code yet, do [software-installation.md](software-installation.md) first. If words like *commit* or *push* are new to you, skim section 1 of [github-beginner-guide.md](github-beginner-guide.md).

The examples use **Group 3**. Replace the 3 with your own group number everywhere.

---

## 1. How we work: one branch per group

```
main  ───────────────────────────────────●  (merged at the final showcase)
        \                               /
grupo-3  ●──●──●──●──●──●──●──●──●──●──●
         Ana  Juan Ana  María ...  (everyone in the group commits here)
```

- **`main`** is the official version of the repo. Nobody works on it directly.
- **Each group has its own branch**, `grupo-3`, and the whole group works on that one branch.
- **Each group has its own folder**, `PROJECTS/Grupo_3/`. Your group only edits that folder, so you never break another group's work.
- **Push at the end of every session.** The branch on GitHub is your backup and how mentors see your work.
- **A draft pull request (PR)** is opened in the first weeks so mentors can comment along the way. It's merged into `main` when the project is finished.

### The rules in one box

> 1. **Pull before you start.** 2. **Push when you finish.** 3. **One person per file** (especially notebooks). 4. **Only touch your group's folder.**

---

## 2. Before your first session

1. **Have a GitHub account.** Create one at [github.com/signup](https://github.com/signup) if you haven't.
2. **Send your GitHub username to the coordinator** so you're added to the [DataDriversUNAV](https://github.com/DataDriversUNAV) organization.
3. **Accept the invitation.** It arrives by email, or you'll see a banner at [github.com/DataDriversUNAV](https://github.com/DataDriversUNAV). Until you accept, you can't see or push to the repo.
4. **Tell Git who you are** (first time on this computer only). Open a terminal (in VS Code: **Terminal → New Terminal**) and run:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "the-email-of-your-github-account@example.com"
   git config --global pull.rebase false
   ```
   The last line tells `git pull` how to combine your commits with your teammates'. Without it, some computers stop with an error the first time both of you have new commits.

---

## 3. Register your group

Every member is in a numbered group, from 1 to 10. If you don't know your number, ask the coordinator. The number gives you your folder and your branch:

| Group | Folder | Branch |
|---|---|---|
| 3 | `PROJECTS/Grupo_3/` | `grupo-3` |

1. Agree on who will be the **team lead** and on a **project name**.
2. The team lead registers the group on GitHub:
   1. Go to the [STUDENTS repo](https://github.com/DataDriversUNAV/STUDENTS) → **Issues** tab → **New issue**.
   2. Choose **New project team** and fill it in: group number, members' GitHub usernames, project name and topic.
   3. Click **Submit new issue**. The coordinator confirms it in a comment.
3. The issue is your group's home page. Use its comments for questions to mentors.

---

## 4. Team lead: set up the branch (once)

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
3. **Create your group's branch** (`grupo-` + your number):
   ```
   git checkout -b grupo-3
   ```
   `checkout -b` means "create a new branch and move onto it".
4. **Open `PROJECTS/Grupo_3/README.md` in VS Code and fill in** at least the project name and authors. The folder and the README already exist. If you can't see them, repeat step 2.
5. **Save a snapshot (commit) and upload it (push):**
   ```
   git add PROJECTS/Grupo_3
   git commit -m "Set up Grupo 3 project"
   git push -u origin grupo-3
   ```
   `-u origin grupo-3` is only needed the first time. It links your local branch to the one on GitHub.
6. Tell your group: **"The branch is up!"**

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
   git checkout grupo-3
   ```
   Git sees that the branch exists on GitHub and creates your local copy automatically.
3. **Check you're on the right branch:**
   ```
   git branch
   ```
   The one with `*` next to it is where you are. It should be `grupo-3`, **not** `main`.

---

## 6. Open a draft pull request (team lead, week 1–3)

A pull request (PR) is how your work will eventually enter `main`. Opening it early as a **draft** lets mentors follow and comment, and it can't be merged by accident.

1. Go to the [STUDENTS repo](https://github.com/DataDriversUNAV/STUDENTS) → **Pull requests** → **New pull request**.
2. Set **base: `main`** and **compare: `grupo-3`**.
3. Click **Create pull request**, then use the small arrow on the green button and pick **Create draft pull request**.
4. Title: `Grupo 3: <your project name>`. In the description, write `Closes #12`, using your group issue's number. This links the PR to your group issue.

---

## 7. Every session: the work loop

Do this **every time** you sit down to work, alone or in class.

```
git checkout grupo-3   # 1. be on your branch
git pull                              # 2. get your teammates' latest work
#    ... work in VS Code, save your files ...
git status                            # 3. see what you changed
git add PROJECTS/Grupo_3
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

### Will `git pull` delete my work?

**No.** `git pull` only brings in what others have pushed. If it would have to overwrite something of yours, it stops and leaves your files as they were. This is true right after cloning and at any later time. Save your files in VS Code first, because Git can only see what is saved to disk.

| What you have on your computer | What `git pull` does | What you do |
|---|---|---|
| New files that aren't on GitHub | Leaves them alone | Nothing |
| Uncommitted edits to files nobody else changed | Leaves them alone | Nothing |
| Uncommitted edits to a file that also changed on GitHub | Stops: `Your local changes ... would be overwritten`. Your file isn't touched | Commit your work, then pull again |
| A new, uncommitted file with the same name as one on GitHub | Stops: `untracked working tree files would be overwritten`. Your file isn't touched | Rename your file, then pull again |
| Commits of yours, and teammates pushed commits too | Combines both | Nothing |
| Commits of yours that changed the same lines as a teammate | Reports a merge conflict and keeps both versions | Follow section 9 |

**What can really lose work** is something else:

- Clicking **Discard Changes** in VS Code.
- Running `git reset --hard`, `git clean`, `git restore <file>` or `git checkout -- <file>`.
- Deleting the folder and cloning again before you've pushed.

If Git shows you an error and you're not sure what to do, stop and ask a mentor. Don't try these commands to make the error go away.

**Commit often and push at the end of every session.** Once your work is pushed, it's safe on GitHub even if your computer breaks.

### Session notebooks: work on a copy

Don't edit or run notebooks directly in `DOCUMENTATION/03-session material/`. Even running one changes the file, so `git pull` will stop if the club later updates it. Copy the notebook into your group's folder and work there.

If `git pull` has already stopped because of a session file you changed, copy your version into your group's folder first. Then undo the change to the original and pull:

```
git restore "DOCUMENTATION/03-session material/session 2/importing_data.ipynb"
git pull
```

### Getting new session materials on your branch

`git pull` only updates the branch you're on, so new material added to `main` doesn't reach `grupo-3` by itself. To bring it in, commit your work first and then run:

```
git pull origin main
git push
```

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
5. **Conflict in a notebook (`.ipynb`)?** Don't try to edit it by hand. Keep one version with `git checkout --theirs path/to/notebook.ipynb` (their version) or `--ours` (yours), then `git add`, `git commit`, `git push`. The version you didn't keep is still in Git's history, so ask a mentor to help you bring back any cells you need.

---

## 10. Before each sharing session

Every 3rd week (see [upcoming-events.md](../02-events-and-activities/upcoming-events.md)) your group presents. **Before the session:**

1. Put your slides, notebook or notes in a `sharing/` folder inside your group's folder, numbered by session: `sharing/01-proposal.pdf`, `sharing/02-first-exploration.ipynb`.
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
   git branch -d grupo-3
   ```

---

## Common problems

| Problem | What it means | Fix |
|---|---|---|
| `fatal: not a git repository` | Your terminal isn't inside the STUDENTS folder | `cd STUDENTS` (or open the folder in VS Code and use its terminal) |
| `Repository not found` / `403` | You haven't accepted the org invitation, or weren't added | Check your email / [github.com/DataDriversUNAV](https://github.com/DataDriversUNAV), or ask the coordinator |
| `error: pathspec 'grupo-...' did not match` | Git doesn't know the branch yet | Run `git fetch` first, and check the spelling. If it still fails, your team lead hasn't pushed the branch yet |
| `Updates were rejected because the remote contains work...` | A teammate pushed while you worked | `git pull`, then `git push` again |
| `Your local changes ... would be overwritten by merge` | Git stopped to protect your edits. Nothing was lost | Commit your work, then `git pull` again |
| `untracked working tree files would be overwritten` | One of your new files has the same name as one on GitHub. Nothing was lost | Rename your file, then `git pull` again |
| `Need to specify how to reconcile divergent branches` | Git needs the setting from section 2 | Run `git config --global pull.rebase false`, then `git pull` again |
| A strange text screen opens after `git pull` | Git is asking you to confirm a merge message | If it's a VS Code tab, close it. In the terminal, type `:wq` and press Enter |
| `Please commit your changes or stash them before you switch branches` | You have unsaved work | Commit it first (section 7) |
| You committed on `main` by mistake | Your work is on the wrong branch | Don't push. Ask a mentor, it's a 1-minute fix |
| Sign-in window keeps popping up | Git needs to log in to GitHub | Sign in with the browser option. It's only asked once per computer |

## Cheat sheet

```
git clone https://github.com/DataDriversUNAV/STUDENTS.git   # download the repo (once)
git fetch                          # learn about new branches on GitHub
git checkout grupo-<number>        # switch to your group's branch
git checkout -b grupo-<number>     # create the branch (team lead, once)
git branch                         # which branch am I on?
git pull                           # get teammates' latest work
git pull origin main               # bring new session materials from main onto your branch
git status                         # what did I change?
git add PROJECTS/Grupo_<number>    # stage changes
git commit -m "What I did"         # save a snapshot
git push                           # upload (first time: git push -u origin grupo-<number>)
```

---
*Last updated: 2026-11-09 · Updated by: Leo · Source: [docs.github.com](https://docs.github.com)*
