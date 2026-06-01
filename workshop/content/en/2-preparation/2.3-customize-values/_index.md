---
title: "2.3 Customize values & ingress"
date: 2025-01-01
weight: 3
---

## Set your own values

1. **Ingress host** in `helm/vprofile/values.yaml`:

   ```yaml
   ingress:
     enabled: true
     host: vprofile.<your-domain>
     servicePort: 8080
   ```

2. **Certificate ARN** in `helm/vprofile/templates/ingress.yaml`:

   ```yaml
   alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<region>:<account-id>:certificate/<id>
   ```

3. (Optional) Change the base64 passwords in `secrets`: `echo -n 'pass' | base64`.

Quick check:

```bash
helm lint helm/vprofile
helm template vprofile helm/vprofile
```

{{% notice tip %}}
Commit and push the `vprofile-helm` changes after editing.
{{% /notice %}}
