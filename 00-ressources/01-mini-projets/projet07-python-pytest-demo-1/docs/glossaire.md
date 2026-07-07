# Glossaire

Tous les mots techniques du projet, expliqués simplement.

| Terme | Explication simple |
|-------|--------------------|
| **API** | Une « porte d'entrée » d'un programme, que d'autres programmes (ou un navigateur) peuvent appeler pour lui demander quelque chose. |
| **Artifact** | Un fichier produit par le pipeline (ex : un rapport de tests) que l'on peut télécharger depuis GitHub. |
| **Branche (branch)** | Une version parallèle du code. `main` est la branche principale. On crée des branches pour travailler sans casser `main`. |
| **CI (Intégration Continue)** | Vérifier automatiquement le code (lint + tests) à chaque changement. |
| **CD (Déploiement/Livraison Continue)** | Publier/déployer automatiquement l'application quand la CI est verte. |
| **Commit** | Une « photo » enregistrée de ton code à un instant donné, avec un message. |
| **Conteneur (container)** | Une instance en cours d'exécution d'une image Docker. L'application qui tourne « dans sa boîte ». |
| **Couverture (coverage)** | Le pourcentage de ton code qui est exécuté par les tests. |
| **Dépendance** | Une bibliothèque externe dont ton projet a besoin (ex : FastAPI). Listées dans `requirements.txt`. |
| **Dépôt (repository / repo)** | Le dossier de ton projet suivi par Git, souvent hébergé sur GitHub. |
| **Docker** | Un outil qui emballe une application et tout ce qu'il lui faut dans une « boîte » (image) qui tourne partout pareil. |
| **Docker Hub** | Un site où l'on stocke et partage des images Docker (comme GitHub, mais pour les images). |
| **Dockerfile** | Le fichier « recette » qui décrit comment construire une image Docker. |
| **FastAPI** | Une bibliothèque Python pour créer des API web rapidement. |
| **Git** | L'outil qui suit l'historique de ton code et permet de le partager. |
| **GitHub** | Un site web qui héberge des dépôts Git et fournit GitHub Actions. |
| **GitHub Actions** | Le service de GitHub qui exécute automatiquement les pipelines CI/CD. |
| **Image (Docker)** | Le modèle figé de ton application emballée. On la « lance » pour obtenir un conteneur. |
| **Job** | Un groupe d'étapes d'un pipeline, exécuté sur une machine. Notre pipeline a 2 jobs : `test` et `docker`. |
| **Lint** | Une vérification automatique du style et de la propreté du code (ici avec `ruff`). |
| **Pipeline / Workflow** | La suite automatisée d'étapes déclenchée par un événement (ici décrite dans `ci-cd.yml`). |
| **Pull Request (PR)** | Une proposition de fusionner des modifications dans une branche, souvent revue avant d'être acceptée. |
| **Push** | Envoyer tes commits locaux vers le dépôt distant (GitHub). |
| **pytest** | L'outil Python qui lance les tests automatiques. |
| **Route (endpoint)** | Une adresse précise de l'API (ex : `/tasks`) qui répond à une requête. |
| **Runner** | La machine (fournie par GitHub) sur laquelle un job s'exécute. |
| **Secret** | Une information sensible (mot de passe, token) stockée de façon chiffrée sur GitHub, jamais visible en clair. |
| **SHA (commit)** | L'identifiant unique d'un commit (un long code). Sert de tag d'image pour retrouver une version précise. |
| **Step (étape)** | Une action unique à l'intérieur d'un job (ex : « installer Python »). |
| **Tag (Docker)** | Une étiquette de version sur une image (ex : `latest`, ou un numéro de version). |
| **Test unitaire** | Un test qui vérifie une petite fonction isolée. |
| **Token (Access Token)** | Une clé secrète qui remplace le mot de passe pour autoriser un accès (ici, à Docker Hub). |
| **uvicorn** | Le serveur qui fait tourner l'application FastAPI. |
| **venv (environnement virtuel)** | Une « bulle » isolée où l'on installe les dépendances d'un projet. |
| **YAML** | Le format texte (avec indentation) utilisé pour écrire le fichier de pipeline. |
