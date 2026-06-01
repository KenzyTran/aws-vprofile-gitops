---
title: "4.1 Create ECR repository"
date: 2025-01-01
weight: 1
---

## Create an ECR repository

Go to **AWS Console -> ECR -> Create repository**:

- Correct **region** (ideally same as SonarServer).
- Repository name: **`vprofileappimg`** (keep this name - the pipeline references it).
- Click **Create**.

Copy the repository **URI** (`<account-id>.dkr.ecr.<region>.amazonaws.com/vprofileappimg`) for later.
