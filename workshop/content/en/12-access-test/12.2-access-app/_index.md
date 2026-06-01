---
title: "12.2 Access the app"
date: 2025-01-01
weight: 2
---

## Access the app and verify the tiers

Open `https://vprofile.<YourDomain>`, log in with `admin_vp` / `admin_vp`:

| Tier | How to check | Confirms |
|------|--------------|----------|
| **DB (MySQL)** | Login works | DB pod + PVC OK |
| **RabbitMQ** | Open the RabbitMQ page | Message broker OK |
| **Memcached** | All users -> pick a user (cached on 2nd load) | Cache OK |

{{% notice info %}}
vProfile was deployed by ArgoCD from the Helm chart in the repo to EKS, accessed over HTTPS. The
cluster state equals what is declared in Git.
{{% /notice %}}
