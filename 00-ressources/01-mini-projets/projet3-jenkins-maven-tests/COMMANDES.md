# Aide-mémoire des commandes (Jenkins + Maven via Docker)

> Ouvrez un terminal **dans ce dossier** (`projet3-jenkins-maven-tests`), là où se trouve `docker-compose.yml`.

## Démarrer Jenkins

```bash
docker compose up -d --build
```

Puis ouvrez **http://localhost:8080**.

> **Le port 8080 est déjà occupé ?** Voir l'**[Annexe — Le port 8080 est déjà occupé ?](#annexe--le-port-8080-est-déjà-occupé-)** en fin de document (les deux solutions y sont détaillées).

## Mot de passe administrateur initial

```bash
docker exec jenkins-maven-tp cat /var/jenkins_home/secrets/initialAdminPassword
```

## Vérifier les outils dans le conteneur

```bash
docker exec jenkins-maven-tp which git     # /usr/bin/git
docker exec jenkins-maven-tp mvn -version   # version de Maven + JDK
```

## Voir les logs

```bash
docker compose logs -f jenkins
```

## Tester le projet Maven en local (optionnel, sans Jenkins)

Placez-vous **dans le dossier `depot-exemple/`** (là où se trouve `pom.xml`), puis lancez :

```bash
docker run --rm -v "${PWD}:/app" -w /app maven:3.9-eclipse-temurin-17 mvn clean package
```

### Que veut dire `${PWD}` et où récupérer le résultat ?

`${PWD}` (Print Working Directory) = **le dossier où vous êtes** dans le terminal. Le shell le remplace tout seul par le chemin courant.

| Morceau | Rôle |
|---|---|
| `docker run` | Lance un conteneur. |
| `--rm` | Supprime le conteneur à la fin (pas de déchet). |
| `-v "${PWD}:/app"` | **Partage** votre dossier courant (`${PWD}`) avec le dossier `/app` du conteneur. |
| `-w /app` | Maven s'exécute dans `/app`. |
| `maven:3.9-eclipse-temurin-17` | Image Docker (Maven + Java 17). |
| `mvn clean package` | La commande lancée. |

**Où récupérer le résultat ?** Grâce au partage `-v`, ce que Maven génère **réapparaît dans VOTRE dossier `depot-exemple/`**, dans un nouveau sous-dossier `target/` :

```text
depot-exemple/
├── pom.xml
├── src/
└── target/                              <- cree par Maven
    ├── calculator-1.0-SNAPSHOT.jar      <- LE JAR (votre livrable)
    ├── classes/                         <- .class compiles
    └── surefire-reports/                <- rapports des tests unitaires
```

> **Selon votre terminal :**
> - **PowerShell (Windows) / bash / zsh :** utilisez `${PWD}` (comme ci-dessus).
> - **Ancien `cmd` Windows :** remplacez `${PWD}` par `%cd%` :
>
> ```bat
> docker run --rm -v "%cd%:/app" -w /app maven:3.9-eclipse-temurin-17 mvn clean package
> ```
>
> Pour **voir** le chemin courant : `echo $PWD` (PowerShell/bash) ou `cd` seul (cmd).

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
docker stop <nom>            # ex: docker stop jenkins-maven-tp
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
