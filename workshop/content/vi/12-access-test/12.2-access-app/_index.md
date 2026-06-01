---
title: "12.2 Truy cập app"
date: 2025-01-01
weight: 2
---

## Truy cập app và xác minh các tier

Mở `https://vprofile.<YourDomain>`, đăng nhập `admin_vp` / `admin_vp`:

| Tier | Cách kiểm tra | Xác nhận |
|------|---------------|----------|
| **DB (MySQL)** | Đăng nhập được | DB pod + PVC hoạt động |
| **RabbitMQ** | Mở trang RabbitMQ | Message broker hoạt động |
| **Memcached** | All users -> chọn 1 user (lần 2 lấy từ cache) | Cache hoạt động |

{{% notice info %}}
vProfile đã được ArgoCD triển khai từ Helm chart trong repo xuống EKS, truy cập qua HTTPS. Trạng
thái cluster = trạng thái khai báo trong Git.
{{% /notice %}}
