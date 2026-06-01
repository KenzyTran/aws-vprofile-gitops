---
title: "4.2 Tạo IAM user cho CI"
date: 2025-01-01
weight: 2
---

## Tạo IAM user cho GitHub Actions

Vào **IAM -> Users -> Create user**:

1. User name: **`github-actions`**.
2. **Attach policies directly**, gắn 2 policy:

   | Policy | Mục đích |
   |--------|----------|
   | `AmazonEC2ContainerRegistryFullAccess` | Push/pull image lên ECR |
   | `AmazonEKSClusterPolicy` | EKS truy cập registry |

3. **Create user** -> tab **Security credentials -> Create access key -> CLI** -> **Download .csv**.

{{% notice warning %}}
**Không** commit access key vào Git. Chỉ lưu vào **GitHub Secrets**. Xong workshop hãy
deactivate/xoá key này.
{{% /notice %}}
