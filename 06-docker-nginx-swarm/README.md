# Module 06 — Docker, Nginx et Swarm

Sixième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il couvre la conteneurisation avec **Docker**, l'exposition des applications avec **Nginx** (reverse proxy et répartition de charge), puis l'orchestration multi-machines avec **Docker Swarm**.

## Objectifs

À la fin de ce module, vous serez capable de :

- Distinguer **conteneurs et machines virtuelles**, **images et conteneurs**, et utiliser les commandes de base (`run`, `ps`, `stop`, `rm`, `pull`, `images`, `exec`).
- Écrire un **Dockerfile** (FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT), **construire une image** et appliquer les bonnes pratiques (couches, `.dockerignore`, multi-stage).
- **Persister des données** (volumes, bind mounts), connecter des conteneurs via les **réseaux** et tout orchestrer avec **docker-compose**.
- Configurer **Nginx** en reverse proxy (`server`, `location`, `proxy_pass`) et en **répartiteur de charge** (`upstream`, round-robin).
- **Orchestrer** un cluster avec **Docker Swarm** : `swarm init`, `join`, `docker stack deploy`, services et mise à l'échelle.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Images et conteneurs](01-images-et-conteneurs.md) | Conteneurs vs VM, image vs conteneur, registry, `run`/`ps`/`stop`/`rm`/`pull`/`exec` |
| 02 | [Dockerfile](02-dockerfile.md) | FROM, RUN, COPY, WORKDIR, EXPOSE, CMD, ENTRYPOINT, `build`, couches, `.dockerignore`, multi-stage |
| 03 | [Volumes et réseaux](03-volumes-et-reseaux.md) | Volumes, bind mounts, réseaux (bridge/host/custom), docker-compose |
| 04 | [Nginx : reverse proxy et répartition de charge](04-nginx-reverse-proxy.md) | server/location/proxy_pass, upstream, round-robin |
| 05 | [Docker Swarm](05-docker-swarm.md) | swarm init/join, stack deploy, services, scaling, auto-réparation |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** et exemples concrets (Dockerfile, commandes `docker`, `nginx.conf`, YAML compose/stack) ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique obligatoire** avec correction détaillée ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
