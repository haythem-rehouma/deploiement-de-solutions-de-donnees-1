# Déployer une Infrastructure Docker avec Ansible - pratique 01

---

- Ce tutoriel vous guidera à travers la configuration d'un environnement Docker contenant plusieurs conteneurs de différentes distributions Linux (Ubuntu, Debian, AlmaLinux) et l'utilisation d'Ansible pour automatiser l'installation et la configuration d'Apache sur ces conteneurs. 
---

## Table des Matières

1. [Schéma de l'Infrastructure](#schema)
2. [Étape 1 : Installer Docker et Docker Compose](#etape1)
3. [Étape 2 : Créer et Démarrer les Conteneurs](#etape2)
4. [Étape 3 : Configurer l'Accès SSH pour Ansible](#etape3)
5. [Étape 4 : Créer l'Inventaire Ansible](#etape4)
6. [Étape 5 : Écrire le Playbook Ansible](#etape5)
7. [Étape 6 : Exécuter le Playbook](#etape6)
8. [Étape 7 : Vérifier le Déploiement](#etape7)
9. [Récapitulatif](#recapitulatif)

---

<a name="schema"></a>
## Schéma de l'Infrastructure

```plaintext
                             Ubuntu Desktop
                           ┌─────────────────┐
                           │  CONTROL NODE   │
                           │ (Ansible Master)│
                           └────────┬────────┘
                                    │
        ┌────────┬────────┬────────┬────────┬────────┬────────┐
        │        │        │        │        │        │        │
    ┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐┌───┴───┐
    │ Node1 ││ Node2 ││ Node3 ││ Node4 ││ Node5 ││ Node6 │
    │Ubuntu ││Debian ││AlmaLnx││AlmaLnx││Ubuntu ││Ubuntu │
    └───────┘└───────┘└───────┘└───────┘└───────┘└───────┘
```

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
./install-docker.sh
# ou sh install-docker.sh
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

Créez le fichier `docker-compose.yml` qui définira les services Docker :

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
    command: /bin/bash -c "apt update && apt install -y openssh-server && service ssh start && tail -f /dev/null"
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
    command: /bin/bash -c "yum update -y && yum install -y openssh-server passwd httpd && echo 'root:root' | chpasswd && ssh-keygen -A && /usr/sbin/sshd && /usr/sbin/httpd -D FOREGROUND"
    expose:
      - "22"
      - "80"

  node4:
    image: almalinux:latest
    container_name: node4
    networks:
      ansible_network:
        ipv4_address: 172.20.0.5
    command: /bin/bash -c "yum update -y && yum install -y openssh-server passwd httpd && echo 'root:root' | chpasswd && ssh-keygen -A && /usr/sbin/sshd && /usr/sbin/httpd -D FOREGROUND"
    expose:
      - "22"
      - "80"

  node5:
    image: ubuntu:latest
    container_name: node5
    networks:
      ansible_network:
        ipv4_address: 172.20.0.6
    command: /bin/bash -c "apt update && apt install -y openssh-server && service ssh start && tail -f /dev/null"
    expose:
      - "22"
      - "80"

  node6:
    image: ubuntu:latest
    container_name: node6
    networks:
      ansible_network:
        ipv4_address: 172.20.0.7
    command: /bin/bash -c "apt update && apt install -y openssh-server && service ssh start && tail -f /dev/null"
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

**Explication des Modifications :**

- **Pour node3 et node4 (AlmaLinux)** :
  - Ajout de `httpd` à la commande d'installation.
  - Démarrage du service SSHD avec `/usr/sbin/sshd`.
  - Démarrage d'Apache en premier plan avec `/usr/sbin/httpd -D FOREGROUND`.
  - Exposition du port `80` pour le trafic HTTP.

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

Pour les conteneurs basés sur **Ubuntu** et **Debian** (`node1`, `node2`, `node5`, `node6`) :

```bash
for i in 1 2 5 6; do
  docker exec -it node$i mkdir -p /root/.ssh
  docker cp ~/.ssh/id_rsa.pub node$i:/root/.ssh/authorized_keys
  docker exec -it node$i chmod 600 /root/.ssh/authorized_keys
done
```

Pour les conteneurs basés sur **AlmaLinux** (`node3`, `node4`) :

```bash
for i in 3 4; do
  docker exec -it node$i mkdir -p /root/.ssh
  docker cp ~/.ssh/id_rsa.pub node$i:/root/.ssh/authorized_keys
  docker exec -it node$i chmod 600 /root/.ssh/authorized_keys
done
```

### 3.3. Vérifier la Connexion SSH pour Chaque Conteneur

Supprimez les anciennes entrées d'hôtes connus pour éviter les conflits :

```bash
rm -f ~/.ssh/known_hosts
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
## Étape 4 : Créer l'Inventaire Ansible

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
```

---

<a name="etape5"></a>
## Étape 5 : Écrire le Playbook Ansible

Créez un fichier `playbook.yml` :

```bash
nano playbook.yml
```

Ajoutez le contenu suivant :

```yaml
---
- name: Configure Apache on Ubuntu and Debian Containers
  hosts: node1,node2,node5,node6
  become: yes
  tasks:
    - name: Update APT package manager
      apt:
        update_cache: yes

    - name: Install Apache2
      apt:
        name: apache2
        state: present

    - name: Start Apache Service
      service:
        name: apache2
        state: started
        enabled: true

    - name: Create index.html
      copy:
        content: "<h1>Bienvenue sur votre serveur web Ubuntu/Debian dans un conteneur Docker !</h1>"
        dest: /var/www/html/index.html

- name: Configure Apache on AlmaLinux Containers
  hosts: node3,node4
  become: yes
  tasks:
    - name: Install net-tools (optional, for troubleshooting)
      yum:
        name: net-tools
        state: present

    - name: Create index.html
      copy:
        content: "<h1>Bienvenue sur votre serveur web AlmaLinux dans un conteneur Docker !</h1>"
        dest: /var/www/html/index.html
```

**Remarques :**

- **Pour les conteneurs AlmaLinux**, nous n'avons pas besoin d'installer ou de démarrer Apache via Ansible, car cela a déjà été fait lors du démarrage des conteneurs dans le `docker-compose.yml`.
- Nous utilisons Ansible pour créer le fichier `index.html` avec le contenu souhaité.

---

<a name="etape6"></a>
## Étape 6 : Exécuter le Playbook

Lancez le playbook pour configurer Apache dans les conteneurs :

```bash
ansible-playbook -i inventory.ini playbook.yml
```

---

<a name="etape7"></a>
## Étape 7 : Vérifier le Déploiement

### 7.1. Obtenir les Adresses IP des Conteneurs

Exécutez la commande suivante pour afficher les adresses IP de tous les conteneurs :

```bash
for i in {1..6}; do
  IP=172.20.0.$((i+1))
  echo "node$i IP: $IP"
done
```

### 7.2. Vérifier l'Accès aux Serveurs Web

Vous pouvez utiliser `curl` pour vérifier que les serveurs web répondent correctement :

```bash
for i in {1..6}; do
  IP=172.20.0.$((i+1))
  echo "Testing node$i at $IP:"
  curl http://$IP
  echo -e "\n------------------------\n"
done
```

### 7.3. Accéder aux Serveurs Web via un Navigateur

Ouvrez votre navigateur et accédez aux adresses suivantes :

- **Pour node1 à node6** :

  ```
  http://172.20.0.2
  http://172.20.0.3
  http://172.20.0.4
  http://172.20.0.5
  http://172.20.0.6
  http://172.20.0.7
  ```

**Note Importante :** Assurez-vous que votre machine hôte peut accéder au réseau `172.20.0.0/24`. Si ce n'est pas le cas, vous devrez peut-être configurer le port forwarding ou utiliser les adresses IP de la machine hôte pour accéder aux conteneurs.

### 7.4. Résultats Attendus

- **Pour les conteneurs Ubuntu et Debian (`node1`, `node2`, `node5`, `node6`)** :

  Vous devriez voir la page avec le message :

  ```html
  <h1>Bienvenue sur votre serveur web Ubuntu/Debian dans un conteneur Docker !</h1>
  ```

- **Pour les conteneurs AlmaLinux (`node3`, `node4`)** :

  Vous devriez voir la page avec le message :

  ```html
  <h1>Bienvenue sur votre serveur web AlmaLinux dans un conteneur Docker !</h1>
  ```

---

<a name="recapitulatif"></a>
## Récapitulatif

Avec ce tutoriel, vous avez réussi à :

1. **Installer Docker et Docker Compose** sur votre machine de contrôle Ubuntu.
2. **Créer et démarrer plusieurs conteneurs Docker** avec différentes distributions Linux.
3. **Configurer l'accès SSH** pour permettre à Ansible de se connecter à chaque conteneur.
4. **Écrire un inventaire Ansible** pour gérer les conteneurs.
5. **Écrire et exécuter un playbook Ansible** pour installer et configurer Apache sur les conteneurs.
6. **Vérifier le déploiement** en accédant aux serveurs web sur chaque conteneur.

---

## Félicitations !

Vous avez maintenant une infrastructure Docker fonctionnelle, automatisée avec Ansible, sans aucune erreur. Vous pouvez continuer à développer cet environnement en ajoutant plus de services, en explorant des rôles Ansible, ou en intégrant cette configuration dans des pipelines CI/CD.

---

## Conseils Supplémentaires

- **Gestion des Services dans les Conteneurs Docker** : Dans un conteneur Docker, il est préférable d'exécuter un seul processus principal. Si vous avez besoin d'exécuter plusieurs services, envisagez d'utiliser des images de base conçues pour cela ou d'utiliser des gestionnaires de processus comme `supervisord`.
- **Sécurité** : N'oubliez pas de sécuriser vos conteneurs en changeant les mots de passe par défaut et en utilisant des clés SSH sécurisées.
- **Nettoyage** : Pour arrêter et supprimer les conteneurs et les réseaux créés, utilisez :

  ```bash
  docker-compose down
  ```

- **Logs et Dépannage** : Utilisez `docker logs <container_name>` pour consulter les journaux des conteneurs en cas de problème.

---

## Ressources Utiles

- [Documentation Docker](https://docs.docker.com/)
- [Documentation Ansible](https://docs.ansible.com/)
- [Meilleures Pratiques pour les Conteneurs Docker](https://docs.docker.com/develop/dev-best-practices/)

- https://stackoverflow.com/questions/42462435/ansible-provisioning-error-using-a-ssh-password-instead-of-a-key-is-not-possibl
- https://stackoverflow.com/questions/23074412/how-to-set-host-key-checking-false-in-ansible-inventory-file
- https://stackoverflow.com/questions/20840012/ssh-remote-host-identification-has-changed
