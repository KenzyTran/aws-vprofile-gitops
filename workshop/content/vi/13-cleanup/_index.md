---
title: "Dọn dẹp"
date: 2025-01-01
weight: 13
chapter: true
pre: "<b>13. </b>"
---

### Dọn dẹp

# Dọn dẹp tài nguyên

Để tránh phát sinh chi phí AWS, xoá tài nguyên theo thứ tự ngược lại sau khi xong.

### Các bước dọn dẹp

1. Xoá Ingress của app và ArgoCD (`kubectl delete ingress ...`) để ALB được giải phóng trước.
2. `terraform destroy` trong `vprofile-infra` (xoá EKS cluster, VPC, node group).
3. Xoá ALB còn sót (nếu có), xoá **ECR repo** nếu không dùng.
4. **Terminate** SonarServer EC2 và xoá security group `sonar-sg`.
5. **Xoá/deactivate** các IAM access key (`github-actions`, `terraform-admin`) và **GitHub PAT**.
6. Xoá bản ghi DNS (CNAME `vprofile`, `argocd`) nếu không còn dùng.

{{% notice warning %}}
Đảm bảo đã xoá hết tài nguyên (đặc biệt EKS, EC2, ALB, EBS) để tránh bị tính tiền ngoài ý muốn.
{{% /notice %}}
