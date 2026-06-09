<a id="top"></a>

# Quiz 1 — Concepts CI/CD, culture DevOps et bases de Git

> **Évaluation sommative** · Quiz de fin de séance 1 (9 juin 2026) · QCM individuel
>
> **Contenus évalués :** concepts CI/CD, culture DevOps (collaboration, automatisation, rétroaction), cycle de vie d'une livraison, bases de Git (dépôt local, commits, historique, branches, dépôt distant).
>
> **Consignes :** 40 questions à choix multiple. Une seule bonne réponse par question. Aucune documentation autorisée sauf indication contraire.

---

**Question 1 :** Que signifie l'acronyme « CI » dans CI/CD ?

a) Continuous Inspection

b) Continuous Integration

c) Code Integrity

d) Container Initialization

---

**Question 2 :** Que signifie « CD » dans CI/CD ?

a) Continuous Delivery / Continuous Deployment

b) Code Development

c) Central Database

d) Container Deployment

---

**Question 3 :** Quel est l'objectif principal de l'intégration continue (CI) ?

a) Supprimer les tests pour aller plus vite

b) Fusionner et valider fréquemment le code par des builds et tests automatisés

c) Déployer manuellement chaque version en production

d) Remplacer les développeurs par des scripts

---

**Question 4 :** Quelle est la différence entre « Continuous Delivery » et « Continuous Deployment » ?

a) Il n'y a aucune différence

b) En Continuous Delivery la mise en production reste une décision manuelle ; en Continuous Deployment elle est automatique

c) Continuous Deployment ne nécessite pas de tests

d) Continuous Delivery déploie automatiquement, Continuous Deployment non

---

**Question 5 :** Lequel des éléments suivants décrit le mieux la culture DevOps ?

a) Un logiciel unique à installer sur les serveurs

b) Une équipe dédiée uniquement à la sécurité

c) Une culture rapprochant développement et exploitation autour de la collaboration, de l'automatisation et de la rétroaction

d) Un langage de programmation

---

**Question 6 :** Quel problème historique le DevOps cherche-t-il à résoudre ?

a) Le manque de langages de programmation

b) Le « mur de la confusion » entre les équipes Dev et Ops

c) L'absence d'ordinateurs portables

d) Le coût de l'électricité des serveurs

---

**Question 7 :** Parmi ces éléments, lequel est un pilier de la culture DevOps ?

a) La centralisation de toutes les décisions chez une seule personne

b) L'automatisation des tâches répétitives

c) Le déploiement une fois par an

d) L'interdiction d'utiliser des outils open source

---

**Question 8 :** Pourquoi la « rétroaction rapide » (fast feedback) est-elle importante ?

a) Parce qu'elle ralentit volontairement les livraisons

b) Parce qu'un problème détecté tôt coûte beaucoup moins cher à corriger

c) Parce qu'elle supprime le besoin de tests

d) Parce qu'elle empêche la collaboration

---

**Question 9 :** Que représente la « boucle infinie » (∞) souvent associée au DevOps ?

a) Un bug qui ne se corrige jamais

b) L'amélioration continue et l'itération sans fin du cycle de vie

c) Un serveur qui redémarre en boucle

d) Une dépendance circulaire dans le code

---

**Question 10 :** Quel bénéfice concret apporte un pipeline CI/CD bien conçu ?

a) Des livraisons plus fréquentes, plus fiables et moins stressantes

b) La suppression de tout besoin de versionner le code

c) L'impossibilité de revenir à une version antérieure

d) Une dépendance totale aux déploiements manuels

---

**Question 11 :** Dans un pipeline CI/CD typique, quelle étape vient juste après l'écriture du code ?

a) La mise en production directe sans contrôle

b) Le versionnement puis le build et les tests automatisés

c) La suppression du dépôt

d) La rédaction de la facture client

---

**Question 12 :** Qu'est-ce qu'un « build » dans un pipeline ?

a) L'étape qui compile/assemble le code en un artefact exécutable

b) L'action de supprimer les branches

c) La rédaction de la documentation

d) L'envoi d'un courriel à l'équipe

---

**Question 13 :** Pourquoi automatiser les tests dans un pipeline CI ?

a) Pour rendre le code plus lent

b) Pour détecter les régressions rapidement et de façon reproductible

c) Pour éviter d'écrire du code

d) Pour augmenter le nombre de bugs

---

**Question 14 :** Qu'est-ce qu'un « artefact » dans une chaîne CI/CD ?

a) Un bug introduit par erreur

b) Le résultat empaqueté d'un build (ex. un .jar, une image)

c) Un commentaire dans le code

d) Un utilisateur du système

---

**Question 15 :** Lequel de ces outils est typiquement utilisé pour l'intégration continue ?

a) Photoshop

b) Jenkins ou GitHub Actions

c) Excel

d) PowerPoint

---

**Question 16 :** Que désigne le principe « Infrastructure as Code » (IaC) ?

a) Écrire le code de l'application en assembleur

b) Décrire et provisionner l'infrastructure au moyen de fichiers de configuration versionnés

c) Interdire toute infrastructure cloud

d) Configurer chaque serveur manuellement à la main

---

**Question 17 :** Pourquoi la « reproductibilité » est-elle un principe central en DevOps ?

a) Pour pouvoir recréer un environnement à l'identique à partir du code et des scripts

b) Pour empêcher les autres de comprendre le projet

c) Parce que « ça marche sur ma machine » suffit

d) Pour ralentir les déploiements

---

