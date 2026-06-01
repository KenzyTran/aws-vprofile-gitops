---
title: "11.5 Apply & verify"
date: 2025-01-01
weight: 5
---

## Apply and verify in the ArgoCD UI

Create the **project first, then the application**:

```bash
kubectl apply -f argocd/projects/vprofile-project.yaml
kubectl apply -f argocd/apps/vprofile-app.yaml
```

In the ArgoCD UI:
- **Settings -> Projects**: see the `vprofile` project.
- **Applications**: app `vprofile` goes **Progressing -> Healthy/Synced**; resources are created
  (`db-pv-claim`, `app-secret`, deployments/services...).

{{% notice tip %}}
If the app shows Unknown, it's usually a wrong path or unpushed manifests. Commit the `argocd/`
folder to `vprofile-helm`.
{{% /notice %}}
