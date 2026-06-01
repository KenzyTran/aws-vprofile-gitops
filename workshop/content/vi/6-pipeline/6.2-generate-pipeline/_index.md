---
title: "6.2 Sinh pipeline bằng AI"
date: 2025-01-01
weight: 2
---

## Sinh pipeline bằng AI coding

Dùng prompt sau cho Copilot/AI để sinh `.github/workflows/ci.yml`:

```text
I have a Java Spring MVC application built with Maven. I need a GitHub Actions
CI/CD pipeline with the following exact flow:

1. feature branch push -> no pipeline runs
2. PR to main -> run: Maven build, unit tests, Checkstyle, SonarQube scan,
   SonarQube quality gate check. Block merge if quality gate fails.
3. merge to main -> build Docker image, push to Amazon ECR with commit SHA and latest as
   tag, then update the image and SHA tag fields in a Helm values.yaml file in a
   separate Helm GitHub repo.

Details:
- Java 21, Maven, Tomcat, WAR packaging
- SonarQube is self-hosted on EC2 (not SonarCloud), use
  sonarsource/sonarqube-scan-action@v2 and
  sonarsource/sonarqube-quality-gate-action@v1.1.0
  Use existing sonar-project.properties for sonar settings.
- Add Maven and SonarQube dependency caching to speed up PR builds
- Dockerfile is at Docker-files/app/multistage/Dockerfile
- ECR repository name: vprofileappimg, region: us-east-1
- Helm repo name: vprofile-helm, values file path: helm/vprofile/values.yaml
- The values.yaml has an app.image and app.tag field that need to be updated using yq
- Use GitHub secrets: SONAR_TOKEN, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
  HELM_REPO_USER, GITOPS_PAT
- Pass ECR registry and image tag between jobs using job outputs
- The docker and helm jobs must NOT run on PRs, only on push to main
```

Cấu trúc `ci.yml` mong đợi (3 job):

```yaml
on:
  push: { branches: [ main ] }          # docker + helm jobs
  pull_request: { branches: [ main ] }  # sonar job
jobs:
  build-and-sonar:      # chỉ chạy khi pull_request
  docker-build-push:    # chỉ chạy khi push; outputs image_tag + ecr_registry
  update-helm:          # chỉ chạy khi push; needs docker-build-push
```

| GitHub Secrets | GitHub Variables |
|----------------|------------------|
| `SONAR_TOKEN`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` | `AWS_REGION`, `ECR_REPOSITORY` |
| `HELM_REPO_USER`, `GITOPS_PAT`, `SLACK_WEBHOOK` | `HELM_REPO_NAME`, `SONAR_HOST_URL` |
