<a id="top"></a>

# TP4 — Kubernetes

> **Travail pratique noté** · Pondération **5 %** · Remise : **dimanche 16 août 2026** (fin de journée, en ligne) · **Travail individuel**
>
> **Modules couverts :** [07 — Kubernetes : bases](../../07-kubernetes-bases/README.md), [08 — Kubernetes : avancé](../../08-kubernetes-avance/README.md)

---

## Objectifs

À la fin de ce TP, vous serez capable de :

- Déployer une application sur un cluster Kubernetes via des manifestes YAML.
- Exposer l'application avec un **Service** et la rendre accessible via un **Ingress**.
- Externaliser la configuration avec un **ConfigMap** et des données sensibles avec un **Secret**.
- Mettre à l'échelle et effectuer une mise à jour progressive (rolling update).

---

## Contexte

Vous déployez sur Kubernetes l'image conteneurisée du TP3 (ou une image fournie), sur un cluster local (**minikube** ou **kind**).

---

## Consignes (étapes)

1. **Déploiement de base**
   - Écrivez un manifeste **Deployment** (image, `replicas: 2`, `livenessProbe`/`readinessProbe`).
   - Appliquez-le (`kubectl apply -f`) et vérifiez les Pods (`kubectl get pods`).

2. **Service**
   - Exposez le Deployment avec un **Service** (ClusterIP + NodePort pour tester).

3. **Ingress**
   - Activez un Ingress Controller (ex. ingress-nginx) et créez une règle **Ingress** (host/path).

4. **Configuration & secrets**
   - Créez un **ConfigMap** (variable non sensible) consommé par l'app.
   - Créez un **Secret** (donnée sensible) injecté en variable d'environnement.

5. **Exploitation**
   - Mettez à l'échelle (`kubectl scale … --replicas=4`).
   - Effectuez une **mise à jour** d'image et observez le rolling update (`kubectl rollout status`), puis un **rollback** (`kubectl rollout undo`).

---

## Livrables attendus

| Livrable | Détail |
|---|---|
| **Manifestes YAML** | `deployment.yaml`, `service.yaml`, `ingress.yaml`, `configmap.yaml`, `secret.yaml` |
| **Captures** | `kubectl get pods,svc,ingress`, accès à l'app, rolling update |
| **Fichier `REPONSES.md`** | Commandes `kubectl` utilisées + explications + captures |

---

## Barème de correction (sur 5 %)

| Critère | Pondération |
|---|---|
| Deployment correct (replicas + probes) | 1 % |
| Service fonctionnel (app accessible) | 1 % |
| Ingress configuré (routage host/path) | 1 % |
| ConfigMap + Secret consommés par l'app | 1 % |
| Scaling + rolling update/rollback + `REPONSES.md` | 1 % |

---

## Conseils

> _Validez chaque manifeste avec `kubectl apply --dry-run=client -f` avant de l'appliquer. Ne mettez jamais un vrai mot de passe dans un ConfigMap : c'est exactement le rôle du Secret._

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
