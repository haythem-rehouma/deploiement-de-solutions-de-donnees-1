# Module 12 — Terraform

Module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il introduit l'**Infrastructure as Code** avec **Terraform** : décrire, versionner et déployer son infrastructure cloud à partir de simples fichiers texte.

## Objectifs

À la fin de ce module, vous serez capable de :

- Expliquer ce qu'est l'**Infrastructure as Code** et l'approche **déclarative**.
- Écrire du **HCL**, configurer des **providers** et déclarer des **ressources**.
- Maîtriser le **workflow** `init` / `plan` / `apply` / `destroy`.
- Paramétrer une configuration avec des **variables**, des **locals** et des **outputs**.
- Comprendre le **fichier d'état** et le stocker de façon sûre via un **backend distant**.
- Factoriser son infrastructure avec des **modules** réutilisables (DRY).

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Providers et workflow](01-providers.md) | IaC, HCL, providers, ressources, `init`/`plan`/`apply`/`destroy` |
| 02 | [Variables et outputs](02-variables-et-outputs.md) | `variable`, types, `tfvars`, `locals`, `output`, validation |
| 03 | [Le fichier d'état](03-state.md) | `tfstate`, local vs distant, backend S3/azurerm, verrouillage, sécurité |
| 04 | [Les modules](04-modules.md) | Réutilisation, DRY, `source`, registry, environnements |

## Format des leçons

Chaque leçon est autonome et suit la même structure pédagogique :

- une **table des matières** cliquable ;
- des **sections repliables** (`<details>`) avec diagrammes **Mermaid** et blocs **HCL** ;
- un **quiz** corrigé (solutions repliables) ;
- une **pratique** avec correction détaillée (code `.tf` + commandes attendues) ;
- une **synthèse** des points à retenir.

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
