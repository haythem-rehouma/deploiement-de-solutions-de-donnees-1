<a id="top"></a>

# Quiz ciblé — Comprendre le projet Docker + Nginx + Swarm

> **Projet [projet01-docker-nginx-swarm](README.md)** · 25 questions d'auto-évaluation
>
> Ces questions portent **précisément sur les fichiers de CE projet** (`docker-compose.yml`, `docker-stack.yml`, `nginx/nginx.conf`, `app/app.py`). Répondez **avant** de dérouler le `Corrigé`. Les bonnes réponses sont réparties entre A, B, C et D.

## Table des matières

| Thème | Questions |
|---|---|
| [A — Structure et rôle des fichiers](#a--structure-et-role-des-fichiers) | 1 à 5 |
| [B — L'application et la variable `BG_COLOR`](#b--lapplication-et-la-variable-bg_color) | 6 à 11 |
| [C — Nginx (reverse proxy + répartition)](#c--nginx-reverse-proxy--repartition) | 12 à 16 |
| [D — docker-compose (mode dev)](#d--docker-compose-mode-dev) | 17 à 20 |
| [E — docker-stack et Swarm](#e--docker-stack-et-swarm) | 21 à 25 |
| [Corrigé récapitulatif](#corrige-recapitulatif) | — |

---

## A — Structure et rôle des fichiers

**1.** Dans ce projet, quel fichier sert au **mode dev (une seule machine)** ?

- A) `docker-stack.yml`
- B) `docker-compose.yml`
- C) `nginx/nginx.conf`
- D) `app/Dockerfile`

<details><summary>Corrigé</summary>

**B.** `docker-compose.yml` est utilisé pour le mode **Compose** (une machine, avec `--scale`). `docker-stack.yml` sert au mode **Swarm**.
</details>

**2.** À quoi sert le dossier `app/` ?

- A) À stocker la configuration Nginx
- B) À contenir l'application web (Flask) et son `Dockerfile`
- C) À conserver les logs
- D) À définir le cluster Swarm

<details><summary>Corrigé</summary>

**B.** `app/` contient `app.py`, `requirements.txt`, `Dockerfile`, `.dockerignore` : c'est l'**application** construite en image.
</details>

**3.** Que fait concrètement l'application web du projet ?

- A) Elle affiche l'heure du serveur
- B) Elle calcule des opérations mathématiques
- C) Elle affiche **le nom (hostname) du conteneur** qui répond
- D) Elle renvoie une erreur 500

<details><summary>Corrigé</summary>

**C.** Elle affiche le **hostname** : en lançant plusieurs répliques, on voit le nom changer → preuve de la répartition de charge.
</details>

**4.** Sur quel **port de l'hôte** l'application est-elle accessible dans ce projet ?

- A) 8080
- B) 5000
- C) 80
- D) 8088

<details><summary>Corrigé</summary>

**D.** **8088** (mappé sur le port 80 de Nginx : `8088:80`). Le port 8080 a été évité à cause d'un conflit sur le poste.
</details>

**5.** Quels sont les **deux services** définis dans ce projet ?

- A) `web` et `nginx`
- B) `app` et `proxy`
- C) `jenkins` et `maven`
- D) `client` et `serveur`

<details><summary>Corrigé</summary>

**A.** `web` (l'app Flask, en répliques) et `nginx` (le reverse proxy / répartiteur).
</details>

---

## B — L'application et la variable `BG_COLOR`

**6.** À quoi sert la variable d'environnement **`BG_COLOR`** ?

- A) À choisir le port d'écoute
- B) À définir la **couleur de fond** de la page affichée par l'app
- C) À nommer le conteneur
- D) À activer Swarm

<details><summary>Corrigé</summary>

**B.** `app.py` lit `BG_COLOR` pour colorer le fond de la page HTML.
</details>

**7.** Dans `app.py`, comment la valeur par défaut de `BG_COLOR` est-elle définie si la variable n'existe pas ?

- A) `os.environ["BG_COLOR"]`
- B) `os.environ.get("BG_COLOR", "#0f172a")`
- C) `input("BG_COLOR")`
- D) Elle plante

<details><summary>Corrigé</summary>

**B.** `os.environ.get("BG_COLOR", "#0f172a")` : renvoie la valeur si présente, sinon `#0f172a` (bleu nuit).
</details>

**8.** Dans `docker-compose.yml`, la ligne `BG_COLOR: "${BG_COLOR:-#0f172a}"` signifie :

- A) Toujours utiliser `#0f172a`
- B) Prendre la variable `BG_COLOR` **du terminal** si définie, **sinon** `#0f172a`
- C) Ignorer la variable
- D) Générer une couleur aléatoire

