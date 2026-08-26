<a id="top"></a>

# Questions — Avez-vous compris Helm et le projet 13 ?

> **Projet [projet13-kubernetes-helm-tp](README.md)** · 36 questions d'auto-évaluation
>
> Ces questions portent **précisément sur CE projet** (`chart/`, `values.yaml`, `values-dev.yaml`, `_helpers.tpl`, `apps/portail`, les trois pannes). Répondez **avant** de dérouler le corrigé. Les bonnes réponses sont réparties entre A, B, C et D.

## Table des matières

| Thème | Questions |
|---|---|
| [A — Helm : idées de base](#a--helm--idees-de-base) | 1 à 6 |
| [B — Anatomie du Chart hedge](#b--anatomie-du-chart-hedge) | 7 à 12 |
| [C — Templates, Values et helpers](#c--templates-values-et-helpers) | 13 à 20 |
| [D — Les trois environnements](#d--les-trois-environnements) | 21 à 26 |
| [E — install, upgrade, rollback](#e--install-upgrade-rollback) | 27 à 31 |
| [F — Les trois pannes du projet](#f--les-trois-pannes-du-projet) | 32 à 36 |
| [Corrigé récapitulatif](#corrige-recapitulatif) | — |

---

## A — Helm : idées de base

**1.** En une phrase, que fait Helm ?

- A) Il remplace Kubernetes : on n'a plus besoin de `kubectl`
- B) Il génère des manifestes Kubernetes à partir de templates et de valeurs, puis les applique comme une unité versionnée
- C) Il construit les images Docker à la place de `docker build`
- D) Il sert uniquement à installer des applications depuis Internet

<details>
<summary>Corrigé</summary>

**B.** Helm rend des templates YAML avec des variables (`values.yaml`), puis applique le résultat dans le cluster sous le nom d'une **release**. `kubectl` reste indispensable pour observer le cluster.
</details>

**2.** Qu'est-ce qu'une **release** Helm ?

- A) Une nouvelle version du code Python de l'application
- B) Un fichier `Chart.yaml` signé
- C) Une **installation** concrète d'un Chart, identifiée par un nom (`hedge-dev`, `hedge-staging`, `hedge-prod`)
- D) Un namespace Kubernetes

<details>
<summary>Corrigé</summary>

**C.** Un même Chart peut être installé plusieurs fois. Chaque installation est une release. Le namespace est le lieu d'isolement ; la release est l'objet Helm.
</details>

**3.** Dans ce projet, quelle affirmation est vraie ?

- A) `{{ .Chart.Name }}` change à chaque `helm install`, `{{ .Release.Name }}` reste identique
- B) `{{ .Release.Name }}` change à chaque `helm install`, `{{ .Chart.Name }}` reste identique
- C) Les deux restent identiques
- D) Les deux changent à chaque `helm upgrade`

<details>
<summary>Corrigé</summary>

**B.** Le Chart s'appelle toujours `hedge`. Le nom de release (`hedge-dev`, `hedge-staging`, `hedge-prod`) change à chaque installation. C'est ce contraste qui permet le multi-environnement.
</details>

**4.** Quelle commande produit le YAML **sans rien déployer** dans le cluster ?

- A) `helm install`
- B) `helm upgrade`
- C) `helm lint`
- D) `helm template`

<details>
<summary>Corrigé</summary>

**D.** `helm template` est un rendu **sec**. `helm lint` vérifie la syntaxe, mais n'affiche pas les manifestes. `install` et `upgrade` touchent le cluster.
</details>

**5.** À quoi sert un fichier dont le nom commence par `_` dans `templates/` (exemple : `_helpers.tpl`) ?

- A) Helm l'applique en premier, avant tous les autres
- B) Il produit un manifeste Kubernetes nommé `_helpers`
- C) Il ne produit **aucun** manifeste : il définit des fonctions réutilisables (`define` / `include`)
- D) Il est ignoré complètement par Helm

<details>
<summary>Corrigé</summary>

**C.** Le préfixe `_` signifie « helper uniquement ». Les fonctions s'appellent ensuite avec `{{ include "hedge.labels" ... }}`.
</details>

**6.** Dans `Chart.yaml`, quelle est la différence entre `version` et `appVersion` ?

