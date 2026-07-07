# Chapitre 2 - Installer les outils

Ce chapitre est pour **Windows** (mais on indique aussi macOS/Linux). Prends ton temps.

> Tu ouvriras souvent un **terminal**. Sur Windows, cherche « **PowerShell** » dans le menu
> Démarrer et ouvre-le.

## 1. Python (obligatoire)

1. Va sur https://www.python.org/downloads/
2. Télécharge la version **3.12** (ou plus récente).
3. Lance l'installateur. **TRÈS IMPORTANT** : coche **« Add python.exe to PATH »** avant
   de cliquer sur « Install Now ».
4. Vérifie :

```powershell
python --version
```

> macOS : `brew install python@3.12` — Linux : `sudo apt install python3 python3-venv python3-pip`

## 2. Git (obligatoire)

1. Va sur https://git-scm.com/downloads
2. Installe (options par défaut).
3. Vérifie : `git --version`

## 3. Docker Desktop (OBLIGATOIRE pour ce projet)

Contrairement à la démo GitHub Actions, ici **Docker est indispensable** : c'est lui qui
fait tourner Jenkins **et** qui construit l'image de l'application.

1. Va sur https://www.docker.com/products/docker-desktop/
2. Télécharge « Docker Desktop for Windows » et installe.
3. Redémarre si demandé, puis **lance Docker Desktop** (il doit rester ouvert).
4. Vérifie :

```powershell
docker --version
docker compose version
```

> Sur Windows, Docker Desktop utilise WSL2. Si l'installation te le demande, accepte
> l'installation de WSL2 (l'assistant te guide).

## 4. Un éditeur de code (recommandé)

Visual Studio Code (https://code.visualstudio.com/) ou Cursor.

## 5. Créer un compte GitHub (obligatoire)

Jenkins ira chercher ton code sur GitHub.

1. https://github.com/ -> « Sign up ».
2. Confirme ton email.

## 6. Créer un compte Docker Hub (obligatoire pour le CD)

1. https://hub.docker.com/ -> « Sign Up ».
2. Note bien ton **Docker ID** (nom d'utilisateur).

## Récapitulatif

| Outil | Obligatoire ? | Vérification |
|-------|---------------|--------------|
| Python 3.12 | Oui | `python --version` |
| Git | Oui | `git --version` |
| Docker Desktop | **Oui** | `docker --version` |
| Compte GitHub | Oui | Connexion sur github.com |
| Compte Docker Hub | Oui | Connexion sur hub.docker.com |

## Prochaine étape

[Chapitre 3 - Comprendre le projet](03-comprendre-le-projet.md).
