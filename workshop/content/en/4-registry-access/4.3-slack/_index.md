---
title: "4.3 Slack app & webhook"
date: 2025-01-01
weight: 3
---

## Create a Slack app and Incoming Webhook

1. Sign in to [slack.com](https://slack.com), create a workspace (e.g. `sentinel`) or reuse one.
2. Create channel **`vprofile-actions`** (Private).
3. Open [api.slack.com/apps](https://api.slack.com/apps) -> **Create New App -> From scratch** (name
   `vpro-act-notifications`), pick the workspace -> **Create app**.
4. **Incoming Webhooks -> Activate**.

   ![Incoming Webhooks page](/images/slack-incoming-webhooks.png)

5. **Add New Webhook to Workspace** -> choose channel `vprofile-actions` -> **Allow**.

   ![Allow webhook](/images/slack-allow-webhook.png)

6. **Copy the Webhook URL** and save it. Test:

   ```bash
   curl -X POST -H 'Content-type: application/json' \
     --data '{"text":"Hello, World!"}' <YOUR_SLACK_WEBHOOK_URL>
   ```
