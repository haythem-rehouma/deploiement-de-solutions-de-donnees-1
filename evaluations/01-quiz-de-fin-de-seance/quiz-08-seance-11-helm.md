<a id="top"></a>

# Quiz — Séance 11 — Helm (charts, values, templates)

> **Évaluation sommative** · Quiz de fin de séance 11 (18 août 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** Helm, le gestionnaire de paquets de Kubernetes · charts (Deployment + Service + Ingress) · values.yaml · templates

---

**Question 1 :** Comment décrit-on le mieux Helm pour Kubernetes ?

a) Un moteur de conteneurs comme Docker

b) Le gestionnaire de paquets de Kubernetes (équivalent d'`apt` ou `npm`)

c) Un fournisseur cloud de load balancers

d) Un outil de monitoring des Pods

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Helm est le gestionnaire de paquets de Kubernetes : il regroupe tous les YAML d'une application dans un paquet versionné que l'on installe, met à jour et désinstalle en une commande.

</details>

---

**Question 2 :** Quelle est la différence entre un **chart** et une **release** ?

a) Aucune, ce sont des synonymes

b) Le chart est l'instance déployée ; la release est le modèle réutilisable

c) Le chart est le modèle (paquet de templates + valeurs) ; la release est une instance installée du chart, avec un nom unique

d) Le chart sert au build, la release au monitoring

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le **chart** est le modèle (la recette) ; une **release** est une instance réellement déployée de ce chart dans le cluster, avec son propre nom. Un même chart peut donner plusieurs releases.

</details>

---

**Question 3 :** À quoi sert le fichier `values.yaml` d'un chart ?

a) À décrire les nodes du cluster

b) À fournir les valeurs par défaut, paramétrables, injectées dans les templates

c) À stocker les logs de l'application

d) À déclarer les dépendances système de l'hôte

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `values.yaml` contient les valeurs par défaut (image, nombre de répliques, ports, options d'ingress…). On les surcharge avec `--set` ou un fichier de valeurs personnalisé lors de l'installation.

</details>

---

**Question 4 :** Dans un template Helm, quelle syntaxe référence le champ `replicaCount` défini dans `values.yaml` ?

a) `{{ .Values.replicaCount }}`

b) `${replicaCount}`

c) `<% replicaCount %>`

d) `{{ values.replicaCount }}`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — Helm utilise le moteur de templates Go : `{{ .Values.replicaCount }}` injecte la valeur issue de `values.yaml`. Les délimiteurs sont les doubles accolades `{{ }}` et l'objet racine des valeurs est `.Values`.

</details>

---

**Question 5 :** Un chart d'application web complet contient typiquement, dans son dossier `templates/`, les manifestes de quels objets Kubernetes ?

a) Uniquement un Pod isolé

b) Un Deployment, un Service et (souvent) un Ingress

c) Seulement un ConfigMap

d) Uniquement un fichier Dockerfile

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Un chart web regroupe généralement un **Deployment** (les Pods), un **Service** (l'accès stable interne) et un **Ingress** (l'exposition HTTP/HTTPS), tous générés à partir des templates et des valeurs.

</details>

---

**Question 6 :** Quelle commande met à jour une release existante après modification du chart ou des valeurs ?

a) `helm install <release> <chart>`

b) `helm delete <release>`

c) `helm upgrade <release> <chart>`

d) `kubectl rollout undo`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `helm upgrade` applique les changements à une release existante en créant une nouvelle révision (permettant un `helm rollback` ultérieur). `helm install` sert au premier déploiement.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
