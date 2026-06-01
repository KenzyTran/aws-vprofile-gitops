---
title: "5.2 Store GitHub Secrets"
date: 2025-01-01
weight: 2
---

## Store GitHub Secrets

Repo `vprofile-app` -> **Settings -> Secrets and variables -> Actions -> Secrets -> New secret**:

| Secret | Value | Source |
|--------|-------|--------|
| `AWS_ACCESS_KEY_ID` | IAM user access key | 4.2 |
| `AWS_SECRET_ACCESS_KEY` | IAM user secret key | 4.2 |
| `SONAR_TOKEN` | SonarQube token | 3.3 |
| `HELM_REPO_USER` | GitHub username | 5.1 |
| `GITOPS_PAT` | GitHub PAT | 5.1 |
| `SLACK_WEBHOOK` | Slack Webhook URL | 4.3 |

![Repository secrets list](/images/github-secrets.png)

{{% notice warning %}}
Secrets **cannot be viewed** after saving. If wrong, delete and recreate.
{{% /notice %}}
