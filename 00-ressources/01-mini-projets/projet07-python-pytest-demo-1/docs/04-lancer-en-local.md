# Chapitre 4 - Lancer le projet en local

Ici, on fait tourner l'application et les tests **sur ta propre machine**, avant même de
toucher à GitHub. C'est la meilleure façon de comprendre ce qui se passe.

> Toutes les commandes ci-dessous se tapent dans **PowerShell**, depuis le dossier du projet.

## Étape 0 : se placer dans le dossier du projet

Dans PowerShell, va dans le dossier du projet avec la commande `cd` (change directory) :

```powershell
cd c:\00-dream\jenkins-python-pytest-demo-1
```

Pour vérifier que tu es au bon endroit, liste les fichiers :

```powershell
ls
```

Tu dois voir `app`, `tests`, `README.md`, etc.

## Étape 1 : créer un environnement virtuel

Un **environnement virtuel** (venv) est une « bulle » isolée où on installe les
bibliothèques du projet, sans polluer le reste de ta machine.

```powershell
python -m venv .venv
```

Cela crée un dossier `.venv`. Ensuite, **active** cet environnement :

```powershell
.\.venv\Scripts\activate
```

Si ça marche, ton invite de commande commence maintenant par `(.venv)`.

> **Erreur d'exécution de script ?** Si PowerShell refuse avec un message sur
> « execution policy », tape cette commande une fois, puis réessaie d'activer :
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
> ```
>
> macOS/Linux : l'activation se fait avec `source .venv/bin/activate`.

## Étape 2 : installer les dépendances

Les dépendances sont les bibliothèques listées dans `requirements.txt` (FastAPI, pytest...).

```powershell
pip install -r requirements.txt
```

Attends que tout se télécharge (ça peut prendre une minute la première fois).

## Étape 3 : lancer les tests

C'est le moment de vérité. Lance pytest :

```powershell
pytest
```

Tu dois voir une série de lignes vertes se terminant par quelque chose comme :

```
============================= 24 passed in 1.12s ==============================
```

**24 passed** = les 24 tests ont réussi. Bravo, le code fonctionne !

Tu verras aussi un tableau de **couverture** (coverage) : c'est le pourcentage de code
qui est vérifié par les tests. Plus c'est haut, mieux c'est.

## Étape 4 : lancer le lint (vérification du style)

Le **lint** vérifie que le code est propre et bien écrit :

```powershell
ruff check .
```

Tu dois voir : `All checks passed!`

## Étape 5 : démarrer l'application pour de vrai

Lance le serveur web :

```powershell
uvicorn app.main:app --reload
```

Laisse cette fenêtre ouverte. Ouvre ensuite ton navigateur et va sur :

- http://127.0.0.1:8000/health  -> tu vois `{"status":"ok","version":"1.0.0"}`
- http://127.0.0.1:8000/docs  -> une belle page interactive pour tester l'API !

Sur la page `/docs`, tu peux cliquer sur une route, « Try it out », remplir les champs et
« Execute » pour voir l'application répondre en direct.

Pour **arrêter** le serveur, reviens dans PowerShell et appuie sur `Ctrl + C`.

## (Optionnel) Étape 6 : tester avec Docker

Si tu as installé Docker Desktop, tu peux construire et lancer l'image :

```powershell
docker build -t taskapi .
docker run -p 8000:8000 taskapi
```

Puis va sur http://127.0.0.1:8000/docs comme avant. La différence : ici l'application
tourne dans une « boîte » Docker, exactement comme elle tournera en production.

## Récapitulatif

Tu sais maintenant :
- créer et activer un environnement virtuel ;
- installer les dépendances ;
- lancer les tests et le lint ;
- démarrer l'application.

## Prochaine étape

Envoyons le code sur GitHub : [Chapitre 5 - Mettre sur GitHub](05-mettre-sur-github.md).
