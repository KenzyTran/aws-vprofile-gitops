---
title: "Introduction"
date: 2025-01-01
weight: 1
chapter: true
pre: "<b>1. </b>"
---

### Introduction

# Workshop Overview

vProfile is a multi-tier Java web app. This workshop builds a full GitOps pipeline for it.

| Component | Role | Image | Port |
|-----------|------|-------|------|
| `vproapp`     | App server (Tomcat running `vprofile-v2.war`) | `vprocontainers/vprofileapp` | 8080 |
| `vprodb`      | Database (MySQL)                              | `vprocontainers/vprofiledb`  | 3306 |
| `vprocache01` | Cache (Memcached)                             | `memcached`                  | 11211 |
| `vpromq01`    | Message broker (RabbitMQ)                     | `rabbitmq`                   | 5672 |

### Architecture

![vProfile GitOps architecture](/images/architecture.png)

GitOps loop: Admin pushes code → GitHub Actions (SonarQube scan, build & push image to ECR, update
`values.yaml`) → ArgoCD syncs the chart to EKS → users reach the app via ALB (HTTPS).

### Three-repo model

| Repo | Content |
|------|---------|
| `vprofile-app`   | Java source, Dockerfile, CI config (SonarQube, GitHub Actions) |
| `vprofile-helm`  | Helm chart + ArgoCD manifests |
| `vprofile-infra` | Terraform for EKS (VPC, node group, OIDC, EBS CSI Driver) |

### Objectives

- Generate a Helm chart from Kubernetes manifests using AI coding
- Build a GitHub Actions CI/CD pipeline (scan, build, push, update manifest)
- Provision EKS with Terraform, install AWS Load Balancer Controller and ArgoCD
- Deploy vProfile via GitOps and test the end-to-end flow

{{% children %}}
