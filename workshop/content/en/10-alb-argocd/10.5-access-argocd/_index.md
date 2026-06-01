---
title: "10.5 Access ArgoCD"
date: 2025-01-01
weight: 5
---

## Access ArgoCD

Get the initial admin password:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Log in:

- **URL:** `https://argocd.<YourDomain>`
- **Username:** `admin`
- **Password:** output of the command above

{{% notice tip %}}
After logging in, change the password in the UI (User Info -> Update Password).
{{% /notice %}}