- A) Aucune : ce sont deux alias du même champ
- B) `version` est la version du **Chart** (emballage Helm) ; `appVersion` est la version de **l'application** déployée
- C) `version` est le numéro de révision Helm ; `appVersion` est le tag Docker
- D) `version` sert à Kubernetes ; `appVersion` sert à Helm

<details>
<summary>Corrigé</summary>

**B.** On peut changer `version` (par exemple `0.1.0` vers `0.2.0`) sans changer le code applicatif, et inversement. Ce n'est pas le numéro de révision (`helm history`), ni automatiquement le tag d'image.
</details>

---

## B — Anatomie du Chart hedge

**7.** Dans ce projet, que contient le dossier `apps/` ?

- A) Les templates Helm à compléter
- B) Le code Python du `portail` et de l'`api`, **à ne pas modifier**
- C) Les trois fichiers `values-<env>.yaml`
- D) Le script `valider.ps1`

<details>
<summary>Corrigé</summary>

**B.** Vous êtes le DevOps : le code applicatif est déjà écrit. Modifier `apps/` est interdit par le règlement du TP.
</details>

**8.** Pourquoi le dossier `chart/casses/` n'est-il **pas** à l'intérieur de `chart/templates/` ?

- A) Helm refuse les fichiers dont le nom commence par `casse-`
- B) Pour que Helm **ne les charge pas automatiquement** : vous les copiez un par un dans `templates/` pour observer le bug
- C) Kubernetes n'accepte pas plus de 5 fichiers dans `templates/`
- D) Ces fichiers sont des images Docker, pas des templates

<details>
<summary>Corrigé</summary>

**B.** Helm rend **tous** les fichiers de `templates/` (sauf ceux préfixés par `_`). Laisser les pannes dans `casses/` évite de casser le Chart avant la mission 6.
</details>

**9.** Dans `values.yaml` de ce projet, sur quel port le **conteneur** `portail` écoute-t-il ?

- A) 80
- B) 30130
- C) 5000
- D) 8000

<details>
<summary>Corrigé</summary>

**C.** `portail.service.targetPort: 5000` (c'est le port Flask). `port: 80` est le port du Service. `nodePort: 30130` est le port exposé sur la machine (DEV). `8000` est le `targetPort` de l'`api`.
</details>

**10.** Dans ce projet, quel type de Service est prévu pour l'`api` dans `values.yaml` ?

- A) NodePort
- B) LoadBalancer
- C) ExternalName
- D) ClusterIP

<details>
<summary>Corrigé</summary>

**D.** L'api reste **interne** au cluster. Le portail l'appelle par DNS (`http://hedge-dev-api`). Seul le portail est en NodePort pour le navigateur.
</details>

**11.** Combien d'images Docker devez-vous construire **une seule fois** avant de déployer les trois environnements ?

- A) Une seule (`hedge:1.0`)
- B) Deux (`hedge-portail:1.0` et `hedge-api:1.0`)
- C) Trois (une par environnement)
- D) Six (deux images × trois environnements)

<details>
<summary>Corrigé</summary>

**B.** Les trois environnements réutilisent **les mêmes images**. Ce qui change, ce sont les **valeurs** injectées (couleur, replicas, message), pas le code.
</details>

**12.** Le portail affiche un bandeau coloré et un message. D'où viennent ces informations ?

- A) Elles sont codées en dur dans `apps/portail/app.py`
- B) Elles viennent de variables d'environnement injectées par Helm depuis les Values
- C) Elles sont lues dans un fichier `couleur.txt` monté en volume
- D) Elles sont choisies au hasard par Flask au démarrage

<details>
<summary>Corrigé</summary>

**B.** `app.py` lit `THEME_COLOR`, `BANNIERE_MESSAGE`, `ENVIRONMENT`, etc. Le **même** code s'adapte à DEV / STAGING / PROD sans modification.
</details>

---

## C — Templates, Values et helpers

**13.** Que rend `{{ .Values.portail.replicas }}` si `values-prod.yaml` contient `portail.replicas: 3` et que vous installez avec `-f values-prod.yaml` ?

- A) `1` (la valeur de `values.yaml` gagne toujours)
- B) `3` (le fichier passé avec `-f` surcharge `values.yaml`)
- C) Une erreur : on ne peut pas avoir la même clé deux fois
- D) `default`

