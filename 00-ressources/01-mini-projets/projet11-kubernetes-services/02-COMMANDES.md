<a id="top"></a>

# Aide-mémoire des commandes — Services Kubernetes

> **Projet [projet11-kubernetes-services](README.md)** · toutes les commandes pour déployer, exposer et tester les Services.

## Table des matières

- [1. Construire l'image et déployer](#1-construire-limage-et-deployer)
- [2. Observer les Services](#2-observer-les-services)
- [3. ClusterIP : découverte de services (DNS)](#3-clusterip--decouverte-de-services-dns)
- [4. NodePort : accès externe](#4-nodeport--acces-externe)
- [5. LoadBalancer : IP externe](#5-loadbalancer--ip-externe)
- [6. Endpoints et sélecteurs](#6-endpoints-et-selecteurs)
- [7. Nettoyage](#7-nettoyage)
- [Annexe — dépannage](#annexe--depannage)

---

## 1. Construire l'image et déployer

Depuis le dossier du projet (`projet11-kubernetes-services`) :

```powershell
kubectl config use-context docker-desktop
docker build -t demo-k8s:1.0 ./app          # (si pas deja construite au projet 10)
kubectl apply -f k8s/                        # deployment + 3 services
kubectl get pods                             # 3 Pods Running
```

---

## 2. Observer les Services

```powershell
kubectl get svc                              # TYPE, CLUSTER-IP, EXTERNAL-IP, PORT(S)
kubectl get svc -o wide
kubectl describe svc demo-clusterip          # details + Endpoints
```

Lecture de `kubectl get svc` :

| Colonne | Signification |
|---|---|
| `TYPE` | ClusterIP / NodePort / LoadBalancer |
| `CLUSTER-IP` | IP interne (toujours présente) |
| `EXTERNAL-IP` | IP externe (LoadBalancer) ou `<none>` |
| `PORT(S)` | `port` du Service (et `:nodePort` pour NodePort) |

---

## 3. ClusterIP : découverte de services (DNS)

Un ClusterIP n'est **pas** joignable depuis l'hôte : on l'appelle **depuis un Pod**, par son **nom**.

```powershell
# Pod client jetable (--rm : supprime a la sortie)
kubectl run client --rm -it --image=curlimages/curl -- sh
```

Puis, dans le shell du Pod :

```sh
curl http://demo-clusterip           # appel PAR NOM (resolu par CoreDNS)
curl http://demo-clusterip           # relancez : le nom du Pod change
exit
```

Tester la **résolution DNS** :

```powershell
kubectl run dnstest --rm -it --image=busybox:1.36 -- sh
# dans le Pod :
nslookup demo-clusterip
wget -qO- http://demo-clusterip
```

---

## 4. NodePort : accès externe

```powershell
kubectl get svc demo-nodeport
# Ouvrir dans le navigateur :
start http://localhost:30082
# ou tester en ligne de commande :
curl http://localhost:30082
```

---

## 5. LoadBalancer : IP externe

```powershell
kubectl get svc demo-lb                      # EXTERNAL-IP doit passer a "localhost"
start http://localhost:8090
curl http://localhost:8090
```

> Si `EXTERNAL-IP` reste `<pending>`, patientez quelques secondes (Docker Desktop provisionne le LB). En cluster **kind**, le type LoadBalancer reste `<pending>` sans MetalLB : utilisez `kubectl port-forward` (voir annexe).

---

## 6. Endpoints et sélecteurs

```powershell
kubectl get endpoints demo-clusterip         # IP des Pods derriere le Service
kubectl get pods -o wide --show-labels       # labels des Pods
kubectl get pods --selector app=demo-back    # memes Pods que le selecteur du Service
```

Voir la répartition (10 requêtes via port-forward) :

```powershell
kubectl port-forward svc/demo-clusterip 8091:80
# dans un AUTRE terminal :
1..10 | ForEach-Object { (Invoke-WebRequest -Headers @{Accept="application/json"} http://localhost:8091).Content }
```

---

## 7. Nettoyage

```powershell
kubectl delete -f k8s/
# ou par objet :
kubectl delete svc demo-clusterip demo-nodeport demo-lb
kubectl delete deployment demo-back
```

---

## Annexe — dépannage

| Symptôme | Cause probable | Solution |
|---|---|---|
| `curl http://demo-clusterip` échoue | Pas depuis un Pod, ou service absent | Appeler **depuis un Pod** ; vérifier `kubectl get svc` |
| Endpoints **vides** | Le **sélecteur** ne correspond à aucun label de Pod | Aligner `selector` (Service) et `labels` (Pods) |
| `EXTERNAL-IP` en `<pending>` | Pas de load balancer (kind, cloud non configuré) | Docker Desktop : patienter ; sinon `kubectl port-forward` |
| `localhost:30082` inaccessible | NodePort non créé / port occupé | `kubectl get svc demo-nodeport` ; changer `nodePort` |
| `ImagePullBackOff` | Image `demo-k8s:1.0` absente du cluster | La construire ; en kind : `kind load docker-image demo-k8s:1.0` |

```powershell
# Solution universelle d'acces temporaire a n'importe quel Service :
kubectl port-forward svc/demo-clusterip 8091:80   # -> http://localhost:8091
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
