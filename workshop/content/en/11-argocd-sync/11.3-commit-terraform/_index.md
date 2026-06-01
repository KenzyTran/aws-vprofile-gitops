---
title: "11.3 Commit Terraform"
date: 2025-01-01
weight: 3
---

## Commit Terraform code to `vprofile-infra`

Use AI to generate `.gitignore` (excluding `.terraform/`, log files) and `README.md`, then:

```bash
cd vprofile-infra
git add .
git commit -m "terraform code"
git push origin main
```
