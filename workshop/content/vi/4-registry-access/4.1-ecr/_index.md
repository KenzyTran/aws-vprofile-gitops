---
title: "4.1 Tạo ECR repository"
date: 2025-01-01
weight: 1
---

## Tạo ECR repository

Vào **AWS Console -> ECR -> Create repository**:

- Đúng **region** (nên cùng region với SonarServer).
- Repository name: **`vprofileappimg`** (giữ đúng tên - pipeline tham chiếu theo tên này).
- Bấm **Create**.

Copy **URI** repository (`<account-id>.dkr.ecr.<region>.amazonaws.com/vprofileappimg`) để dùng sau.
