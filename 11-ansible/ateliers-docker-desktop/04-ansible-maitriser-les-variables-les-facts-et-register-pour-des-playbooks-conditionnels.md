# 04 — Utiliser les variables, facts, register et conditions avec Docker Desktop

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


## 1. Variable simple, liste et dictionnaire

Fichier fourni : [playbooks/04-variables.yml](laboratoire-docker-desktop/playbooks/04-variables.yml).

```yaml
---
- name: Manipuler une variable, une liste et un dictionnaire
  hosts: node1
  gather_facts: false
  vars:
    fav_color: bleu
    port_nums: [21, 22, 80, 443]
    users:
      bob:
        username: bob
        uid: 1001
        shell: /bin/bash
      alice:
        username: alice
        uid: 1002
        shell: /bin/zsh
  tasks:
    - name: Afficher la couleur
      ansible.builtin.debug:
        msg: "Ma couleur preferee est {{ fav_color }}."
    - name: Afficher le deuxieme port
      ansible.builtin.debug:
        msg: "Le deuxieme port est {{ port_nums[1] }}."
    - name: Afficher l'identifiant de Bob
      ansible.builtin.debug:
        msg: "L'UID de Bob est {{ users.bob.uid }}."
```

```powershell
docker compose exec controleur ansible-playbook playbooks/04-variables.yml
```

Résultats attendus : la couleur bleu, le deuxième port 22 et l’UID déclaré 1001. Les indices d’une liste commencent à zéro. Une variable décrit une valeur ; la présence de `shell: /bin/zsh` dans un dictionnaire n’installe pas ce shell et ne crée aucun compte.

## 2. Charger un fichier de variables externe

Fichier fourni : [playbooks/vars/myvars.yml](laboratoire-docker-desktop/playbooks/vars/myvars.yml).

```yaml
---
port_nums: [21, 22, 80, 443]
users:
  alice:
    username: alice
    uid: 1002
    shell: /bin/zsh
```

Fichier fourni : [playbooks/04-variables-externes.yml](laboratoire-docker-desktop/playbooks/04-variables-externes.yml).

```yaml
---
- name: Charger des variables externes
  hosts: node1
  gather_facts: false
  vars_files:
    - vars/myvars.yml
  tasks:
    - name: Afficher le premier port
      ansible.builtin.debug:
        msg: "Premier port : {{ port_nums[0] }}"
    - name: Afficher la valeur du shell
      ansible.builtin.debug:
        msg: "Shell declare : {{ users.alice.shell }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/04-variables-externes.yml
```

Résultats attendus : premier port 21 et valeur de shell `/bin/zsh`. Le chemin `vars/myvars.yml` est résolu relativement au playbook situé dans `playbooks`.

## 3. Examiner les facts des nœuds

Fichier fourni : [playbooks/04-facts.yml](laboratoire-docker-desktop/playbooks/04-facts.yml).

```yaml
---
- name: Observer les conteneurs Linux depuis Windows
  hosts: node_containers
  gather_facts: true
  tasks:
    - name: Afficher la distribution, le nom et l'IP interne
      ansible.builtin.debug:
        msg:
          - "Distribution : {{ ansible_facts['distribution'] }}"
          - "Famille : {{ ansible_facts['os_family'] }}"
          - "Nom : {{ ansible_facts['hostname'] }}"
          - "IP interne : {{ ansible_facts.get('default_ipv4', {}).get('address', 'non disponible') }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/04-facts.yml
```

Les facts décrivent les **conteneurs cibles**. Ils afficheront Ubuntu, Debian ou AlmaLinux alors que votre poste est Windows. Le nom configuré est node1 à node6. L’IP observée est interne au réseau Docker ; le navigateur Windows utilise toujours les ports `localhost`.

Le paquet `iproute2` ou `iproute` des images permet la collecte des informations réseau. La lecture de l’IP prévoit une valeur de repli si cette information n’est pas disponible. L’accès explicite par `ansible_facts` évite de dépendre de l’injection automatique des facts dans des variables globales.

