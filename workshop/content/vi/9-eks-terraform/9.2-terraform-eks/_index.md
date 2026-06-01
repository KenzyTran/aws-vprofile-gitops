---
title: "9.2 Sinh Terraform EKS"
date: 2025-01-01
weight: 2
---

## Sinh Terraform code cho EKS

Dùng prompt sau để sinh 4 file (`main.tf`, `variables.tf`, `outputs.tf`, `backend.tf`):

```text
Create minimal Terraform configuration for AWS EKS cluster with these requirements:

Files: main.tf (VPC, subnets, IAM roles, EKS cluster, node group), variables.tf, outputs.tf,
backend.tf (S3 backend without dynamodb locking).

Specifications:
- Region: us-east-1
- Cluster name: vprofile-eks-cluster
- VPC: 10.0.0.0/16 with ONLY public subnets across 2 AZs
- Node group: 1 t3.large instance (min=1, max=2, desired=1) in public subnets
- Minimal resources for cost optimization - NO private subnets, NO NAT gateways
- Include proper EKS subnet tags for load balancer integration
- Outputs: cluster_endpoint, cluster_name, cluster_arn
- Ensure code is formatted with terraform fmt. Keep it minimal.
```

{{% notice info %}}
Backend S3 cần **bucket có sẵn**. Tạo trước, ví dụ:
```bash
aws s3 mb s3://gitops-terraformcode-2026 --region us-east-1
```
Tên bucket là duy nhất toàn cầu - đặt tên của bạn và sửa trong `backend.tf`.
{{% /notice %}}

Thiết kế tối giản: chỉ public subnet (2 AZ), không NAT; node `t3.large` (min1/desired1/max2); S3
backend không DynamoDB; subnet có tag cho ALB.
