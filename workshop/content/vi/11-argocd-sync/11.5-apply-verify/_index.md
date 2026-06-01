---
title: "11.5 Apply & xác minh"
date: 2025-01-01
weight: 5
---

## Apply và xác minh trên ArgoCD UI

Tạo **project trước, application sau**:

```bash
kubectl apply -f argocd/projects/vprofile-project.yaml
kubectl apply -f argocd/apps/vprofile-app.yaml
```

Vào ArgoCD UI:
- **Settings -> Projects**: thấy project `vprofile`.
- **Applications**: app `vprofile` **Progressing -> Healthy/Synced**, các resource được tạo
  (`db-pv-claim`, `app-secret`, deployment/service...).

{{% notice tip %}}
Nếu app báo Unknown, thường do sai path hoặc chưa commit/push manifest. Commit thư mục `argocd/` vào
repo `vprofile-helm`.
{{% /notice %}}
