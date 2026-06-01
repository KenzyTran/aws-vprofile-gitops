---
title: "10.3 Ingress for ArgoCD"
date: 2025-01-01
weight: 3
---

## Create an Ingress for ArgoCD

Get the ACM certificate ARN:

```bash
aws acm list-certificates --region us-east-1 \
  --query "CertificateSummaryList[*].{Domain:DomainName, ARN:CertificateArn}" --output table
```

Create `argocd-ingress.yaml` (replace `<YourCertificate-ARN>` and `<YourDomain>`) with the same ALB
annotations as the Vietnamese page (`backend-protocol: HTTPS`, port `443`). Apply and watch the ALB
DNS:

```bash
kubectl apply -f argocd-ingress.yaml
kubectl get ingress argocd-ingress -n argocd -w
```
