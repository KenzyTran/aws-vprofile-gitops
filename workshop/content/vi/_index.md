---
title: "vProfile GitOps Workshop"
date: 2025-01-01
weight: 0
---

# vProfile GitOps Workshop

### Giới thiệu

Workshop hướng dẫn triển khai ứng dụng web multi-tier **vProfile** lên **AWS EKS** theo mô hình
**GitOps**. Pipeline CI bằng **GitHub Actions** (phân tích chất lượng code với SonarQube, build &
push Docker image lên ECR), pipeline CD bằng **ArgoCD** tự đồng bộ Helm chart xuống cluster.

| Thông tin | Chi tiết |
|-----------|----------|
| Thời gian | ~4-6 giờ |
| Cấp độ | Intermediate / Advanced |
| Chi phí | Có phát sinh (EKS, EC2, ALB) - nhớ dọn dẹp sau khi xong |

### Yêu cầu

- Tài khoản AWS, tài khoản GitHub
- Một domain + chứng chỉ ACM (cho HTTPS)
- Kiến thức cơ bản về Docker, Kubernetes, Git

### Nội dung

{{% children depth="1" %}}