<details>
<summary>Corrigé</summary>

**B.** `values.yaml` fournit les défauts. Chaque `values-<env>.yaml` **surcharge** uniquement ce qui change. C'est le principe même du multi-environnement.
</details>

**14.** Pourquoi un fichier `values-prod.yaml` qui redéfinit `portail.image.repository` est-il une **erreur pédagogique** dans ce projet ?

- A) Parce que le champ `repository` n'existe pas
- B) Parce que l'image est identique dans les trois environnements : cette clé n'a pas de raison d'être recopiée
- C) Parce que Helm refuse plus de 10 clés dans un fichier de valeurs
- D) Parce que le repository doit être défini uniquement dans `Chart.yaml`

<details>
<summary>Corrigé</summary>

**B.** On ne recopie dans `values-<env>.yaml` **que** ce qui distingue l'environnement (replicas, nodePort, couleur, message, `environment`). Recopier le reste, c'est revenir au copier-coller que Helm est censé remplacer.
</details>

**15.** Dans ce projet, le helper `hedge.fullname` doit produire, pour la release `hedge-dev` et le composant `portail` :

- A) `hedge-portail`
- B) `portail-hedge-dev`
- C) `hedge-dev-portail`
- D) `hedge`

<details>
<summary>Corrigé</summary>

**C.** Format `<release>-<composant>`. C'est ce préfixe qui évite les collisions de noms entre DEV, STAGING et PROD (et même dans un même namespace).
</details>

**16.** Quels labels doivent **seuls** figurer dans `hedge.selectorLabels` ?

- A) `name`, `instance`, `component` — les trois qui ne changeront jamais pour cette instance
- B) Tous les labels de `hedge.labels`, y compris `version` et `hedge/environment`
- C) Uniquement `hedge/environment`
- D) Uniquement `helm.sh/chart`

<details>
<summary>Corrigé</summary>

**A.** `spec.selector.matchLabels` est **immuable**. Y mettre `version`, `helm.sh/chart` ou `hedge/environment` fera échouer le premier `helm upgrade` qui change ces valeurs.
</details>

**17.** Pourquoi `BACKEND_URL` du portail ne peut-il pas valoir `http://api` en dur ?

- A) Parce que Flask refuse les URL sans numéro de port
- B) Parce que le Service s'appelle `hedge-<release>-api` (ex. `hedge-dev-api`) : le nom DNS dépend de la release
- C) Parce que l'api n'a pas de Service
- D) Parce que le portail n'appelle jamais l'api

<details>
<summary>Corrigé</summary>

**B.** Le helper `hedge.fullname` construit `hedge-dev-api`, `hedge-staging-api`, `hedge-prod-api`. Un nom en dur `api` ne résout rien dans le namespace.
</details>

**18.** Que fait `{{ .Values.environment | quote }}` ?

- A) Il convertit la valeur en entier
- B) Il ajoute des **guillemets** autour de la valeur rendue (indispensable pour une string YAML)
- C) Il affiche la valeur en majuscules
- D) Il ignore la valeur si elle est vide

<details>
<summary>Corrigé</summary>

**B.** `quote` produit `"dev"` plutôt que `dev`. Sans guillemets, certaines valeurs YAML (couleurs hexadécimales, messages) peuvent casser le manifeste.
</details>

**19.** Pourquoi `replicas: "{{ .Values.portail.replicas }}"` (avec des guillemets autour de tout le template) est-il dangereux ?

- A) Helm refuse les guillemets dans un Deployment
- B) Kubernetes attend un **entier** ; le rendu devient la **chaîne** `"1"`, que l'API refuse
- C) La valeur sera toujours 0
- D) Les guillemets multiplient le nombre de replicas par deux

<details>
<summary>Corrigé</summary>

**B.** Ne jamais quotter un entier. On écrit `replicas: {{ .Values.portail.replicas }}`, pas `replicas: "{{ ... }}"`.
</details>

**20.** À quoi sert `nindent 4` dans `{{ include "hedge.labels" ... | nindent 4 }}` ?

- A) À limiter le helper à 4 labels
- B) À indenter correctement le YAML rendu (sinon le manifeste est illisible ou invalide)
- C) À créer 4 replicas
- D) À attendre 4 secondes avant le rendu

