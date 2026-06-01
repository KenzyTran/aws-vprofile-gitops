---
title: "6.3 Rà soát pipeline"
date: 2025-01-01
weight: 3
---

## Rà soát và dọn pipeline sau khi sinh

| Vấn đề thường gặp | Cách xử lý |
|-------------------|-----------|
| Thêm `role-to-assume` / OIDC | Xoá - chỉ dùng access key + secret key |
| Thiếu bước thông báo Slack | Thêm step gửi `SLACK_WEBHOOK` |
| Định nghĩa lại biến đã có | Dùng trực tiếp `${{ vars.* }}` |
| Lệnh Checkstyle rườm rà | Rút gọn `mvn verify checkstyle:checkstyle -B` |
| Bước "create ECR if needed" | Không cần (đã tạo ở 4.1) |
| `yq` cập nhật sai cách | Cập nhật theo key path `app.image`/`app.tag` |
| Thiếu `SONAR_HOST_URL` | Đảm bảo đã tạo (5.3) |
