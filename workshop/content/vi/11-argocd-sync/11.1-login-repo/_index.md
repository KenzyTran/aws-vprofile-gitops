---
title: "11.1 Login & thêm Git repo"
date: 2025-01-01
weight: 1
---

## Đăng nhập ArgoCD CLI và thêm Git repo

```bash
argocd login argocd.<YourDomain> --username admin
argocd repo add git@github.com:<YourGithubAccount>/vprofile-helm.git \
  --ssh-private-key-path ~/.ssh/<Keyname>
```

{{% notice tip %}}
Lỗi lần đầu thì thử lại. Có thể thêm repo qua UI: Settings -> Repositories -> Connect repo, dán
private key.
{{% /notice %}}
