# vProfile App

A Java Spring MVC web application (WAR, deployed on Tomcat) backed by MySQL,
RabbitMQ, Memcached, and Elasticsearch. Built with Maven and shipped to Amazon
ECR via a GitHub Actions GitOps pipeline.

## Tech stack

- Java 21, Spring MVC / Spring Security / Spring Data JPA, Hibernate
- Maven (WAR packaging), Tomcat 10
- MySQL, RabbitMQ, Memcached, Elasticsearch
- Docker (multistage build), Amazon ECR, Helm (GitOps)

## Project layout

```
src/                          Application source and tests
Docker-files/app/multistage/  Multistage Dockerfile (build WAR -> Tomcat image)
sonar-project.properties      SonarQube scanner settings
pom.xml                       Maven build
.github/workflows/ci.yml      CI/CD pipeline
```

## Build locally

```bash
mvn clean verify              # compile, run unit tests, package WAR
mvn checkstyle:checkstyle     # generate target/checkstyle-result.xml
```

The WAR is produced at `target/vprofile-v2.war`.

## CI/CD pipeline

Defined in `.github/workflows/ci.yml`.

| Trigger | Jobs | Purpose |
|---------|------|---------|
| Push to a feature branch | none | No pipeline runs |
| PR to `main` | `build-and-sonar` | Maven build, unit tests, Checkstyle, SonarQube scan and quality gate. A failed gate blocks the merge. |
| Merge to `main` | `docker-build-push` -> `update-helm` | Build the Docker image, push to ECR tagged with the commit SHA and `latest`, then bump `app.image` / `app.tag` in the Helm GitOps repo. |

The quality gate uses a self-hosted SonarQube server. To enforce merge
blocking, mark `build-and-sonar` as a required status check on `main`.

### Required GitHub configuration

Secrets:
`SONAR_TOKEN`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `HELM_REPO_USER`,
`GITOPS_PAT`

Variables:
`AWS_REGION`, `ECR_REPOSITORY`, `HELM_REPO_NAME`, `SONAR_HOST_URL`

## Docker

```bash
docker build -f Docker-files/app/multistage/Dockerfile -t vprofileappimg .
```

The image runs the app on Tomcat at port `8080`.
