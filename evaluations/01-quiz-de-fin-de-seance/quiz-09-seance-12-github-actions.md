<a id="top"></a>

# Quiz — Séance 12 — CI/CD Kubernetes avec GitHub Actions

> **Évaluation sommative** · Quiz bilan de fin de séance 12 (25 août 2026) · Pondération 1 % · QCM individuel en fin de séance
>
> **Contenus évalués :** CI/CD Kubernetes avec GitHub Actions · workflows, déclencheurs et secrets · build et push d'images Docker · déploiement avec kubectl et Helm

---

**Question 1 :** Où doit-on placer un fichier de workflow GitHub Actions pour que GitHub le détecte et l'exécute automatiquement ?

a) À la racine du dépôt, dans `workflow.yml`

b) Dans `.github/workflows/`

c) Dans `/etc/github/`

d) Dans un dossier `ci/` libre

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — GitHub détecte automatiquement tout fichier `.yml`/`.yaml` placé dans le dossier `.github/workflows/` à la racine du dépôt.

</details>

---

**Question 2 :** Dans un workflow, quelle clé de premier niveau définit **quand** (sur quel événement) le workflow se déclenche ?

a) `jobs`

b) `runs-on`

c) `on`

d) `steps`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — La clé `on` déclare les événements déclencheurs (`push`, `pull_request`, `workflow_dispatch`, `schedule`…). C'est le cœur de l'automatisation.

</details>

---

**Question 3 :** Dans un job, à quoi sert la clé `runs-on: ubuntu-latest` ?

a) À choisir le système du runner (la machine virtuelle) qui exécute le job

b) À installer Ubuntu sur le cluster Kubernetes

c) À définir le nom de l'image Docker à construire

d) À déclencher le workflow toutes les nuits

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — `runs-on` indique le type de runner (système d'exploitation de la machine) sur lequel les étapes du job s'exécutent, par exemple `ubuntu-latest`.

</details>

---

**Question 4 :** Comment référence-t-on, dans un workflow, un mot de passe ou un token stocké de manière sécurisée dans les paramètres du dépôt ?

a) En l'écrivant en clair dans le YAML

b) Via `${{ secrets.NOM_DU_SECRET }}`

c) Via `${{ env.PASSWORD }}` uniquement

d) En le mettant dans le message de commit

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Les secrets configurés dans le dépôt s'utilisent avec l'expression `${{ secrets.NOM }}`. Ils ne doivent jamais apparaître en clair dans le fichier de workflow ni dans les logs.

</details>

---

**Question 5 :** Avant de pousser une image vers un registre privé (Docker Hub, GHCR…), quelle étape est indispensable dans le workflow ?

a) Supprimer le Dockerfile

b) S'authentifier auprès du registre (étape de login avec des identifiants stockés en secrets)

c) Désactiver le cache Docker

d) Créer un Ingress

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Il faut d'abord se connecter au registre (ex. action `docker/login-action` avec username + token en secrets) avant de pouvoir `push` l'image construite.

</details>

---

**Question 6 :** Quelle bonne pratique recommande-t-on pour **taguer** l'image construite dans une pipeline CI/CD, afin de garder une traçabilité ?

a) Utiliser toujours `latest` exclusivement

b) Ne jamais taguer l'image

c) Taguer avec une référence unique (ex. le SHA du commit), en plus éventuellement de `latest`

d) Utiliser un tag aléatoire différent à chaque exécution sans lien avec le code

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Taguer avec le SHA du commit (ou un numéro de version) lie chaque image à une version précise du code, ce qui rend les déploiements et rollbacks traçables. `latest` seul est ambigu pour la production.

</details>

---

**Question 7 :** Dans l'étape de déploiement d'une pipeline, quelle commande applique un manifeste Kubernetes au cluster ?

a) `docker build`

b) `git push`

c) `kubectl apply -f`

d) `helm package`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `kubectl apply -f <manifeste>` envoie l'état désiré au cluster (création/mise à jour des objets). Alternative avec Helm : `helm upgrade --install`.

</details>

---

**Question 8 :** Pour déployer via Helm dans un workflow et créer la release si elle n'existe pas encore, quelle commande est la plus adaptée ?

a) `helm install` (échoue si la release existe déjà)

b) `helm upgrade --install <release> <chart>`

c) `helm delete <release>`

d) `helm template <chart>`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `helm upgrade --install` met à jour la release si elle existe, sinon la crée. C'est idempotent et donc idéal pour une pipeline CI/CD rejouée à chaque déploiement.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
