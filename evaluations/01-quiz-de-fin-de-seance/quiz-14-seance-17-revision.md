<a id="top"></a>

# Quiz — Séance 17 — Révision générale (synthèse transversale du cours)

> **Évaluation sommative** · Quiz de fin de séance 17 (29 septembre 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** révision transversale (Git, Maven, Jenkins, Docker, Kubernetes, Helm, GitHub Actions, Ansible, Terraform, monitoring)

---

**Question 1 :** Quelle commande Git crée une nouvelle branche `feature` et bascule immédiatement dessus ?

a) `git branch feature`

b) `git checkout -b feature`

c) `git merge feature`

d) `git switch --merge feature`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `git checkout -b feature` (équivalent moderne : `git switch -c feature`) crée la branche et s'y positionne en une seule commande. `git branch feature` la crée sans s'y déplacer.

</details>

---

**Question 2 :** Dans un projet Java, quelle commande Maven compile le code, exécute les tests et produit l'artefact (ex. un `.jar`) ?

a) `mvn clean`

b) `mvn compile`

c) `mvn package`

d) `mvn validate`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — La phase `package` du cycle de vie Maven enchaîne compilation, tests, puis empaquetage de l'artefact (JAR/WAR) dans le répertoire `target/`. On la combine souvent avec `clean` : `mvn clean package`.

</details>

---

**Question 3 :** Quelle instruction d'un `Dockerfile` définit la commande exécutée au démarrage du conteneur ?

a) `RUN`

b) `COPY`

c) `FROM`

d) `CMD`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : d)** — `CMD` (ou `ENTRYPOINT`) précise la commande lancée au démarrage du conteneur. `RUN` exécute des commandes au moment du build de l'image, et `FROM` définit l'image de base.

</details>

---

**Question 4 :** Dans Kubernetes, quel objet expose un ensemble de pods sous une adresse réseau stable et assure la répartition de charge entre eux ?

a) Un `Service`

b) Un `Namespace`

c) Un `Secret`

d) Un `PersistentVolume`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — Un `Service` fournit un point d'accès réseau stable (IP/DNS) vers un groupe de pods sélectionnés par labels, et répartit le trafic entre eux, indépendamment du cycle de vie de chaque pod.

</details>

---

**Question 5 :** Dans un workflow GitHub Actions, quel élément définit l'événement déclencheur (ex. un push sur `main`) ?

a) `jobs:`

b) `on:`

c) `steps:`

d) `runs-on:`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — La clé `on:` d'un fichier de workflow YAML déclare les événements qui déclenchent l'exécution (ex. `on: push: branches: [main]`). `jobs:` définit les tâches, `runs-on:` la machine, et `steps:` les étapes.

</details>

---

**Question 6 :** Vous devez provisionner une infrastructure cloud déclarative et reproductible (réseau, machines, etc.) à partir de code versionné. Quel outil du cours est le plus adapté ?

a) Prometheus

b) Helm

c) Terraform

d) Jenkins

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Terraform est l'outil d'Infrastructure as Code (IaC) : il décrit de façon déclarative les ressources cloud et les provisionne de manière reproductible. Helm cible le déploiement applicatif sur Kubernetes, Prometheus le monitoring, et Jenkins l'orchestration de pipelines.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
