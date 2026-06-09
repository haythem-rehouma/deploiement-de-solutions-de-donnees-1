<a id="top"></a>

# Quiz — Séance 2 — Git avancé et GitHub

> **Évaluation sommative** · Quiz de fin de séance 2 (16 juin 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** branches et stratégies, merge et rebase, pull requests, workflow collaboratif.

---

**Question 1 :** Quelle commande crée une nouvelle branche et bascule dessus immédiatement ?

a) `git branch -new ma-branche`

b) `git checkout -b ma-branche`

c) `git switch --create-only ma-branche`

d) `git merge ma-branche`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `git checkout -b ma-branche` (ou son équivalent moderne `git switch -c ma-branche`) crée la branche puis s'y positionne en une seule commande.

</details>

---

**Question 2 :** Quelle est la différence principale entre `git merge` et `git rebase` ?

a) `merge` supprime l'historique tandis que `rebase` le conserve intégralement.

b) `merge` crée un commit de fusion en préservant l'historique, tandis que `rebase` rejoue les commits pour produire un historique linéaire.

c) Les deux commandes sont strictement identiques, seul le nom change.

d) `rebase` ne fonctionne qu'avec les dépôts distants, jamais en local.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `merge` réunit deux branches via un commit de fusion (historique non linéaire mais fidèle), alors que `rebase` réapplique les commits par-dessus une autre base pour obtenir un historique linéaire et propre.

</details>

---

**Question 3 :** À quoi sert principalement une *pull request* (PR) sur GitHub ?

a) À supprimer définitivement une branche du dépôt distant.

b) À proposer l'intégration de modifications et à permettre leur revue avant la fusion.

c) À télécharger l'intégralité du dépôt sur sa machine locale.

d) À compiler automatiquement le projet sur les serveurs de GitHub.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — La *pull request* est le mécanisme central de collaboration : elle ouvre une discussion et une revue de code autour de modifications proposées avant de les fusionner dans la branche cible.

</details>

---

**Question 4 :** Dans un workflow collaboratif de type *feature branch*, où le développement d'une nouvelle fonctionnalité doit-il se faire ?

a) Directement sur la branche `main` pour gagner du temps.

b) Sur une branche dédiée créée à partir de `main`, puis fusionnée via une PR.

c) Dans un dépôt totalement séparé, sans aucun lien avec l'original.

d) Uniquement dans les fichiers de configuration `.git/`.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Chaque fonctionnalité est développée sur sa propre branche issue de `main`, puis réintégrée par une *pull request* relue, ce qui protège la branche principale.

</details>

---

**Question 5 :** Que se passe-t-il lorsqu'un *conflit de fusion* (merge conflict) survient ?

a) Git annule toute l'opération et supprime les deux branches.

b) Git modifie le code automatiquement sans avertir le développeur.

c) Git marque les zones en conflit dans les fichiers et demande une résolution manuelle avant de poursuivre.

d) Le conflit est ignoré et le dernier commit l'emporte silencieusement.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Quand deux modifications touchent les mêmes lignes, Git insère des marqueurs (`<<<<<<<`, `=======`, `>>>>>>>`) et attend que le développeur choisisse manuellement la version à conserver, puis valide la résolution.

</details>

---

**Question 6 :** Avant de pousser ses commits, un développeur veut récupérer les dernières modifications de la branche distante. Quelle commande est la plus appropriée ?

a) `git clone`

b) `git pull`

c) `git init`

d) `git stash`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `git pull` récupère (`fetch`) puis intègre (`merge` ou `rebase`) les changements distants dans la branche locale ; `git clone` ne sert qu'à copier un dépôt pour la première fois.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
