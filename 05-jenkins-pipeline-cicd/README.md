# Module 05 — Jenkins : pipeline CI/CD

Cinquième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il fait passer du build manuel au **pipeline as code** : écrire un `Jenkinsfile`, automatiser build et tests Maven, déclencher le pipeline automatiquement et en suivre l'exécution.

## Objectifs

À la fin de ce module, vous serez capable de :

- Écrire un **Jenkinsfile déclaratif** (`pipeline`, `agent`, `stages`, `steps`, `environment`, `options`, `post`).
- Construire un **pipeline CI/CD** concret : `checkout scm`, build Maven, tests, archivage des artefacts.
- Configurer des **déclencheurs** : webhooks GitHub, polling SCM, cron, chaînes upstream/downstream.
- **Visualiser** un pipeline avec la Stage View et Blue Ocean (statut, logs, durées, échecs).

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Jenkinsfile déclaratif](01-jenkinsfile-declaratif.md) | `pipeline`, `agent`, `stages`/`steps`, `environment`, `options`, `parameters`, `post` |
| 02 | [Pipeline CI/CD avec Git et Maven](02-pipeline-git-maven.md) | `checkout scm`, `mvn package`, tests, JUnit, `archiveArtifacts` |
| 03 | [Déclencheurs](03-declencheurs.md) | Webhooks GitHub, `pollSCM`, `cron`, syntaxe `H`, upstream/downstream |
| 04 | [Visualisation du pipeline](04-visualisation-pipeline.md) | Stage View, Blue Ocean, couleurs/statut, logs, durées, tendances |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** et exemples de **Jenkinsfile** ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée (Jenkinsfile complet attendu) ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
