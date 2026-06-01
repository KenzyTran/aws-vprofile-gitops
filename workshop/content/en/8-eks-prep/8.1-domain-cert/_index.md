---
title: "8.1 Domain & certificate"
date: 2025-01-01
weight: 1
---

## Domain and public certificate (ACM)

To reach vProfile and ArgoCD over **HTTPS** you need:

- A **domain** (GoDaddy or another provider).
- A **public certificate** in **AWS Certificate Manager (ACM)** for that domain (free).

{{% notice info %}}
This cert ARN is used in `ingress.yaml` (section 2.3). Without a domain you can still follow along
but won't get clean HTTPS URLs.
{{% /notice %}}
