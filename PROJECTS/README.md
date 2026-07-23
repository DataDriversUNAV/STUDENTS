<table width="100%">
<tr>
<td align="left"><img src="../../DOCUMENTATION/01-getting-started/images/unav%20logo.png" width="250"></td>
<td align="right"><img src="../../DOCUMENTATION/01-getting-started/images/data%20logo.png" width="200"></td>
</tr>
</table>

# Student Projects

This is where members submit their own work. Each project gets its own subfolder, submitted via pull request — this is the club's main hands-on collaboration workflow.

## How to submit a project

1. If you haven't already, follow [github-beginner-guide.md](../DOCUMENTATION/01-getting-started/github-beginner-guide.md) to clone the repo and create a branch.
2. Create a new folder here named after your project, using lowercase and hyphens: `PROJECTS/your-project-name/` (e.g. `PROJECTS/sales-forecast-juan-and-maria/`).
3. Copy [project-submission-template.md](project-submission-template.md) into your folder as `README.md` and fill it in.
4. Add your code/notebooks. If your dataset is large, don't commit it directly — add a link to where it can be downloaded instead (e.g. Google Drive, Kaggle).
5. Commit, push, and open a pull request. Full steps in [CONTRIBUTING.md](../../CONTRIBUTING.md).
6. Tag a science collaborator for review.

## Folder naming

`project-name-yourname/` or `project-name-team/` — keep it short, lowercase, hyphen-separated, no spaces.

## What makes a good submission

- A filled-out README (from the template) explaining what the project does and how to run it
- Clean, commented code
- Clear indication of data sources (or how to obtain the data)

## Example structure

```
PROJECTS/
└── sales-forecast-juan-and-maria/
    ├── README.md          (from project-submission-template.md)
    ├── notebook.ipynb
    ├── data/               (or a DATA_SOURCE.md linking to it)
    └── requirements.txt
```

---
*Last updated: — · Updated by: —*
