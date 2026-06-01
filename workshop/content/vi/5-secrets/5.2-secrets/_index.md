---
title: "5.2 Lưu GitHub Secrets"
date: 2025-01-01
weight: 2
---

## Lưu GitHub Secrets

Repo `vprofile-app` -> **Settings -> Secrets and variables -> Actions -> Secrets -> New secret**:

| Secret | Giá trị | Nguồn |
|--------|---------|-------|
| `AWS_ACCESS_KEY_ID` | Access key IAM user | 4.2 |
| `AWS_SECRET_ACCESS_KEY` | Secret key IAM user | 4.2 |
| `SONAR_TOKEN` | Token SonarQube | 3.3 |
| `HELM_REPO_USER` | GitHub username | 5.1 |
| `GITOPS_PAT` | GitHub PAT | 5.1 |
| `SLACK_WEBHOOK` | Slack Webhook URL | 4.3 |

![Danh sách Repository secrets](/images/github-secrets.png)

{{% notice warning %}}
Secret **không xem lại được** sau khi lưu. Nhập sai phải xoá và tạo lại.
{{% /notice %}}
