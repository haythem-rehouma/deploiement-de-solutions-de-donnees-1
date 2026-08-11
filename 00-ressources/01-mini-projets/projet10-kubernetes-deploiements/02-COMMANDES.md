<a id="top"></a>

# Aide-mémoire des commandes — Kubernetes

> **Projet [projet10-kubernetes-deploiements](README.md)** · toutes les commandes pour démarrer, tester et manipuler le cluster.

## Table des matières

- [0. Activer Kubernetes (Docker Desktop)](#0-activer-kubernetes-docker-desktop)
- [1. Construire l'image](#1-construire-limage)
- [2. Déployer l'application](#2-deployer-lapplication)
- [3. Observer (pods, services, deployments)](#3-observer-pods-services-deployments)
- [4. Tester la répartition de charge](#4-tester-la-repartition-de-charge)
- [5. Manipuler un Pod (exec, logs, port-forward)](#5-manipuler-un-pod-exec-logs-port-forward)
- [6. Changer la configuration (ConfigMap / arrière-plan)](#6-changer-la-configuration-configmap--arriere-plan)
- [7. Scaling, rolling update, rollback](#7-scaling-rolling-update-rollback)
- [8. Auto-réparation](#8-auto-reparation)
- [9. Nettoyage](#9-nettoyage)
- [Annexe A — minikube / kind](#annexe-a--minikube--kind)
- [Annexe B — dépannage](#annexe-b--depannage)

---

## 0. Activer Kubernetes (Docker Desktop)

Docker Desktop **→ Settings (⚙️) → Kubernetes → ✅ Enable Kubernetes → Apply & Restart**.

```powershell
kubectl get nodes                 # doit afficher docker-desktop  Ready
kubectl config current-context    # doit afficher docker-desktop
kubectl version --short
```

> **Rien d'autre à installer** : `kubectl` est fourni avec Docker Desktop.

---

## 1. Construire l'image

Depuis le dossier du projet (`projet10-kubernetes-deploiements`) :

```powershell
docker build -t demo-k8s:1.0 ./app
```

> Avec **Docker Desktop**, l'image locale est **directement visible** par le cluster (même daemon Docker). C'est pourquoi le manifeste utilise `imagePullPolicy: IfNotPresent`.

---

## 2. Déployer l'application

```powershell
kubectl apply -f k8s/                 # applique configmap + deployment + service
```

Ou fichier par fichier :

```powershell
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Puis ouvrez le navigateur : **http://localhost:30080**

---

## 3. Observer (pods, services, deployments)

```powershell
kubectl get all                       # vue d'ensemble
kubectl get pods -o wide              # les Pods (IP, noeud, etat)
kubectl get deployment demo-web
kubectl get service demo-web
kubectl describe deployment demo-web  # details + evenements
kubectl describe pod <nom-du-pod>     # detail d'un Pod (probes, image, events)
kubectl get pods --watch             # suivre les changements en direct (Ctrl+C pour quitter)
```

---

## 4. Tester la répartition de charge

Rechargez `http://localhost:30080` plusieurs fois : le **nom du Pod** change.

En ligne de commande (PowerShell) :

```powershell
1..10 | ForEach-Object { (Invoke-WebRequest -Headers @{Accept="application/json"} http://localhost:30080).Content }
```

En bash :

```bash
for i in $(seq 1 10); do curl -s -H "Accept: application/json" http://localhost:30080; echo; done
```

---

## 5. Manipuler un Pod (exec, logs, port-forward)

```powershell
kubectl logs <nom-du-pod>                      # logs d'un Pod
kubectl logs -l app=demo-web --tail=20        # logs de TOUS les Pods du label
kubectl exec -it <nom-du-pod> -- sh           # ouvrir un shell dans le Pod
kubectl exec <nom-du-pod> -- env              # voir les variables d'environnement injectees
kubectl port-forward svc/demo-web 8080:80     # acceder au Service via http://localhost:8080
```

---

## 6. Changer la configuration (ConfigMap / arrière-plan)

1. Éditez `k8s/configmap.yaml` (ex. `BG_COLOR: "#7c3aed"`).
2. Réappliquez puis **relancez** les Pods pour recharger les variables :

```powershell
kubectl apply -f k8s/configmap.yaml
kubectl rollout restart deployment demo-web
kubectl rollout status deployment demo-web
```

3. Rechargez la page : le fond a changé.

> Voir la valeur active dans un Pod :
> ```powershell
> kubectl exec <nom-du-pod> -- env | Select-String BG_COLOR
> ```

---

## 7. Scaling, rolling update, rollback

```powershell
# Scaling manuel
kubectl scale deployment demo-web --replicas=5
kubectl get pods                              # 5 Pods maintenant
kubectl scale deployment demo-web --replicas=3

# Rolling update : changez APP_VERSION dans le ConfigMap puis
kubectl apply -f k8s/configmap.yaml
kubectl rollout restart deployment demo-web
kubectl rollout status deployment demo-web    # suit le deploiement progressif

# Historique et rollback
kubectl rollout history deployment demo-web
kubectl rollout undo deployment demo-web      # revient a la version precedente
```

---

## 8. Auto-réparation

```powershell
kubectl get pods
kubectl delete pod <nom-du-pod>               # on en supprime un a la main
kubectl get pods --watch                      # Kubernetes en recree un automatiquement
```

---

## 9. Nettoyage

```powershell
kubectl delete -f k8s/                        # supprime service + deployment + configmap
# ou individuellement :
kubectl delete service demo-web
kubectl delete deployment demo-web
kubectl delete configmap demo-config
```

---

## Annexe A — minikube / kind

Si vous n'utilisez **pas** le Kubernetes de Docker Desktop, l'image locale n'est pas visible par le cluster : il faut la **charger**.

**minikube :**
```powershell
minikube start
minikube image load demo-k8s:1.0             # rend l'image dispo dans le cluster
kubectl apply -f k8s/
minikube service demo-web --url              # obtient l'URL d'acces
```

**kind :**
```powershell
kind create cluster
kind load docker-image demo-k8s:1.0          # charge l'image dans le cluster
kubectl apply -f k8s/
kubectl port-forward svc/demo-web 8080:80    # http://localhost:8080
```

---

## Annexe B — dépannage

| Symptôme | Cause probable | Solution |
|---|---|---|
| `ErrImagePull` / `ImagePullBackOff` | Le cluster ne trouve pas l'image | Vérifier `imagePullPolicy: IfNotPresent` + image `demo-k8s:1.0` construite ; en minikube/kind, charger l'image (Annexe A) |
| Pod en `CrashLoopBackOff` | L'app plante au démarrage | `kubectl logs <pod>` pour lire l'erreur |
| Pod `Pending` | Ressources insuffisantes | `kubectl describe pod <pod>` (section Events) |
| `localhost:30080` inaccessible | Service non créé / mauvais port | `kubectl get svc` ; sinon `kubectl port-forward svc/demo-web 8080:80` |
| `kubectl` ne répond pas | Mauvais contexte | `kubectl config use-context docker-desktop` |
| Sonde qui échoue | `/health` non atteignable | Vérifier le port `5000` et la route `/health` |

```powershell
# Diagnostic rapide
kubectl get events --sort-by=.lastTimestamp
kubectl describe pod <nom-du-pod>
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
