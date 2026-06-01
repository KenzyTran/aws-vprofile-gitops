---
title: "5.1 Tạo GitHub PAT"
date: 2025-01-01
weight: 1
---

## Tạo GitHub PAT (Personal Access Token)

{{% notice info %}}
Tạo PAT trong **tài khoản sở hữu repo `vprofile-helm`**.
{{% /notice %}}

1. **GitHub -> Settings -> Developer settings -> Personal access tokens -> Tokens (classic)**.
2. **Generate new token (classic)**.
3. Note: `gitops-pipeline`; Expiration: 30 days; Scope: tick **`repo`**.

   ![Tạo PAT classic scope repo](/images/github-pat-classic.png)

4. **Generate token** -> **copy và lưu lại PAT**.
5. Ghi lại **GitHub username** của bạn.
