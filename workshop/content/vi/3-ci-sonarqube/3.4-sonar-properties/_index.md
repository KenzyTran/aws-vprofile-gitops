---
title: "3.4 sonar-project.properties"
date: 2025-01-01
weight: 4
---

## Tạo `sonar-project.properties` và commit

Tạo file ở **thư mục gốc** repo `vprofile-app`:

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

Commit toàn bộ source + file cấu hình:

```bash
cd vprofile-app
git add .
git commit -m "init"
git push origin main
```
