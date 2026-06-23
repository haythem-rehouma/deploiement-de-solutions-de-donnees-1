# Jenkins LTS avec JDK 17 (java + javac + git) auquel on ajoute Maven.
# La pipeline peut alors executer : mvn clean package (compilation + tests unitaires + JAR).
FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends maven \
    && rm -rf /var/lib/apt/lists/*

USER jenkins
