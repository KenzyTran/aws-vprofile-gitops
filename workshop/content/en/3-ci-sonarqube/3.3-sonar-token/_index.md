---
title: "3.3 Log in & create token"
date: 2025-01-01
weight: 3
---

## Log in to SonarQube and create a token

1. Open `http://<sonar-server-public-ip>` (port 80).
2. Log in with `admin` / `admin`, then **change the password**.
3. Create a token: **Account -> My Account -> Security**:
   - Name: `actions`, Type: **User Token**, Expires: 30 days -> **Generate** and **save the token**.

![Generate a User Token on SonarQube](/images/sonar-generate-token.png)

{{% notice info %}}
This token (and the other keys) will be stored in **GitHub Secrets** in chapter 5.
{{% /notice %}}
