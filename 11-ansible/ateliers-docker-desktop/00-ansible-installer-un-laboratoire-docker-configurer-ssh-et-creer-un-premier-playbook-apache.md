# 00 — Préparer Ansible avec Docker Desktop et PowerShell sous Windows

## Objectif

Créer un laboratoire réutilisable pour tous les chapitres, tester six connexions Ansible, puis installer Apache sur deux nœuds. Le dossier [laboratoire-docker-desktop](laboratoire-docker-desktop/) contient déjà les configurations et les playbooks : vous pouvez les lire, les modifier et les exécuter directement.

## 1. Préparer Windows

1. Installer ou ouvrir [Docker Desktop pour Windows](https://docs.docker.com/desktop/setup/install/windows-install/).
2. Utiliser le mode **Linux containers**. Lorsque le menu Docker propose « Switch to Windows containers », vous êtes déjà dans le bon mode.
3. Si le moteur choisi est WSL 2, activer la fonctionnalité demandée par Docker Desktop et terminer les redémarrages éventuels. Une distribution Ubuntu personnelle n’est pas nécessaire pour ces exercices.
4. Ouvrir **PowerShell**, puis se placer dans le laboratoire.

```powershell
git clone https://github.com/haythem-rehouma/laboratoire-docker-desktop.git
cd laboratoire-docker-desktop
docker version
docker compose version
docker info --format '{{.OSType}}'
```

Résultat attendu : une partie Client et une partie Server dans la version Docker, Compose disponible, et `linux` pour le type de moteur. L’accès Internet sert à télécharger les images et les paquets. [Prérequis Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [fonctionnement avec WSL 2](https://docs.docker.com/desktop/features/wsl/).

## 2. Comprendre les fichiers fournis

| Fichier ou dossier | Utilité |
|---|---|
| `compose.yaml` | Démarre le contrôleur, les six nœuds et les volumes de clés |
| `docker/controleur.Dockerfile` | Installe Python, Ansible et la collection d’archivage dans le contrôleur |
| `docker/debian.Dockerfile`, `docker/alma.Dockerfile` | Préparent SSH et Python pour les nœuds |
| `docker/controleur.sh` | Génère la clé du laboratoire dans un volume Docker |
| `docker/noeud.sh` | Autorise la clé publique et démarre SSH dans chaque nœud |
| `ansible.cfg` | Définit l’inventaire, la clé, les rôles et les options SSH |
| `inventory.ini` | Répertorie les six nœuds et leurs groupes |
| `playbooks/`, `roles/` | Contiennent les exercices prêts à exécuter |

Le contrôleur utilise Python 3.12 et la branche Ansible Core 2.20. Les nœuds incluent leur Python système. La [matrice Ansible](https://docs.ansible.com/projects/ansible/latest/reference_appendices/release_and_maintenance.html) permet de vérifier la compatibilité lors d’une évolution des versions. Les versions précises installées se consultent avec les commandes ci-dessous.

## 3. Construire et démarrer le laboratoire

```powershell
docker compose config --quiet
docker compose up -d --build --wait
docker compose ps
docker compose exec controleur ansible --version
docker compose exec controleur ansible-galaxy collection list community.general
```

Attendre que les sept services soient actifs. Le contrôleur crée sa clé avant le démarrage des nœuds ; les contrôles de santé attendent ensuite le service SSH.

Le dossier Windows est monté dans le contrôleur sous `/workspace`. `ANSIBLE_CONFIG` pointe explicitement vers `/workspace/ansible.cfg`, y compris lorsque le dossier partagé est présenté avec des permissions très larges. La clé privée reste dans le volume Linux `cle_privee`, où ses permissions sont adaptées à SSH. Les nœuds reçoivent uniquement la clé publique.

## 4. Lire la configuration Compose

Fichier fourni : [compose.yaml](laboratoire-docker-desktop/compose.yaml).

```yaml
name: ansible-desktop
services:
  controleur:
    build:
      context: .
      dockerfile: docker/controleur.Dockerfile
    volumes:
      - .:/workspace
      - cle_privee:/keys
      - cle_publique:/public
      - hotes_connus:/root/.ssh
    healthcheck:
      test: ["CMD", "test", "-s", "/public/id_ed25519.pub"]
      interval: 2s
      timeout: 2s
      retries: 30

  node1:
    hostname: node1
    build:
      context: .
      dockerfile: docker/debian.Dockerfile
      args:
        BASE_IMAGE: ubuntu:24.04
    depends_on:
      controleur:
        condition: service_healthy
    volumes:
      - cle_publique:/public:ro
    ports:
      - "127.0.0.1:8081:80"
    healthcheck:
      test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/127.0.0.1/22'"]
      interval: 3s
      timeout: 2s
      retries: 30

  node2:
    hostname: node2
    build:
      context: .
      dockerfile: docker/debian.Dockerfile
      args:
        BASE_IMAGE: debian:12
    depends_on:
      controleur:
        condition: service_healthy
    volumes:
      - cle_publique:/public:ro
    ports:
      - "127.0.0.1:8082:80"
    healthcheck:
      test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/127.0.0.1/22'"]
      interval: 3s
      timeout: 2s
      retries: 30

  node3:
    hostname: node3
    build:
      context: .
      dockerfile: docker/alma.Dockerfile
    depends_on:
      controleur:
        condition: service_healthy
    volumes:
      - cle_publique:/public:ro
    ports:
      - "127.0.0.1:8083:80"
    healthcheck:
      test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/127.0.0.1/22'"]
      interval: 3s
      timeout: 2s
      retries: 30

  node4:
    hostname: node4
    build:
      context: .
      dockerfile: docker/alma.Dockerfile
    depends_on:
      controleur:
        condition: service_healthy
    volumes:
      - cle_publique:/public:ro
    ports:
      - "127.0.0.1:8084:80"
    healthcheck:
      test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/127.0.0.1/22'"]
      interval: 3s
      timeout: 2s
      retries: 30

  node5:
    hostname: node5
    build:
      context: .
      dockerfile: docker/debian.Dockerfile
      args:
        BASE_IMAGE: ubuntu:24.04
    depends_on:
      controleur:
        condition: service_healthy
    volumes:
      - cle_publique:/public:ro
    ports:
      - "127.0.0.1:8085:80"
    healthcheck:
      test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/127.0.0.1/22'"]
      interval: 3s
      timeout: 2s
      retries: 30

  node6:
    hostname: node6
    build:
      context: .
      dockerfile: docker/debian.Dockerfile
      args:
        BASE_IMAGE: ubuntu:24.04
    depends_on:
      controleur:
        condition: service_healthy
    volumes:
      - cle_publique:/public:ro
    ports:
      - "127.0.0.1:8086:80"
    healthcheck:
      test: ["CMD-SHELL", "bash -c 'exec 3<>/dev/tcp/127.0.0.1/22'"]
      interval: 3s
      timeout: 2s
      retries: 30

volumes:
  cle_privee:
  cle_publique:
  hotes_connus:
```

Tous les services utilisent le réseau commun créé par Compose. Ansible joint `node1` à `node6` grâce à leurs noms. Les ports 8081 à 8086 publient HTTP vers Windows ; le port SSH reste interne au réseau du laboratoire. La publication est limitée à `127.0.0.1`.

Une déclaration `expose` ne fournit pas à elle seule une adresse web Windows. Ici, `ports` établit la correspondance entre un port Windows et le port 80 du conteneur. Sources : [réseau Compose](https://docs.docker.com/compose/how-tos/networking/), [ports Docker Desktop](https://docs.docker.com/desktop/features/networking/).

## 5. Vérifier l’inventaire et SSH

Fichier fourni : [inventory.ini](laboratoire-docker-desktop/inventory.ini).

```ini
[node_containers]
node1
node2
node3
node4
node5
node6

[web]
node1
node5

[database]
node2
node3

[mail]
node4
node6

[ubuntu]
node1
node5
node6

[debian]
node2

[alma]
node3
node4

[all:vars]
ansible_user=root
ansible_python_interpreter=/usr/bin/python3
```

Dans ce réseau, `node1` sert aussi de nom de connexion ; aucun relevé d’adresse IP n’est nécessaire. Les fichiers `/usr/bin/python3`, `/keys/id_ed25519` et `/workspace` désignent des chemins **dans les conteneurs**.

```powershell
docker compose exec controleur ansible-inventory --graph
docker compose exec controleur ansible all -m ansible.builtin.ping
docker compose exec controleur ansible node1 -m ansible.builtin.command -a "hostname"
```

Le module Ansible `ping` doit retourner `pong` pour les six nœuds. Il vérifie l’exécution du module Python après connexion SSH ; il ne s’agit pas du ping réseau ICMP de Windows.

Le premier contact SSH accepte et mémorise la nouvelle clé d’hôte dans le volume dédié au contrôleur. Une clé d’hôte déjà connue qui change provoquera une erreur à examiner dans le [guide de dépannage](03-ansible-diagnostiquer-les-avertissements-python-et-les-erreurs-d-archivage-des-journaux.md).

## 6. Exécuter le premier playbook Apache

Fichier fourni : [playbooks/00-premier-apache.yml](laboratoire-docker-desktop/playbooks/00-premier-apache.yml).

```yaml
---
- name: Deployer Apache avec Docker Desktop
  hosts: node1,node2
  gather_facts: true
  roles:
    - apache
```

`hosts` sélectionne les nœuds. `gather_facts` collecte leurs caractéristiques. Le rôle `apache` regroupe les tâches d’installation, de création de page, de démarrage et de vérification. Ses tâches détaillées sont expliquées au [chapitre 01](01-ansible-deployer-et-configurer-apache-sur-des-conteneurs-docker-ubuntu-debian-et-almalinux.md).

```powershell
docker compose exec controleur ansible-playbook playbooks/00-premier-apache.yml
(Invoke-WebRequest -UseBasicParsing http://localhost:8081).Content
(Invoke-WebRequest -UseBasicParsing http://localhost:8082).Content
```

Ouvrir aussi [node1](http://localhost:8081) et [node2](http://localhost:8082) dans le navigateur. Chaque page indique le nom du nœud et sa distribution. Les ports des quatre autres nœuds répondront après leur installation Apache au chapitre 01.

Rejouer le playbook. Les tâches de configuration doivent rester stables lorsque leur état cible est déjà obtenu : c’est l’idempotence. Les vérifications qui lisent l’état du système ne déclarent pas de modification.

## 7. Savoir où saisir une commande

| Besoin | Commande à saisir dans PowerShell |
|---|---|
| Exécuter Ansible | `docker compose exec controleur ansible all -m ansible.builtin.ping` |
| Lire un fichier local | `Get-Content .\inventory.ini` |
| Modifier le premier exercice | `notepad .\playbooks\00-premier-apache.yml` |
| Lire un fichier d’un nœud | `docker compose exec node1 cat /var/www/html/index.html` |
| Tester une page web | `Invoke-WebRequest -UseBasicParsing http://localhost:8081` |

Les paquets sont installés **dans les conteneurs** par les Dockerfiles ou Ansible. Les commandes APT et DNF ne sont pas des commandes PowerShell pour installer Docker sur Windows.

## 8. Annexe : commandes ponctuelles et écriture de fichiers

Après le déploiement, observer un nœud depuis PowerShell :

```powershell
docker compose exec controleur ansible node1 -m ansible.builtin.command -a "date"
docker compose exec controleur ansible web --list-hosts
docker compose exec controleur ansible mail --list-hosts
docker compose exec controleur ansible-inventory --host node1
```

Pour comparer `tee` et `>>`, ouvrir explicitement un terminal **dans node1** :

```powershell
docker compose exec node1 bash
```

Puis saisir ces commandes Bash dans ce terminal de conteneur :

```bash
echo "Premiere ligne" > /tmp/comparaison.txt
echo "Ajout silencieux" >> /tmp/comparaison.txt
echo "Ajout affiche" | tee -a /tmp/comparaison.txt
cat /tmp/comparaison.txt
exit
```

`>>` ajoute sans afficher ; `tee -a` ajoute et affiche ; `tee` sans `-a` remplace le contenu. Les permissions requises dépendent du fichier cible. Le compte du nœud est ici root. Après `exit`, vous retrouvez PowerShell.

## 9. Arrêter et reprendre

```powershell
docker compose stop
docker compose start
```

Ces commandes conservent les mêmes conteneurs et leurs fichiers. Le script de démarrage relance Apache s’il a déjà été installé. Une suppression avec `docker compose down` exige de rejouer les exercices après recréation ; voir le README.
