# Chapitre 2 - Installer les outils

Ce chapitre est pour **Windows** (mais on indique aussi macOS/Linux). On installe seulement
ce qui est nécessaire. Prends ton temps, coche chaque étape.

> Tu ouvriras souvent un **terminal**. Sur Windows, cherche « **PowerShell** » dans le menu
> Démarrer et ouvre-le. C'est la fenêtre où l'on tape des commandes.

## 1. Python (obligatoire)

Python est le langage de notre application.

1. Va sur https://www.python.org/downloads/
2. Télécharge la version **3.12** (ou plus récente).
3. Lance l'installateur. **TRÈS IMPORTANT** : coche la case
   **« Add python.exe to PATH »** en bas de la fenêtre, AVANT de cliquer sur « Install Now ».
4. Vérifie l'installation en tapant dans PowerShell :

```powershell
python --version
```

Tu dois voir quelque chose comme `Python 3.12.x`. Si oui, c'est bon.

> macOS : `brew install python@3.12` — Linux : `sudo apt install python3 python3-venv python3-pip`

## 2. Git (obligatoire)

Git sert à sauvegarder ton code et à l'envoyer sur GitHub.

1. Va sur https://git-scm.com/downloads
2. Télécharge et installe (laisse toutes les options par défaut, clique « Next » jusqu'au bout).
3. Vérifie :

```powershell
git --version
```

Tu dois voir `git version 2.x.x`.

## 3. Un éditeur de code (recommandé)

Si tu n'en as pas déjà un, installe **Visual Studio Code** (ou tu utilises **Cursor**, que
tu as déjà). Télécharge VS Code ici : https://code.visualstudio.com/

## 4. Docker Desktop (optionnel pour les tests en local)

Docker permet de construire l'image de l'application **sur ta machine**. Ce n'est **pas
obligatoire** : GitHub le fera pour toi dans le cloud. Mais c'est utile pour comprendre.

1. Va sur https://www.docker.com/products/docker-desktop/
2. Télécharge « Docker Desktop for Windows » et installe.
3. Redémarre l'ordinateur si demandé, puis lance Docker Desktop.
4. Vérifie :

```powershell
docker --version
```

> Si Docker te paraît compliqué au début, **saute-le** : tu peux faire toute la démo sans
> l'installer localement.

## 5. Créer un compte GitHub (obligatoire)

GitHub héberge ton code et fait tourner la CI/CD.

1. Va sur https://github.com/ et clique sur **« Sign up »**.
2. Choisis un nom d'utilisateur, un email, un mot de passe.
3. Confirme ton email.

## 6. Créer un compte Docker Hub (obligatoire pour la partie CD)

Docker Hub stockera l'image de ton application.

1. Va sur https://hub.docker.com/ et clique sur **« Sign Up »**.
2. Choisis un **Docker ID** (nom d'utilisateur), un email, un mot de passe.
3. Confirme ton email.

> Note bien ton **Docker ID** quelque part : on en aura besoin plus tard.

## Récapitulatif

| Outil | Obligatoire ? | Vérification |
|-------|---------------|--------------|
| Python 3.12 | Oui | `python --version` |
| Git | Oui | `git --version` |
| Éditeur de code | Recommandé | — |
| Docker Desktop | Optionnel | `docker --version` |
| Compte GitHub | Oui | Connexion sur github.com |
| Compte Docker Hub | Oui (pour le CD) | Connexion sur hub.docker.com |

## Prochaine étape

[Chapitre 3 - Comprendre le projet](03-comprendre-le-projet.md).
