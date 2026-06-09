# Module 14 — Atelier d'intégration

Avant-dernier module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
C'est l'**atelier de synthèse** : on relie tous les outils vus séparément (Git, CI, Docker, Kubernetes, Helm, monitoring) en **une seule chaîne CI/CD automatisée**, de bout en bout.

## Objectifs

À la fin de ce module, vous serez capable de :

- Décrire l'**architecture globale** d'une chaîne CI/CD complète (Git → CI → Docker → registre → K8s/Helm → monitoring).
- **Déclencher** un pipeline depuis Git, via Jenkins ou GitHub Actions.
- **Construire et pousser** une image Docker taguée de façon immuable.
- **Déployer** automatiquement sur Kubernetes avec **Helm** (`helm upgrade --install`).
- Mettre en place le **monitoring** (Prometheus + Grafana) et fermer la boucle de rétroaction.
- Assembler le tout dans **un pipeline unique** avec garde-fous (`needs:`, sondes de santé, rollback).

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Chaîne CI/CD complète de bout en bout](01-chaine-cicd-complete.md) | Schéma global, Git → CI → Docker → Helm → Prometheus/Grafana, pipeline complet, pratique guidée |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
