---
title: "3.2 Create SonarQube server (EC2)"
date: 2025-01-01
weight: 2
---

## Create a SonarQube server on EC2

Go to **AWS Console -> EC2 -> Launch Instance**:

| Field | Value |
|-------|-------|
| Name | `SonarServer` |
| AMI / OS | Ubuntu Server (latest LTS) |
| Instance type | **t2.medium** (at least 4 GB RAM) |
| Key pair | Create `SonarKey` |
| Security group | Create `sonar-sg` |

Security group `sonar-sg`: open **port 22** (My IP) and **port 80** (Anywhere).

{{% notice info %}}
Access SonarQube over **port 80** (Nginx proxies to `127.0.0.1:9000`). It is token-protected, so
exposing port 80 is acceptable for this workshop.
{{% /notice %}}

Paste the user-data script (same as the Vietnamese page) into **Advanced details -> User data**. It
installs Java 21, PostgreSQL, SonarQube 26.4 and Nginx, then reboots. Launch and wait **5-10 min**.
