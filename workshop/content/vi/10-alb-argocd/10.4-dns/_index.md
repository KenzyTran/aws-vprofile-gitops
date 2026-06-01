---
title: "10.4 Cấu hình DNS"
date: 2025-01-01
weight: 4
---

## Cấu hình DNS (GoDaddy)

Thêm bản ghi **CNAME** trỏ `argocd.<domain>` về ALB:

| Type | Name | Value |
|------|------|-------|
| CNAME | `argocd` | `<ALB-DNS-endpoint>` (từ bước 10.3) |
