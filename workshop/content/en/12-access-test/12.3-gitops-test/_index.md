---
title: "12.3 Test the GitOps loop"
date: 2025-01-01
weight: 3
---

## Test the end-to-end GitOps loop

Prove that a code commit flows all the way through CI -> helm update -> automatic ArgoCD deploy.

**Prepare:** get the latest app repo, start SonarServer and update `SONAR_HOST_URL` if the IP
changed, note the current image tag.

**Run:**

```bash
git add .
git commit -m "test pipeline"
git push origin feature-X        # feature push -> NOT triggered
```

1. Raise a **Pull Request** `feature-X -> main` -> runs sonar + quality gate.
2. Quality gate passes -> **Merge** -> build/push image (new SHA tag) + update `values.yaml`.
3. **ArgoCD auto-syncs** (auto-poll ~3 min or click **Sync**).
4. Watch the rolling update: new pod with the new tag -> Healthy -> old pod removed.

{{% notice info %}}
**Complete GitOps loop:** code -> CI (scan/quality gate) -> build/push image (ECR) -> update
`values.yaml` (Git) -> ArgoCD syncs Git -> cluster. **Git is the single source of truth** - no
manual `kubectl apply`.
{{% /notice %}}
