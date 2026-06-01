---
title: "Chạy pipeline qua PR"
date: 2025-01-01
weight: 7
chapter: true
pre: "<b>7. </b>"
---

### Chạy pipeline qua PR

# Chạy pipeline qua Pull Request

`main` được bảo vệ: mọi thay đổi đi qua feature branch -> PR -> merge. PR chạy job sonar; merge chạy
job docker + helm.

{{% children %}}
