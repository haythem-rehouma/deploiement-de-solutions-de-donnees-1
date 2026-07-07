# Guide complet CI/CD avec Jenkins, de A à Z (pour débutants)

Bienvenue ! Ce guide t'explique **tout, depuis zéro**, pour comprendre et faire tourner
une chaîne CI/CD complète avec **Python (pytest)**, **Jenkins** et **Docker Hub**.

Aucune connaissance préalable n'est requise. Suis les chapitres **dans l'ordre**.

> Ce projet est le « jumeau » de la démo GitHub Actions, mais ici c'est **Jenkins** qui
> orchestre le pipeline. Comparer les deux est très instructif.

## Sommaire

| # | Chapitre | Ce que tu vas apprendre |
|---|----------|--------------------------|
| 1 | [C'est quoi CI/CD (et Jenkins) ?](01-c-est-quoi-ci-cd.md) | Le vocabulaire et l'idée générale |
| 2 | [Installer les outils](02-installer-les-outils.md) | Python, Git, Docker, et les comptes nécessaires |
| 3 | [Comprendre le projet](03-comprendre-le-projet.md) | À quoi sert chaque fichier et chaque dossier |
| 4 | [Lancer le projet en local](04-lancer-en-local.md) | Faire tourner l'API et les tests sur ta machine |
| 5 | [Démarrer Jenkins dans Docker](05-demarrer-jenkins.md) | Lancer Jenkins avec docker-compose et le configurer |
| 6 | [Comprendre le Jenkinsfile](06-comprendre-le-jenkinsfile.md) | Lire le pipeline stage par stage |
| 7 | [Configurer les accès Docker Hub](07-configurer-docker-hub.md) | Créer un token et les credentials Jenkins |
| 8 | [Créer et lancer le job](08-lancer-et-observer.md) | Créer le pipeline dans Jenkins et l'exécuter |
| 9 | [Expériences pédagogiques](09-experiences-pedagogiques.md) | Casser un test exprès, etc. |
| 10 | [Dépannage (FAQ)](10-depannage-faq.md) | Les erreurs courantes et comment les résoudre |
| — | [Glossaire](glossaire.md) | Tous les mots techniques expliqués simplement |

## En résumé (l'objectif final)

À la fin de ce guide, à chaque fois que tu modifies le code et que Jenkins lance le pipeline :

1. Jenkins récupère le code et **installe** l'environnement Python.
2. Il lance le **lint** et les **tests** pytest.
3. Si tout réussit (et seulement sur `main`), il **construit** une image Docker et la
   **publie** sur Docker Hub.

Et tout ça, orchestré par **Jenkins**, que tu fais tourner toi-même dans Docker.
