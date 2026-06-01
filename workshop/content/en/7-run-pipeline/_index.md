---
title: "Run pipeline via PR"
date: 2025-01-01
weight: 7
chapter: true
pre: "<b>7. </b>"
---

### Run pipeline via PR

# Run the pipeline via Pull Request

`main` is protected: changes go feature branch -> PR -> merge. A PR runs the sonar job; a merge runs
the docker + helm jobs.

{{% children %}}
