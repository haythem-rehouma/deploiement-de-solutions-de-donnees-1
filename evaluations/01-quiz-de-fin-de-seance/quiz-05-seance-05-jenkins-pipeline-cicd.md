<a id="top"></a>

# Quiz — Séance 5 — Pipelines CI/CD avec Jenkins (Quiz bilan)

> **Évaluation sommative** · Quiz bilan de fin de séance 5 (7 juillet 2026) · Pondération 1 % · QCM individuel en fin de séance
>
> **Contenus évalués :** Jenkinsfile déclaratif, pipeline CI/CD Git + Maven, déclencheurs (webhooks, cron), visualisation du pipeline. Inclut quelques questions de rappel sur les séances précédentes (Git, Maven, Jenkins).

---

**Question 1 :** Qu'est-ce que le *pipeline as code* dans Jenkins ?

a) Une configuration faite uniquement à la souris dans l'interface web.

b) La définition du pipeline dans un fichier `Jenkinsfile` versionné à la racine du dépôt, à côté du code.

c) Un plugin qui supprime le besoin d'écrire des tests.

d) Un format binaire stocké dans la base de données de Jenkins.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le *pipeline as code* place toute la définition du build dans un `Jenkinsfile` versionné dans Git, ce qui rend le pipeline relisable en revue de code, reproductible et historisé.

</details>

---

**Question 2 :** Dans un pipeline déclaratif Jenkins, quels deux blocs sont **obligatoires** ?

a) `environment` et `post`

b) `options` et `parameters`

c) `agent` et `stages`

d) `triggers` et `tools`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Tout pipeline déclaratif doit comporter au minimum un bloc `agent` (où il s'exécute) et un bloc `stages` (les étapes). Sans eux, Jenkins refuse de valider le Jenkinsfile.

</details>

---

**Question 3 :** Dans la structure d'un pipeline déclaratif, où place-t-on les commandes concrètes à exécuter (par exemple `sh 'mvn clean package'`) ?

a) Directement dans le bloc `pipeline { }`.

b) Dans un bloc `steps` à l'intérieur de chaque `stage`.

c) Dans le bloc `environment`.

d) Dans le bloc `post { always { } }` uniquement.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — La hiérarchie est `pipeline → stages → stage → steps`. Les commandes concrètes vivent dans le bloc `steps` de chaque `stage`.

</details>

---

**Question 4 :** Quel déclencheur fait démarrer un build de manière **instantanée**, dès qu'un `push` arrive sur GitHub, sans interroger le dépôt en permanence ?

a) Le polling SCM.

b) Le build périodique (cron).

c) Le webhook GitHub.

d) Le déclenchement manuel.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le webhook est une notification *poussée* : GitHub envoie une requête HTTP à Jenkins dès le `push`, déclenchant le build immédiatement, contrairement au polling qui interroge à intervalles réguliers.

</details>

---

**Question 5 :** Dans la syntaxe cron de Jenkins, que signifie l'expression `H/15 * * * *` placée dans un déclencheur ?

a) Exécuter le build une seule fois à minuit.

b) Exécuter le build toutes les 15 minutes, en répartissant la charge grâce au symbole `H`.

c) Exécuter le build le 15 de chaque mois.

d) Désactiver tous les déclencheurs.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `H/15 * * * *` lance le job environ toutes les 15 minutes. Le `H` (*hash*) répartit l'exécution dans l'intervalle pour éviter que tous les jobs ne démarrent exactement à la même seconde.

</details>

---

**Question 6 :** Quelle vue de Jenkins permet de visualiser graphiquement les *stages* d'un pipeline (succès, échec, durée de chaque étape) ?

a) La page « Gérer Jenkins ».

b) La vue *Stage View* / *Blue Ocean* du pipeline.

c) Le fichier `pom.xml`.

d) La console d'administration des plugins.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — La *Stage View* (et l'interface *Blue Ocean*) affiche chaque `stage` sous forme de colonnes colorées, indiquant le statut et la durée, ce qui facilite le diagnostic d'un pipeline.

</details>

---

**Question 7 :** *(Rappel — Maven)* Dans un pipeline CI, l'étape `sh 'mvn -B clean package'` enchaîne deux actions. Que fait-elle exactement ?

a) Elle déploie l'application en production sans la compiler.

b) Elle nettoie le dossier `target/` puis compile, teste et empaquette le projet (`.jar`/`.war`).

c) Elle crée une nouvelle branche Git nommée `package`.

d) Elle installe Jenkins sur la machine.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `clean` supprime le dossier `target/`, puis `package` exécute tout le cycle (`validate` → `compile` → `test` → `package`), produisant un artefact propre. L'option `-B` (*batch*) évite les sorties interactives.

</details>

---

**Question 8 :** *(Rappel — Git)* Dans un workflow CI/CD, pourquoi est-il recommandé de fusionner une *feature branch* dans `main` via une *pull request* plutôt que de pousser directement sur `main` ?

a) Parce que c'est obligatoire pour que Maven compile.

b) Parce que la PR permet la revue de code, déclenche le pipeline de validation et protège la branche principale.

c) Parce que `main` ne peut techniquement pas recevoir de commits.

d) Parce que cela supprime l'historique des commits.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — La *pull request* introduit un point de contrôle : revue par les pairs, exécution automatique du pipeline CI sur la branche, et protection de `main` contre les changements non validés.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
