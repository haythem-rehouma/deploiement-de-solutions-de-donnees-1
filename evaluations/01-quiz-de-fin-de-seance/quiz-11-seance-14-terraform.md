<a id="top"></a>

# Quiz — Séance 14 — Terraform (providers, variables, outputs, state, modules)

> **Évaluation sommative** · Quiz de fin de séance 14 (8 septembre 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** providers, variables, outputs, state, modules

---

**Question 1 :** Quel est le rôle d'un `provider` dans Terraform ?

a) Stocker l'état de l'infrastructure de façon distante

b) Servir de plugin permettant à Terraform de dialoguer avec une API (AWS, Azure, Docker, etc.)

c) Définir les variables d'entrée d'une configuration

d) Regrouper plusieurs ressources réutilisables

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Un provider est un plugin qui sait communiquer avec l'API d'une plateforme cible (AWS, GCP, Azure, Kubernetes, Docker…) afin de créer et gérer les ressources correspondantes.

</details>

---

**Question 2 :** Quelle commande applique les changements après avoir vérifié le plan d'exécution ?

a) `terraform deploy`

b) `terraform run`

c) `terraform apply`

d) `terraform push`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `terraform apply` exécute les actions nécessaires pour atteindre l'état désiré décrit dans la configuration. Il est généralement précédé de `terraform plan`.

</details>

---

**Question 3 :** À quoi sert le fichier `terraform.tfstate` ?

a) À stocker les identifiants d'accès au provider

b) À enregistrer la correspondance entre la configuration et les ressources réelles déployées

c) À définir les valeurs par défaut des variables

d) À documenter les sorties (outputs) du module

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le fichier d'état (state) mémorise la cartographie entre les ressources décrites dans le code et celles réellement provisionnées. Il permet à Terraform de connaître l'infrastructure existante et de calculer les écarts.

</details>

---

**Question 4 :** Comment déclare-t-on une variable d'entrée dans Terraform ?

a) `variable "region" { default = "us-east-1" }`

b) `var region = "us-east-1"`

c) `input region { value = "us-east-1" }`

d) `set region = "us-east-1"`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — Une variable d'entrée se déclare avec le bloc `variable "nom" { ... }`, dans lequel on peut préciser `type`, `default`, `description`, etc. On y fait ensuite référence via `var.nom`.

</details>

---

**Question 5 :** Quel est l'objectif principal d'un `output` dans Terraform ?

a) Sauvegarder l'état dans un bucket distant

b) Exposer des valeurs (ex. IP publique, ID de ressource) après le déploiement

c) Importer une ressource existante dans le state

d) Détruire les ressources inutilisées

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Les `output` rendent visibles certaines valeurs calculées après `apply` (adresses IP, identifiants, URL…). Elles servent aussi à transmettre des données d'un module à un autre.

</details>

---

**Question 6 :** Pourquoi utilise-t-on un état distant (remote state, ex. backend S3) plutôt qu'un fichier `tfstate` local lors d'un travail en équipe ?

a) Pour accélérer la commande `terraform plan`

b) Pour partager l'état et permettre le verrouillage (lock) afin d'éviter les modifications concurrentes

c) Pour chiffrer automatiquement le code Terraform

d) Pour éviter d'avoir à déclarer un provider

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Un backend distant centralise le fichier d'état pour que toute l'équipe travaille sur la même source de vérité, et fournit un mécanisme de verrouillage (state locking) empêchant deux `apply` simultanés de corrompre l'état.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
