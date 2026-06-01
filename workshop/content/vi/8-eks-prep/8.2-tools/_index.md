---
title: "8.2 Cài công cụ local"
date: 2025-01-01
weight: 2
---

## Cài công cụ trên máy local

Cần: `aws`, `terraform`, `kubectl`, `helm`, `eksctl`.

**Windows** (PowerShell as Administrator):

```powershell
choco install awscli terraform kubernetes-cli kubernetes-helm -y
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install eksctl
```

**macOS** (Homebrew):

```bash
brew install awscli terraform kubernetes-cli helm eksctl
```

Kiểm tra: `aws --version`, `terraform -version`, `kubectl version --client`, `helm version`,
`eksctl version`.
