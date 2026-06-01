---
title: "7.1 Commit the pipeline"
date: 2025-01-01
weight: 1
---

## Commit the pipeline to the feature branch

```bash
cd vprofile-app
git add .
git commit -m "Pipeline"
git push origin feature-X
```

{{% notice info %}}
Pushing to a feature branch does **not** trigger the pipeline. Check the **Actions** tab - nothing runs.
{{% /notice %}}
