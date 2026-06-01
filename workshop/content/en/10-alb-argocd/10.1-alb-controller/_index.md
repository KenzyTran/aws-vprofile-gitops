---
title: "10.1 AWS LB Controller"
date: 2025-01-01
weight: 1
---

## Install the AWS Load Balancer Controller

Follow the same commands as the Vietnamese page: (1) download the IAM policy and create it,
(2) `eksctl create iamserviceaccount` (IRSA, replace `<account-id>`), (3) install cert-manager and
wait, (4) `helm upgrade --install aws-load-balancer-controller` (replace `<EKS-VPC-ID>` obtained via
`aws eks describe-cluster ... resourcesVpcConfig.vpcId`), (5) verify with `kubectl get pods` and
`kubectl logs`.
