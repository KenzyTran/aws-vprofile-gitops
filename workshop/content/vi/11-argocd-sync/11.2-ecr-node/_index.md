---
title: "11.2 Quyền ECR cho node"
date: 2025-01-01
weight: 2
---

## Cấp quyền ECR cho node group EKS

{{% notice info %}}
Repo Terraform mẫu đã gắn sẵn `AmazonEC2ContainerRegistryReadOnly` vào node role nên **không cần làm
thủ công**. Phần dưới để tham khảo khi node role chưa có policy đó.
{{% /notice %}}

```bash
aws eks list-nodegroups --cluster-name vprofile-eks-cluster --region us-east-1
aws eks describe-nodegroup --cluster-name vprofile-eks-cluster \
  --nodegroup-name <ng-name> --region us-east-1 --query "nodegroup.nodeRole" --output text
aws iam attach-role-policy --role-name <node-role> \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
```
