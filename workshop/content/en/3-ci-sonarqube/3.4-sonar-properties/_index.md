---
title: "3.4 sonar-project.properties"
date: 2025-01-01
weight: 4
---

## Create `sonar-project.properties` and commit

Create the file at the **root** of the `vprofile-app` repo:

```properties
sonar.projectKey=vprofile-app
sonar.projectName=vprofile-app
sonar.projectVersion=1.0
sonar.sources=src/
sonar.java.binaries=target/classes
sonar.junit.reportsPath=target/surefire-reports/
sonar.coverage.jacoco.xmlReportPaths=target/site/jacoco/jacoco.xml
sonar.java.checkstyle.reportPaths=target/checkstyle-result.xml
```

Commit the source + config:

```bash
cd vprofile-app
git add .
git commit -m "init"
git push origin main
```
