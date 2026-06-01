---
title: "11.1 Login & add Git repo"
date: 2025-01-01
weight: 1
---

## Log in to ArgoCD CLI and add the Git repo

```bash
argocd login argocd.<YourDomain> --username admin
argocd repo add git@github.com:<YourGithubAccount>/vprofile-helm.git \
  --ssh-private-key-path ~/.ssh/<Keyname>
```

{{% notice tip %}}
If it errors the first time, retry. You can also add the repo in the UI: Settings -> Repositories ->
Connect repo, paste the private key.
{{% /notice %}}
