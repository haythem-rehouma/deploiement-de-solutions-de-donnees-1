# Déployer une Infrastructure Docker avec Ansible - pratique 02

Ce tutoriel vous guidera pas à pas dans la configuration d'une infrastructure Docker contenant plusieurs conteneurs de différentes distributions Linux (Ubuntu, Debian, AlmaLinux) et dans l'utilisation d'Ansible pour automatiser des tâches sur ces conteneurs. 

---

## Table des Matières

1. [Introduction](#introduction)
2. [Étape 1 : Installer Docker et Docker Compose](#etape1)
3. [Étape 2 : Créer et Démarrer les Conteneurs](#etape2)
4. [Étape 3 : Configurer l'Accès SSH pour Ansible](#etape3)
5. [Étape 4 : Créer l'Inventaire Ansible avec Groupes](#etape4)
6. [Étape 5 : Lister les Hôtes par Groupe](#etape5)
7. [Étape 6 : Tester la Connectivité et Exécuter des Commandes](#etape6)
8. [Étape 7 : Exécuter des Actions Spécifiques sur des Groupes](#etape7)
9. [Étape 8 : Écrire et Exécuter un Playbook Ansible](#etape8)
10. [Étape 9 : Vérifier le Déploiement](#etape9)
11. [Conclusion](#conclusion)

---

<a name="introduction"></a>
## Introduction

Nous allons déployer une infrastructure Docker avec plusieurs conteneurs de différentes distributions Linux, configurer l'accès SSH pour Ansible, organiser les conteneurs en groupes dans un inventaire Ansible, et automatiser des tâches sur ces conteneurs en tenant compte des spécificités de chaque distribution.

---

<a name="etape1"></a>
## Étape 1 : Installer Docker et Docker Compose

Sur votre machine de contrôle (Ubuntu Desktop), exécutez les commandes suivantes pour installer Docker et Docker Compose :

```bash
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release git
git clone https://github.com/hrhouma/install-docker.git
cd install-docker/
chmod +x install-docker.sh
sudo ./install-docker.sh
docker version
docker compose version
```

---

<a name="etape2"></a>
## Étape 2 : Créer et Démarrer les Conteneurs

### 2.1. Créer un Répertoire de Travail

Créez un nouveau répertoire pour votre projet et accédez-y :

```bash
mkdir ansible_project
cd ansible_project
```

### 2.2. Créer le Fichier `docker-compose.yml`

Créez le fichier `docker-compose.yml` :

```bash
nano docker-compose.yml
```

### 2.3. Contenu du Fichier `docker-compose.yml`

Copiez et collez le contenu suivant dans le fichier, en veillant à ce que la configuration pour les conteneurs AlmaLinux soit correcte :

```yaml
version: '3'

services:
  node1:
    image: ubuntu:latest
    container_name: node1
    networks:
      ansible_network:
        ipv4_address: 172.20.0.2
    command: /bin/bash -c "apt update && apt install -y openssh-server python3 && service ssh start && tail -f /dev/null"
    expose:
      - "22"
      - "80"

  node2:
    image: debian:latest
    container_name: node2
    networks:
      ansible_network:
        ipv4_address: 172.20.0.3
    command: /bin/bash -c "apt update && apt install -y openssh-server python3 && service ssh start && tail -f /dev/null"
    expose:
      - "22"
      - "80"

  node3:
    image: almalinux:latest
    container_name: node3
    networks:
      ansible_network:
        ipv4_address: 172.20.0.4
    command: /bin/bash -c "yum update -y && yum install -y openssh-server passwd python3 && echo 'root:root' | chpasswd && ssh-keygen -A && /usr/sbin/sshd -D"
    expose:
      - "22"
      - "80"

  node4:
    image: almalinux:latest
    container_name: node4
    networks:
      ansible_network:
        ipv4_address: 172.20.0.5
    command: /bin/bash -c "yum update -y && yum install -y openssh-server passwd python3 && echo 'root:root' | chpasswd && ssh-keygen -A && /usr/sbin/sshd -D"
    expose:
      - "22"
      - "80"

  node5:
    image: ubuntu:latest
    container_name: node5
    networks:
      ansible_network:
        ipv4_address: 172.20.0.6
    command: /bin/bash -c "apt update && apt install -y openssh-server python3 && service ssh start && tail -f /dev/null"
    expose:
      - "22"
      - "80"

  node6:
    image: ubuntu:latest
    container_name: node6
    networks:
      ansible_network:
        ipv4_address: 172.20.0.7
    command: /bin/bash -c "apt update && apt install -y openssh-server python3 && service ssh start && tail -f /dev/null"
    expose:
      - "22"
      - "80"

networks:
  ansible_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
```

**Remarques Importantes :**

- **Python3** est installé sur tous les conteneurs pour assurer la compatibilité avec Ansible.
- Les conteneurs AlmaLinux exécutent `sshd -D` pour garder le conteneur actif.
- Les ports `22` et `80` sont exposés pour SSH et HTTP.

### 2.4. Démarrer les Conteneurs

Exécutez la commande suivante pour démarrer tous les conteneurs en arrière-plan :

```bash
docker-compose up -d
```

Vérifiez que les conteneurs sont en cours d'exécution :

```bash
docker ps
```

---

<a name="etape3"></a>
## Étape 3 : Configurer l'Accès SSH pour Ansible

### 3.1. Générer une Clé SSH (si elle n'existe pas)

Générez une clé SSH sans phrase de passe :

```bash
ssh-keygen -t rsa -b 2048 -N "" -f ~/.ssh/id_rsa
```

### 3.2. Copier la Clé Publique vers Chaque Conteneur

Pour tous les conteneurs (`node1` à `node6`) :

```bash
for i in {1..6}; do
  docker exec -it node$i mkdir -p /root/.ssh
  docker cp ~/.ssh/id_rsa.pub node$i:/root/.ssh/authorized_keys
  docker exec -it node$i chmod 600 /root/.ssh/authorized_keys
done
```

### 3.3. Vérifier la Connexion SSH pour Chaque Conteneur

Supprimez les anciennes entrées d'hôtes connus pour éviter les conflits :

```bash
rm -f ~/.ssh/known_hosts
ssh-keygen -R 172.20.0.2
ssh-keygen -R 172.20.0.3
ssh-keygen -R 172.20.0.4
ssh-keygen -R 172.20.0.5
ssh-keygen -R 172.20.0.6
ssh-keygen -R 172.20.0.7

```

Ensuite, vérifiez la connexion SSH :

```bash
for i in {1..6}; do
  IP=172.20.0.$((i+1))
  ssh -o StrictHostKeyChecking=no root@$IP exit
done
```

---

<a name="etape4"></a>
## Étape 4 : Créer l'Inventaire Ansible avec Groupes

Créez un fichier `inventory.ini` dans votre répertoire de travail :

```bash
nano inventory.ini
```

Ajoutez le contenu suivant :

```ini
[node_containers]
node1 ansible_host=172.20.0.2 ansible_user=root
node2 ansible_host=172.20.0.3 ansible_user=root
node3 ansible_host=172.20.0.4 ansible_user=root
node4 ansible_host=172.20.0.5 ansible_user=root
node5 ansible_host=172.20.0.6 ansible_user=root
node6 ansible_host=172.20.0.7 ansible_user=root

[web]
node1
node5

[database]
node2
node3

[mail]
node4
node6
```

---

<a name="etape5"></a>
## Étape 5 : Lister les Hôtes par Groupe

### 5.1. Lister les Hôtes du Groupe `web`

```bash
ansible web -i inventory.ini --list-hosts
```

### 5.2. Lister les Hôtes du Groupe `mail`

```bash
ansible mail -i inventory.ini --list-hosts
```

### 5.3. Lister Tous les Hôtes Définis

```bash
ansible all -i inventory.ini --list-hosts
```

### 5.4. Lister les Détails d'un Hôte Spécifique (`node1`)

```bash
ansible node1 -i inventory.ini --list-hosts
```

---

<a name="etape6"></a>
## Étape 6 : Tester la Connectivité et Exécuter des Commandes

### 6.1. Tester la Connectivité avec `ping` pour Tous les Conteneurs

```bash
ansible all -m ping -i inventory.ini
```

### 6.2. Afficher la Date Actuelle sur `node1`

```bash
ansible node1 -m command -a "date" -i inventory.ini
```

### 6.3. Afficher la Date Actuelle sur Tous les Conteneurs

```bash
ansible all -m command -a "date" -i inventory.ini
```

---

<a name="etape7"></a>
## Étape 7 : Exécuter des Actions Spécifiques sur des Groupes

### 7.1. Redémarrer le Service Apache sur le Groupe `web`

Nous devons tenir compte des différences entre les distributions :

- Sur **Ubuntu/Debian**, le service Apache s'appelle `apache2`.
- Sur **AlmaLinux**, le service s'appelle `httpd`.

Cependant, dans le groupe `web`, nous avons `node1` et `node5`, qui sont tous deux des conteneurs Ubuntu. Nous utiliserons donc `apache2`.



**Installer Apache sur le Groupe `web` :**

```bash
ansible web -m apt -a "name=apache2 state=present" -i inventory.ini
```

**Démarrer et Activer le Service Apache :**

```bash
ansible web -m service -a "name=apache2 state=started enabled=yes" -i inventory.ini
```

**Redémarrer le Service Apache sur le Groupe `web`**

```bash
ansible web -m service -a "name=apache2 state=restarted" -i inventory.ini
```

**Note :** Si vous aviez des conteneurs AlmaLinux dans le groupe `web`, vous devriez utiliser des conditions ou séparer les tâches.

### 7.2. Vérifier l'Uptime sur le Groupe `mail`

Le conteneur `node4` (AlmaLinux) semble ne pas avoir la commande `uptime` installée par défaut. Nous allons installer `procps` qui fournit `uptime`.

#### 7.2.1. Installer `procps` sur les Conteneurs AlmaLinux

```bash
ansible mail -m yum -a "name=procps-ng state=present" -i inventory.ini
```

#### 7.2.2. Vérifier l'Uptime

```bash
ansible mail -m command -a "uptime" -i inventory.ini
ansible node4 -m command -a "uptime" -i inventory.ini
ansible node6 -m command -a "uptime" -i inventory.ini
```

### 7.3. Vérifier l'Utilisation du Disque sur le Groupe `database`

La commande `df` devrait être disponible sur toutes les distributions.

```bash
ansible database -m command -a "df -h" -i inventory.ini
```

### 7.4. Installer `vim` sur le Groupe `database`

Nous avons des conteneurs Ubuntu/Debian et AlmaLinux dans le groupe `database`. Nous devons utiliser le gestionnaire de paquets approprié pour chaque distribution.

#### 7.4.1. Créer un Playbook pour Gérer les Différentes Distributions

Créez un fichier `install_vim.yml` :

```bash
nano install_vim.yml
```

Contenu :

```yaml
- name: Install vim on database servers
  hosts: database
  become: yes
  tasks:
    - name: Install vim on Debian-based systems
      apt:
        name: vim
        state: present
      when: ansible_facts['os_family'] == 'Debian'

    - name: Install vim on RedHat-based systems
      yum:
        name: vim-enhanced
        state: present
      when: ansible_facts['os_family'] == 'RedHat'
```

#### 7.4.2. Exécuter le Playbook

```bash
ansible-playbook -i inventory.ini install_vim.yml
```

---

<a name="etape8"></a>
## Étape 8 : Écrire et Exécuter un Playbook Ansible

### 8.1. Créer un Playbook pour Configurer Apache sur Tous les Serveurs Web

Créez un fichier `configure_apache.yml` :

```bash
nano configure_apache.yml
```

Contenu :

```yaml
- name: Configure Apache on Web Servers
  hosts: web
  become: yes
  tasks:
    - name: Install Apache on Debian-based systems
      apt:
        name: apache2
        state: present
      when: ansible_facts['os_family'] == 'Debian'

    - name: Start Apache on Debian-based systems
      service:
        name: apache2
        state: started
        enabled: true
      when: ansible_facts['os_family'] == 'Debian'

    - name: Install Apache on RedHat-based systems
      yum:
        name: httpd
        state: present
      when: ansible_facts['os_family'] == 'RedHat'

    - name: Start Apache on RedHat-based systems
      service:
        name: httpd
        state: started
        enabled: true
      when: ansible_facts['os_family'] == 'RedHat'

    - name: Create index.html
      copy:
        content: "<h1>Bienvenue sur votre serveur web!</h1>"
        dest: /var/www/html/index.html
```

### 8.2. Exécuter le Playbook

```bash
ansible-playbook -i inventory.ini configure_apache.yml
```

---

<a name="etape9"></a>
## Étape 9 : Vérifier le Déploiement

### 9.1. Obtenir les Adresses IP des Conteneurs

```bash
for i in {1..6}; do
  IP=172.20.0.$((i+1))
  echo "node$i IP: $IP"
done
```

### 9.2. Vérifier l'Accès aux Serveurs Web

Utilisez `curl` pour tester les serveurs web :

```bash
for i in 1 5; do
  IP=172.20.0.$((i+1))
  echo "Testing node$i at $IP:"
  curl http://$IP
  echo -e "\n------------------------\n"
done
```

Vous devriez voir le message :

```html
<h1>Bienvenue sur votre serveur web!</h1>
```

---

<a name="conclusion"></a>
## Conclusion

Nous avons réussi à :

- Installer Docker et Docker Compose.
- Créer et démarrer plusieurs conteneurs Docker de différentes distributions.
- Configurer l'accès SSH pour Ansible.
- Créer un inventaire Ansible avec des groupes.
- Exécuter des commandes spécifiques en tenant compte des différences entre les distributions.
- Écrire et exécuter des playbooks Ansible pour automatiser des tâches.

---

## Conseils Supplémentaires

- **Modules Ansible Appropriés :** Utilisez le module `apt` pour Debian/Ubuntu et `yum` pour RedHat/AlmaLinux.
- **Conditions dans les Playbooks :** Utilisez les conditions `when` pour exécuter des tâches spécifiques à une distribution.
- **Installer les Paquets Nécessaires :** Assurez-vous que les commandes que vous voulez utiliser sont disponibles (par exemple, installer `procps` pour la commande `uptime` sur AlmaLinux).
- **Gestion des Services :** Le nom du service Apache diffère selon la distribution (`apache2` vs `httpd`).


