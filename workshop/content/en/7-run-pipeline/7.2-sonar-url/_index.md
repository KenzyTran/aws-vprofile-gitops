---
title: "7.2 Update SONAR_HOST_URL"
date: 2025-01-01
weight: 2
---

## Update the `SONAR_HOST_URL` variable

The sonar job uses `${{ vars.SONAR_HOST_URL }}`. Make sure it points correctly:

- URL form: `http://<sonar-server-public-ip>` (Nginx listens on port 80, default HTTP).

{{% notice warning %}}
The public IP changes on Stop/Start. If you just restarted SonarServer, grab the new IP, update
`SONAR_HOST_URL`, and wait ~5 minutes for SonarQube to start before raising the PR.
{{% /notice %}}
