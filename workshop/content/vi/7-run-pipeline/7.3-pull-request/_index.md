---
title: "7.3 Raise Pull Request"
date: 2025-01-01
weight: 3
---

## Raise Pull Request (chạy job Sonar)

1. Repo `vprofile-app` -> **Pull requests -> New pull request**.
2. Merge **`feature-X` -> `main`** -> **Create pull request**.

PR kích hoạt **chỉ job `build-and-sonar`**; `docker-build-push` và `update-helm` bị **skip**:

![PR đang chạy check, Docker/Helm bị skip](/images/pr-checks.png)

Khi xong, run hiển thị **Success**:

![Actions run thành công, job Sonar pass](/images/actions-pr-run-success.png)
