---
title: "9.3 Review & apply"
date: 2025-01-01
weight: 3
---

## Review and apply Terraform

Review the four files, then run:

```bash
terraform init
terraform plan
terraform apply       # type "yes"
```

{{% notice warning %}}
Provisioning EKS takes about **15-20 minutes**.
{{% /notice %}}

Then connect kubectl:

```bash
aws eks update-kubeconfig --name vprofile-eks-cluster --region us-east-1
kubectl get nodes
```
