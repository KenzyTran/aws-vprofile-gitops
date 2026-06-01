---
title: "7.6 Xác minh kết quả"
date: 2025-01-01
weight: 6
---

## Xác minh kết quả

- **ECR** (`vprofileappimg`): có image với tag commit SHA + `latest`.

  ![ECR có image với tag SHA và latest](/images/ecr-image-tags.png)

- **Repo `vprofile-helm`** -> `helm/vprofile/values.yaml`: `app.image` và `app.tag` đã cập nhật.

{{% notice info %}}
Đến đây CI hoàn chỉnh: code -> scan/quality gate -> build/push image -> tự cập nhật `values.yaml`.
{{% /notice %}}
