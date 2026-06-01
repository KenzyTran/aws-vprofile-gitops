---
title: "2.1 Create 3 GitHub repos"
date: 2025-01-01
weight: 1
---

## Create the three GitHub repos

Create `vprofile-app`, `vprofile-helm`, `vprofile-infra`. Clone them into one working folder:

```bash
git clone https://github.com/<username>/vprofile-app.git
git clone https://github.com/<username>/vprofile-helm.git
git clone https://github.com/<username>/vprofile-infra.git
```

{{% notice info %}}
`vprofile-app` already contains the source + Dockerfiles, `vprofile-helm` already contains the
`kubedefs/` folder (original manifests). `vprofile-infra` starts empty.
{{% /notice %}}
