---
title: "4.2 Create CI IAM user"
date: 2025-01-01
weight: 2
---

## Create an IAM user for GitHub Actions

Go to **IAM -> Users -> Create user**:

1. User name: **`github-actions`**.
2. **Attach policies directly**, attach two policies:

   | Policy | Purpose |
   |--------|---------|
   | `AmazonEC2ContainerRegistryFullAccess` | Push/pull images to ECR |
   | `AmazonEKSClusterPolicy` | EKS access to the registry |

3. **Create user** -> **Security credentials -> Create access key -> CLI** -> **Download .csv**.

{{% notice warning %}}
**Never** commit the access key to Git. Store it only in **GitHub Secrets**. Deactivate/delete this
key when the workshop is over.
{{% /notice %}}
