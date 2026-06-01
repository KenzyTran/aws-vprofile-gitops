---
title: "7.5 Merge & chạy Docker + Helm"
date: 2025-01-01
weight: 5
---

## Merge và chạy job Docker + Helm

Khi check pass, bấm **Merge pull request -> Confirm merge**. Merge = push vào `main` -> kích hoạt:

- **`docker-build-push`**: build image, push lên ECR với tag `<commit-sha>` + `latest`.
- **`update-helm`**: clone `vprofile-helm` (dùng `GITOPS_PAT`), dùng `yq` cập nhật `app.tag` trong
  `values.yaml`, commit & push.

![Actions run sau merge: Docker và Helm job chạy](/images/actions-merge-run-success.png)
