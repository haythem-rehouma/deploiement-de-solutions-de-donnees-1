<a id="top"></a>

# Quiz — Séance 1 — Introduction au DevOps et bases de Git

> **Évaluation sommative** · Quiz de fin de séance 1 (9 juin 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** présentation du cours, culture DevOps (collaboration, automatisation, rétroaction), bases de Git (dépôt local, commits, historique, branches, dépôt distant).

---

**Question 1 :** Parmi les énoncés suivants, lequel décrit le mieux la culture DevOps ?

a) Un outil unique qui remplace tous les serveurs d'une entreprise.

b) Une approche qui rapproche le développement et l'exploitation autour de la collaboration, de l'automatisation et de la rétroaction.

c) Un langage de programmation dédié au déploiement d'applications.

d) Une certification obligatoire pour devenir administrateur système.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le DevOps est avant tout une culture qui brise les silos entre les équipes Dev et Ops, en s'appuyant sur la collaboration, l'automatisation et les boucles de rétroaction rapides.

</details>

---

**Question 2 :** Quelle commande permet d'initialiser un nouveau dépôt Git local dans le dossier courant ?

a) `git start`

b) `git create`

c) `git init`

d) `git new`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `git init` crée un nouveau dépôt local en générant le sous-dossier caché `.git/` qui contient tout l'historique et la configuration.

</details>

---

**Question 3 :** Avant de pouvoir créer un commit, quelle étape est nécessaire pour préparer les fichiers modifiés ?

a) Les ajouter à la zone d'index (*staging area*) avec `git add`.

b) Les compresser dans une archive `.zip`.

c) Les pousser directement sur le dépôt distant.

d) Les renommer avec l'extension `.commit`.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — `git add` place les modifications dans la zone d'index ; `git commit` enregistre ensuite uniquement ce qui a été indexé.

</details>

---

**Question 4 :** Quelle commande affiche l'historique des commits d'un dépôt ?

a) `git history`

b) `git log`

c) `git show-history`

d) `git commits`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `git log` liste les commits du plus récent au plus ancien, avec leur identifiant (*hash*), l'auteur, la date et le message.

</details>

---

**Question 5 :** Que représente une branche dans Git ?

a) Une copie complète et indépendante du dépôt sur un autre serveur.

b) Une ligne de développement parallèle, matérialisée par un pointeur léger vers un commit.

c) Un fichier de configuration listant les collaborateurs du projet.

d) Une sauvegarde automatique effectuée toutes les heures.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Une branche est un simple pointeur déplaçable vers un commit ; elle permet de travailler en parallèle sans toucher à la branche principale.

</details>

---

**Question 6 :** Pour envoyer vos commits locaux vers un dépôt distant (par exemple GitHub), quelle commande utilisez-vous ?

a) `git upload`

b) `git send`

c) `git push`

d) `git export`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `git push` publie les commits locaux vers le dépôt distant ; à l'inverse, `git pull` récupère les modifications distantes vers le dépôt local.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
