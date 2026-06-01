---
title: "Giới thiệu"
date: 2025-01-01
weight: 1
chapter: true
pre: "<b>1. </b>"
---

### Giới thiệu

# Tổng quan Workshop

vProfile là ứng dụng web Java gồm nhiều tầng (tier). Workshop dựng trọn quy trình GitOps cho nó.

| Thành phần | Vai trò | Image | Port |
|------------|---------|-------|------|
| `vproapp`     | App server (Tomcat chạy `vprofile-v2.war`) | `vprocontainers/vprofileapp` | 8080 |
| `vprodb`      | Database (MySQL)                            | `vprocontainers/vprofiledb`  | 3306 |
| `vprocache01` | Cache (Memcached)                           | `memcached`                  | 11211 |
| `vpromq01`    | Message broker (RabbitMQ)                   | `rabbitmq`                   | 5672 |

### Kiến trúc

![Kiến trúc GitOps vProfile](/images/architecture.png)

Vòng GitOps: Admin push code → GitHub Actions (SonarQube scan, build & push image lên ECR, cập nhật
`values.yaml`) → ArgoCD đồng bộ chart xuống EKS → người dùng truy cập app qua ALB (HTTPS).

### Mô hình 3 repo

| Repo | Nội dung |
|------|----------|
| `vprofile-app`   | Source code Java, Dockerfile, cấu hình CI (SonarQube, GitHub Actions) |
| `vprofile-helm`  | Helm chart + manifest ArgoCD |
| `vprofile-infra` | Terraform dựng EKS (VPC, node group, OIDC, EBS CSI Driver) |

### Mục tiêu

- Sinh Helm chart từ manifest Kubernetes bằng AI coding
- Dựng pipeline CI/CD GitHub Actions (scan, build, push, cập nhật manifest)
- Dùng Terraform dựng EKS, cài AWS Load Balancer Controller và ArgoCD
- Triển khai vProfile theo GitOps và kiểm thử luồng end-to-end

{{% children %}}
