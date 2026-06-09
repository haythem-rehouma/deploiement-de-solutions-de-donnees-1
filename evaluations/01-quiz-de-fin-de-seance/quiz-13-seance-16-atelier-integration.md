<a id="top"></a>

# Quiz bilan — Séance 16 — Atelier d'intégration (chaîne CI/CD de bout en bout)

> **Évaluation sommative** · Quiz bilan de fin de séance 16 (22 septembre 2026) · Pondération 1 % · QCM individuel en fin de séance
>
> **Contenus évalués :** chaîne CI/CD complète de bout en bout (Git → Jenkins/GitHub Actions → Docker → Kubernetes/Helm → monitoring)

---

**Question 1 :** Dans une chaîne CI/CD complète, quel événement déclenche typiquement le démarrage automatique du pipeline ?

a) Le redémarrage manuel du cluster Kubernetes

b) Un `git push` (ou une pull request) sur le dépôt

c) L'expiration du fichier `terraform.tfstate`

d) Le déclenchement d'une alerte Prometheus

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le pipeline d'intégration continue est déclenché par un événement de versionnement (push, merge ou pull request), capté via un webhook par Jenkins ou par un workflow GitHub Actions.

</details>

---

**Question 2 :** Quelle est la place logique de l'exécution des tests automatisés dans la chaîne CI/CD ?

a) Après le déploiement en production uniquement

b) Pendant la phase d'intégration continue, après le build et avant de produire l'image livrable

c) Jamais : les tests sont manuels en CI/CD

d) Uniquement au moment du `helm install`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Les tests (unitaires, intégration) s'exécutent tôt dans le pipeline, juste après la compilation/build : on veut détecter les régressions avant de construire et publier l'artefact, selon le principe « fail fast ».

</details>

---

**Question 3 :** Après le build de l'application, quelle étape permet de la rendre portable et reproductible avant le déploiement ?

a) La construction d'une image Docker et son push vers un registre

b) La création d'un fichier `inventory.ini`

c) L'exécution de `terraform plan`

d) La configuration d'un dashboard Grafana

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — On empaquette l'application dans une image Docker (via un `Dockerfile`), puis on la pousse vers un registre (Docker Hub, GHCR, ECR…). L'image devient l'artefact immuable déployé ensuite.

</details>

---

**Question 4 :** Quel outil sert à packager et déployer une application sur Kubernetes via des « charts » paramétrables ?

a) Ansible

b) Prometheus

c) Helm

d) Maven

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Helm est le gestionnaire de paquets de Kubernetes : un chart regroupe les manifestes (Deployment, Service, etc.) avec des valeurs paramétrables (`values.yaml`), facilitant déploiements et mises à jour.

</details>

---

**Question 5 :** Dans un manifeste Kubernetes, quel objet garantit qu'un nombre donné de réplicas d'un pod reste en permanence en cours d'exécution ?

a) Un `Service`

b) Un `ConfigMap`

c) Un `Ingress`

d) Un `Deployment`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : d)** — Le `Deployment` (via le ReplicaSet sous-jacent) maintient le nombre de réplicas souhaité, recrée les pods défaillants et orchestre les mises à jour progressives (rolling updates).

</details>

---

**Question 6 :** Quel mécanisme permet de revenir rapidement à la version précédente d'une application après un déploiement défectueux ?

a) Un `git clone` du dépôt

b) Un rollback (ex. `kubectl rollout undo` ou `helm rollback`)

c) Une règle d'alerte Prometheus

d) Une variable d'environnement `DEBUG=true`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Kubernetes et Helm conservent l'historique des révisions : `kubectl rollout undo deployment/<nom>` ou `helm rollback <release>` restaurent rapidement l'état antérieur connu comme stable.

</details>

---

**Question 7 :** Une fois l'application déployée, quel est le rôle de l'étape de monitoring dans la chaîne ?

a) Compiler le code source de l'application

b) Surveiller métriques, logs et déclencher des alertes en cas d'anomalie en production

c) Construire les images Docker

d) Définir les variables Terraform

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le monitoring (Prometheus/Grafana + gestion des logs) clôt la boucle CI/CD : il observe l'application en production, mesure sa santé et déclenche des alertes, permettant une réaction rapide aux incidents.

</details>

---

**Question 8 :** Quel énoncé décrit le mieux la différence entre intégration continue (CI) et déploiement continu (CD) ?

a) La CI concerne le build/test automatisés du code ; le CD automatise la livraison/déploiement de l'application

b) La CI déploie en production ; le CD compile le code

c) Ce sont deux noms exacts pour la même étape

d) La CI gère le monitoring ; le CD gère les inventaires Ansible

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — L'intégration continue automatise l'assemblage et la validation du code (build + tests) à chaque changement. Le déploiement continu prolonge la chaîne en livrant/déployant automatiquement l'artefact validé vers les environnements cibles.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
