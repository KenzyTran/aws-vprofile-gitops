---
title: "7.5 Merge & run Docker + Helm"
date: 2025-01-01
weight: 5
---

## Merge and run the Docker + Helm jobs

When checks pass, click **Merge pull request -> Confirm merge**. A merge = push to `main` ->
triggers:

- **`docker-build-push`**: build the image, push to ECR with tags `<commit-sha>` + `latest`.
- **`update-helm`**: clone `vprofile-helm` (with `GITOPS_PAT`), use `yq` to update `app.tag` in
  `values.yaml`, commit & push.

![Actions run after merge: Docker and Helm jobs run](/images/actions-merge-run-success.png)
