# Aide-mémoire complet — Docker + Nginx + Swarm

> Ouvrez un terminal **dans ce dossier** (`projet01-docker-nginx-swarm`).
> Interface web du projet : **http://localhost:8088**

## Table des matières

| # | Section |
|---|---|
| 1 | [Vérifier que Docker est prêt](#1-verifier-que-docker-est-pret) |
| 2 | [Démarrer / arrêter (mode Compose)](#2-demarrer--arreter-mode-compose) |
| 3 | [Tester la répartition de charge](#3-tester-la-repartition-de-charge) |
| 4 | [Manipuler DANS les conteneurs (`docker exec`)](#4-manipuler-dans-les-conteneurs-docker-exec) |
| 5 | [Changer l'arrière-plan de la page](#5-changer-larriere-plan-de-la-page) |
| 6 | [Commandes Nginx à connaître](#6-commandes-nginx-a-connaitre) |
| 7 | [Logs et diagnostic](#7-logs-et-diagnostic) |
| 8 | [Mode Swarm (cluster)](#8-mode-swarm-cluster) |
| 9 | [Nettoyage](#9-nettoyage) |

---

## 1. Vérifier que Docker est prêt

```bash
docker --version
docker compose version
docker info                 # doit repondre sans erreur (moteur demarre)
```

---

## 2. Démarrer / arrêter (mode Compose)

- La URL à tester dans le navigateur est la suivante : http://localhost:8088/
```bash
# Demarrer avec 3 repliques (construit l'image la 1ere fois)
docker compose up -d --build --scale web=3

# Etat des conteneurs du projet
docker compose ps

# Changer le nombre de repliques a chaud
docker compose up -d --scale web=5

# Redemarrer un service
docker compose restart nginx

# Arreter (garde les images) / tout supprimer
docker compose down
```

> `-d` = arrière-plan (*detached*). Sans `-d`, les logs défilent dans le terminal (Ctrl+C pour quitter).

---

## 3. Tester la répartition de charge

```bash
# En ligne de commande (le nom du conteneur doit CHANGER d'une fois a l'autre)
curl -H "Accept: application/json" http://localhost:8088/

# Boucle de 6 requetes (PowerShell)
1..6 | ForEach-Object { (Invoke-WebRequest http://localhost:8088/ -Headers @{Accept='application/json'} -UseBasicParsing).Content }

# Boucle de 6 requetes (bash / macOS / Linux)
for i in $(seq 6); do curl -s -H "Accept: application/json" http://localhost:8088/; echo; done
```

Dans le **navigateur** : ouvrez http://localhost:8088 et rechargez (Ctrl+R).

---

## 4. Manipuler DANS les conteneurs (`docker exec`)

```bash
# Lister les conteneurs (repere les noms/ID)
docker ps

# Ouvrir un shell interactif dans un conteneur web (image slim => bash present)
docker exec -it projet01-docker-nginx-swarm-web-1 bash

# Si "bash" absent (images alpine comme nginx), utilisez sh :
docker exec -it projet01-docker-nginx-swarm-nginx-1 sh
```

Une fois **à l'intérieur** du conteneur, essayez :

```bash
hostname                 # le nom du conteneur (celui affiche sur la page !)
ls -l                    # fichiers de l'app (/app)
cat app.py               # le code de l'application
env | sort               # variables d'environnement (dont BG_COLOR)
ps aux                   # processus qui tournent dans le conteneur
whoami                   # utilisateur courant
exit                     # quitter le conteneur
```

Sans entrer dans le conteneur (commande unique) :

```bash
docker exec projet01-docker-nginx-swarm-web-1 hostname
docker exec projet01-docker-nginx-swarm-web-1 env
docker exec projet01-docker-nginx-swarm-web-1 python -c "print('coucou depuis le conteneur')"
```

> **À retenir :** `docker exec -it <conteneur> <commande>` exécute une commande dans un conteneur **déjà démarré**. `-i` = interactif, `-t` = terminal.

---

## 5. Changer l'arrière-plan de la page

La couleur de fond est pilotée par la variable d'environnement **`BG_COLOR`** (lue par `app.py`).

### Méthode A — via `docker-compose.yml` (recommandée)

Modifiez la valeur dans `docker-compose.yml` :

```yaml
    environment:
      BG_COLOR: "#7c3aed"     # violet (essayez #b91c1c rouge, #047857 vert...)
```

Puis appliquez :

```bash
docker compose up -d --scale web=3
```

Rechargez http://localhost:8088 : le fond a changé.

### Méthode B — à la volée, sans éditer le fichier

```bash
# PowerShell
$env:BG_COLOR="#b91c1c"; docker compose up -d --scale web=3

# bash / macOS / Linux
BG_COLOR="#047857" docker compose up -d --scale web=3
```

> Pour que ça marche, `docker-compose.yml` peut aussi s'écrire `BG_COLOR: "${BG_COLOR:-#0f172a}"` (prend la variable du terminal, sinon la valeur par défaut).

### Méthode C — changer le code puis reconstruire

Éditez le HTML/CSS dans `app/app.py`, puis **reconstruisez l'image** :

```bash
docker compose up -d --build --scale web=3
```

> **Pourquoi rebuild ?** Le code est **figé dans l'image** au moment du `build`. Modifier `app.py` sur votre PC n'a d'effet qu'après un nouveau `--build` (le conteneur ne voit pas vos fichiers en direct, sauf *bind mount*).

---

## 6. Commandes Nginx à connaître

Nginx tourne dans le conteneur `...-nginx-1`. Sa config est montée depuis `nginx/nginx.conf`.

```bash
# Voir la configuration active
docker exec projet01-docker-nginx-swarm-nginx-1 cat /etc/nginx/nginx.conf

# TESTER la syntaxe de la config (indispensable avant de recharger)
docker exec projet01-docker-nginx-swarm-nginx-1 nginx -t

# RECHARGER Nginx sans couper le service (applique une nouvelle config)
docker exec projet01-docker-nginx-swarm-nginx-1 nginx -s reload

# Version de Nginx
docker exec projet01-docker-nginx-swarm-nginx-1 nginx -v
```

**Modifier la config puis l'appliquer** (le fichier est monté en *bind mount*, donc éditer `nginx/nginx.conf` sur votre PC suffit) :

```bash
# 1. editez nginx/nginx.conf
# 2. verifiez la syntaxe
docker exec projet01-docker-nginx-swarm-nginx-1 nginx -t
# 3. rechargez
docker exec projet01-docker-nginx-swarm-nginx-1 nginx -s reload
```

Notions Nginx clés (voir la [leçon 04](../04-nginx-reverse-proxy.md)) :

| Directive | Rôle |
|---|---|
| `server { listen 80; }` | un serveur virtuel qui écoute un port |
| `location / { ... }` | règles pour une URL |
| `proxy_pass http://web:5000;` | **reverse proxy** vers le service `web` |
| `resolver 127.0.0.11;` | DNS interne Docker (pour la **répartition de charge**) |
| `upstream nom { server a; server b; }` | groupe de backends (round-robin) |

---

## 7. Logs et diagnostic

```bash
# Logs de tous les services (suivi en direct)
docker compose logs -f

# Logs d'un seul service
docker compose logs -f nginx
docker compose logs -f web

# Ressources consommees en temps reel
docker stats

# Inspecter un conteneur (IP, montages, variables...)
docker inspect projet01-docker-nginx-swarm-web-1

# Reseaux et volumes
docker network ls
docker volume ls
```

---

## 8. Mode Swarm (cluster)

```bash
# 1. Construire l'image (Swarm ne construit pas)
docker compose build

# 2. Initialiser le cluster (une seule fois)
docker swarm init

# 3. Deployer le stack (3 repliques web + 1 nginx)
docker stack deploy -c docker-stack.yml demo

# 4. Observer
docker stack services demo         # web 3/3, nginx 1/1
docker service ps demo_web          # les taches (repliques)

# 5. Mise a l'echelle
docker service scale demo_web=5

# 6. Auto-reparation : supprimez une replique, Swarm la recree
docker ps --filter name=demo_web
docker rm -f <id_conteneur_web>
docker service ps demo_web

# 7. Arreter
docker stack rm demo
docker swarm leave --force          # quitter Swarm (optionnel)
```

---

## 9. Nettoyage

```bash
docker compose down                 # arrete ce projet (mode Compose)
docker stack rm demo                # arrete le stack (mode Swarm)

# Nettoyage global Docker (attention : supprime tout ce qui est inutilise)
docker system prune -f              # conteneurs/reseaux/images pendantes
docker image rm demo-web:1.0        # supprimer l'image du projet
```

## Changer le port publié

Si **8088** est occupé, modifiez `8088:80` dans `docker-compose.yml` **et** `docker-stack.yml` (ex. `9090:80`), puis relancez.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
