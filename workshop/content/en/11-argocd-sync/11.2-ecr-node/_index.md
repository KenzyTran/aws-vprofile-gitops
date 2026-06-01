---
title: "11.2 ECR access for nodes"
date: 2025-01-01
weight: 2
---

## Grant ECR access to the EKS node group

{{% notice info %}}
The sample Terraform already attaches `AmazonEC2ContainerRegistryReadOnly` to the node role, so this
is **not needed manually**. Below is for reference if your node role lacks the policy.
{{% /notice %}}

```bash
aws eks list-nodegroups --cluster-name vprofile-eks-cluster --region us-east-1
aws eks describe-nodegroup --cluster-name vprofile-eks-cluster \
  --nodegroup-name <ng-name> --region us-east-1 --query "nodegroup.nodeRole" --output text
aws iam attach-role-policy --role-name <node-role> \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
```
