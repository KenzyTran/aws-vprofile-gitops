---
title: "10.4 Configure DNS"
date: 2025-01-01
weight: 4
---

## Configure DNS (GoDaddy)

Add a **CNAME** record pointing `argocd.<domain>` to the ALB:

| Type | Name | Value |
|------|------|-------|
| CNAME | `argocd` | `<ALB-DNS-endpoint>` (from step 10.3) |
