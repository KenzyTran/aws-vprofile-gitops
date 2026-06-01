---
title: "7.4 Kiểm tra Quality Gate"
date: 2025-01-01
weight: 4
---

## Kiểm tra Quality Gate trên SonarQube

Mở SonarServer -> thấy project **`vprofile-app`** với kết quả phân tích.

![SonarQube Quality Gate Passed](/images/sonar-quality-gate-passed.png)

- Mặc định dùng **default quality gate**. Nếu **fail**, không thể merge vào `main`.
- Có thể tạo **custom quality gate** rồi gắn vào project nếu cần.
