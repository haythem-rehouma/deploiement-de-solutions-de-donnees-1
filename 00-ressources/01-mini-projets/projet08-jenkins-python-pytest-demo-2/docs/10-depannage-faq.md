# Chapitre 10 - Dépannage (FAQ)

Les problèmes les plus courants et leurs solutions.

## Problèmes en local (Python)

### `python n'est pas reconnu`

Python n'est pas installé, ou « Add to PATH » n'a pas été coché. Réinstalle (voir
[Chapitre 2](02-installer-les-outils.md)). Essaie aussi `py --version`.

### PowerShell refuse d'activer le venv (« execution policy »)

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### `pytest n'est pas reconnu`

Ton venv n'est pas activé, ou les dépendances ne sont pas installées :

```powershell
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Problèmes avec Docker / Jenkins

### `docker : command not found` ou `Cannot connect to the Docker daemon`

Docker Desktop n'est pas lancé. Ouvre-le et attends qu'il soit « running », puis réessaie.

### `docker compose up` échoue au build

- Vérifie ta connexion internet (l'image télécharge des paquets).
- Relance : `docker compose up -d --build`.
- Regarde l'erreur exacte : `docker compose logs`.

### Je n'arrive pas à ouvrir http://localhost:8080

- Vérifie que le conteneur tourne : `docker ps` (cherche `jenkins-demo`).
- Attends une minute : Jenkins met du temps à démarrer la première fois.
- Regarde les logs : `docker logs -f jenkins-demo`.

### Je ne trouve pas le mot de passe initial

```powershell
docker exec jenkins-demo cat /var/jenkins_home/secrets/initialAdminPassword
```

Si « No such file », attends que Jenkins finisse de démarrer et réessaie.

## Problèmes dans le pipeline Jenkins

### Stage « Setup Python » : `python3: not found`

Cela veut dire que Jenkins ne tourne pas avec notre image personnalisée. Assure-toi d'avoir
lancé Jenkins via `docker compose up -d --build` (et pas une image Jenkins standard).

### Stage « Build & Push » : `docker: not found` ou erreur de socket

- Le client Docker doit être présent (il l'est dans notre image) **et** le socket monté.
- Vérifie dans `docker-compose.yml` la ligne
  `- /var/run/docker.sock:/var/run/docker.sock`.
- Sur Windows/WSL2, assure-toi que Docker Desktop expose bien le socket (option activée par
  défaut).

### Stage « Build & Push » : `unauthorized` / login refusé

Le problème vient des credentials :
- Vérifie que l'ID des credentials est **exactement** `dockerhub`.
- Vérifie que le token Docker Hub a les droits **« Read & Write »**.
- Recrée un token si besoin et mets à jour les credentials.

### Le stage « Build & Push » est ignoré (skipped)

C'est **normal** si :
- un stage précédent (Test) a échoué, ou
- la branche n'est pas `main` (`when { branch 'main' }`).

### Comment déclencher Jenkins automatiquement à chaque push ?

- **Simple (polling)** : config du job -> « Build Triggers » -> « Poll SCM » -> `H/2 * * * *`.
- **Instantané (webhook)** : il faut que Jenkins soit joignable depuis internet. En local,
  utilise **ngrok** :
  ```powershell
  ngrok http 8080
  ```
  puis configure un webhook GitHub (`Settings > Webhooks`) vers
  `https://<ton-ngrok>/github-webhook/`.

## Toujours bloqué ?

- Relis le chapitre concerné, lentement.
- Copie le message d'erreur exact dans un moteur de recherche.
- Consulte le [Glossaire](glossaire.md).
