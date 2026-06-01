---
title: "2.2 Generate Helm chart with AI"
date: 2025-01-01
weight: 2
---

## Generate the Helm chart from `kubedefs/`

In the `vprofile-helm` repo, use AI coding with the prompt below to convert the manifests in
`kubedefs/` into a Helm chart under `helm/vprofile`.

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

Expected result: a `helm/vprofile` chart with `Chart.yaml`, `values.yaml` and the nine template
files listed above.