<details>
<summary>Corrigé</summary>

**B.** Helm injecte un bloc de plusieurs lignes. Sans `nindent`, l'indentation YAML casse et vous obtenez `error converting YAML to JSON`.
</details>

---

## D — Les trois environnements

**21.** Dans ce projet, quel `nodePort` est réservé à **STAGING** ?

- A) 30130
- B) 30131
- C) 30132
- D) 30500

<details>
<summary>Corrigé</summary>

**B.** DEV = 30130, STAGING = 30131, PROD = 30132. Le 30500 est le portail du **projet 12**, pas de celui-ci.
</details>

**22.** Combien de replicas `portail` + `api` devez-vous avoir en **PROD** une fois le Chart correctement déployé ?

- A) 1 + 1
- B) 2 + 2
- C) 3 + 3
- D) 5 + 1

<details>
<summary>Corrigé</summary>

**C.** PROD : 3 portails et 3 apis. DEV : 1+1. STAGING : 2+2. Au total, **12 Pods** applicatifs côte à côte.
</details>

**23.** Quelle couleur de bandeau correspond à l'environnement **DEV** ?

- A) Orange `#ea580c`
- B) Vert `#16a34a`
- C) Gris `#64748b`
- D) Bleu `#2563eb`

<details>
<summary>Corrigé</summary>

**D.** Bleu = DEV, orange = STAGING, vert = PROD. Le gris `#64748b` est la couleur **par défaut** de `values.yaml` (environnement `default`), pas celle d'un des trois fichiers d'environnement.
</details>

**24.** Pourquoi déployer chaque environnement dans **son propre namespace** (`hedge-dev`, `hedge-staging`, `hedge-prod`) ?

- A) Helm refuse deux releases dans le même namespace, même avec des noms différents
- B) Pour isoler les objets, éviter les collisions de NodePort internes, et coller à la réalité d'une entreprise (un namespace par environnement)
- C) Parce que Docker Desktop n'autorise qu'un namespace
- D) Parce que `values.yaml` l'impose

<details>
<summary>Corrigé</summary>

**B.** Helm **autorise** plusieurs releases dans un même namespace (c'est d'ailleurs le piège de la panne 1 si les noms sont en dur). Les namespaces restent la bonne pratique : isolation, quotas, RBAC, clarté.
</details>

**25.** Quelle commande installe correctement l'environnement DEV de **ce** projet ?

- A) `kubectl apply -f chart/environments/values-dev.yaml`
- B) `helm install hedge-dev .\chart -f .\chart\environments\values-dev.yaml -n hedge-dev --create-namespace`
- C) `helm template hedge-dev .\chart`
- D) `docker compose up -d`

<details>
<summary>Corrigé</summary>

**B.** On pointe le **Chart** (`.\chart`), on surcharge avec `-f values-dev.yaml`, on nomme la release `hedge-dev`, on crée le namespace. `helm template` ne déploie rien. `values-dev.yaml` n'est pas un manifeste `kubectl`.
</details>

**26.** Si vous ouvrez `http://localhost:30132` et que le bandeau est **vert**, que voyez-vous nécessairement dans le JSON `/api-json` ?

- A) `"env": "dev"`
- B) `"env": "staging"`
- C) `"env": "prod"` et `"backend": "ok"` si l'api du même namespace répond
- D) `"env": "default"`

<details>
<summary>Corrigé</summary>

**C.** Le port 30132 est celui de PROD. Le champ `env` vient de `.Values.environment`. `backend: ok` prouve que `BACKEND_URL` pointe bien vers le Service api **de cette release**.
</details>

---

## E — install, upgrade, rollback

**27.** Après `helm install hedge-dev ...` puis `helm upgrade hedge-dev ... --set portail.replicas=5`, que montre `helm history hedge-dev -n hedge-dev` ?

- A) Une seule révision : Helm écrase l'historique
- B) Au moins deux révisions : 1 = Install, 2 = Upgrade
- C) Zéro révision : l'historique n'existe que après un rollback
- D) Uniquement la révision 5, parce que replicas vaut 5

<details>
<summary>Corrigé</summary>

**B.** Chaque `install` / `upgrade` / `rollback` crée une **révision**. C'est ce journal qui rend le retour arrière possible.
</details>

