---
title: "5.3 Store GitHub Variables"
date: 2025-01-01
weight: 3
---

## Store GitHub Variables

**Variables -> New repository variable**:

| Variable | Value (example) | Meaning |
|----------|-----------------|---------|
| `AWS_REGION` | `us-east-1` | Region in use |
| `ECR_REPOSITORY` | `vprofileappimg` | ECR repo name |
| `HELM_REPO_NAME` | `vprofile-helm` | Helm repo to commit to |
| `SONAR_HOST_URL` | `http://<sonar-public-ip>/` | SonarServer URL |

![Repository variables list](/images/github-variables.png)

{{% notice info %}}
`SONAR_HOST_URL` uses the SonarServer public IP, which changes on each Stop/Start. **Update** it
whenever you restart the server before running the pipeline.
{{% /notice %}}
