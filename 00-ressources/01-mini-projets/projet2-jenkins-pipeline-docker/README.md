<a id="top"></a>

# Projet 2 — Pipeline Jenkins (Hello World) avec Docker

> **Pratique guidée** · Module [05 — Jenkins : pipeline CI/CD](../README.md)
>
> Objectif : lancer **Jenkins sans l'installer** (via Docker), puis créer un **pipeline** qui récupère un dépôt GitHub et exécute un programme **Java** et un programme **Python**.
>
> Pressé ? Voir l'**[aide-mémoire des commandes](COMMANDES.md)**.

---

## Pourquoi Docker ?

Installer Jenkins « à la main » (service, Java, configuration) est long et différent sur chaque machine. Ici, **Docker** vous donne un Jenkins prêt à l'emploi, **identique sur Windows, macOS et Linux**.

L'image Docker de ce projet contient déjà tout ce dont la pipeline a besoin : **Jenkins**, **Java (java + javac)**, **Git** et **Python 3**.

```mermaid
flowchart LR
    repo["Votre depot GitHub<br/>HelloWorld.java, hello.py, Jenkinsfile"] -->|"git (checkout)"| jenkins["Jenkins (conteneur Docker)<br/>java + javac + python3"]
    jenkins --> build["Stage Build<br/>javac / java / python3"]
    build --> result["Console : Hello, World !"]
```

---

## Prérequis

- **Docker Desktop** installé et démarré.
- Un compte **GitHub** + un **jeton d'accès personnel** (Personal Access Token) si votre dépôt est **privé**.

```bash
docker --version
docker compose version
```

---

## Structure du projet

```text
projet2-jenkins-pipeline-docker/
├── docker-compose.yml          <- lance Jenkins
├── Dockerfile                  <- Jenkins + Java + Python 3
├── README.md                   <- ce fichier
├── COMMANDES.md                <- aide-memoire
└── depot-exemple/              <- les 3 fichiers a mettre dans VOTRE depot GitHub
    ├── HelloWorld.java
    ├── hello.py
    └── Jenkinsfile
```

---

## Étape A — Démarrer Jenkins

Dans un terminal, **dans ce dossier** :

```bash
docker compose up -d --build
```

La première fois, Docker construit l'image (téléchargement de Jenkins + installation de Python). Patientez 2-3 minutes, puis ouvrez **http://localhost:8080**.

### Récupérer le mot de passe administrateur initial

```bash
docker exec jenkins-tp cat /var/jenkins_home/secrets/initialAdminPassword
```

Copiez ce mot de passe, collez-le dans la page de déverrouillage, puis :
1. Cliquez **« Installer les plugins suggérés »** (inclut Git et Pipeline).
2. Créez votre **compte administrateur**.
3. Validez l'URL Jenkins (laissez `http://localhost:8080/`).

---

## Étape B — Créer votre dépôt GitHub

1. Créez un dépôt GitHub (ex. `hello-python`).
2. Ajoutez-y les **3 fichiers** du dossier [`depot-exemple/`](depot-exemple) : `HelloWorld.java`, `hello.py`, `Jenkinsfile`.
3. **Modifiez l'URL** dans le `Jenkinsfile` pour pointer vers **votre** dépôt :

```groovy
git branch: 'main', url: 'https://github.com/VOTRE-COMPTE/hello-python.git'
```

> Vérifiez le **nom de votre branche** (`main` ou `master`).

---

## Étape C — Créer la pipeline dans Jenkins

Sur le tableau de bord Jenkins :

| # | Action |
|---|---|
| 01 | **New Item** → saisir un nom → type **Pipeline** → **OK**. |
| 02 | Section *Build Triggers* : cocher **Poll SCM** (planning `H/2 * * * *` pour vérifier toutes les 2 min, optionnel). |
| 03 | Section *Pipeline* : **Definition = Pipeline script from SCM**. |
| 04 | **SCM = Git**. |
| 05 | **Repository URL** = l'URL de votre dépôt (ex. `https://github.com/VOTRE-COMPTE/hello-python.git`). |
| 06 | **Credentials** (si dépôt privé) : **Add → Jenkins → Username with password** → *Username* = votre identifiant GitHub, *Password* = **votre jeton GitHub**. Pour un dépôt **public**, aucun credential nécessaire. |
| 07 | **Sélectionnez** ensuite le credential créé (oubli fréquent !). |
| 08 | **Branch Specifier** : remplacez `*/master` par **`*/main`** si votre branche s'appelle `main`. |
| 09 | **Script Path** = `Jenkinsfile` (par défaut). Cliquez **Apply** puis **Save**. |

### Chemin de Git (déjà bon avec Docker)

Comme Jenkins tourne ici dans un **conteneur Linux**, Git est à **`/usr/bin/git`**. Pour le vérifier :

```bash
docker exec jenkins-tp which git      # -> /usr/bin/git
```

Si besoin : *Manage Jenkins → Tools → Git installations* → *Name* = `Default`, *Path* = `/usr/bin/git`, puis **Apply/Save**. (Le chemin Windows `C:\Program Files\Git\cmd\git.exe` ne concerne **pas** ce montage Docker.)

---

