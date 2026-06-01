---
title: "7.3 Raise a Pull Request"
date: 2025-01-01
weight: 3
---

## Raise a Pull Request (runs the Sonar job)

1. Repo `vprofile-app` -> **Pull requests -> New pull request**.
2. Merge **`feature-X` -> `main`** -> **Create pull request**.

The PR triggers **only `build-and-sonar`**; `docker-build-push` and `update-helm` are **skipped**:

![PR checks running, Docker/Helm skipped](/images/pr-checks.png)

When done, the run shows **Success**:

![Successful Actions run, Sonar job passed](/images/actions-pr-run-success.png)
