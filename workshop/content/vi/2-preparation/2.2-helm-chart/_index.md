---
title: "2.2 Sinh Helm chart bằng AI"
date: 2025-01-01
weight: 2
---

## Sinh Helm chart từ `kubedefs/`

Trong repo `vprofile-helm`, dùng AI coding với prompt dưới đây để chuyển các manifest trong
`kubedefs/` thành Helm chart trong `helm/vprofile`.

```text
Create a Helm chart from the Kubernetes manifests in the kubedefs folder.

Requirements:
    Chart name: vprofile
    Folder structure: helm/vprofile
        Separate each resource type into individual template files (
        app-deployment.yaml, db-deployment.yaml, mc-deployment.yaml, rmq-deployment.yaml,
        services.yaml, ingress.yaml, secret.yaml, pvc.yaml, dockerregistry-secret.yaml)

Use separate variable sections for
app, db, memcached, rabbitmq, initcontainers, ingress, secrets, dockerregistry in values.yaml
One level nesting only in values.yaml

Variables:
    Common: image, tag, replicas, containerPort, servicePort, storageClass, storageSize, defaultUser
    ingress: enabled, host, servicePort
    dockerregistry: enabled, server, username, password, email

All image tags must default to latest. image name and tag should be separate variables.
db.storageClass must be set to gp2 for AWS EKS EBS volumes.

Ingress must use AWS ALB controller with annotations
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/certificate-arn: <Enter Your Certificate ARN>
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTP":80},{"HTTPS":443}]'
    alb.ingress.kubernetes.io/ssl-redirect: '443'
    alb.ingress.kubernetes.io/backend-protocol: HTTP

Docker registry secret must be conditionally rendered with an enabled flag (default false).
Include imagePullSecrets in app and db deployments only when dockerregistry.enabled is true.
initContainers use command not args. Keep it simple and minimal.
```

Kết quả mong đợi:

```
helm/vprofile/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── app-deployment.yaml   ├── db-deployment.yaml
    ├── mc-deployment.yaml     ├── rmq-deployment.yaml
    ├── services.yaml          ├── ingress.yaml
    ├── secret.yaml            ├── pvc.yaml
    └── dockerregistry-secret.yaml
```
