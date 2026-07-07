# Guide complet CI/CD de A à Z (pour débutants)

Bienvenue ! Ce guide t'explique **tout, depuis zéro**, pour comprendre et faire tourner
une chaîne CI/CD complète avec **Python (pytest)**, **GitHub Actions** et **Docker Hub**.

Aucune connaissance préalable n'est requise. Suis les chapitres **dans l'ordre**.

> Astuce : coche mentalement chaque étape. Si quelque chose ne marche pas, va voir
> directement le chapitre [10 - Dépannage (FAQ)](10-depannage-faq.md).

## Sommaire

| # | Chapitre | Ce que tu vas apprendre |
|---|----------|--------------------------|
| 1 | [C'est quoi CI/CD ?](01-c-est-quoi-ci-cd.md) | Le vocabulaire et l'idée générale, avec une analogie simple |
| 2 | [Installer les outils](02-installer-les-outils.md) | Python, Git, Docker, et créer les comptes nécessaires |
| 3 | [Comprendre le projet](03-comprendre-le-projet.md) | À quoi sert chaque fichier et chaque dossier |
| 4 | [Lancer le projet en local](04-lancer-en-local.md) | Faire tourner l'API et les tests sur ta machine |
| 5 | [Mettre le code sur GitHub](05-mettre-sur-github.md) | Créer un dépôt et envoyer ton code |
| 6 | [Comprendre le pipeline](06-comprendre-le-pipeline.md) | Lire et comprendre le fichier `ci-cd.yml` ligne par ligne |
| 7 | [Configurer Docker Hub](07-configurer-docker-hub.md) | Créer un token et l'ajouter en secret sur GitHub |
| 8 | [Lancer et observer la démo](08-lancer-et-observer.md) | Déclencher le pipeline et regarder ce qui se passe |
| 9 | [Expériences pédagogiques](09-experiences-pedagogiques.md) | Casser un test exprès, faire une PR, etc. |
| 10 | [Dépannage (FAQ)](10-depannage-faq.md) | Les erreurs courantes et comment les résoudre |
| — | [Glossaire](glossaire.md) | Tous les mots techniques expliqués simplement |

## En résumé (l'objectif final)

À la fin de ce guide, à chaque fois que tu modifies le code et que tu l'envoies sur GitHub :

1. GitHub lance **automatiquement** les tests.
2. Si les tests réussissent, il **construit** une image Docker.
3. Il **publie** cette image sur Docker Hub, prête à être utilisée n'importe où.

Et tout ça, **sans que tu aies quoi que ce soit à faire manuellement**. C'est ça, la magie du CI/CD.