<details><summary>Corrigé</summary>

**B.** La syntaxe `${VAR:-defaut}` prend la variable de l'environnement, avec une **valeur par défaut**.
</details>

**9.** Après avoir changé `BG_COLOR` dans `docker-compose.yml`, quelle commande applique le changement ?

- A) `docker compose up -d --scale web=3`
- B) `nginx -s reload`
- C) `docker build`
- D) `git push`

<details><summary>Corrigé</summary>

**A.** On relance `docker compose up -d --scale web=3` : Compose recrée les conteneurs `web` avec la nouvelle variable.
</details>

**10.** Pour tester la couleur **à la volée** (PowerShell), sans éditer le fichier, on écrit :

- A) `set BG_COLOR red`
- B) `$env:BG_COLOR="#b91c1c"; docker compose up -d --scale web=3`
- C) `docker run BG_COLOR`
- D) `export BG_COLOR=#b91c1c`

<details><summary>Corrigé</summary>

**B.** En PowerShell, `$env:BG_COLOR="..."` définit la variable, puis Compose la récupère grâce à `${BG_COLOR:-...}`. *(En bash on utiliserait `export`/préfixe de commande.)*
</details>

**11.** Si je modifie **le code Python** de `app.py`, que faut-il faire pour que le conteneur en tienne compte ?

- A) Rien, c'est automatique
- B) Recharger Nginx
- C) **Reconstruire l'image** avec `docker compose up -d --build`
- D) Redémarrer l'ordinateur

<details><summary>Corrigé</summary>

**C.** Le code est **figé dans l'image** au build. Sans *bind mount*, il faut `--build` pour reconstruire (contrairement à une **variable d'env**, modifiable sans rebuild).
</details>

---

## C — Nginx (reverse proxy + répartition)

**12.** Dans `nginx.conf`, que fait `proxy_pass $backend;` où `$backend = http://web:5000` ?

- A) Sert un fichier local
- B) **Transmet** la requête au service `web` sur le port 5000
- C) Bloque la requête
- D) Redémarre Nginx

<details><summary>Corrigé</summary>

**B.** C'est le **reverse proxy** : Nginx relaie vers l'app `web:5000`.
</details>

**13.** Pourquoi la ligne `resolver 127.0.0.11;` est-elle présente ?

- A) C'est l'adresse de l'app
- B) C'est le **DNS interne de Docker**, nécessaire pour re-résoudre `web` et répartir la charge entre répliques
- C) Pour chiffrer le trafic
- D) Pour ouvrir le port 8088

<details><summary>Corrigé</summary>

**B.** `127.0.0.11` est le résolveur DNS intégré de Docker ; combiné à la variable `$backend`, il permet le **load balancing**.
</details>

**14.** Pourquoi passer par une **variable** `$backend` au lieu d'écrire directement l'URL dans `proxy_pass` ?

- A) Pour faire plus court
- B) Parce que sinon Nginx **fige une seule IP** au démarrage et ne répartit pas entre les répliques
- C) Parce que c'est obligatoire en YAML
- D) Pour désactiver le proxy

<details><summary>Corrigé</summary>

**B.** Avec une valeur littérale, Nginx résout **une fois**. La variable + `resolver` forcent une **re-résolution** régulière.
</details>

**15.** Le service `web` utilise `expose: "5000"` et **non** `ports`. Pourquoi ?

- A) Pour publier 5000 sur l'hôte
- B) Pour que **seul Nginx** (dans le réseau Docker) accède à `web:5000`, sans l'exposer au monde extérieur
- C) Parce que `ports` est interdit
- D) Pour accélérer le build

<details><summary>Corrigé</summary>

**B.** `expose` rend le port accessible **en interne** seulement ; le public passe par Nginx (port 8088).
</details>

**16.** Après avoir modifié `nginx/nginx.conf`, quelle est la bonne séquence ?

- A) `docker build` puis `git push`
- B) `nginx -t` (tester) puis `nginx -s reload` (recharger)
- C) `docker rm` puis `docker run`
- D) Rien à faire

<details><summary>Corrigé</summary>

**B.** On **teste** la syntaxe (`nginx -t`) puis on **recharge** sans coupure (`nginx -s reload`). Le fichier étant monté en *bind mount*, l'édition sur l'hôte suffit.
</details>

---

## D — docker-compose (mode dev)

**17.** Quelle commande lance le projet avec **3 répliques** de `web` ?

- A) `docker compose up -d --scale web=3`
- B) `docker stack deploy web=3`
- C) `docker run --replicas 3`
- D) `docker compose scale=3`

<details><summary>Corrigé</summary>

**A.** `docker compose up -d --scale web=3`.
</details>

