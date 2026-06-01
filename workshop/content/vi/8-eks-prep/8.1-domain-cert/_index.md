---
title: "8.1 Domain & certificate"
date: 2025-01-01
weight: 1
---

## Domain và public certificate (ACM)

Để truy cập vProfile và ArgoCD qua **HTTPS**, cần:

- Một **domain** (GoDaddy hoặc nhà cung cấp khác).
- Một **public certificate** trong **AWS Certificate Manager (ACM)** cho domain đó (miễn phí).

{{% notice info %}}
Cert ARN này được dùng trong `ingress.yaml` (mục 2.3). Nếu không có domain bạn vẫn theo dõi được
nhưng sẽ không có URL HTTPS đẹp.
{{% /notice %}}