**28.** `helm rollback hedge-dev 1 -n hedge-dev` fait quoi ?

- A) Supprime la release
- B) Réapplique l'état de la **révision 1** et crée une **nouvelle** révision (souvent n° 3) décrite comme `Rollback to 1`
- C) Revient au code Git du premier commit
- D) Remet `values.yaml` à zéro sur le disque

<details>
<summary>Corrigé</summary>

**B.** Le rollback n'efface pas l'historique : il ajoute une révision. `values-dev.yaml` sur votre disque ne change pas.
</details>

**29.** Quelle est la différence fondamentale entre `helm upgrade --set portail.replicas=5` et `kubectl scale deploy/hedge-dev-portail --replicas=5` ?

- A) Aucune : les deux font exactement la même chose
- B) `kubectl scale` est plus lent
- C) `helm upgrade` est **tracé et annulable** par Helm ; `kubectl scale` sort du contrôle de Helm et sera **écrasé** au prochain upgrade sans `--set`
- D) `kubectl scale` est interdit par Kubernetes sur un objet créé par Helm

<details>
<summary>Corrigé</summary>

**C.** Helm reconverge vers les Values au prochain `upgrade`. Une modification manuelle (`scale`, `edit`) est une dette invisible. C'est la question de réflexion de la mission 5.
</details>

**30.** `helm uninstall hedge-dev -n hedge-dev` supprime-t-il le namespace `hedge-dev` ?

- A) Oui, toujours
- B) Non : il retire les objets de la release, pas le namespace (sauf si vous le supprimez ensuite avec `kubectl delete namespace`)
- C) Oui, mais seulement si le namespace est vide
- D) Non, et les Deployments restent en place

<details>
<summary>Corrigé</summary>

**B.** `uninstall` enlève Deployment, Service, etc. de la release. Le namespace survit. D'où la commande de nettoyage du README : `kubectl delete namespace hedge-dev ...`.
</details>

**31.** Que se passe-t-il si vous faites `kubectl delete pod hedge-dev-portail-xxxxx -n hedge-dev` sur un Pod créé par le Deployment Helm ?

- A) Le Pod disparaît définitivement ; Helm affiche une erreur
- B) Le Deployment **recrée** immédiatement un Pod ; Helm n'a rien à « savoir » : il gère le Deployment, pas chaque Pod
- C) Tous les Pods du namespace sont tués
- D) Helm lance automatiquement un rollback

<details>
<summary>Corrigé</summary>

**B.** Helm déclare le Deployment. Kubernetes maintient le nombre de replicas. Supprimer un Pod est le geste pédagogique d'auto-réparation, pas une panne Helm.
</details>

---

## F — Les trois pannes du projet

**32.** Panne 1 (`casse-1-configmap.yaml`) : pourquoi la deuxième release dans le **même** namespace échoue-t-elle ?

- A) Parce que Helm n'autorise qu'une release par cluster
- B) Parce que `metadata.name: hedge-config` est un nom **statique** : les deux releases se disputent le même objet
- C) Parce que le ConfigMap n'a pas de `data`
- D) Parce que `values-staging.yaml` est invalide

<details>
<summary>Corrigé</summary>

**B.** Le correctif est de préfixer le nom avec la release : `{{ include "hedge.fullname" (dict "root" . "composant" "config") }}` produit `hedge-dev-config` et `hedge-staging-config`.
</details>

**33.** Panne 2 (`casse-2-worker-deployment.yaml`) : quel message Kubernetes voyez-vous au `helm upgrade --set environment=recette` ?

- A) `nil pointer evaluating interface {}.replicas`
- B) `ConfigMap "hedge-config" exists and cannot be imported`
- C) `spec.selector: Invalid value: ...: field is immutable`
- D) `ImagePullBackOff`

<details>
<summary>Corrigé</summary>

**C.** `hedge/environment` est dans `matchLabels`. Changer `environment` change le selector, ce que Kubernetes refuse. A et B sont les symptômes des pannes 3 et 1.
</details>

**34.** Dans un Deployment, où a-t-on le **droit** de mettre le label `hedge/environment` ?

- A) Uniquement dans `spec.selector.matchLabels`
- B) Dans les labels du Pod (`template.metadata.labels`) et les labels de l'objet, **pas** dans `matchLabels`
- C) Nulle part : ce label est interdit par Kubernetes
- D) Uniquement dans `Chart.yaml`

