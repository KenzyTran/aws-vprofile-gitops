---
title: "6.3 Review the pipeline"
date: 2025-01-01
weight: 3
---

## Review and clean up the generated pipeline

| Common issue | Fix |
|--------------|-----|
| Added `role-to-assume` / OIDC | Remove - use access key + secret key only |
| Missing Slack notification | Add a step sending `SLACK_WEBHOOK` |
| Re-declares existing variables | Use `${{ vars.* }}` directly |
| Verbose Checkstyle command | Simplify to `mvn verify checkstyle:checkstyle -B` |
| "create ECR if needed" step | Not needed (created in 4.1) |
| `yq` updates incorrectly | Update by key path `app.image`/`app.tag` |
| Missing `SONAR_HOST_URL` | Ensure it exists (5.3) |
