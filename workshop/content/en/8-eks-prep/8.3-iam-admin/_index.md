---
title: "8.3 Administrator IAM user"
date: 2025-01-01
weight: 3
---

## Create an Administrator IAM user (for Terraform)

Go to **IAM -> Users -> Create user**:

1. User name: `terraform-admin`.
2. **Attach policies directly** -> **`AdministratorAccess`** -> **Create user**.
3. **Security credentials -> Create access key -> CLI** -> **download** the access + secret keys.

{{% notice warning %}}
This key has **admin** rights - keep it local, **never** commit it. **Delete the key/user right
after the workshop.**
{{% /notice %}}
