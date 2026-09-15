# 03 — Écrire des playbooks, importer des tâches et utiliser des tags

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


## 1. Créer un fichier sur les six nœuds

Fichier fourni : [playbooks/03-premier-fichier.yml](laboratoire-docker-desktop/playbooks/03-premier-fichier.yml).

```yaml
---
- name: Creer un fichier sur les six noeuds
  hosts: node_containers
  tasks:
    - name: Creer le fichier de configuration
      ansible.builtin.copy:
        dest: /tmp/foo.conf
        content: "Configuration du laboratoire Docker Desktop\n"
        owner: root
        mode: '0664'
```

```powershell
docker compose exec controleur ansible-playbook playbooks/03-premier-fichier.yml
docker compose exec controleur ansible all -m ansible.builtin.command -a "cat /tmp/foo.conf"
```

Le module `copy` fixe le contenu et les permissions du fichier. Une seconde exécution garde le fichier inchangé si le contenu correspond déjà. Le chemin `/tmp/foo.conf` est situé dans chaque conteneur cible.

## 2. Installer des outils et archiver les journaux

Fichier fourni : [playbooks/03-multitaches.yml](laboratoire-docker-desktop/playbooks/03-multitaches.yml).

```yaml
---
- name: Installer tmux et archiver les journaux
  hosts: node_containers
  tasks:
    - name: Rafraichir APT pour les paquets du laboratoire
      ansible.builtin.apt:
        update_cache: true
        cache_valid_time: 3600
      when: ansible_facts['os_family'] == 'Debian'
      tags: install_tmux
    - name: Installer tmux
      ansible.builtin.package:
        name: tmux
        state: present
      tags: install_tmux
    - name: Creer une archive des journaux
      community.general.archive:
        path: /var/log
        dest: /tmp/logs.tar.gz
        format: gz
        mode: '0644'
        exclusion_patterns:
          - /var/log/wtmp
          - /var/log/btmp
      tags: archive_logs

- name: Installer Git sur les noeuds Ubuntu
  hosts: ubuntu
  tasks:
    - name: Installer Git avec mise a jour du cache
      ansible.builtin.apt:
        name: git
        state: present
        update_cache: true
        cache_valid_time: 3600
      tags: install_git
```

Le premier ensemble de tâches cible les six nœuds. Le second cible uniquement `ubuntu`. Le module générique `package` convient à tmux parce que le nom du paquet est commun aux trois distributions.

Le module `community.general.archive` appartient à la collection installée **dans le contrôleur** par `requirements.yml`. Son code s’exécute sur le nœud avec Python. Pour exclure des éléments contenus dans un répertoire, le paramètre est `exclusion_patterns`. L’ancien paramètre `excludes` n’est pas valide pour ce module. [Référence du module archive](https://docs.ansible.com/projects/ansible/latest/collections/community/general/archive_module.html).

```powershell
docker compose exec controleur ansible-galaxy collection list community.general
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --syntax-check
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml
```

## 3. Vérifier le résultat

```powershell
docker compose exec controleur ansible all -m ansible.builtin.command -a "ls -lh /tmp/logs.tar.gz"
docker compose exec controleur ansible all -m ansible.builtin.command -a "tar -tzf /tmp/logs.tar.gz"
docker compose exec controleur ansible all -m ansible.builtin.command -a "tmux -V"
docker compose exec controleur ansible ubuntu -m ansible.builtin.command -a "git --version"
```

Les conteneurs peuvent contenir peu de journaux. Leur contenu évolue pendant le laboratoire ; une archive n’est donc pas nécessairement identique entre deux exécutions.

Pour récupérer une archive sur Windows, depuis le dossier du laboratoire :

```powershell
docker compose cp node1:/tmp/logs.tar.gz ./logs-node1.tar.gz
```

## 4. Réutiliser des tâches avec import_tasks

Fichier fourni : [playbooks/tasks/groupes.yml](laboratoire-docker-desktop/playbooks/tasks/groupes.yml).

```yaml
---
- name: Creer le groupe developpeurs
  ansible.builtin.group:
    name: developpeurs
    state: present
- name: Creer le groupe securite
  ansible.builtin.group:
    name: securite
    state: present
- name: Creer le groupe finance
  ansible.builtin.group:
    name: finance
    state: present
```

Ce fichier contient une liste de tâches, sans `hosts` ni enveloppe `tasks`. Il est importé par le playbook suivant :

Fichier fourni : [playbooks/03-importation.yml](laboratoire-docker-desktop/playbooks/03-importation.yml).

```yaml
---
- name: Reutiliser des taches de gestion des groupes
  hosts: node_containers
  tasks:
    - name: Importer les taches communes
      ansible.builtin.import_tasks: tasks/groupes.yml
```

```powershell
docker compose exec controleur ansible-playbook playbooks/03-importation.yml
docker compose exec controleur ansible all -m ansible.builtin.command -a "getent group developpeurs securite finance"
```

Le chemin d’importation est relatif au playbook qui le contient. Garder le dossier `playbooks/tasks` à sa place.

## 5. Choisir les tâches avec des tags

```powershell
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --list-tags
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --tags install_tmux
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --tags archive_logs
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --tags install_git
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --skip-tags install_tmux
```

Chaque sélection garde ses prérequis : la mise à jour APT de tmux porte le même tag et l’installation Git actualise son propre cache. Le tag `archive_logs` ne suppose pas que tmux ou Git a été installé.

## 6. Faire le lien avec les rôles

`import_tasks` assemble un fichier de tâches à un playbook. Un rôle organise un ensemble réutilisable dans un dossier conventionnel. Le rôle Apache du chapitre 01 utilise `roles/apache/tasks/main.yml` et peut être appelé par plusieurs playbooks.

Exercice : ajouter une quatrième tâche de groupe dans `playbooks/tasks/groupes.yml`, rejouer le playbook d’importation et vérifier ce nouveau groupe. Les modifications restent confinées aux conteneurs du laboratoire.

## 7. Dépannage

Si l’archive est absente, vérifier la réussite de la tâche, le tag sélectionné, la collection sur le contrôleur et le chemin sur la cible. Le [guide de diagnostic](03-ansible-diagnostiquer-les-avertissements-python-et-les-erreurs-d-archivage-des-journaux.md) fournit les commandes détaillées.
