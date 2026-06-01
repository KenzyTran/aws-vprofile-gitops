---
title: "7.4 Check the Quality Gate"
date: 2025-01-01
weight: 4
---

## Check the Quality Gate on SonarQube

Open SonarServer -> see project **`vprofile-app`** with the analysis result.

![SonarQube Quality Gate Passed](/images/sonar-quality-gate-passed.png)

- The **default quality gate** is used. If it **fails**, you cannot merge into `main`.
- You can create a **custom quality gate** and attach it to the project if needed.
