---
title: "7.1 Commit pipeline"
date: 2025-01-01
weight: 1
---

## Commit pipeline vào feature branch

```bash
cd vprofile-app
git add .
git commit -m "Pipeline"
git push origin feature-X
```

{{% notice info %}}
Push lên feature branch **không** kích hoạt pipeline. Kiểm tra tab **Actions** - không có workflow chạy.
{{% /notice %}}
