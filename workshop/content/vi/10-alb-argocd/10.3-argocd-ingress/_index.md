---
title: "10.3 Ingress cho ArgoCD"
date: 2025-01-01
weight: 3
---

## Tạo Ingress cho ArgoCD

Lấy ACM certificate ARN:

```bash
aws acm list-certificates --region us-east-1 \
  --query "CertificateSummaryList[*].{Domain:DomainName, ARN:CertificateArn}" --output table
```

Tạo `argocd-ingress.yaml` (thay `<YourCertificate-ARN>` và `<YourDomain>`):

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: argocd-ingress
  namespace: argocd
  annotations:
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/certificate-arn: <YourCertificate-ARN>
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80},{"HTTPS":443}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443'
    alb.ingress.kubernetes.io/backend-protocol: HTTPS
spec:
  rules:
  - host: argocd.<YourDomain>
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: argocd-server
            port:
              number: 443
```

Apply và lấy DNS của ALB:

```bash
kubectl apply -f argocd-ingress.yaml
kubectl get ingress argocd-ingress -n argocd -w
```
