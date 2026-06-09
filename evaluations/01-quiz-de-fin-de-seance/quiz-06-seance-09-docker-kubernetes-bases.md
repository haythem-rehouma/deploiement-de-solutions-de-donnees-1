<a id="top"></a>

# Quiz — Séance 9 — Docker, Nginx, Swarm et bases de Kubernetes

> **Évaluation sommative** · Quiz de fin de séance 9 (4 août 2026) · Pondération 1 % · QCM individuel en fin de séance
>
> **Contenus évalués :** Docker (images, conteneurs, Dockerfile, volumes, réseaux) · Nginx reverse proxy et load balancer · Docker Swarm · bases de Kubernetes (pods, Deployments, Services)

---

**Question 1 :** Quelle est la différence fondamentale entre une image Docker et un conteneur ?

a) Aucune, ce sont deux mots pour la même chose

b) L'image est le modèle figé (read-only) ; le conteneur est une instance en cours d'exécution de cette image

c) Le conteneur est le modèle figé ; l'image est l'instance en exécution

d) L'image s'exécute, le conteneur se stocke sur Docker Hub

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — L'image est un gabarit en lecture seule (couches empilées) ; le conteneur est une instance vivante créée à partir de l'image, avec sa propre couche d'écriture éphémère.

</details>

---

**Question 2 :** Dans un Dockerfile, quelle instruction définit la commande exécutée par défaut au démarrage du conteneur ?

a) `RUN`

b) `COPY`

c) `CMD`

d) `FROM`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `CMD` (ou `ENTRYPOINT`) fixe la commande lancée au démarrage. `RUN` exécute des commandes pendant la construction de l'image, `FROM` choisit l'image de base et `COPY` ajoute des fichiers.

</details>

---

**Question 3 :** Que deviennent les données écrites dans le système de fichiers d'un conteneur après un `docker rm`, si aucun volume n'a été monté ?

a) Elles sont définitivement perdues

b) Elles sont sauvegardées automatiquement dans l'image

c) Elles sont poussées sur Docker Hub

d) Elles passent dans le réseau bridge

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — La couche d'écriture du conteneur est éphémère. Sans volume ni bind mount, supprimer le conteneur efface ses données. C'est pourquoi on utilise un volume pour une base de données.

</details>

---

**Question 4 :** Pourquoi créer un réseau bridge **personnalisé** plutôt que d'utiliser le bridge par défaut ?

a) Pour consommer moins de mémoire

b) Parce que le bridge par défaut est désactivé

c) Parce qu'il fournit une résolution DNS interne : les conteneurs se joignent par leur nom

d) Pour exposer automatiquement tous les ports

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Sur un réseau bridge personnalisé, Docker fournit un DNS interne ; un conteneur peut joindre un autre par son nom (ex. `bd`) au lieu de devoir connaître son adresse IP.

</details>

---

**Question 5 :** Placé devant plusieurs instances d'une application, quel rôle Nginx joue-t-il lorsqu'il répartit les requêtes entrantes entre ces instances ?

a) Base de données

b) Reverse proxy faisant office de load balancer (répartiteur de charge)

c) Système d'orchestration de conteneurs

d) Registre d'images

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — En reverse proxy, Nginx reçoit les requêtes des clients et les distribue (load balancing) vers plusieurs serveurs applicatifs en amont (bloc `upstream`), tout en masquant l'architecture interne.

</details>

---

**Question 6 :** Dans Docker Swarm, quel terme désigne le nombre de copies identiques d'un service que l'on souhaite faire tourner ?

a) Les nodes

b) Les managers

c) Les répliques (`replicas`)

d) Les volumes

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — On déclare un nombre de **répliques** (`replicas`) ; Swarm crée autant de tâches (conteneurs) et les maintient automatiquement, redémarrant celles qui tombent (auto-réparation).

</details>

---

**Question 7 :** Dans Kubernetes, quelle est l'unité de déploiement la plus petite, qui encapsule un ou plusieurs conteneurs partageant le réseau et le stockage ?

a) Le Service

b) Le Pod

c) Le Deployment

d) Le Node

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le **Pod** est la plus petite unité déployable de Kubernetes. Il regroupe un ou plusieurs conteneurs partageant la même adresse IP et les mêmes volumes. Un Deployment gère un ensemble de Pods identiques.

</details>

---

**Question 8 :** Comment un Service Kubernetes sait-il vers quels Pods router le trafic ?

a) Par les adresses IP fixes des Pods

b) Par l'ordre de création des Pods

c) Grâce au couple labels/selector : il cible les Pods portant les labels correspondants

d) En lisant le Dockerfile des Pods

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le Service utilise un `selector` qui correspond aux **labels** des Pods (ex. `app=web`). Les IP des Pods étant changeantes, c'est l'étiquetage (label/selector) qui relie Service et Pods, jamais une IP fixe.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
