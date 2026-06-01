---
title: "9.4 EBS CSI Driver"
date: 2025-01-01
weight: 4
---

## Thêm EBS CSI Driver (IRSA)

DB dùng PVC `storageClass: gp2` nên cần **EBS CSI Driver** để EKS tạo EBS volume. Prompt bổ sung:

```text
Add EBS CSI Driver IRSA to EKS cluster in Terraform:
1. Associate OIDC provider with EKS cluster
2. Create IAM role "AmazonEKS_EBS_CSI_DriverRole" with OIDC trust relationship
3. Attach policy "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
4. Enable the aws-ebs-csi-driver addon with the service account role ARN
5. Do NOT create a Kubernetes service account - AWS addon will create it.
```

Apply lại:

```bash
terraform init -upgrade
terraform plan
terraform apply       # gõ "yes"
```

{{% notice info %}}
IRSA = IAM Roles for Service Accounts: gắn IAM role vào service account của addon qua OIDC. Trong
repo mẫu, phần này nằm sẵn trong `main.tf` nên chỉ cần `terraform apply` một lần.
{{% /notice %}}
