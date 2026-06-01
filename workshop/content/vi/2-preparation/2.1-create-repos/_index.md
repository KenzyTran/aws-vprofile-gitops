---
title: "2.1 Tạo 3 repo GitHub"
date: 2025-01-01
weight: 1
---

## Tạo 3 repo trên GitHub

Tạo 3 repo: `vprofile-app`, `vprofile-helm`, `vprofile-infra`. Clone về chung một thư mục làm việc:

```bash
git clone https://github.com/<username>/vprofile-app.git
git clone https://github.com/<username>/vprofile-helm.git
git clone https://github.com/<username>/vprofile-infra.git
```

{{% notice info %}}
`vprofile-app` chứa sẵn source + Dockerfile, `vprofile-helm` chứa sẵn thư mục `kubedefs/` (manifest
gốc). `vprofile-infra` ban đầu để trống.
{{% /notice %}}
