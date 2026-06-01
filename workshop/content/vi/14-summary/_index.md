---
title: "Tổng kết"
date: 2025-01-01
weight: 14
chapter: true
pre: "<b>14. </b>"
---

### Tổng kết

# Tổng kết Workshop

Chúc mừng bạn đã hoàn thành workshop! Bạn đã dựng trọn một pipeline GitOps CI/CD cho ứng dụng
multi-tier vProfile.

### Bạn đã học được

- Sinh Helm chart từ manifest Kubernetes bằng AI coding.
- Dựng SonarQube server và tích hợp quality gate vào pipeline.
- Xây pipeline CI/CD GitHub Actions: scan -> build/push image (ECR) -> cập nhật `values.yaml`.
- Dùng Terraform dựng EKS (public subnet, EBS CSI Driver) và OIDC/IRSA.
- Cài AWS Load Balancer Controller và ArgoCD, expose qua HTTPS.
- Triển khai ứng dụng theo GitOps với ArgoCD và kiểm thử luồng end-to-end.

### Vòng GitOps

code -> CI (Sonar/quality gate) -> build image (ECR) -> cập nhật `values.yaml` (Git) -> ArgoCD đồng
bộ Git -> EKS. **Git là nguồn chân lý duy nhất.**

### Tham khảo

- [AWS Documentation](https://docs.aws.amazon.com/)
- [ArgoCD Documentation](https://argo-cd.readthedocs.io/)
- [AWS Load Balancer Controller](https://kubernetes-sigs.github.io/aws-load-balancer-controller/)
- [First Cloud Journey](https://cloudjourney.awsstudygroup.com/)
