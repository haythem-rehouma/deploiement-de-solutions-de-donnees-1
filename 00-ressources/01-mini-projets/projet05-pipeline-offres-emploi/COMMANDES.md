# Aide-mémoire des commandes (Pipeline offres d'emploi via Jenkins + Docker)

> Ouvrez un terminal **dans ce dossier** (`projet05-pipeline-offres-emploi`), là où se trouve `docker-compose.yml`.

## Démarrer Jenkins

```bash
docker compose up -d --build
```

Puis ouvrez **http://localhost:8080** (aucun mot de passe : l'assistant est désactivé).

> **Le port 8080 est déjà occupé ?** Voir l'**[Annexe — Le port 8080 est déjà occupé ?](#annexe--le-port-8080-est-déjà-occupé-)** en fin de document.

## Vérifier les outils dans le conteneur

```bash
docker exec jenkins-offres-tp python3 --version   # Python 3.x
docker exec jenkins-offres-tp which git           # /usr/bin/git
```

## Voir les logs

```bash
docker compose logs -f jenkins
```

## Tester le scraping + la génération HTML en local (sans Jenkins)

Placez-vous **dans `depot-exemple/`**, puis lancez tout dans un conteneur Python :

```bash
docker run --rm -v "${PWD}:/app" -w /app python:3.12-slim \
  bash -lc "pip install -r requirements.txt && python scraper.py && python html_generator.py"
```

Résultats produits dans `depot-exemple/` :

```text
depot-exemple/
├── data/jobs.csv          <- les offres extraites
├── public/index.html      <- le rapport HTML (ouvrez-le dans un navigateur)
└── logs/log.txt           <- journal d'execution
```

> Sur l'ancien `cmd` Windows, remplacez `${PWD}` par `%cd%`.

## Tester la détection de changements en local

```bash
# 1er scraping = reference
docker run --rm -v "${PWD}:/app" -w /app python:3.12-slim bash -lc "pip install -r requirements.txt && python scraper.py"
cp data/jobs.csv data/jobs_previous.csv

# Comparer (vide = identique)
diff data/jobs.csv data/jobs_previous.csv && echo "AUCUN CHANGEMENT" || echo "CHANGEMENTS"
```

## Pousser le projet sur GitHub (depuis depot-exemple/)

```bash
cd depot-exemple
git init
git add .
git commit -m "Initial commit : pipeline offres d'emploi"
git branch -M main
git remote add origin https://github.com/VOTRE-COMPTE/pipeline-offres.git
git push -u origin main
```

## Arrêter / réinitialiser

```bash
docker compose stop          # arreter (donnees conservees)
docker compose down          # supprimer le conteneur (volume conserve)
docker compose down -v       # tout supprimer (config Jenkins incluse)
```

---

## Annexe — Le port 8080 est déjà occupé ?

Si `docker compose up` affiche une erreur du type :

```text
Error response from daemon: ports are not available: exposing port TCP 0.0.0.0:8080 ...
bind: Only one usage of each socket address ... is normally permitted.
```

…c'est qu'**une autre application utilise déjà le port 8080** (souvent un autre Jenkins, Tomcat ou un serveur Java déjà lancé).

Vous avez **deux solutions** au choix : **arrêter le processus** qui occupe le port (Solution A), ou **utiliser un autre port** sans rien arrêter (Solution B).

### Solution A — Trouver et arrêter le processus qui occupe le port 8080

**Étape 1 — repérer le programme.** Avant de tuer un processus, vérifiez d'abord s'il s'agit d'un conteneur Docker.

```bash
docker ps                    # un conteneur apparait-il sur le port 8080 ?
```

- **Si c'est un conteneur Docker**, arrêtez-le proprement :

```bash
docker stop <nom>            # ex: docker stop jenkins-offres-tp
```

- **Sinon** (programme classique sur le PC), suivez les commandes selon votre système.

**Windows (PowerShell) :**

```powershell
# 1. Trouver le PID (numero de processus) qui ecoute sur le port 8080
Get-NetTCPConnection -LocalPort 8080 -State Listen | Select-Object OwningProcess

# 2. Voir de quel programme il s'agit (remplacez 8144 par le PID trouve)
Get-Process -Id 8144

# 3. Arreter ce processus (remplacez 8144 par le PID trouve)
Stop-Process -Id 8144 -Force
```

**Windows (ancien `cmd`) :**

```bat
:: 1. Trouver le PID qui ecoute sur 8080 (derniere colonne = PID)
netstat -ano | findstr :8080

:: 2. Arreter ce processus (remplacez 8144 par le PID trouve)
taskkill /PID 8144 /F
```

**macOS / Linux :**

```bash
# 1. Trouver le PID qui occupe le port 8080
lsof -i :8080
# 2. Arreter ce processus (remplacez 8144 par le PID trouve)
kill -9 8144
```

**Étape 2 — relancer Jenkins :**

```bash
docker compose up -d --build
```

### Solution B — Utiliser un autre port (sans rien arrêter)

Dans `docker-compose.yml`, changez le **port de gauche** (celui du PC). Le port de droite (8080, interne à Jenkins) ne change pas :

```yaml
    ports:
      - "8081:8080"   # 8081 = port sur votre PC, 8080 = port interne de Jenkins
```

Puis relancez et ouvrez **http://localhost:8081** :

```bash
docker compose up -d --build
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
