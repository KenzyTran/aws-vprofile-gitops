---
title: "11.4 ArgoCD manifests"
date: 2025-01-01
weight: 4
---

## Create ArgoCD manifests in `vprofile-helm`

Open `vprofile-helm`, `git pull` first (to get the pipeline-updated `values.yaml`). Create folders:

```bash
cd vprofile-helm
mkdir -p argocd/projects argocd/apps
```

Create `argocd/projects/vprofile-project.yaml` (AppProject) and `argocd/apps/vprofile-app.yaml`
(Application) as on the Vietnamese page. Key fields for the Application: `project: vprofile`,
`repoURL` = your SSH URL, `path: helm/vprofile`, `valueFiles: [values.yaml]`, namespace `vprofile`,
`syncPolicy.automated` with `prune` + `selfHeal`, and `syncOptions` `CreateNamespace=true`.

{{% notice warning %}}
**Path fix:** AI often writes `path: helm/vprofile-chart`, but the chart lives at `helm/vprofile`.
This must match.
{{% /notice %}}
