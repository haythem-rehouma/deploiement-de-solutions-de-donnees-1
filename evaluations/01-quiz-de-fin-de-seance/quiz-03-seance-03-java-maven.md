<a id="top"></a>

# Quiz — Séance 3 — Projets Java avec Maven

> **Évaluation sommative** · Quiz de fin de séance 3 (23 juin 2026) · Pondération 1 % · QCM individuel en fin de séance
>
> **Contenus évalués :** Maven, fichier `pom.xml`, gestion des dépendances, phases du cycle de vie de build.

---

**Question 1 :** Quel est le rôle principal de Maven dans un projet Java ?

a) Compiler le code uniquement, sans gérer les dépendances.

b) Automatiser la construction du projet : compilation, tests, gestion des dépendances et packaging.

c) Remplacer la machine virtuelle Java (JVM) à l'exécution.

d) Servir de système de contrôle de version comme Git.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Maven est un outil de build qui automatise la compilation, l'exécution des tests, la résolution des dépendances et la production des artefacts (`.jar`/`.war`).

</details>

---

**Question 2 :** Quel fichier constitue le cœur de la configuration d'un projet Maven ?

a) `build.gradle`

b) `package.json`

c) `pom.xml`

d) `maven.config`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le `pom.xml` (*Project Object Model*) décrit le projet : coordonnées, dépendances, plugins et configuration du build.

</details>

---

**Question 3 :** Quels sont les trois éléments qui identifient de manière unique un artefact (ses *coordonnées*) dans le `pom.xml` ?

a) `name`, `description`, `url`

b) `groupId`, `artifactId`, `version`

c) `package`, `class`, `method`

d) `host`, `port`, `path`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le triplet `groupId` / `artifactId` / `version` (souvent abrégé GAV) identifie de façon unique un artefact, qu'il s'agisse du projet lui-même ou d'une dépendance.

</details>

---

**Question 4 :** Où Maven stocke-t-il par défaut les dépendances téléchargées sur la machine locale ?

a) Dans le dossier `target/` du projet.

b) Dans le dépôt local `~/.m2/repository`.

c) Directement dans le dossier `src/main/java`.

d) Dans la base de données du serveur d'intégration continue.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Maven met en cache les dépendances dans le dépôt local `~/.m2/repository` afin de ne pas les retélécharger à chaque build.

</details>

---

**Question 5 :** Lorsque vous exécutez `mvn package`, quelles phases sont lancées et dans quel ordre ?

a) Uniquement `package`, sans rien d'autre.

b) `package` puis `compile` puis `test`, dans cet ordre.

c) `validate` → `compile` → `test` → `package`, car demander une phase exécute toutes les précédentes.

d) `clean` → `deploy` → `package`.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Dans le cycle de vie *default*, demander une phase exécute automatiquement toutes celles qui la précèdent : `mvn package` lance donc `validate`, `compile` et `test` avant `package`.

</details>

---

**Question 6 :** Quelle phase du cycle de vie copie l'artefact construit dans le dépôt local `~/.m2` pour le rendre disponible aux autres projets de la même machine ?

a) `compile`

b) `deploy`

c) `install`

d) `validate`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `install` place l'artefact dans le dépôt local `~/.m2`. La phase `deploy`, elle, va plus loin en publiant l'artefact sur un dépôt distant partagé.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
