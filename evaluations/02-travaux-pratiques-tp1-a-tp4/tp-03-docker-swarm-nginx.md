<a id="top"></a>

# TP3 — Docker, Swarm et Nginx

> **Travail pratique noté** · Pondération **5 %** · Remise : **dimanche 2 août 2026** (fin de journée, en ligne) · **Travail individuel**
>
> **Module couvert :** [06 — Docker, Nginx et Swarm](../../06-docker-nginx-swarm/README.md)

---

## Objectifs

À la fin de ce TP, vous serez capable de :

- Écrire un **Dockerfile** et construire une image d'application.
- Gérer la persistance (volumes) et la communication entre conteneurs (réseaux).
- Configurer **Nginx** en reverse proxy / répartiteur de charge.
- Déployer un **mini stack** sur un cluster **Docker Swarm** et le mettre à l'échelle.

---

## Contexte

Vous conteneurisez une application simple (la vôtre ou une app web fournie), puis vous la placez derrière Nginx et la déployez en Swarm avec plusieurs répliques.

---

## Consignes (étapes)

1. **Image Docker**
   - Écrivez un **`Dockerfile`** (idéalement multi-stage) pour votre application.
   - Construisez l'image (`docker build -t mon-app:1.0 .`) et testez un conteneur (`docker run`).

2. **Volumes & réseaux**
   - Ajoutez une persistance (volume nommé) si l'app a des données.
   - Créez un réseau personnalisé et faites communiquer 2 conteneurs (ex. app + base).

3. **Nginx reverse proxy**
   - Configurez Nginx (`nginx.conf`) avec un `upstream` et `proxy_pass`.
   - Mettez **au moins 2 instances** de l'app derrière Nginx (répartition de charge).

4. **Docker Swarm**
   - Initialisez un cluster (`docker swarm init`).
   - Rédigez un fichier `stack.yml` et déployez (`docker stack deploy`).
   - Mettez le service à l'échelle (`docker service scale … =3`) et vérifiez l'auto-réparation.

---

## Livrables attendus

| Livrable | Détail |
|---|---|
| **`Dockerfile`** | Versionné, fonctionnel (build sans erreur) |
| **`nginx.conf`** | Reverse proxy + `upstream` de répartition de charge |
| **`stack.yml`** | Déploiement Swarm avec répliques |
| **Captures** | `docker service ls`, requêtes réparties sur plusieurs instances |
| **Fichier `REPONSES.md`** | Commandes utilisées + explications + captures |

---

## Barème de correction (sur 5 %)

| Critère | Pondération |
|---|---|
| `Dockerfile` correct + image construite | 1 % |
| Volumes et/ou réseau personnalisé fonctionnels | 1 % |
| Nginx reverse proxy + répartition de charge | 1,5 % |
| Déploiement Swarm + mise à l'échelle | 1 % |
| `REPONSES.md` (captures + explications) | 0,5 % |

---

## Conseils

> _Utilisez un `.dockerignore` pour des images légères, et testez chaque conteneur isolément avant de tout assembler. En Swarm, `docker service ps <service>` est votre meilleur outil de diagnostic._

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
