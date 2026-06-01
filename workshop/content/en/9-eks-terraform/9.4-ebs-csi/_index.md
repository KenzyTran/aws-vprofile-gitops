---
title: "9.4 EBS CSI Driver"
date: 2025-01-01
weight: 4
---

## Add the EBS CSI Driver (IRSA)

The DB uses a `storageClass: gp2` PVC, so the **EBS CSI Driver** is needed for EKS to create EBS
volumes. Supplemental prompt:

```text
Add EBS CSI Driver IRSA to EKS cluster in Terraform:
1. Associate OIDC provider with EKS cluster
2. Create IAM role "AmazonEKS_EBS_CSI_DriverRole" with OIDC trust relationship
3. Attach policy "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
4. Enable the aws-ebs-csi-driver addon with the service account role ARN
5. Do NOT create a Kubernetes service account - AWS addon will create it.
```

Re-apply:

```bash
terraform init -upgrade
terraform plan
terraform apply       # type "yes"
```

{{% notice info %}}
IRSA = IAM Roles for Service Accounts: binds an IAM role to the addon's service account via OIDC. In
the sample repo this is already in `main.tf`, so a single `terraform apply` is enough.
{{% /notice %}}
