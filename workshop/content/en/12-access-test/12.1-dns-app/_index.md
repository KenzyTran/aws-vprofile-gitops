---
title: "12.1 DNS for the app"
date: 2025-01-01
weight: 1
---

## Get the Ingress endpoint and point DNS

```bash
kubectl get ingress -n vprofile
```

Add a CNAME pointing `vprofile.<domain>` to the ALB:

| Type | Name | Value |
|------|------|-------|
| CNAME | `vprofile` | `<ALB-DNS-endpoint>` |

Wait ~5-10 minutes for DNS to publish.
