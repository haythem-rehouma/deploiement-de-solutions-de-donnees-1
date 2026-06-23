# Aide-mémoire des commandes (Jenkins via Docker)

> Ouvrez un terminal **dans ce dossier** (`projet2-jenkins-pipeline-docker`), là où se trouve `docker-compose.yml`.

## Démarrer Jenkins

```bash
docker compose up -d --build
```

Puis ouvrez **http://localhost:8080**.

## Mot de passe administrateur initial

```bash
docker exec jenkins-tp cat /var/jenkins_home/secrets/initialAdminPassword
```

## Voir les logs (suivi du démarrage)

```bash
docker compose logs -f jenkins
```

## Vérifier les outils dans le conteneur

```bash
docker exec jenkins-tp which git       # /usr/bin/git
docker exec jenkins-tp which java
docker exec jenkins-tp which javac
docker exec jenkins-tp which python3   # /usr/bin/python3
```

## Ouvrir un terminal dans le conteneur

```bash
docker exec -it jenkins-tp bash
```

## Arrêter / réinitialiser

```bash
docker compose stop          # arreter (donnees conservees)
docker compose down          # supprimer le conteneur (volume conserve)
docker compose down -v       # tout supprimer (config Jenkins incluse)
```

## Reconstruire l'image après modification du Dockerfile

```bash
docker compose up -d --build
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
