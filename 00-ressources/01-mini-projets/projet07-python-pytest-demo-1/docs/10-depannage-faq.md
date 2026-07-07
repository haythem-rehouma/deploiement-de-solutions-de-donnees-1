# Chapitre 10 - Dépannage (FAQ)

Les problèmes les plus courants et leurs solutions. Cherche ton message d'erreur ci-dessous.

## Problèmes en local

### `python n'est pas reconnu...` / `python: command not found`

Python n'est pas installé, ou tu as oublié de cocher **« Add python.exe to PATH »** pendant
l'installation. Réinstalle Python en cochant bien cette case (voir [Chapitre 2](02-installer-les-outils.md)).
Essaie aussi `py --version` sur Windows.

### PowerShell refuse d'activer le venv (« execution policy »)

Tape ceci une fois, puis réessaie d'activer :

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### `pip install` échoue

- Vérifie que ton environnement virtuel est activé (l'invite commence par `(.venv)`).
- Vérifie ta connexion internet.
- Mets pip à jour : `python -m pip install --upgrade pip`.

### `pytest n'est pas reconnu`

Ton venv n'est pas activé, ou les dépendances ne sont pas installées. Fais :

```powershell
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### Le port 8000 est déjà utilisé

Une autre application utilise le port. Lance sur un autre port :

```powershell
uvicorn app.main:app --reload --port 8001
```

## Problèmes avec Git / GitHub

### `git n'est pas reconnu`

Git n'est pas installé. Voir [Chapitre 2](02-installer-les-outils.md).

### `git push` demande sans cesse un mot de passe / échoue

GitHub n'accepte plus les mots de passe pour `git push`. Utilise la fenêtre de connexion
qui s'ouvre dans le navigateur, ou installe **GitHub CLI** (`gh auth login`).

### `remote origin already exists`

Tu as déjà lié un dépôt. Pour le remplacer :

```powershell
git remote remove origin
git remote add origin https://github.com/TON_USER/TON_REPO.git
```

### Je ne vois pas d'onglet « Actions »

Assure-toi que le fichier `.github/workflows/ci-cd.yml` a bien été envoyé (`git push`), et
qu'il est dans le bon dossier (`.github/workflows/`). Vérifie sur GitHub que le fichier existe.

## Problèmes avec le pipeline (GitHub Actions)

### Le job `docker` échoue avec une erreur de login / `unauthorized`

Le problème vient presque toujours des secrets Docker Hub :

- Vérifie que les secrets s'appellent **exactement** `DOCKERHUB_USERNAME` et `DOCKERHUB_TOKEN`.
- Vérifie que le token Docker Hub a les droits **« Read & Write »**.
- Recrée un token si tu as un doute (voir [Chapitre 7](07-configurer-docker-hub.md)) et
  mets à jour le secret `DOCKERHUB_TOKEN`.

### Le job `docker` ne se lance jamais

C'est **normal** si :
- le job `test` a échoué (`needs: test`), ou
- tu n'es pas sur la branche `main` (`if: github.ref == 'refs/heads/main'`).

### Le job `test` échoue mais ça marchait en local

- Vérifie que tu as bien `push` la dernière version de ton code.
- Regarde les logs du step « Lancer les tests » pour voir **quel** test échoue.
- Parfois, un test dépend de ta machine : les logs t'indiqueront la cause exacte.

### Erreur `Status code 204 must not have a response body`

C'est une erreur FastAPI si une route en 204 renvoie un corps. Dans ce projet, la route
DELETE utilise déjà `response_class=Response` pour l'éviter. Si tu ajoutes une route en 204,
pense à ne rien renvoyer.

## Toujours bloqué ?

- Relis le chapitre correspondant, lentement.
- Copie le message d'erreur exact dans un moteur de recherche.
- Consulte le [Glossaire](glossaire.md) si un mot n'est pas clair.
