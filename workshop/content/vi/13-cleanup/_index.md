---
title: "Dọn dẹp"
date: 2025-01-01
weight: 13
chapter: true
pre: "<b>13. </b>"
---

### Dọn dẹp

# Dọn dẹp tài nguyên (tránh phát sinh chi phí AWS)

{{% notice warning %}}
Dọn dẹp **sai thứ tự** là nguyên nhân số một gây tốn tiền ngoài ý muốn. Hai ALB, các EBS volume
của PVC, NAT Gateway và Elastic IP vẫn bị tính tiền kể cả khi bạn nghĩ đã xoá cluster. Làm **đúng
thứ tự dưới đây** và chạy **checklist xác minh** ở cuối.
{{% /notice %}}

Nguyên tắc: dọn dẹp theo **thứ tự ngược** với lúc dựng. Quan trọng nhất là **giải phóng các tài
nguyên do Kubernetes tạo ra (ALB, EBS) TRƯỚC khi `terraform destroy`** — nếu không, AWS Load
Balancer Controller bị xoá cùng cluster sẽ không kịp dọn ALB, để lại load balancer mồ côi khiến
`terraform destroy` thất bại và bạn tiếp tục bị tính tiền.

---

## Bước 0 — Chuẩn bị

Nếu đã từng sửa code, đảm bảo bản local là mới nhất (hoặc xoá và clone lại cho sạch):

```bash
cd vprofile-app   && git pull
cd ../vprofile-helm && git pull
cd ../vprofile-infra && git pull
```

Xác định trước **hai** load balancer sẽ phải biến mất (một của vProfile, một của ArgoCD):

```bash
# Console: EC2 > Load Balancers (đúng region). Hoặc CLI:
aws elbv2 describe-load-balancers \
  --query "LoadBalancers[].{Name:LoadBalancerName,DNS:DNSName}" --output table
```

---

## Bước 1 — Xoá Ingress và workload để giải phóng ALB + EBS

Xoá Ingress trước để **AWS Load Balancer Controller tự xoá 2 ALB** (lúc này controller còn sống):

```bash
kubectl get ingress -A
kubectl delete ingress vpro-ingress    -n vprofile
kubectl delete ingress argocd-ingress  -n argocd
```

Xoá workload vProfile để **PVC được xoá → EBS CSI tự xoá EBS volume** của MySQL (reclaim policy
`Delete`). Cách gọn nhất là xoá namespace (hoặc xoá Application trong ArgoCD):

```bash
kubectl delete ns vprofile
kubectl get pvc -A          # phải trống, không còn PVC nào treo
```

{{% notice warning %}}
Chờ tới khi **cả 2 ALB biến mất** (kiểm tra lại EC2 > Load Balancers). Nếu sau vài phút ALB vẫn còn
hoặc Ingress không xoá được, **xoá ALB thủ công** trong AWS Console — nếu không `terraform destroy`
sẽ kẹt ở subnet/VPC vì còn ENI của load balancer.
{{% /notice %}}

---

## Bước 2 — Xoá AWS Load Balancer Controller (IAM service account)

Service account này được tạo bằng `eksctl` (kèm một CloudFormation stack). Xoá bằng `delete`:

```bash
eksctl delete iamserviceaccount \
  --cluster vprofile-eks-cluster \
  --namespace kube-system \
  --name aws-load-balancer-controller
```

Lệnh này mất một chút thời gian (xoá luôn CloudFormation stack tương ứng). IAM policy
`AWSLoadBalancerControllerIAMPolicy` có thể giữ lại — **không tốn tiền**; xoá sau cũng được.

---

## Bước 3 — `terraform destroy` (xoá EKS, VPC, node group)

```bash
cd vprofile-infra
terraform init      # không bắt buộc, chạy cho chắc nếu đã sửa code
terraform destroy
```

Lệnh này xoá EKS control plane, node group (EC2 worker), VPC, subnet, route table, **NAT Gateway**
và **Elastic IP** (nếu có trong cấu hình). Đợi chạy xong và xác nhận `Destroy complete!`.

{{% notice tip %}}
Muốn dựng lại để luyện tập? Bạn **không cần làm lại từ đầu**: chỉ cần `terraform apply`, rồi đi tiếp
từ bước tạo `iamserviceaccount` ở phần chuẩn bị EKS (IAM policy đã có sẵn).
{{% /notice %}}

---

## Bước 4 — SonarQube EC2

{{% notice info %}}
**Khuyến nghị: Stop, đừng Terminate.** Dựng lại SonarServer khá mất công. Vào EC2 > **Stop
instance** để khỏi tốn tiền compute; khi cần luyện tập thì Start lại (nhớ cập nhật `SONAR_HOST_URL`
vì public IP đổi sau mỗi lần Stop/Start).
{{% /notice %}}

Nếu chắc chắn không dùng nữa:

- **Terminate** instance `SonarServer`.
- Xoá security group `sonar-sg`.

Lưu ý: EC2 ở trạng thái *Stopped* vẫn bị tính tiền cho **EBS root volume** (nhỏ), nhưng không tính
tiền compute.

---

## Bước 5 — IAM, GitHub PAT, ECR, DNS (phần còn lại)

- **IAM access keys**: xoá/deactivate key của `github-actions` và `terraform-admin`.
- **GitHub PAT**: thu hồi (revoke) Personal Access Token đã tạo.
- **ECR**: xoá repo image nếu không dùng (lưu trữ image bị tính tiền theo dung lượng).
- **DNS**: xoá bản ghi CNAME `vprofile` và `argocd` ở nhà cung cấp tên miền.
- (Tuỳ chọn) xoá IAM policy `AWSLoadBalancerControllerIAMPolicy`.

---

## Checklist xác minh (đúng region) — KHÔNG còn tài nguyên tính tiền

Đi qua từng mục trong AWS Console (đúng region đã dùng):

| Dịch vụ | Cần kiểm tra | Tốn tiền nếu bỏ sót |
|---------|--------------|---------------------|
| EC2 > Load Balancers | 2 ALB đã biến mất | ALB tính tiền theo giờ |
| EC2 > Volumes (EBS)  | Không còn volume `available`/mồ côi (gp2 của PVC) | EBS tính tiền theo GB |
| EC2 > Elastic IPs    | Không còn EIP nào *không gắn* | EIP rảnh bị tính tiền |
| EC2 > Instances      | Worker node đã xoá; SonarServer Stopped/Terminated | compute |
| VPC > NAT Gateways   | Đã xoá hết | NAT đắt nhất, tính theo giờ + data |
| EKS > Clusters       | `vprofile-eks-cluster` đã biến mất | control plane theo giờ |
| CloudFormation       | Stack `eksctl-*` đã xoá | (kéo theo tài nguyên) |
| ECR                  | Repo đã xoá nếu không dùng | lưu trữ image |
| IAM                  | Access keys/PAT đã thu hồi | rủi ro bảo mật |

{{% notice warning %}}
Hai thứ hay bị quên nhất và tốn tiền âm thầm: **NAT Gateway** và **EBS volume mồ côi** do PVC chưa
xoá trước khi destroy cluster. Luôn kiểm tra hai mục này lần cuối.
{{% /notice %}}
