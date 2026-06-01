---
title: "7.6 Verify the result"
date: 2025-01-01
weight: 6
---

## Verify the result

- **ECR** (`vprofileappimg`): an image with the commit SHA tag + `latest`.

  ![ECR image with SHA and latest tags](/images/ecr-image-tags.png)

- **Repo `vprofile-helm`** -> `helm/vprofile/values.yaml`: `app.image` and `app.tag` are updated.

{{% notice info %}}
CI is now complete: code -> scan/quality gate -> build/push image -> auto-update `values.yaml`.
{{% /notice %}}
