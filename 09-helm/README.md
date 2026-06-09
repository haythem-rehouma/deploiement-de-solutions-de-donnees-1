# Module 09 — Helm

Neuvième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il introduit **Helm**, le gestionnaire de paquets de Kubernetes : empaqueter, paramétrer et déployer des applications complètes en une commande.

## Objectifs

À la fin de ce module, vous serez capable de :

- Expliquer le **problème résolu par Helm** et le situer comme gestionnaire de paquets de Kubernetes.
- Distinguer les trois concepts clés : **chart**, **release** et **repository**.
- **Installer Helm**, ajouter des dépôts, et utiliser `helm install` / `list` / `uninstall` / `upgrade` / `rollback`.
- Créer un chart avec **`helm create`**, comprendre sa structure (`Chart.yaml`, `templates/`, `values.yaml`, `charts/`), le packager et gérer ses **dépendances**.
- Paramétrer un chart via **`values.yaml`**, surcharger les valeurs (`--set`, `-f`) et gérer plusieurs **environnements**.
- Écrire des **templates** avec le moteur Go : syntaxe `{{ }}`, objets `.Values` / `.Release` / `.Chart`, fonctions, pipelines et helpers (`_helpers.tpl`).

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Introduction à Helm](01-introduction-helm.md) | Problème résolu, chart/release/repository, installation, `install`/`list`/`uninstall` |
| 02 | [Charts](02-charts.md) | Structure, `Chart.yaml`, `helm create`, packaging, dépendances |
| 03 | [Le fichier values.yaml](03-values-yaml.md) | Valeurs par défaut, `--set` / `-f`, priorité, environnements multiples |
| 04 | [Templates](04-templates.md) | Moteur Go, `{{ }}`, `.Values`/`.Release`/`.Chart`, fonctions, pipelines, `_helpers.tpl`, `template`/`lint` |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** ;
- des exemples concrets de **YAML** (`Chart.yaml`, `values.yaml`, templates Go) et de commandes **bash** (`helm …`) ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
