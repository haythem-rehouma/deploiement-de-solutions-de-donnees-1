# Module 19 — Kubernetes : suite de la théorie (partie 4)

Dix-neuvième et dernier module du cours **Développement et déploiement de solutions de données** (420-D30-BB).

Ce module clôt le parcours Kubernetes entamé aux modules [07 (bases)](../07-kubernetes-bases/README.md), [08 (avancé)](../08-kubernetes-avance/README.md), puis poursuivi aux parties 1 à 3 ([16](../16-kubernetes-suite-theorie-partie-1/README.md), [17](../17-kubernetes-suite-theorie-partie-2/README.md), [18](../18-kubernetes-suite-theorie-partie-3/README.md)). Il traite des sujets qui séparent un cluster « qui marche » d'un cluster **exploitable en production** : le **placement** des Pods, la **mise à l'échelle automatique**, le **contrôle des accès** et le **cloisonnement réseau**.

## Prérequis

- Module 07 : Pods, Deployments, Services.
- Module 08 : Ingress, ConfigMaps, Secrets.
- Module 18 : stockage persistant, StatefulSet, charges spécialisées, namespaces et quotas.

## Objectifs

À la fin de ce module, vous serez capable de :

- Maîtriser le **placement des Pods** : `nodeSelector`, **affinité** et **anti-affinité**, **taints et tolerations**, répartition topologique.
- Mettre en place la **mise à l'échelle automatique** avec le **HPA**, et comprendre le rôle du **metrics-server**, du **VPA** et du **Cluster Autoscaler**.
- Protéger la disponibilité pendant les opérations de maintenance avec un **PodDisruptionBudget**.
- Contrôler **qui a le droit de faire quoi** grâce au **RBAC** (Role, ClusterRole, ServiceAccount) et durcir les Pods avec le **securityContext**.
- Cloisonner les communications entre Pods avec les **NetworkPolicy**.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Placement des Pods et scheduling](01-scheduling-et-placement.md) | Fonctionnement du scheduler, `nodeSelector`, affinité/anti-affinité, taints et tolerations, `topologySpreadConstraints`, priorités |
| 02 | [Mise à l'échelle automatique](02-autoscaling.md) | metrics-server, HPA (CPU, mémoire, métriques personnalisées), comportement de montée/descente, VPA, Cluster Autoscaler, PodDisruptionBudget |
| 03 | [Sécurité : RBAC et comptes de service](03-securite-rbac.md) | Authentification vs autorisation, Role/ClusterRole, RoleBinding, ServiceAccount, `securityContext`, bonnes pratiques |
| 04 | [Politiques réseau (NetworkPolicy)](04-network-policies.md) | Modèle réseau plat, CNI, règles `Ingress`/`Egress`, sélecteurs, isolation par défaut, modèles courants |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **diagrammes Mermaid** et des **manifestes YAML** commentés ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée ;
- une **synthèse** des points à retenir.

## Pour aller plus loin

Les projets pratiques associés se trouvent dans le module 07 :

- [projet10 — Premiers pas avec Kubernetes](../07-kubernetes-bases/projet10-kubernetes-deploiements/README.md) (Pods, Deployments, ConfigMap, scaling) ;
- [projet11 — Les Services Kubernetes](../07-kubernetes-bases/projet11-kubernetes-services/README.md) (ClusterIP, NodePort, LoadBalancer, DNS).

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
