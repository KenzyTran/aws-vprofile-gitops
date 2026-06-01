---
title: "10.5 Truy cập ArgoCD"
date: 2025-01-01
weight: 5
---

## Truy cập ArgoCD

Lấy mật khẩu admin ban đầu:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Đăng nhập:

- **URL:** `https://argocd.<YourDomain>`
- **Username:** `admin`
- **Password:** kết quả lệnh trên

{{% notice tip %}}
Sau khi đăng nhập, đổi mật khẩu trong UI (User Info -> Update Password).
{{% /notice %}}