**18.** Pourquoi le service `web` n'a-t-il **pas** de `container_name` ?

- A) Par oubli
- B) Parce qu'un nom fixe **empêcherait** de lancer plusieurs répliques (chaque conteneur doit avoir un nom unique)
- C) Parce que c'est interdit avec Nginx
- D) Pour cacher le conteneur

<details><summary>Corrigé</summary>

**B.** Avec `container_name`, une seule instance est possible : incompatible avec `--scale`.
</details>

**19.** La clé `image: demo-web:1.0` dans `docker-compose.yml` sert notamment à :

- A) Télécharger une image officielle
- B) **Nommer l'image construite** pour pouvoir la **réutiliser en Swarm** (`docker-stack.yml`)
- C) Publier un port
- D) Définir la couleur

<details><summary>Corrigé</summary>

**B.** Le tag `demo-web:1.0` est réutilisé par le stack Swarm, qui ne construit pas l'image lui-même.
</details>

**20.** Que fait `docker compose ps` dans ce projet ?

- A) Liste toutes les images Docker du système
- B) Affiche les **conteneurs du projet** (répliques `web` + `nginx`) et leur état
- C) Supprime les conteneurs
- D) Recharge Nginx

<details><summary>Corrigé</summary>

**B.** Il liste les conteneurs gérés par ce `docker-compose.yml`.
</details>

---

## E — docker-stack et Swarm

**21.** Pour déployer le projet en Swarm, quelle est la **bonne séquence** ?

- A) `docker compose up` puis `docker swarm init`
- B) `docker swarm init` puis `docker stack deploy -c docker-stack.yml demo`
- C) `docker stack deploy` puis `docker build`
- D) `docker service create` uniquement

<details><summary>Corrigé</summary>

**B.** On **initialise** le cluster (`docker swarm init`) **puis** on déploie le stack. (Il faut aussi avoir construit l'image `demo-web:1.0` au préalable.)
</details>

**22.** Dans `docker-stack.yml`, où est déclaré le **nombre de répliques** de `web` ?

- A) `ports: 3`
- B) `scale: 3`
- C) `deploy: { replicas: 3 }`
- D) `environment: REPLICAS=3`

<details><summary>Corrigé</summary>

**C.** `deploy.replicas: 3`. En Swarm, on **déclare** l'état voulu (au lieu du `--scale` de Compose).
</details>

**23.** La clé `deploy:` de `docker-stack.yml` est :

- A) Utilisée par `docker compose` en mode dev
- B) **Ignorée** par `docker compose` et **utilisée** par Swarm (`docker stack deploy`)
- C) Obligatoire dans tous les Dockerfile
- D) Une directive Nginx

<details><summary>Corrigé</summary>

**B.** C'est pour ça qu'on a **deux fichiers** : `deploy` (replicas, restart_policy, update_config) ne sert qu'à Swarm.
</details>

**24.** Le stack est déployé sous le nom `demo`. Quelle commande met le service `web` à **5 répliques** ?

- A) `docker compose up --scale web=5`
- B) `docker service scale demo_web=5`
- C) `docker stack scale 5`
- D) `docker run -n 5 demo`

<details><summary>Corrigé</summary>

**B.** En Swarm, le service se nomme `<stack>_<service>` → `demo_web`. Donc `docker service scale demo_web=5`.
</details>

**25.** Grâce à `restart_policy: { condition: on-failure }`, si un conteneur `web` plante :

- A) Le cluster entier s'arrête
- B) Rien, il reste mort
- C) Swarm **recrée automatiquement** une réplique pour maintenir l'état déclaré (auto-réparation)
- D) Il faut refaire `stack deploy`

<details><summary>Corrigé</summary>

**C.** Swarm assure l'**auto-réparation** : il maintient en permanence le nombre de répliques demandé.
</details>

---

<a id="corrige-recapitulatif"></a>

## Corrigé récapitulatif

| Q | Rép | Q | Rép | Q | Rép | Q | Rép | Q | Rép |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 6 | B | 11 | C | 16 | B | 21 | B |
| 2 | B | 7 | B | 12 | B | 17 | A | 22 | C |
| 3 | C | 8 | B | 13 | B | 18 | B | 23 | B |
| 4 | D | 9 | A | 14 | B | 19 | B | 24 | B |
| 5 | A | 10 | B | 15 | B | 20 | B | 25 | C |

**Barème indicatif :** 1 point par question sur 25.

| Score | Niveau |
|---|---|
| 22–25 | Excellent — vous maîtrisez le projet |
| 17–21 | Bien — quelques détails à revoir |
| 12–16 | Moyen — relisez le `README.md` et `COMMANDES.md` |
| < 12 | À retravailler — refaites les manipulations |

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
