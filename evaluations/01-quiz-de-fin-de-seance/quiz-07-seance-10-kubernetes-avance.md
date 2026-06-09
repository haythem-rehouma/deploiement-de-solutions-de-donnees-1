<a id="top"></a>

# Quiz — Séance 10 — Kubernetes avancé (Ingress, ConfigMaps, Secrets, LoadBalancer)

> **Évaluation sommative** · Quiz bilan de fin de séance 10 (11 août 2026) · Pondération 1 % · QCM individuel en fin de séance
>
> **Contenus évalués :** Ingress et routage HTTP (L7) · ConfigMaps · Secrets · Service Cloud LoadBalancer · rappels des bases de Kubernetes (Pods, Services)

---

**Question 1 :** À quelle couche réseau travaille un Ingress, et que sait-il faire qu'un Service LoadBalancer ne fait pas ?

a) Couche 4 (TCP) ; il chiffre le trafic

b) Couche 7 (HTTP) ; il route selon le nom de domaine et le chemin de l'URL

c) Couche 2 (Ethernet) ; il gère les adresses MAC

d) Couche 3 (IP) ; il attribue des IP aux Pods

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — L'Ingress opère en couche 7 (HTTP/HTTPS) : il « lit » l'URL et les en-têtes pour router vers le bon Service selon l'hôte et le chemin. Un Service LoadBalancer travaille en couche 4 (TCP/UDP) et ne comprend pas le contenu HTTP.

</details>

---

**Question 2 :** Un objet `Ingress` est appliqué dans le cluster mais le routage ne fonctionne pas. Quelle est la cause la plus probable ?

a) Le cluster n'a pas de nodes

b) Aucun Ingress Controller (ex. ingress-nginx) n'est installé pour interpréter les règles

c) Les Pods n'ont pas de Dockerfile

d) Le Service cible est de type ClusterIP

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Un objet `Ingress` n'est qu'une règle déclarative ; il ne fait rien seul. Il faut un **Ingress Controller** (un pod, souvent NGINX) qui observe ces règles et configure réellement le reverse-proxy.

</details>

---

**Question 3 :** Quel objet Kubernetes utilise-t-on pour externaliser des données de configuration **non sensibles** (ex. niveau de log, URL d'API) hors de l'image ?

a) Un Secret

b) Un Ingress

c) Un ConfigMap

d) Un PersistentVolume

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le **ConfigMap** stocke des paires clé/valeur de configuration non sensibles. On peut les injecter dans un Pod comme variables d'environnement ou comme fichiers montés.

</details>

---

**Question 4 :** À propos des Secrets Kubernetes, quelle affirmation est correcte ?

a) Les valeurs sont chiffrées de façon irréversible

b) base64 est un encodage, pas un chiffrement : la valeur est décodable instantanément

c) Un Secret ne peut pas être injecté dans un Pod

d) Les Secrets se stockent obligatoirement sur Docker Hub

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Les valeurs d'un Secret sont stockées **encodées en base64** dans `data`. base64 est un simple encodage réversible, pas du chiffrement. La sécurité réelle repose sur le contrôle d'accès (RBAC) et le chiffrement au repos d'etcd.

</details>

---

**Question 5 :** Dans un manifeste de Pod, quelle construction injecte **toutes** les clés d'un ConfigMap d'un coup comme variables d'environnement ?

a) `env.valueFrom.configMapKeyRef`

b) `envFrom.configMapRef`

c) `volumeMounts.configMap`

d) `spec.selector.configMap`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — `envFrom.configMapRef` importe en bloc toutes les clés du ConfigMap. À l'inverse, `env.valueFrom.configMapKeyRef` n'importe qu'**une seule** clé (avec renommage possible).

</details>

---

**Question 6 :** Quel type de Service demande à un fournisseur cloud (AWS, GCP, Azure) de provisionner un répartiteur de charge externe avec une IP publique ?

a) `ClusterIP`

b) `NodePort`

c) `LoadBalancer`

d) `Headless`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le type `LoadBalancer` déclenche, chez un fournisseur cloud, la création d'un load balancer managé (ELB, etc.) avec une IP publique routant vers les Pods. Sur un cluster local sans intégration cloud, il reste souvent en `<pending>`.

</details>

---

**Question 7 :** (Rappel bases) Pourquoi un Service est-il nécessaire alors qu'un Pod possède déjà sa propre adresse IP ?

a) Parce que les Pods n'ont jamais d'IP

b) Parce que l'IP d'un Pod est éphémère (recréation) ; le Service offre un point d'accès stable et le load balancing

c) Parce que le Service remplace le conteneur

d) Parce que seuls les Services peuvent exécuter du code

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Les Pods sont jetables et changent d'IP à chaque recréation. Le Service fournit un nom DNS et une IP stables, et répartit le trafic vers l'ensemble des Pods correspondant à son selector.

</details>

---

**Question 8 :** (Rappel bases) Quelle ressource Kubernetes gère un ensemble de Pods identiques, maintient le nombre désiré de répliques et permet les mises à jour progressives ?

a) Le ConfigMap

b) L'Ingress

c) Le Deployment

d) Le Secret

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le **Deployment** déclare l'état désiré (image + nombre de répliques) ; son contrôleur crée/recrée les Pods via un ReplicaSet et orchestre les rolling updates et rollbacks.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
