---
title: "11.4 ArgoCD manifests"
date: 2025-01-01
weight: 4
---

## Tạo ArgoCD manifests trong repo `vprofile-helm`

Mở `vprofile-helm`, `git pull` trước (lấy `values.yaml` pipeline đã cập nhật). Tạo thư mục:

```bash
cd vprofile-helm
mkdir -p argocd/projects argocd/apps
```

**`argocd/projects/vprofile-project.yaml`** (AppProject - đặt ranh giới):

```yaml
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: vprofile
  namespace: argocd
spec:
  description: vProfile application project
  sourceRepos:
    - git@github.com:<YourGithubAccount>/vprofile-helm.git
  destinations:
    - namespace: vprofile
      server: https://kubernetes.default.svc
  clusterResourceWhitelist:
    - group: ""
      kind: Namespace
  namespaceResourceWhitelist:
    - group: "*"
      kind: "*"
```

**`argocd/apps/vprofile-app.yaml`** (Application):

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: vprofile
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: vprofile
  source:
    repoURL: git@github.com:<YourGithubAccount>/vprofile-helm.git
    targetRevision: main
    path: helm/vprofile          # ĐÚNG path là helm/vprofile (KHÔNG phải helm/vprofile-chart)
    helm:
      valueFiles:
        - values.yaml
  destination:
    server: https://kubernetes.default.svc
    namespace: vprofile
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
      - ServerSideApply=true
```

{{% notice warning %}}
**Sửa lỗi path:** AI hay ghi `path: helm/vprofile-chart`, nhưng chart nằm ở `helm/vprofile`. Phải
khớp đúng path này.
{{% /notice %}}

`syncPolicy`: `prune` xoá resource khỏi cluster nếu xoá khỏi repo; `selfHeal` đưa cluster về đúng
trạng thái repo; `CreateNamespace` tự tạo namespace `vprofile`.
