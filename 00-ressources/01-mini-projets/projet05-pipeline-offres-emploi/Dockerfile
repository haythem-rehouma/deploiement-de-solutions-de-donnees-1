# Jenkins LTS (JDK 17, git) auquel on ajoute Python 3 + venv + pip.
# La pipeline peut alors : creer un venv, installer requirements.txt,
# lancer le scraping (scraper.py) et la generation HTML (html_generator.py).
FROM jenkins/jenkins:lts-jdk17

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-venv \
        python3-pip \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

USER jenkins

# Plugins utiles : pipelines, Git/GitHub, publication HTML (rapport visible dans Jenkins).
RUN jenkins-plugin-cli --plugins \
    workflow-aggregator \
    git \
    github \
    htmlpublisher

# Conteneur pret a l'emploi (on saute l'assistant initial).
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
