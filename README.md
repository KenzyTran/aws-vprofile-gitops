# aws-vprofile-gitops

Workshop hướng dẫn triển khai ứng dụng multi-tier **vProfile** lên **AWS EKS** theo mô hình
**GitOps**: CI bằng **GitHub Actions** (SonarQube, Docker, ECR) và CD bằng **ArgoCD**.

**Tài liệu thực hành đầy đủ:** [HUONG-DAN-THUC-HANH.md](HUONG-DAN-THUC-HANH.md) - 44 bước, từ dựng
hạ tầng tới chạy pipeline CI/CD qua Pull Request.

## Cấu trúc repo

| Thư mục | Nội dung |
| --- | --- |
| `vprofile-app/` | Source code ứng dụng Java (Maven) + `Docker-files/` cho app, db, web |
| `vprofile-infra/` | Terraform dựng hạ tầng AWS (EKS, networking, ArgoCD ingress) |
| `vprofile-helm/` | Helm chart, ArgoCD apps/projects và Kubernetes manifests (`kubedefs/`) |
| `workshop/` | Trang web workshop (Hugo, song ngữ VI/EN) |
| `docs/` | Sơ đồ kiến trúc và hình ảnh minh hoạ |
| `scripts/` | Script phụ trợ (sinh sơ đồ kiến trúc) |

## Kiến trúc

![Kiến trúc](docs/images/architecture.png)
