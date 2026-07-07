# Glossaire

Tous les mots techniques du projet, expliqués simplement.

| Terme | Explication simple |
|-------|--------------------|
| **Agent (Jenkins)** | La machine (ou le conteneur) où un pipeline s'exécute. Ici `agent any` = le contrôleur Jenkins. |
| **API** | Une « porte d'entrée » d'un programme, appelable par d'autres programmes ou un navigateur. |
| **Branche (branch)** | Une version parallèle du code. `main` est la branche principale. |
| **Build (Jenkins)** | Une exécution du pipeline. Chaque build a un numéro (1, 2, 3...). |
| **CI (Intégration Continue)** | Vérifier automatiquement le code (lint + tests) à chaque changement. |
| **CD (Déploiement Continu)** | Publier/déployer automatiquement l'application quand la CI est verte. |
| **Commit** | Une « photo » enregistrée du code à un instant donné, avec un message. |
| **Conteneur (container)** | Une instance en cours d'exécution d'une image Docker. |
| **Contrôleur (Jenkins controller)** | Le cœur de Jenkins : l'interface web et l'orchestrateur des builds. |
| **Couverture (coverage)** | Le pourcentage de code exécuté par les tests. |
| **Credentials (Jenkins)** | Les identifiants secrets stockés dans Jenkins (ex : token Docker Hub), chiffrés. |
| **Dépendance** | Une bibliothèque externe requise (ex : FastAPI). Listée dans `requirements.txt`. |
| **Dépôt (repository / repo)** | Le dossier de ton projet suivi par Git, souvent hébergé sur GitHub. |
| **Docker** | Un outil qui emballe une application dans une « boîte » (image) qui tourne partout pareil. |
| **Docker Compose** | Un outil pour décrire et lancer un ou plusieurs conteneurs via un fichier `docker-compose.yml`. |
| **Docker Hub** | Un site où l'on stocke et partage des images Docker. |
| **Dockerfile** | Le fichier « recette » qui décrit comment construire une image Docker. |
| **FastAPI** | Une bibliothèque Python pour créer des API web rapidement. |
| **Git** | L'outil qui suit l'historique du code et permet de le partager. |
| **GitHub** | Un site web qui héberge des dépôts Git. |
| **Image (Docker)** | Le modèle figé de ton application emballée. On la « lance » pour obtenir un conteneur. |
| **Jenkins** | Un serveur d'automatisation (chef d'orchestre) qui exécute les pipelines CI/CD. |
| **Jenkinsfile** | Le fichier qui décrit le pipeline Jenkins (stages et steps). |
| **Lint** | Une vérification automatique du style et de la propreté du code (ici `ruff`). |
| **Pipeline** | La suite automatisée d'étapes exécutée par Jenkins. |
| **Plugin (Jenkins)** | Une extension qui ajoute des fonctionnalités à Jenkins (Git, Docker, JUnit...). |
| **Poll SCM** | Une option où Jenkins vérifie régulièrement le dépôt pour lancer un build s'il y a du nouveau. |
| **Post (Jenkins)** | Un bloc d'actions exécutées après les stages (ex : publier un rapport, afficher un message). |
| **Push** | Envoyer tes commits vers le dépôt distant (GitHub), ou une image vers Docker Hub. |
| **pytest** | L'outil Python qui lance les tests automatiques. |
| **Route (endpoint)** | Une adresse précise de l'API (ex : `/tasks`). |
| **Socket Docker** | Le canal (`/var/run/docker.sock`) qui permet à Jenkins de piloter le Docker de l'hôte. |
| **Stage** | Une grande étape du pipeline (Setup, Lint, Test, Build...). |
| **Step** | Une commande unique dans un stage (ex : `sh 'pytest'`). |
| **Tag (Docker)** | Une étiquette de version sur une image (ex : `latest`, `build-3`). |
| **Test unitaire** | Un test qui vérifie une petite fonction isolée. |
| **Token (Access Token)** | Une clé secrète qui remplace le mot de passe (ici, pour Docker Hub). |
| **uvicorn** | Le serveur qui fait tourner l'application FastAPI. |
| **venv (environnement virtuel)** | Une « bulle » isolée où l'on installe les dépendances d'un projet. |
| **Webhook** | Une notification automatique envoyée par GitHub à Jenkins à chaque push. |
