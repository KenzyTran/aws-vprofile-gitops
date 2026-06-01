---
title: "4.3 Slack app & webhook"
date: 2025-01-01
weight: 3
---

## Tạo Slack app và Incoming Webhook

1. Đăng nhập [slack.com](https://slack.com), tạo workspace (vd `sentinel`) hoặc dùng sẵn.
2. Tạo channel **`vprofile-actions`** (Private).
3. Mở [api.slack.com/apps](https://api.slack.com/apps) -> **Create New App -> From scratch** (tên
   `vpro-act-notifications`), chọn workspace -> **Create app**.
4. **Incoming Webhooks -> Activate**.

   ![Trang Incoming Webhooks](/images/slack-incoming-webhooks.png)

5. **Add New Webhook to Workspace** -> chọn channel `vprofile-actions` -> **Allow**.

   ![Cấp quyền webhook](/images/slack-allow-webhook.png)

6. **Copy Webhook URL** và lưu lại. Kiểm tra:

   ```bash
   curl -X POST -H 'Content-type: application/json' \
     --data '{"text":"Hello, World!"}' <YOUR_SLACK_WEBHOOK_URL>
   ```
