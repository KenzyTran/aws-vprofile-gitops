---
title: "10.2 Install ArgoCD"
date: 2025-01-01
weight: 2
---

## Install ArgoCD

```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm upgrade argocd argo/argo-cd --version 9.5.2 --install --create-namespace -n argocd
kubectl rollout status deployment argocd-server -n argocd
```
