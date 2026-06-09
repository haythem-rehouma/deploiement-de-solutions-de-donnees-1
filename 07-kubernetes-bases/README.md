# Module 07 — Kubernetes : concepts de base

Septième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Après Docker, ce module introduit **Kubernetes (K8s)**, l'orchestrateur qui automatise le déploiement, la mise à l'échelle et la résilience des applications conteneurisées.

## Objectifs

À la fin de ce module, vous serez capable de :

- Expliquer le rôle de **Kubernetes** et son **architecture** (control plane vs nodes).
- Démarrer un **cluster local** (minikube / kind) et le piloter avec **kubectl**.
- Créer et inspecter des **Pods** via des manifestes YAML.
- Déployer des applications avec des **Deployments** : scaling, rolling updates, rollback.
- Exposer vos applications avec des **Services** (ClusterIP, NodePort, LoadBalancer) et la **découverte de services**.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Architecture de Kubernetes](01-architecture.md) | Pourquoi K8s, control plane (API server, etcd, scheduler, controller-manager), nodes (kubelet, kube-proxy, runtime), kubectl, minikube/kind |
| 02 | [Les Pods](02-pods.md) | Pod = unité déployable, manifeste YAML, cycle de vie, multi-conteneurs, `kubectl run/get/describe/logs` |
| 03 | [Les Deployments](03-deployments.md) | Deployment, ReplicaSet, scaling, rolling updates, rollback, manifeste YAML |
| 04 | [Les Services](04-services.md) | ClusterIP, NodePort, LoadBalancer, découverte de services, labels/sélecteurs |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** et manifestes YAML ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée (manifeste + commandes kubectl + résultat) ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
