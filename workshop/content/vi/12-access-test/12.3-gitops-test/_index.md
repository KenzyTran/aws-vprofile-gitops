---
title: "12.3 Kiểm thử GitOps"
date: 2025-01-01
weight: 3
---

## Kiểm thử luồng GitOps end-to-end

Chứng minh một commit code tự động chảy hết qua CI -> cập nhật helm -> ArgoCD tự deploy.

**Chuẩn bị:** lấy bản app repo mới nhất, bật SonarServer và cập nhật `SONAR_HOST_URL` nếu IP đổi,
ghi lại tag image hiện tại.

**Thực hiện:**

```bash
git add .
git commit -m "test pipeline"
git push origin feature-X        # push feature -> KHÔNG trigger
```

1. Raise **Pull Request** `feature-X -> main` -> chạy sonar + quality gate.
2. Quality gate pass -> **Merge** -> build/push image (tag SHA mới) + cập nhật `values.yaml`.
3. **ArgoCD tự đồng bộ** (auto-poll ~3 phút hoặc bấm **Sync**).
4. Quan sát rolling update: pod mới với tag mới -> Healthy -> xoá pod cũ.

{{% notice info %}}
**Vòng GitOps hoàn chỉnh:** code -> CI (scan/quality gate) -> build/push image (ECR) -> cập nhật
`values.yaml` (Git) -> ArgoCD đồng bộ Git -> cluster. **Git là nguồn chân lý duy nhất** - không
`kubectl apply` thủ công.
{{% /notice %}}
