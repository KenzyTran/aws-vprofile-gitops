---
title: "11.3 Commit Terraform"
date: 2025-01-01
weight: 3
---

## Commit Terraform code lên `vprofile-infra`

Dùng AI sinh `.gitignore` (bỏ `.terraform/`, file log) và `README.md`, rồi:

```bash
cd vprofile-infra
git add .
git commit -m "terraform code"
git push origin main
```
