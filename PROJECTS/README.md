<table width="100%">
<tr>
<td align="left"><img src="../assets/logos/unav-logo.png" width="250"></td>
<td align="right"><img src="../assets/logos/data-logo.png" width="200"></td>
</tr>
</table>

# Student Projects

This is where members submit their own work. Every member delivers one project at their level by the final showcase (see [groups-and-attendance.md](../DOCUMENTATION/02-events-and-activities/groups-and-attendance.md)). Each project gets its own subfolder, submitted via pull request.

- **Foundations** → [`PROJECTS/foundations/`](foundations/README.md): a data-analysis project.
- **Advanced** → [`PROJECTS/advanced/`](advanced/README.md): an investigation project.

## How to submit a project

1. Follow [group-project-collaboration.md](../DOCUMENTATION/01-getting-started/group-project-collaboration.md): register your team, then get your project branch `project-<project-name>`. One branch per project, shared by the whole team.
2. Create a new folder inside your group's folder, using lowercase and hyphens: `PROJECTS/foundations/your-project-name/` or `PROJECTS/advanced/your-project-name/` (e.g. `PROJECTS/advanced/sales-forecast-juan-and-maria/`).
3. Copy [project-submission-template.md](project-submission-template.md) into your folder as `README.md` and fill it in.
4. Add your code/notebooks. If your dataset is large, don't commit it directly — add a link to where it can be downloaded instead (e.g. Google Drive, Kaggle).
5. Commit, push, and open a pull request. Full steps in [CONTRIBUTING.md](../CONTRIBUTING.md).
6. Before each sharing session, add that session's materials to a `sharing/` subfolder in your project.
7. Tag a science collaborator for review.

## Folder naming

`project-name-yourname/` or `project-name-team/` — keep it short, lowercase, hyphen-separated, no spaces.

## What makes a good submission

- A filled-out README (from the template) explaining what the project does and how to run it
- Clean, commented code
- Clear indication of data sources (or how to obtain the data)

## Example structure

```
PROJECTS/
├── foundations/
│   └── netflix-eda-ana/
└── advanced/
    └── sales-forecast-juan-and-maria/
        ├── README.md          (from project-submission-template.md)
        ├── notebook.ipynb
        ├── sharing/            (materials for each sharing session)
        ├── data/               (or a DATA_SOURCE.md linking to it)
        └── requirements.txt
```

---
*Last updated: 2026-10-05 · Updated by: Leo*
