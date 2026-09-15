# 02 — Organiser l’inventaire et administrer les groupes depuis PowerShell

**Environnement : Windows, PowerShell et Docker Desktop en mode conteneurs Linux.**

Préparer d’abord le [laboratoire du chapitre 00](00-ansible-installer-un-laboratoire-docker-configurer-ssh-et-creer-un-premier-playbook-apache.md). Les commandes de ce chapitre se saisissent dans PowerShell, depuis le dossier qui contient `compose.yaml` :

```powershell
Set-Location "C:\Users\rehou\Downloads\Compressed\deploiement-de-solutions-de-donnees-main\deploiement-de-solutions-de-donnees-main\12-ansible-playbooks-roles\laboratoire-docker-desktop"
```

```powershell
docker compose ps
docker compose exec controleur ansible all -m ansible.builtin.ping
```

Les six nœuds doivent répondre `pong`. Les fichiers YAML fournis se modifient avec VS Code ou le Bloc-notes sous Windows. Le dossier est partagé avec le contrôleur sous `/workspace` ; une modification enregistrée est immédiatement visible par Ansible.


## 1. Lire l’inventaire partagé

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

Un même nœud appartient à plusieurs groupes : node1 est dans `node_containers`, `web` et `ubuntu`. Les groupes fonctionnels réunissent parfois plusieurs distributions : `mail` contient AlmaLinux et Ubuntu ; `database` contient Debian et AlmaLinux.

Les noms DNS du réseau Compose remplacent les adresses IP recopiées à la main. Le contrôleur et les cibles doivent appartenir au même projet réseau. [Résolution des noms Compose](https://docs.docker.com/compose/how-tos/networking/).

## 2. Lister les groupes et inspecter un hôte

```powershell
docker compose exec controleur ansible-inventory --graph
docker compose exec controleur ansible web --list-hosts
docker compose exec controleur ansible mail --list-hosts
docker compose exec controleur ansible database --list-hosts
docker compose exec controleur ansible all --list-hosts
docker compose exec controleur ansible-inventory --host node1
```

`--list-hosts` affiche la sélection des hôtes. `ansible-inventory --host node1` affiche les variables de cet hôte. Le contrôleur n’apparaît pas comme une cible de l’inventaire.

## 3. Exécuter des commandes ponctuelles

```powershell
docker compose exec controleur ansible all -m ansible.builtin.ping
docker compose exec controleur ansible node1 -m ansible.builtin.command -a "date"
docker compose exec controleur ansible all -m ansible.builtin.command -a "date"
docker compose exec controleur ansible mail -m ansible.builtin.command -a "uptime"
docker compose exec controleur ansible database -m ansible.builtin.command -a "df -h"
```

Le module `command` exécute le programme sur les cibles. Le texte placé après `-a` reste entre guillemets dans PowerShell. Il n’interprète pas les redirections ou les tubes d’un shell.

`uptime` est fourni par `procps` sur Debian/Ubuntu et `procps-ng` sur AlmaLinux, déjà préparés dans les images. Les conteneurs partagent le noyau de la machine virtuelle Docker : cet uptime n’est pas nécessairement leur durée de vie individuelle. Pour connaître leur démarrage, consulter Docker Desktop ou `docker compose ps`.

## 4. Configurer et redémarrer les serveurs web

```powershell
docker compose exec controleur ansible-playbook playbooks/02-apache-web.yml
docker compose exec controleur ansible web -m ansible.builtin.command -a "apache2ctl -k graceful"
```

Le groupe web contient ici node1 et node5, tous deux Ubuntu. `apache2ctl -k graceful` recharge Apache après son installation et son démarrage par le rôle. Cette commande n’est pas à envoyer au groupe `all` : AlmaLinux utilise `httpd`.

Vérifier depuis Windows :

```powershell
(Invoke-WebRequest -UseBasicParsing http://localhost:8081).Content
(Invoke-WebRequest -UseBasicParsing http://localhost:8085).Content
```

## 5. Installer Vim sur un groupe mixte

Fichier fourni : [playbooks/02-installer-vim.yml](laboratoire-docker-desktop/playbooks/02-installer-vim.yml).

```yaml
---
- name: Installer Vim sur le groupe database
  hosts: database
  tasks:
    - name: Installer Vim avec APT
      ansible.builtin.apt:
        name: vim
        state: present
        update_cache: true
        cache_valid_time: 3600
      when: ansible_facts['os_family'] == 'Debian'
    - name: Installer Vim avec DNF
      ansible.builtin.dnf:
        name: vim-enhanced
        state: present
      when: ansible_facts['os_family'] == 'RedHat'
```

```powershell
docker compose exec controleur ansible-playbook playbooks/02-installer-vim.yml
docker compose exec controleur ansible database -m ansible.builtin.command -a "vim --version"
```

Les conditions assurent que chaque gestionnaire de paquets traite uniquement les nœuds compatibles. Cette logique est nécessaire lorsqu’un groupe fonctionnel rassemble plusieurs familles de systèmes.

## 6. Cibler une distribution

```powershell
docker compose exec controleur ansible alma -m ansible.builtin.dnf -a "name=procps-ng state=present"
docker compose exec controleur ansible ubuntu -m ansible.builtin.apt -a "name=procps state=present update_cache=true"
```

Une commande DNF vise `alma`. Elle ne vise pas `mail`, qui contient aussi un nœud Ubuntu. Pour des tâches communes plus complexes, un playbook avec conditions est plus lisible.

## 7. À retenir

- Le nom d’un groupe exprime une sélection ; il ne garantit pas une distribution commune.
- Les groupes et variables sont conservés dans un seul inventaire utilisé par tous les chapitres.
- Les commandes sont saisies dans PowerShell et exécutées par le contrôleur Ansible.
- Les URL `localhost` concernent Windows ; les noms `node1` à `node6` concernent le réseau interne.
