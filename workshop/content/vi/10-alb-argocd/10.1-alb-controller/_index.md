---
title: "10.1 AWS LB Controller"
date: 2025-01-01
weight: 1
---

## Cài AWS Load Balancer Controller

**1. Tải IAM policy và tạo policy:**

```bash
curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
aws iam create-policy --policy-name AWSLoadBalancerControllerIAMPolicy --policy-document file://iam_policy.json
```

**2. Tạo IAM service account (IRSA)** (thay `<account-id>`):

```bash
eksctl create iamserviceaccount \
  --cluster vprofile-eks-cluster --namespace kube-system \
  --name aws-load-balancer-controller \
  --attach-policy-arn arn:aws:iam::<account-id>:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve --region us-east-1
aws eks update-kubeconfig --name vprofile-eks-cluster --region us-east-1
```

**3. Cài cert-manager:**

```bash
kubectl apply --validate=false -f https://github.com/cert-manager/cert-manager/releases/download/v1.16.1/cert-manager.yaml
kubectl wait --for=condition=available --timeout=180s \
  deployment/cert-manager deployment/cert-manager-cainjector deployment/cert-manager-webhook -n cert-manager
```

**4. Cài controller bằng Helm** (thay `<EKS-VPC-ID>`):

```bash
aws eks describe-cluster --name vprofile-eks-cluster --region us-east-1 \
  --query "cluster.resourcesVpcConfig.vpcId" --output text
helm repo add eks https://aws.github.io/eks-charts
helm repo update
helm upgrade --install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system --set clusterName=vprofile-eks-cluster --set region=us-east-1 \
  --set vpcId=<EKS-VPC-ID> --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```

**5. Kiểm tra:**

```bash
kubectl get pods -n kube-system -l app.kubernetes.io/name=aws-load-balancer-controller
kubectl logs -n kube-system deployment/aws-load-balancer-controller --tail=30
```
