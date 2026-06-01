---
title: "9.3 Review & apply"
date: 2025-01-01
weight: 3
---

## Review và apply Terraform

Review 4 file rồi chạy:

```bash
terraform init
terraform plan
terraform apply       # gõ "yes"
```

{{% notice warning %}}
Dựng EKS mất khoảng **15-20 phút**.
{{% /notice %}}

Sau khi xong, kết nối kubectl:

```bash
aws eks update-kubeconfig --name vprofile-eks-cluster --region us-east-1
kubectl get nodes
```
