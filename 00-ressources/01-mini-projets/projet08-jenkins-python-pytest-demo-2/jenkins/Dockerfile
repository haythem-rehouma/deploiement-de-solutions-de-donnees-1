# Image Jenkins personnalisée pour la démo :
# on part de Jenkins LTS et on ajoute Python 3 (pour pytest) et le client Docker
# (pour construire et pousser l'image de l'application).
FROM jenkins/jenkins:lts-jdk17

USER root

# Python 3 + venv + pip (pour lancer pytest / ruff) et outils de base
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 python3-venv python3-pip \
        ca-certificates curl gnupg lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Client Docker (docker CLI) : Jenkins l'utilisera via le socket monté
RUN install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc \
    && chmod a+r /etc/apt/keyrings/docker.asc \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo $VERSION_CODENAME) stable" \
        > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

# Pré-installation de plugins utiles (évite de les cliquer à la main)
RUN jenkins-plugin-cli --plugins \
    workflow-aggregator \
    git \
    docker-workflow \
    junit \
    credentials-binding

USER jenkins
