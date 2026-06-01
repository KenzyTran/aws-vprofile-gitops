---
title: "3.3 Đăng nhập & tạo token"
date: 2025-01-01
weight: 3
---

## Đăng nhập SonarQube và tạo token

1. Mở `http://<public-ip-sonar-server>` (port 80).
2. Đăng nhập mặc định `admin` / `admin`, rồi **đổi mật khẩu**.
3. Tạo token: **Account -> My Account -> Security**:
   - Name: `actions`, Type: **User Token**, Expires: 30 days -> **Generate** và **lưu token**.

![Tạo User Token trên SonarQube](/images/sonar-generate-token.png)

{{% notice info %}}
Token này (cùng các key khác) sẽ được lưu vào **GitHub Secrets** ở chương 5.
{{% /notice %}}
