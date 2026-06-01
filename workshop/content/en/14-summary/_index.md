---
title: "Summary"
date: 2025-01-01
weight: 14
chapter: true
pre: "<b>14. </b>"
---

### Summary

# Workshop Summary

Congratulations on completing the workshop! You built a full GitOps CI/CD pipeline for the
multi-tier vProfile application.

### What you learned

- Generated a Helm chart from Kubernetes manifests using AI coding.
- Stood up a SonarQube server and integrated a quality gate into the pipeline.
- Built a GitHub Actions CI/CD pipeline: scan -> build/push image (ECR) -> update `values.yaml`.
- Used Terraform to provision EKS (public subnets, EBS CSI Driver) and OIDC/IRSA.
- Installed the AWS Load Balancer Controller and ArgoCD, exposed over HTTPS.
- Deployed the app via GitOps with ArgoCD and tested the end-to-end loop.

### GitOps loop

code -> CI (Sonar/quality gate) -> build image (ECR) -> update `values.yaml` (Git) -> ArgoCD syncs
Git -> EKS. **Git is the single source of truth.**

### References

- [AWS Documentation](https://docs.aws.amazon.com/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/)
- [First Cloud Journey](https://cloudjourney.awsstudygroup.com/)
