<table width="100%">
<tr>
<td align="left"><img src="../assets/logos/unav-logo.png" width="250"></td>
<td align="right"><img src="../assets/logos/data-logo.png" width="200"></td>
</tr>
</table>

# Student Projects

This is where members submit their own work. Every member belongs to a numbered group, from 1 to 10, and each group has one folder and one shared branch. If you don't know your group number, ask the coordinator.

| Your group | Your folder | Your branch |
|---|---|---|
| Group 1 | [`PROJECTS/Grupo_1/`](Grupo_1/) | `grupo-1` |
| Group 2 | [`PROJECTS/Grupo_2/`](Grupo_2/) | `grupo-2` |
| Group *N* | `PROJECTS/Grupo_N/` | `grupo-N` |

The same pattern applies up to [`Grupo_12`](Grupo_12/). Project milestones for each sharing session are in [upcoming-events.md](../DOCUMENTATION/02-events-and-activities/upcoming-events.md).

## How to submit a project

1. Follow [group-project-collaboration.md](../DOCUMENTATION/01-getting-started/group-project-collaboration.md): register your group, then create or join your branch `grupo-<number>`.
2. Fill in the `README.md` that is already in your group's folder.
3. Add your code and notebooks to your group's folder. If your dataset is large, don't commit it directly. Add a link to where it can be downloaded instead (e.g. Google Drive, Kaggle).
4. Commit, push, and open a draft pull request. Full steps are in [CONTRIBUTING.md](../CONTRIBUTING.md).
5. Before each sharing session, add that session's materials to a `sharing/` subfolder in your group's folder.
6. When the project is finished, mark the pull request as ready and tag a science collaborator for review.

**Only edit your own group's folder.** That way you never break another group's work.

## What makes a good submission

- A filled-out README explaining what the project does and how to run it
- Clean, commented code
- Clear indication of data sources (or how to obtain the data)

## Example structure

```
PROJECTS/
├── Grupo_1/
├── Grupo_2/
├── Grupo_3/
│   ├── README.md           (project description)
│   ├── 01-cleaning-ana.ipynb
│   ├── 02-eda-juan.ipynb
│   ├── sharing/            (materials for each sharing session)
│   ├── data/               (or a DATA_SOURCE.md linking to it)
│   └── requirements.txt
└── ...
```

---
*Last updated: 2026-11-09 · Updated by: Leo*
