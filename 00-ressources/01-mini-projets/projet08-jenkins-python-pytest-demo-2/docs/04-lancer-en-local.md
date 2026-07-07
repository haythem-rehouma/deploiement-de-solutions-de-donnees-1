# Chapitre 4 - Lancer le projet en local

Avant de toucher à Jenkins, faisons tourner l'application et les tests **sur ta machine**.
C'est la meilleure façon de vérifier que le code fonctionne.

> Toutes les commandes se tapent dans **PowerShell**, depuis le dossier du projet.

## Étape 0 : se placer dans le dossier

```powershell
cd c:\00-dream\jenkins-python-pytest-demo-2
ls
```

Tu dois voir `app`, `tests`, `Jenkinsfile`, `docker-compose.yml`, etc.

## Étape 1 : créer un environnement virtuel

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

Ton invite doit maintenant commencer par `(.venv)`.

> **Erreur « execution policy » ?** Tape ceci une fois, puis réessaie :
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
> macOS/Linux : `source .venv/bin/activate`

## Étape 2 : installer les dépendances

```powershell
pip install -r requirements.txt
```

## Étape 3 : lancer les tests

```powershell
pytest
```

Tu dois voir se terminer par :

```
============================= 24 passed in 1.12s ==============================
```

**24 passed** = les 24 tests réussissent.

## Étape 4 : lancer le lint

```powershell
ruff check .
```

Attendu : `All checks passed!`

## Étape 5 : démarrer l'application

```powershell
uvicorn app.main:app --reload
```

Puis va sur :
- http://127.0.0.1:8000/health
- http://127.0.0.1:8000/docs (page interactive)

Arrête avec `Ctrl + C`.

## (Optionnel) Construire l'image de l'application

```powershell
docker build -t taskapi .
docker run -p 8000:8000 taskapi
```

C'est exactement l'image que Jenkins construira et publiera plus tard.

## Prochaine étape

Passons au cœur du sujet : [Chapitre 5 - Démarrer Jenkins](05-demarrer-jenkins.md).