## Étape D — Lancer le build

Cliquez sur **Build Now**. Ouvrez le build → **Console Output**. Vous devez voir :

```text
Running on Unix
Hello, World from Jenkins Pipeline!     (java)
Hello, World from Jenkins Pipeline!     (python3)
Finished: SUCCESS
```

> Comme Jenkins est sous Linux ici, c'est la branche `isUnix()` qui s'exécute (`javac`, `java`, `python3`). Les commandes `bat`/Windows ne sont utilisées que sur un Jenkins installé sous Windows.

---

## Arrêter / réinitialiser

```bash
docker compose stop          # arrete Jenkins (les donnees sont conservees)
docker compose down          # supprime le conteneur (le volume reste)
docker compose down -v       # TOUT supprimer, y compris la config Jenkins
```

---

## Annexe 1 — Contenu des fichiers

### `Jenkinsfile` (version utilisée avec ce Docker, Linux)

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VOTRE-COMPTE/hello-python.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo "Running on Unix"'
                        sh 'javac HelloWorld.java'
                        sh 'java HelloWorld'
                        sh 'python3 hello.py'
                    } else {
                        bat 'echo "Running on Windows"'
                        bat 'javac HelloWorld.java'
                        bat 'java HelloWorld'
                        bat 'python hello.py'
                    }
                }
            }
        }
    }
}
```

### `hello.py`

```python
print("Hello, World from Jenkins Pipeline!")
```

### `HelloWorld.java`

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from Jenkins Pipeline!");
    }
}
```

> **Syntaxe Groovy importante :** on n'écrit pas `git clone ...` dans un Jenkinsfile. On utilise l'étape Git : `git branch: 'main', url: '...'`.

---

## Annexe 2 — Variantes du Jenkinsfile (pour information)

Si vous installez Jenkins **directement sur votre machine** (hors Docker), les chemins Java/Python diffèrent. Ces variantes sont fournies à titre de référence.

<details>
<summary>Version Windows (Jenkins installé sous Windows)</summary>

```groovy
pipeline {
    agent any
    environment {
        JAVA_HOME = 'C:\\Program Files\\Java\\jdk1.8.0_202'
        PYTHON_HOME = 'C:\\Users\\rehou\\AppData\\Local\\Microsoft\\WindowsApps'
        PATH = "${env.PATH};${JAVA_HOME}\\bin;${PYTHON_HOME}"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hrhouma/hello-python.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'echo "Running on Unix"'
                        sh 'javac HelloWorld.java'
                        sh 'java HelloWorld'
                        sh 'python3 hello.py'
                    } else {
                        bat 'echo "Running on Windows"'
                        bat 'javac HelloWorld.java'
                        bat 'java HelloWorld'
                        bat 'python hello.py'
                    }
                }
            }
        }
    }
}
```
</details>

<details>
<summary>Version Linux/Windows « 2 en 1 » (avec withEnv)</summary>

```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hrhouma/hello-python.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        withEnv([
                            "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64",
                            "PYTHON_HOME=/usr/bin",
                            "PATH=${env.PATH}:${JAVA_HOME}/bin:${PYTHON_HOME}"
                        ]) {
                            sh 'echo "Running on Unix"'
                            sh 'javac HelloWorld.java'
                            sh 'java HelloWorld'
                            sh 'python3 hello.py'
                        }
                    } else {
                        withEnv([
                            "JAVA_HOME=C:\\Program Files\\Java\\jdk1.8.0_202",
                            "PYTHON_HOME=C:\\Users\\rehou\\AppData\\Local\\Microsoft\\WindowsApps",
                            "PATH=${env.PATH};${JAVA_HOME}\\bin;${PYTHON_HOME}"
                        ]) {
                            bat 'echo "Running on Windows"'
                            bat 'javac HelloWorld.java'
                            bat 'java HelloWorld'
                            bat 'python hello.py'
                        }
                    }
                }
            }
        }
    }
}
```
</details>

---

## Annexe 3 — Trouver les emplacements de Java et Python

**Dans le conteneur Docker (Linux) :**

```bash
docker exec jenkins-tp which git       # /usr/bin/git
docker exec jenkins-tp which java       # chemin du JDK de l'image
docker exec jenkins-tp which javac
docker exec jenkins-tp which python3    # /usr/bin/python3
```

**Sur une machine Linux (Ubuntu), si vous installez Jenkins sans Docker :**

```bash
sudo apt-get update
sudo apt-get install openjdk-8-jdk
which java     # /usr/bin/java
which javac    # /usr/bin/javac
which python3  # /usr/bin/python3
```

**Sur Windows (terminal) :**

```bat
for %i in (java.exe) do @echo.   %~$PATH:i
for %i in (python.exe) do @echo.   %~$PATH:i
```

---

## Références

- [Jenkins could not run git](https://stackoverflow.com/questions/8639501/jenkins-could-not-run-git)
- [Execute a python script from git via Jenkins](https://stackoverflow.com/questions/56291513/execute-a-python-script-that-is-on-my-git-via-jenkins)
- [unix which java equivalent on windows](https://stackoverflow.com/questions/3454424/unix-which-java-equivalent-command-on-windows)

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
