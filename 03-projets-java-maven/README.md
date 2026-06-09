# Module 03 — Projets Java et Maven

Troisième module du cours **Développement et déploiement de solutions de données** (420-D30-BB).
Il couvre la construction de projets Java avec **Apache Maven** : structure standard, `pom.xml`, gestion des dépendances et cycle de vie de build.

## Objectifs

À la fin de ce module, vous serez capable de :

- Expliquer ce qu'est **Maven** et le principe « convention plutôt que configuration ».
- Reconnaître la **structure standard** d'un projet Maven (`src/main/java`, `target/`…) et installer Maven.
- Lire et rédiger un **`pom.xml`** : coordonnées GAV, propriétés et héritage parent.
- **Déclarer des dépendances**, choisir leurs portées et comprendre la résolution transitive.
- Parcourir le **cycle de vie** Maven : `compile`, `test`, `package`, `install`, `deploy`.

## Contenu

| # | Leçon | Thèmes |
|---|---|---|
| 01 | [Introduction à Maven](01-introduction-maven.md) | Build automation, convention over configuration, structure standard, installation |
| 02 | [Le fichier pom.xml](02-pom-xml.md) | Structure du pom, coordonnées GAV, propriétés, héritage parent |
| 03 | [Gestion des dépendances](03-dependances.md) | Déclaration, portées (compile/test/provided/runtime), dépôts, transitif |
| 04 | [Cycle de vie et phases](04-cycle-de-vie.md) | Phases, compilation, tests (JUnit/Surefire), packaging (jar/war), install/deploy |

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
