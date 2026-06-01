---
title: "vProfile GitOps Workshop"
date: 2025-01-01
weight: 0
---

# vProfile GitOps Workshop

### Introduction

This workshop walks through deploying the multi-tier **vProfile** web application to **AWS EKS**
using a **GitOps** model. CI runs on **GitHub Actions** (SonarQube code-quality analysis, Docker
build & push to ECR); CD runs on **ArgoCD**, which automatically syncs the Helm chart to the cluster.

| Info | Details |
|------|---------|
| Duration | ~4-6 hours |
| Level | Intermediate / Advanced |
| Cost | Incurs charges (EKS, EC2, ALB) - clean up afterwards |

### Requirements

- AWS account, GitHub account
- A domain + ACM certificate (for HTTPS)
- Basic knowledge of Docker, Kubernetes, Git

### Content

{{% children depth="1" %}}
