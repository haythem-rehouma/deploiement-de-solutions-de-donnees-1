# Module 11 — Ansible

Module **Ansible** du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il enseigne l'automatisation de la configuration des serveurs **sans agent** : de l'inventaire des machines jusqu'aux playbooks idempotents, en passant par les rôles réutilisables.

## Objectifs

À la fin de ce module, vous serez capable de :

- Expliquer le modèle **sans agent** d'Ansible (push par **SSH**) et écrire un **inventaire** (statique INI/YAML, groupes, variables, dynamique).
- Lancer des **commandes ad-hoc** (`ansible -m ping`) pour tester un parc.
- Écrire et exécuter des **playbooks YAML** (`hosts`, `tasks`, modules `apt`/`copy`/`template`/`service`).
- Structurer un projet en **rôles** (tasks/handlers/templates/defaults/vars) et utiliser les **handlers** (`notify`) ainsi qu'**Ansible Galaxy**.
- Comprendre et garantir l'**idempotence** (`ok` vs `changed`), et vérifier avec `--check` et `--diff`.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Ansible et les inventaires](01-inventaires.md) | Sans agent, SSH, inventaires INI/YAML, groupes, variables, dynamique, ad-hoc `ping` |
| 02 | [Playbooks Ansible](02-playbooks.md) | YAML, `hosts`/`tasks`, modules `apt`/`copy`/`template`/`service`, variables, `ansible-playbook` |
| 03 | [Rôles et handlers](03-roles-et-handlers.md) | Structure d'un rôle, réutilisation, handlers + `notify`, Ansible Galaxy |
| 04 | [Idempotence](04-idempotence.md) | État désiré, `changed` vs `ok`, modules idempotents vs `command`/`shell`, `--check`/`--diff` |

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