<details>
<summary>Corrigé</summary>

**B.** Les labels du Pod peuvent être riches et variables. Le **selector** doit rester un sous-ensemble **stable**. C'est toute la distinction `hedge.labels` vs `hedge.selectorLabels`.
</details>

**35.** Panne 3 (`casse-3-cache-deployment.yaml`) : que signifie l'erreur `nil pointer evaluating interface {}.replicas` sur `.Values.portal.replicas` ?

- A) Le cluster n'a plus de RAM
- B) Le chemin est **faux** : `values.yaml` définit `portail` (avec un **i**), pas `portal` — Helm évalue `nil.replicas`
- C) Il faut écrire `.Release.portal.replicas`
- D) Le champ `replicas` est interdit dans un Deployment créé par Helm

<details>
<summary>Corrigé</summary>

**B.** Une seule lettre de trop. Premier réflexe : `helm template --debug` et lire le **chemin** dans le message d'erreur.
</details>

**36.** Vous devez ajouter demain un 4e environnement `pre-prod`. Quels fichiers créez-vous, lesquels ne touchez-vous **pas** ?

- A) Vous dupliquez tout le dossier `chart/` et vous renommez le Chart
- B) Vous créez uniquement `chart/environments/values-preprod.yaml` (et un `helm install` + namespace) ; les templates et `values.yaml` restent inchangés
- C) Vous ajoutez un 4e Deployment en dur dans `templates/`
- D) Vous modifiez `apps/portail/app.py` pour reconnaître `pre-prod`

<details>
<summary>Corrigé</summary>

**B.** C'est la promesse de Helm : un Chart, N fichiers de valeurs. Si vous devez toucher les templates pour un nouvel environnement, le Chart est mal conçu.
</details>

---

## Corrigé récapitulatif

| # | Réponse | Idée à retenir |
|---|---|---|
| 1 | B | Helm = templates + values + release |
| 2 | C | Une release = une installation nommée |
| 3 | B | `.Release.Name` change, `.Chart.Name` non |
| 4 | D | `helm template` = rendu sec |
| 5 | C | `_helpers.tpl` ne crée aucun objet |
| 6 | B | `version` = Chart ; `appVersion` = appli |
| 7 | B | `apps/` est figé |
| 8 | B | `casses/` hors de `templates/` volontairement |
| 9 | C | Conteneur portail = port 5000 |
| 10 | D | api = ClusterIP |
| 11 | B | Deux images, trois environnements |
| 12 | B | Couleur et message viennent des env vars Helm |
| 13 | B | `-f` surcharge `values.yaml` |
| 14 | B | Ne recopier que ce qui diffère |
| 15 | C | `hedge-dev-portail` |
| 16 | A | Selector = name + instance + component |
| 17 | B | `BACKEND_URL` doit inclure le nom de release |
| 18 | B | `quote` = guillemets YAML |
| 19 | B | Ne jamais quotter un entier `replicas` |
| 20 | B | `nindent` sauve l'indentation |
| 21 | B | STAGING = 30131 |
| 22 | C | PROD = 3 + 3 |
| 23 | D | DEV = bleu `#2563eb` |
| 24 | B | Un namespace par environnement |
| 25 | B | `helm install ... -f values-dev.yaml -n hedge-dev` |
| 26 | C | 30132 = prod + backend ok |
| 27 | B | L'historique accumule les révisions |
| 28 | B | Rollback = nouvelle révision |
| 29 | C | `scale` hors Helm sera écrasé |
| 30 | B | `uninstall` ne tue pas le namespace |
| 31 | B | Delete pod = auto-réparation du Deployment |
| 32 | B | Nom en dur = collision entre releases |
| 33 | C | Selector immuable |
| 34 | B | Label variable OK sur le Pod, interdit dans `matchLabels` |
| 35 | B | Typo `portal` / `portail` |
| 36 | B | Un nouvel env = un fichier de valeurs |

**Score indicatif :** 30/36 ou plus = vous pouvez expliquer le projet à un camarade. En dessous de 24/36, relisez les sections « Concepts essentiels », « Mission 3 » et « Mission 6 » de [`00-ENONCE.md`](00-ENONCE.md).

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
