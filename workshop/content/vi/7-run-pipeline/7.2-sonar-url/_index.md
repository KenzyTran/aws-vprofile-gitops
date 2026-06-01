---
title: "7.2 Cập nhật SONAR_HOST_URL"
date: 2025-01-01
weight: 2
---

## Cập nhật biến `SONAR_HOST_URL`

Job sonar dùng `${{ vars.SONAR_HOST_URL }}`. Đảm bảo trỏ đúng:

- Định dạng URL: `http://<public-ip-sonar-server>` (Nginx nghe port 80, mặc định HTTP).

{{% notice warning %}}
Public IP đổi mỗi lần Stop/Start EC2. Nếu vừa bật lại SonarServer, lấy IP mới và cập nhật lại
`SONAR_HOST_URL`, chờ ~5 phút cho SonarQube khởi động trước khi raise PR.
{{% /notice %}}
