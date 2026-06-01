---
title: "Clean Up"
date: 2025-01-01
weight: 13
chapter: true
pre: "<b>13. </b>"
---

### Clean Up

# Clean up resources

To avoid AWS charges, delete resources in reverse order after finishing.

### Clean-up steps

1. Delete the app and ArgoCD Ingress (`kubectl delete ingress ...`) so the ALB is freed first.
2. `terraform destroy` in `vprofile-infra` (deletes the EKS cluster, VPC, node group).
3. Delete any leftover ALB, delete the **ECR repo** if unused.
4. **Terminate** the SonarServer EC2 and delete the `sonar-sg` security group.
5. **Delete/deactivate** the IAM access keys (`github-actions`, `terraform-admin`) and **GitHub PAT**.
6. Remove the DNS records (CNAME `vprofile`, `argocd`) if no longer needed.

{{% notice warning %}}
Make sure all resources are deleted (especially EKS, EC2, ALB, EBS) to avoid unexpected charges.
{{% /notice %}}
