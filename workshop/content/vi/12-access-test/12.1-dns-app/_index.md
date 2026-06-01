---
title: "12.1 DNS cho app"
date: 2025-01-01
weight: 1
---

## Lấy endpoint Ingress và trỏ DNS

```bash
kubectl get ingress -n vprofile
```

Thêm CNAME trong DNS trỏ `vprofile.<domain>` về ALB:

| Type | Name | Value |
|------|------|-------|
| CNAME | `vprofile` | `<ALB-DNS-endpoint>` |

Chờ ~5-10 phút cho DNS publish.