## 4. Capturer stdout et rc avec register

Fichier fourni : [playbooks/04-register.yml](laboratoire-docker-desktop/playbooks/04-register.yml).

```yaml
---
- name: Capturer le resultat de uptime
  hosts: node1
  gather_facts: false
  tasks:
    - name: Lire uptime
      ansible.builtin.command: uptime
      register: server_uptime
      changed_when: false
    - name: Afficher stdout et rc
      ansible.builtin.debug:
        msg: "{{ server_uptime.stdout }} ; code retour={{ server_uptime.rc }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/04-register.yml
```

`register` stocke le résultat de la tâche ; `stdout` contient le texte et `rc` son code de retour. `changed_when: false` indique que lire uptime ne modifie pas le système. Dans Docker, l’uptime peut refléter le noyau partagé de la machine virtuelle ; il ne mesure pas directement le temps depuis la création de chaque conteneur.

## 5. Décider puis contrôler l’état final

Fichier fourni : [playbooks/04-conditions.yml](laboratoire-docker-desktop/playbooks/04-conditions.yml).

```yaml
---
- name: Installer Git si necessaire puis verifier son etat final
  hosts: node1
  tasks:
    - name: Collecter les paquets installes
      ansible.builtin.package_facts:
        manager: auto
    - name: Installer Git quand il est absent
      ansible.builtin.apt:
        name: git
        state: present
        update_cache: true
        cache_valid_time: 3600
      when: "'git' not in ansible_facts['packages']"
    - name: Lire la version apres installation
      ansible.builtin.command: git --version
      register: git_final
      changed_when: false
    - name: Afficher le resultat final
      ansible.builtin.debug:
        msg: "{{ git_final.stdout }}"
      when: git_final.rc == 0
```

```powershell
docker compose exec controleur ansible-playbook playbooks/04-conditions.yml
```

Le playbook collecte les paquets, installe Git si nécessaire, puis exécute `git --version` pour vérifier l’état **après** l’installation. Une variable enregistrée avant l’installation ne se met pas à jour toute seule. La version affichée doit donc provenir d’une nouvelle tâche.

Si le chapitre 03 a déjà installé Git sur node1, l’installation sera ignorée et la vérification finale sera tout de même exécutée.

## 6. Adapter les paquets à la famille du système

Fichier fourni : [playbooks/04-systemes.yml](laboratoire-docker-desktop/playbooks/04-systemes.yml).

```yaml
---
- name: Installer un outil selon la famille du conteneur
  hosts: node_containers
  tasks:
    - name: Installer procps sur Ubuntu et Debian
      ansible.builtin.apt:
        name: procps
        state: present
        update_cache: true
        cache_valid_time: 3600
      when: ansible_facts['os_family'] == 'Debian'
    - name: Installer procps-ng sur AlmaLinux
      ansible.builtin.dnf:
        name: procps-ng
        state: present
      when: ansible_facts['os_family'] == 'RedHat'
```

```powershell
docker compose exec controleur ansible-playbook playbooks/04-systemes.yml
docker compose exec controleur ansible all -m ansible.builtin.command -a "uptime"
```

L’exercice utilise `procps` et `procps-ng`, disponibles dans les dépôts des images. Ils sont déjà installés pour les autres exercices, ce qui permet aussi d’observer une exécution idempotente. Le paquet `htop` de l’ancienne version dépendait d’un dépôt supplémentaire sur AlmaLinux.

## 7. Vérifications de compréhension

1. Changer `fav_color`, enregistrer le YAML dans Windows et relancer uniquement le playbook des variables.
2. Changer le premier port du fichier externe, puis vérifier que son affichage change.
3. Comparer les facts de node2 et node3.
4. Rejouer le playbook de conditions et expliquer pourquoi la version de Git est affichée dans les deux cas.

Pour approfondir : [variables et register](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html), [conditions](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_conditionals.html).
