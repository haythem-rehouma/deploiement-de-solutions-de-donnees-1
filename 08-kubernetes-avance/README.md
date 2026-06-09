# Module 08 — Kubernetes : concepts avancés

Huitième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Après les bases de Kubernetes (Pods, Deployments, Services), ce module aborde l'**exposition réseau avancée** et la **gestion de la configuration** : Ingress (routage HTTP L7), ConfigMaps, Secrets et Service LoadBalancer dans le cloud.

## Objectifs

À la fin de ce module, vous serez capable de :

- Mettre en place un **Ingress** et un **Ingress Controller** pour router le trafic HTTP/HTTPS par host et par path, avec terminaison TLS.
- Externaliser la configuration d'une application avec des **ConfigMaps** (variables d'environnement et volumes montés).
- Gérer les données sensibles avec des **Secrets**, comprendre les limites de base64 et sécuriser via **RBAC** et **chiffrement at rest**.
- Distinguer **ConfigMap** et **Secret** et savoir lequel utiliser.
- Exposer une application sur Internet avec un **Service LoadBalancer** et comprendre l'intégration cloud (AWS / GCP / Azure), le provisionnement automatique, les coûts.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Ingress et routage HTTP (L7)](01-ingress.md) | Ingress Controller (nginx), règles host/path, TLS, vs LoadBalancer |
| 02 | [ConfigMaps : configuration externalisée](02-configmaps.md) | Création, env vars, volumes montés, bonnes pratiques |
| 03 | [Secrets : données sensibles](03-secrets.md) | base64, consommation, RBAC, chiffrement at rest, vs ConfigMap |
| 04 | [Service LoadBalancer dans le cloud](04-cloud-loadbalancer.md) | Provisionnement auto, AWS/GCP/Azure, coûts, vs Ingress |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** et manifestes **YAML** ;
- des exemples **`kubectl`** réalistes ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
