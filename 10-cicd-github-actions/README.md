# Module 10 — CI/CD avec GitHub Actions

Dixième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il automatise toute la chaîne : tester, construire une image Docker, puis déployer sur Kubernetes — sans intervention manuelle, directement depuis GitHub.

## Objectifs

À la fin de ce module, vous serez capable de :

- Écrire des **workflows GitHub Actions** (`.github/workflows/*.yml`) avec `on`, `jobs`, `runs-on` et `steps`.
- Choisir les bons **déclencheurs** (`push`, `pull_request`, `schedule`, manuel) et utiliser les **actions du Marketplace**.
- Gérer des **secrets** de façon sécurisée.
- **Construire et publier** une image Docker vers un registry (GHCR) avec tags et cache.
- **Déployer sur Kubernetes** depuis un workflow avec `kubectl` et `helm`, en gérant **environnements** et **approbations**.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Workflows GitHub Actions](01-workflows.md) | `on`, `jobs`, `runs-on`, `steps`, déclencheurs, Marketplace, secrets |
| 02 | [Construire et publier une image Docker](02-build-et-push-images.md) | `login-action`, GHCR, `build-push-action`, tags, cache |
| 03 | [Déploiement avec kubectl et Helm](03-deploiement-kubectl-helm.md) | kubeconfig (secret), `kubectl apply`, `helm upgrade`, environnements, approbations |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** ;
- des **workflows YAML** réalistes et des commandes commentées ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
