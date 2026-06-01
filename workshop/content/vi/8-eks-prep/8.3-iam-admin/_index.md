---
title: "8.3 IAM user Administrator"
date: 2025-01-01
weight: 3
---

## Tạo IAM user quyền Administrator (cho Terraform)

Vào **IAM -> Users -> Create user**:

1. User name: `terraform-admin`.
2. **Attach policies directly** -> **`AdministratorAccess`** -> **Create user**.
3. **Security credentials -> Create access key -> CLI** -> **download** access key + secret key.

{{% notice warning %}}
Key này có **quyền admin** - chỉ lưu trên máy bạn, **không** commit Git. **Xoá key/user ngay khi
xong workshop.**
{{% /notice %}}
