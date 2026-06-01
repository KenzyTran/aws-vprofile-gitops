---
title: "Clean Up"
date: 2025-01-01
weight: 13
chapter: true
pre: "<b>13. </b>"
---

### Clean Up

# Clean up resources (avoid AWS charges)

{{% notice warning %}}
Cleaning up in the **wrong order** is the number-one cause of surprise bills. The two ALBs, the PVC
EBS volumes, NAT Gateways and Elastic IPs keep costing money even when you think the cluster is
gone. Follow the **exact order below** and run the **verification checklist** at the end.
{{% /notice %}}

Principle: clean up in **reverse order** of how you built it. The key point is to **release the
resources Kubernetes created (ALB, EBS) BEFORE `terraform destroy`** — otherwise the AWS Load
Balancer Controller gets deleted with the cluster and never cleans up the ALBs, leaving orphaned
load balancers that make `terraform destroy` fail while you keep paying.

---

## Step 0 — Prepare

If you changed code, make sure your local copy is up to date (or delete and re-clone for a clean
state):

```bash
cd vprofile-app   && git pull
cd ../vprofile-helm && git pull
cd ../vprofile-infra && git pull
```

Identify the **two** load balancers that must disappear (one for vProfile, one for ArgoCD):

```bash
# Console: EC2 > Load Balancers (correct region). Or CLI:
aws elbv2 describe-load-balancers \
  --query "LoadBalancers[].{Name:LoadBalancerName,DNS:DNSName}" --output table
```

---

## Step 1 — Delete Ingress and workloads to free ALB + EBS

Delete the Ingresses first so the **AWS Load Balancer Controller removes both ALBs** (while the
controller is still alive):

```bash
kubectl get ingress -A
kubectl delete ingress vpro-ingress    -n vprofile
kubectl delete ingress argocd-ingress  -n argocd
```

Delete the vProfile workload so the **PVC is removed → the EBS CSI driver deletes the MySQL EBS
volume** (reclaim policy `Delete`). The simplest way is to delete the namespace (or the ArgoCD
Application):

```bash
kubectl delete ns vprofile
kubectl get pvc -A          # must be empty, no PVC left hanging
```

{{% notice warning %}}
Wait until **both ALBs are gone** (re-check EC2 > Load Balancers). If after a few minutes an ALB is
still there or an Ingress won't delete, **delete the ALB manually** in the AWS Console — otherwise
`terraform destroy` gets stuck on the subnet/VPC because of the load balancer's ENIs.
{{% /notice %}}

---

## Step 2 — Delete the AWS Load Balancer Controller (IAM service account)

This service account was created with `eksctl` (plus a CloudFormation stack). Delete it with
`delete`:

```bash
eksctl delete iamserviceaccount \
  --cluster vprofile-eks-cluster \
  --namespace kube-system \
  --name aws-load-balancer-controller
```

This takes a little while (it also deletes the matching CloudFormation stack). You may keep the IAM
policy `AWSLoadBalancerControllerIAMPolicy` — it **costs nothing**; delete it later if you want.

---

## Step 3 — `terraform destroy` (delete EKS, VPC, node group)

```bash
cd vprofile-infra
terraform init      # optional, run it to be safe if you changed code
terraform destroy
```

This deletes the EKS control plane, node group (EC2 workers), VPC, subnets, route tables, **NAT
Gateways** and **Elastic IPs** (if defined). Wait for it to finish and confirm `Destroy complete!`.

{{% notice tip %}}
Want to rebuild for practice? You **don't need to start from scratch**: just `terraform apply`, then
continue from the `iamserviceaccount` step in the EKS prep section (the IAM policy already exists).
{{% /notice %}}

---

## Step 4 — SonarQube EC2

{{% notice info %}}
**Recommended: Stop, don't Terminate.** Rebuilding SonarServer is some effort. Go to EC2 > **Stop
instance** to avoid compute charges; Start it again when you practice (remember to update
`SONAR_HOST_URL` because the public IP changes after each Stop/Start).
{{% /notice %}}

If you are sure you won't use it again:

- **Terminate** the `SonarServer` instance.
- Delete the `sonar-sg` security group.

Note: a *Stopped* EC2 instance is still charged for its **EBS root volume** (small), but not for
compute.

---

## Step 5 — IAM, GitHub PAT, ECR, DNS (the rest)

- **IAM access keys**: delete/deactivate the keys for `github-actions` and `terraform-admin`.
- **GitHub PAT**: revoke the Personal Access Token you created.
- **ECR**: delete the image repo if unused (image storage is billed by size).
- **DNS**: remove the CNAME records `vprofile` and `argocd` at your domain provider.
- (Optional) delete the IAM policy `AWSLoadBalancerControllerIAMPolicy`.

---

## Verification checklist (correct region) — NO billable resources left

Go through each item in the AWS Console (in the region you used):

| Service | Check | Costs money if missed |
|---------|-------|-----------------------|
| EC2 > Load Balancers | both ALBs gone | ALB billed hourly |
| EC2 > Volumes (EBS)  | no `available`/orphaned volume (the PVC's gp2) | EBS billed per GB |
| EC2 > Elastic IPs    | no *unattached* EIP | idle EIP is billed |
| EC2 > Instances      | workers deleted; SonarServer Stopped/Terminated | compute |
| VPC > NAT Gateways   | all deleted | NAT is the priciest, hourly + data |
| EKS > Clusters       | `vprofile-eks-cluster` gone | control plane hourly |
| CloudFormation       | `eksctl-*` stacks deleted | (drags resources along) |
| ECR                  | repo deleted if unused | image storage |
| IAM                  | access keys/PAT revoked | security risk |

{{% notice warning %}}
The two most-forgotten money sinks: **NAT Gateways** and **orphaned EBS volumes** from a PVC that
wasn't deleted before destroying the cluster. Always double-check these two last.
{{% /notice %}}
