# 01 — Déployer Apache sur Ubuntu, Debian et AlmaLinux avec Docker Desktop

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


## 1. Objectif et architecture

Utiliser Ansible pour installer Apache sur les six nœuds du même laboratoire. Les nœuds 1, 5 et 6 utilisent Ubuntu 24.04, le nœud 2 Debian 12, les nœuds 3 et 4 AlmaLinux 9. Le contrôle reste lancé depuis PowerShell.

Les images de base fournissent SSH et Python. L’installation d’Apache constitue l’exercice Ansible, y compris sur AlmaLinux.

## 2. Lire le playbook principal

Fichier fourni : [playbooks/01-apache-multidistribution.yml](laboratoire-docker-desktop/playbooks/01-apache-multidistribution.yml).

```yaml
---
- name: Deployer Apache avec Docker Desktop
  hosts: node_containers
  gather_facts: true
  roles:
    - apache
```

Ce playbook applique le rôle `apache` au groupe `node_containers`. Un rôle est un dossier de tâches réutilisables ; Ansible trouve celui-ci grâce à `roles_path` dans `ansible.cfg`. Le même rôle sert au premier exercice et au groupe web du chapitre 02.

## 3. Lire les tâches du rôle

Fichier fourni : [roles/apache/tasks/main.yml](laboratoire-docker-desktop/roles/apache/tasks/main.yml).

```yaml
---
- name: Installer Apache sur Ubuntu et Debian
  ansible.builtin.apt:
    name: apache2
    state: present
    update_cache: true
    cache_valid_time: 3600
    policy_rc_d: 101
  when: ansible_facts['os_family'] == 'Debian'

- name: Installer Apache sur AlmaLinux
  ansible.builtin.dnf:
    name: httpd
    state: present
  when: ansible_facts['os_family'] == 'RedHat'

- name: Creer la page du noeud
  ansible.builtin.copy:
    content: "<h1>{{ inventory_hostname }} - {{ ansible_facts['distribution'] }} - Docker Desktop</h1>\n"
    dest: /var/www/html/index.html
    mode: '0644'

- name: Verifier si Apache tourne deja
  ansible.builtin.command:
    argv:
      - pgrep
      - -x
      - "{{ 'apache2' if ansible_facts['os_family'] == 'Debian' else 'httpd' }}"
  register: apache_process
  changed_when: false
  failed_when: apache_process.rc not in [0, 1]

- name: Preparer le repertoire de processus AlmaLinux
  ansible.builtin.file:
    path: /run/httpd
    state: directory
    mode: '0755'
  when: ansible_facts['os_family'] == 'RedHat'

- name: Demarrer Apache dans le conteneur
  ansible.builtin.command:
    argv:
      - "{{ 'apache2ctl' if ansible_facts['os_family'] == 'Debian' else 'httpd' }}"
      - -k
      - start
  when: apache_process.rc == 1
  changed_when: true

- name: Verifier la reponse HTTP dans le noeud
  ansible.builtin.uri:
    url: http://127.0.0.1/
    return_content: true
  register: apache_http
  until: apache_http.status == 200
  retries: 10
  delay: 1

- name: Verifier le contenu de la page
  ansible.builtin.assert:
    that: inventory_hostname in apache_http.content
```

### Installation selon la distribution

- Ubuntu et Debian : le module `ansible.builtin.apt` installe `apache2`.
- AlmaLinux : le module `ansible.builtin.dnf` installe `httpd`.
- Les conditions utilisent `ansible_facts['os_family']`, collecté sur chaque cible.
- Le fichier de page est placé dans `/var/www/html/index.html` sur chaque nœud.

### Démarrage dans un conteneur

Les conteneurs fournis exécutent SSH comme processus principal et ne démarrent pas systemd. Le rôle vérifie la présence du processus Apache puis lance `apache2ctl -k start` ou `httpd -k start` quand il est absent. `policy_rc_d: 101` évite un démarrage implicite pendant l’installation APT.

Cette organisation permet d’étudier l’administration SSH de plusieurs machines dans un laboratoire local. Le script de démarrage du nœud relance aussi Apache après un arrêt et une reprise du même conteneur.

## 4. Valider et exécuter

```powershell
docker compose exec controleur ansible-playbook playbooks/01-apache-multidistribution.yml --syntax-check
docker compose exec controleur ansible-playbook playbooks/01-apache-multidistribution.yml
```

Attendre un récapitulatif avec `failed=0` et `unreachable=0` pour chaque nœud. Une tâche peut être `skipped` si elle concerne une autre distribution.

## 5. Vérifier les six pages depuis Windows

```powershell
8081..8086 | ForEach-Object {
    $url = "http://localhost:$_"
    $page = Invoke-WebRequest -UseBasicParsing -Uri $url
    [PSCustomObject]@{ Adresse = $url; Code = $page.StatusCode; Contenu = $page.Content.Trim() }
}
```

| URL | Nœud attendu |
|---|---|
| [localhost:8081](http://localhost:8081) | node1 |
| [localhost:8082](http://localhost:8082) | node2 |
| [localhost:8083](http://localhost:8083) | node3 |
| [localhost:8084](http://localhost:8084) | node4 |
| [localhost:8085](http://localhost:8085) | node5 |
| [localhost:8086](http://localhost:8086) | node6 |

Ces adresses passent par les ports publiés par Docker Desktop. Entre conteneurs, la connexion utilise le nom du service et le port interne. [Réseau Docker Desktop](https://docs.docker.com/desktop/features/networking/).

## 6. Contrôler l’idempotence et la reprise

```powershell
docker compose exec controleur ansible-playbook playbooks/01-apache-multidistribution.yml
docker compose restart node3
docker compose ps node3
(Invoke-WebRequest -UseBasicParsing http://localhost:8083).Content
```

Attendre que node3 soit à nouveau sain avant le dernier contrôle. Au second passage du playbook, une installation déjà conforme doit rester inchangée. Une lecture HTTP ne modifie pas le nœud.

## 7. Diagnostic ciblé

```powershell
docker compose logs --tail 50 node3
docker compose exec node3 httpd -t
docker compose exec controleur ansible node3 -m ansible.builtin.command -a "pgrep -a httpd"
docker compose port node3 80
```

Si un port est occupé, changer uniquement le port Windows dans `compose.yaml`, appliquer avec `docker compose up -d --wait`, puis suivre le dépannage de recréation et rejouer le playbook pour les nœuds recréés.
