---
title: "2.3 Tùy chỉnh values & ingress"
date: 2025-01-01
weight: 3
---

## Thay giá trị riêng của bạn

1. **Ingress host** trong `helm/vprofile/values.yaml`:

   ```yaml
   ingress:
     enabled: true
     host: vprofile.<domain-cua-ban>
     servicePort: 8080
   ```

2. **Certificate ARN** trong `helm/vprofile/templates/ingress.yaml`:

   ```yaml
   alb.ingress.kubernetes.io/certificate-arn: arn:aws:acm:<region>:<account-id>:certificate/<id>
   ```

3. (Tuỳ chọn) Đổi mật khẩu base64 trong `secrets`: `echo -n 'pass' | base64`.

Kiểm tra nhanh:

```bash
helm lint helm/vprofile
helm template vprofile helm/vprofile
```

{{% notice tip %}}
Commit và push các thay đổi của `vprofile-helm` sau khi chỉnh.
{{% /notice %}}
