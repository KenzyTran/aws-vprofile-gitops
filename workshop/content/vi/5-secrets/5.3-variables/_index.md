---
title: "5.3 Lưu GitHub Variables"
date: 2025-01-01
weight: 3
---

## Lưu GitHub Variables

Tab **Variables -> New repository variable**:

| Variable | Giá trị (ví dụ) | Ý nghĩa |
|----------|-----------------|---------|
| `AWS_REGION` | `us-east-1` | Region đang dùng |
| `ECR_REPOSITORY` | `vprofileappimg` | Tên ECR repo |
| `HELM_REPO_NAME` | `vprofile-helm` | Repo helm để commit |
| `SONAR_HOST_URL` | `http://<sonar-public-ip>/` | URL SonarServer |

![Danh sách Repository variables](/images/github-variables.png)

{{% notice info %}}
`SONAR_HOST_URL` dùng public IP của SonarServer. IP đổi mỗi lần Stop/Start EC2 nên **cập nhật lại**
giá trị này mỗi khi bật lại server trước khi chạy pipeline.
{{% /notice %}}
