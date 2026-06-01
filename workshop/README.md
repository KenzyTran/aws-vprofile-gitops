# vProfile GitOps Workshop

Workshop hướng dẫn triển khai ứng dụng multi-tier **vProfile** lên **AWS EKS** theo mô hình
**GitOps**: CI bằng **GitHub Actions** (SonarQube, Docker, ECR) và CD bằng **ArgoCD**. Xây dựng
bằng Hugo theo format [First Cloud Journey (FCJ)](https://cloudjourney.awsstudygroup.com/), hỗ trợ
song ngữ (Tiếng Việt / English).

## Chạy local

```bash
git clone https://github.com/KenzyTran/vprofile-gitops-workshop.git
cd vprofile-gitops-workshop
git submodule update --init --recursive
hugo server -D
```

Mở http://localhost:1313

## Cấu trúc nội dung

```
content/
  vi/                 # Tiếng Việt (mặc định)
  en/                 # English
    1-introduction/
    2-preparation/
    3-ci-sonarqube/
    4-registry-access/
    5-secrets/
    6-pipeline/
    7-run-pipeline/
    8-eks-prep/
    9-eks-terraform/
    10-alb-argocd/
    11-argocd-sync/
    12-access-test/
    13-cleanup/
    14-summary/
```

## Deploy

Push lên nhánh `main` sẽ tự build và deploy lên GitHub Pages qua
`.github/workflows/deploy.yml` (bật GitHub Pages → Source: GitHub Actions).