**Question 18 :** Qu'est-ce qu'un système de contrôle de version comme Git permet de faire ?

a) Compiler automatiquement du code C++

b) Suivre l'historique des modifications et collaborer sans s'écraser mutuellement

c) Héberger des vidéos

d) Remplacer une base de données

---

**Question 19 :** On dit que Git est « distribué ». Qu'est-ce que cela signifie ?

a) Chaque personne possède une copie complète du dépôt, historique inclus

b) Git ne fonctionne qu'en ligne

c) Le code est réparti aléatoirement entre les machines

d) Seul le serveur central contient l'historique

---

**Question 20 :** Quelle commande initialise un nouveau dépôt Git local ?

a) `git start`

b) `git init`

c) `git new`

d) `git create`

---

**Question 21 :** Quelles sont, dans l'ordre, les trois zones de Git ?

a) Dépôt local → staging → répertoire de travail

b) Répertoire de travail → zone de staging → dépôt local

c) Staging → dépôt → répertoire de travail

d) Répertoire de travail → dépôt → staging

---

**Question 22 :** À quoi sert la commande `git add` ?

a) À créer une branche

b) À préparer des changements dans la zone de staging

c) À envoyer le code sur le serveur distant

d) À supprimer un fichier

---

**Question 23 :** Qu'enregistre un `git commit` ?

a) Un instantané des changements préparés, avec un message

b) Uniquement le nom de l'auteur

c) La suppression définitive du dépôt

d) Une copie de l'écran

---

**Question 24 :** Lequel est un bon message de commit ?

a) `truc`

b) `wip`

c) `Corrige le calcul de la TVA dans la facture`

d) `.`

---

**Question 25 :** À quoi sert un fichier `.gitignore` ?

a) À accélérer le processeur

b) À indiquer à Git quels fichiers ne pas versionner (temporaires, secrets, dépendances)

c) À supprimer l'historique

d) À ignorer les commits des autres

---

**Question 26 :** Pourquoi ne faut-il jamais committer un mot de passe ou une clé API ?

a) Parce que cela ralentit Git

b) Parce qu'un secret reste dans l'historique même après suppression

c) Parce que Git refuse les fichiers texte

d) Ce n'est pas un problème

---

**Question 27 :** À quoi sert une branche dans Git ?

a) À supprimer l'historique du projet

b) À développer de façon isolée sans toucher à la version principale

c) À compiler le code plus vite

d) À se connecter à Internet

---

**Question 28 :** Quelle commande crée une branche et bascule dessus en une seule opération ?

a) `git branch nom`

b) `git switch -c nom`

c) `git merge nom`

d) `git log nom`

---

**Question 29 :** Que fait l'opération `git merge` ?

a) Elle supprime une branche

b) Elle intègre les changements d'une branche dans une autre

c) Elle initialise un dépôt

d) Elle renomme un fichier

---

**Question 30 :** Quand survient un conflit de fusion ?

a) À chaque fusion, systématiquement

b) Quand deux branches ont modifié la même ligne d'un même fichier

c) Quand on installe Git

d) Quand on crée une branche

---

**Question 31 :** Quelle commande affiche l'historique des commits ?

a) `git status`

b) `git log`

c) `git add`

d) `git remote`

---

**Question 32 :** Qu'est-ce qu'un dépôt distant (remote) ?

a) Une branche locale

b) Une copie du dépôt hébergée sur un serveur, accessible par l'équipe

c) Un fichier de configuration local

d) Un commit particulier

---

**Question 33 :** Comment s'appelle, par convention, le dépôt distant principal ?

a) `master`

b) `origin`

c) `cloud`

d) `server`

---

**Question 34 :** Quelle commande envoie les commits locaux vers le dépôt distant ?

a) `git pull`

b) `git push`

c) `git clone`

d) `git fetch`

---

**Question 35 :** Quelle est la différence entre `git fetch` et `git pull` ?

a) Aucune, ce sont des synonymes

b) `fetch` télécharge sans fusionner ; `pull` télécharge et fusionne

c) `pull` supprime l'historique

d) `fetch` envoie les commits au serveur

---

**Question 36 :** Dans quel cas utilise-t-on `git clone` ?

a) Pour créer une branche locale

b) Pour récupérer une copie complète d'un dépôt distant existant

c) Pour résoudre un conflit

d) Pour supprimer un dépôt

---

**Question 37 :** GitHub est principalement :

a) Un éditeur de texte hors ligne

b) Une plateforme d'hébergement de dépôts Git et de collaboration

c) Un langage de programmation

d) Un système d'exploitation

---

**Question 38 :** Quel est le rôle d'une « pull request » sur GitHub ?

a) Supprimer définitivement une branche

b) Proposer des changements et permettre une revue de code avant fusion

c) Télécharger un dépôt sur sa machine

d) Lancer un serveur web

---

**Question 39 :** Quelle bonne habitude réduit fortement les conflits en équipe ?

a) Ne jamais faire de commits

b) Faire `git pull` avant de commencer à travailler et avant de pousser

c) Travailler tous sur la même branche sans communiquer

d) Supprimer le dépôt distant régulièrement

---

**Question 40 :** Pourquoi Git est-il considéré comme le socle de toute la chaîne DevOps ?

a) Parce qu'il remplace Docker et Kubernetes

b) Parce que le code versionné est le point de départ du CI/CD, des déploiements et de la collaboration

c) Parce qu'il héberge les bases de données de production

d) Parce qu'il génère automatiquement la documentation

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
