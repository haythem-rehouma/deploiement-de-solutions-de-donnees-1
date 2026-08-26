# Projet 13 — Kubernetes & Helm : industrialiser un déploiement multi-environnement

> **Niveau :** intermédiaire → avancé · **Durée :** 4 à 6 h · **Outils :** Docker Desktop, Kubernetes, Helm 3 ou 4

---

## En une phrase

Vous prenez une application composée de **deux services Python** et vous la déployez **trois fois côte à côte** — en `DEV` (bleu), `STAGING` (orange), `PROD` (vert) — avec **un seul Chart Helm** et **trois fichiers de valeurs**. À la fin, vous avez trois dashboards colorés dans votre navigateur, vous savez faire un `helm upgrade` + `rollback`, et vous avez réparé trois templates truffés de bugs réels.

---

## Ce que vous allez apprendre

- Écrire un **Chart Helm** propre from scratch (Chart.yaml, values.yaml, templates, helpers).
- **Templater** des manifestes Kubernetes (`Deployment`, `Service`) avec des valeurs paramétrables.
- **Isoler la configuration par environnement** avec `values-<env>.yaml`.
- Déployer **plusieurs releases** du même chart dans des namespaces distincts.
- Faire un **`helm upgrade`** puis un **`helm rollback`** — et comprendre pourquoi c'est fondamentalement différent de `kubectl scale`.
- Reconnaître et corriger **3 bugs réels** vus en entreprise : collision de nom, selector immuable violé, path Values erroné.

---

## Démarrage rapide (5 étapes)

```powershell
# 1) Verifier l'environnement
kubectl config use-context docker-desktop
helm version --short           # v3.x ou v4.x

# 2) Construire les images (une seule fois)
docker build -t hedge-portail:1.0 .\apps\portail
docker build -t hedge-api:1.0     .\apps\api

# 3) Lire l'enonce
notepad .\00-ENONCE.md         # ou VS Code, ou cursor .

# 4) Ecrire votre chart dans chart/ ...

# 5) Deployer et valider
helm install hedge-dev .\chart -f .\chart\environments\values-dev.yaml -n hedge-dev --create-namespace
.\outils\valider.ps1
```

---

## Cartographie des documents

| Fichier | À qui | Rôle |
|---|---|---|
| **`00-ENONCE.md`** | **Étudiant** | Le sujet complet, avec annexes et concepts. **À lire en premier.** |
| **[`01-QUESTIONS.md`](01-QUESTIONS.md)** | **Étudiant** | 36 questions pour vérifier que Helm et ce projet sont compris. Corrigés repliables. |
| `apps/` | Étudiant (lecture seule) | Le code Python à ne pas toucher |
| `chart/` | Étudiant (à compléter) | Le Chart Helm en squelette |
| `chart/casses/` | Étudiant (à lire, copier, réparer) | Les 3 templates défectueux de la mission 6 |
| `outils/valider.ps1` | Étudiant | Score automatique à tout moment |
| `CORRECTION-PROF.md` | **Enseignant uniquement** | Solutions détaillées, barème, pièges, script démo |

---

<details>
<summary><strong>Correction résumée (à ne consulter qu'après avoir sérieusement essayé)</strong></summary>

### Chart.yaml (Mission 1)

```yaml
apiVersion: v2
name: hedge
description: Application multi-environnement (portail + api) pilotee par Helm
type: application
version: 0.1.0
appVersion: "1.0.0"
```

### Helpers (Mission 3)

- `hedge.fullname` : `printf "%s-%s" .root.Release.Name .composant`
- `hedge.labels` : les 7 labels standard (`app.kubernetes.io/*` + `helm.sh/chart` + `hedge/environment`)
- `hedge.selectorLabels` : **seulement 3 labels** — `name`, `instance`, `component`

### Les 3 environnements (Mission 4)

Chaque `values-<env>.yaml` ne redéfinit **que** ce qui différencie son environnement des autres :

| Env | `environment` | `portail.replicas` | `nodePort` | Couleur |
|---|---|---|---|---|
| dev | `dev` | 1 | 30130 | `#2563eb` |
| staging | `staging` | 2 | 30131 | `#ea580c` |
| prod | `prod` | 3 | 30132 | `#16a34a` |

### Les 3 pannes (Mission 6)

| Panne | Cause | Correctif en une ligne |
|---|---|---|
| 1 — ConfigMap | `metadata.name: hedge-config` en dur | Utiliser `{{ include "hedge.fullname" ... }}` |
| 2 — worker | `hedge/environment` dans `matchLabels` | Remplacer le bloc par `{{ include "hedge.selectorLabels" ... }}` |
| 3 — cache | `.Values.portal.replicas` (typo) | Corriger en `.Values.portail.replicas` |

**Détails complets, justifications, pénalités et scripts dans [`CORRECTION-PROF.md`](CORRECTION-PROF.md).**

</details>

---

## Prérequis d'environnement

- **Docker Desktop** avec **Kubernetes activé** (*Settings → Kubernetes → Enable Kubernetes*)
- **≥ 4 Go de RAM** alloués à Docker Desktop (le TP fait tourner ~12 Pods)
- **Helm 3 ou 4** installé (`winget install Helm.Helm` ou `choco install kubernetes-helm`)
- **Ports 30130, 30131, 30132** libres sur `localhost`

---

## Nettoyage après séance

```powershell
helm uninstall hedge-dev     -n hedge-dev
helm uninstall hedge-staging -n hedge-staging
helm uninstall hedge-prod    -n hedge-prod
kubectl delete namespace hedge-dev hedge-staging hedge-prod
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
