---
title: "5.1 Create GitHub PAT"
date: 2025-01-01
weight: 1
---

## Create a GitHub PAT (Personal Access Token)

{{% notice info %}}
Create the PAT in the **account that owns the `vprofile-helm` repo**.
{{% /notice %}}

1. **GitHub -> Settings -> Developer settings -> Personal access tokens -> Tokens (classic)**.
2. **Generate new token (classic)**.
3. Note: `gitops-pipeline`; Expiration: 30 days; Scope: check **`repo`**.

   ![Create PAT classic with repo scope](/images/github-pat-classic.png)

4. **Generate token** -> **copy and save the PAT**.
5. Note your **GitHub username**.
