# Module 18 — Kubernetes : suite de la théorie (partie 3)

Dix-huitième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).

Ce module **prolonge la théorie** vue aux modules [07 — Kubernetes : bases](../07-kubernetes-bases/README.md), [08 — Kubernetes : avancé](../08-kubernetes-avance/README.md) et aux parties 1 et 2 ([16](../16-kubernetes-suite-theorie-partie-1/README.md), [17](../17-kubernetes-suite-theorie-partie-2/README.md)). Il traite de tout ce qui touche à **l'état, au stockage et aux différents types de charges de travail** : autant de notions indispensables dès qu'une application dépasse le simple conteneur sans état.

## Prérequis

- Module 07 : Pods, Deployments, Services.
- Module 08 : Ingress, ConfigMaps, Secrets.
- Modules 16 et 17 : mise en place d'un cluster local et manipulations de base.
- Un cluster local fonctionnel (Kubernetes de Docker Desktop, voir le [projet 10](../07-kubernetes-bases/projet10-kubernetes-deploiements/README.md)).

## Objectifs

À la fin de ce module, vous serez capable de :

- Distinguer les **volumes éphémères** des **volumes persistants**, et expliquer le trio **PV / PVC / StorageClass**.
- Choisir le bon **mode d'accès** et la bonne **politique de récupération** pour un volume.
- Déployer une application **avec état** grâce aux **StatefulSet** (identité stable, `volumeClaimTemplates`).
- Utiliser les charges de travail spécialisées : **DaemonSet**, **Job** et **CronJob**.
- Cloisonner et encadrer un cluster avec les **Namespaces**, les **ResourceQuota**, les **LimitRange** et les classes de **QoS**.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Volumes et stockage persistant](01-volumes-et-stockage-persistant.md) | Volumes éphémères, PersistentVolume, PersistentVolumeClaim, StorageClass, modes d'accès, politiques de récupération, provisionnement dynamique |
| 02 | [StatefulSet : les applications avec état](02-statefulset.md) | Deployment vs StatefulSet, identité réseau stable, Service headless, `volumeClaimTemplates`, ordre de démarrage, mises à jour |
| 03 | [DaemonSet, Jobs et CronJobs](03-daemonset-jobs-cronjobs.md) | Un Pod par nœud, tâches ponctuelles, tâches planifiées, parallélisme, reprise sur échec, nettoyage |
| 04 | [Namespaces, quotas et limites](04-namespaces-quotas-et-limites.md) | Cloisonnement logique, `requests`/`limits`, ResourceQuota, LimitRange, classes de QoS, éviction |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **diagrammes Mermaid** et des **manifestes YAML** commentés ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée ;
- une **synthèse** des points à retenir.

## Suite

Le module [19 — Kubernetes : suite de la théorie (partie 4)](../19-kubernetes-suite-theorie-partie-4/README.md) poursuit avec le **placement des Pods**, la **mise à l'échelle automatique**, la **sécurité (RBAC)** et les **politiques réseau**.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
