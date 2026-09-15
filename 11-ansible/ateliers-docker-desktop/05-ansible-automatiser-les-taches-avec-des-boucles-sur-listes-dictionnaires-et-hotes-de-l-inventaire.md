# 05 — Automatiser les listes, dictionnaires, utilisateurs et hôtes avec des boucles

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


## 1. Parcourir une liste

Fichier fourni : [playbooks/05-liste.yml](laboratoire-docker-desktop/playbooks/05-liste.yml).

```yaml
---
- name: Parcourir une liste
  hosts: node1
  gather_facts: false
  vars:
    prime_numbers: [2, 3, 5, 7, 11]
  tasks:
    - name: Afficher chaque nombre premier
      ansible.builtin.debug:
        msg: "Nombre premier : {{ item }}"
      loop: "{{ prime_numbers }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/05-liste.yml
```

`loop` exécute la tâche pour chaque élément et `item` contient la valeur courante. Les nombres affichés sont 2, 3, 5, 7 et 11.

## 2. Créer des utilisateurs à partir d’une liste de dictionnaires

Fichier fourni : [playbooks/05-utilisateurs.yml](laboratoire-docker-desktop/playbooks/05-utilisateurs.yml).

```yaml
---
- name: Creer les comptes du laboratoire
  hosts: database
  gather_facts: false
  vars:
    db_users:
      - username: alice
        uid: 2001
      - username: bob
        uid: 2002
      - username: charlie
        uid: 2003
  tasks:
    - name: Creer chaque utilisateur avec connexion par mot de passe verrouillee
      ansible.builtin.user:
        name: "{{ item.username }}"
        uid: "{{ item.uid }}"
        shell: /bin/bash
        create_home: true
        password_lock: true
        state: present
      loop: "{{ db_users }}"
      loop_control:
        label: "{{ item.username }}"
```

```powershell
docker compose exec controleur ansible database --list-hosts
docker compose exec controleur ansible-playbook playbooks/05-utilisateurs.yml
docker compose exec controleur ansible database -m ansible.builtin.command -a "getent passwd alice bob charlie"
```

L’inventaire commun définit database avec node2 et node3. Les comptes sont créés dans ces deux conteneurs. Les UID 2001 à 2003 appartiennent à cet exercice ; ils ne décrivent pas des comptes Windows.

Les comptes ont leur authentification par mot de passe verrouillée : l’objectif porte sur la boucle et les attributs utilisateurs. Cela évite les mots de passe d’exemple en clair et les changements de hash à chaque passage. La clé root du laboratoire reste le moyen d’accès Ansible.

Le filtre `password_hash` peut être étudié séparément lorsque la gestion d’un secret est nécessaire ; `passlib` est disponible dans le contrôleur. Un hash calculé avec un sel aléatoire à chaque exécution provoquerait des changements répétés. Le playbook fourni n’en dépend pas.

Rejouer le playbook : les comptes déjà conformes doivent rester inchangés.

## 3. Convertir un dictionnaire avec dict2items

Fichier fourni : [playbooks/05-dictionnaire.yml](laboratoire-docker-desktop/playbooks/05-dictionnaire.yml).

```yaml
---
- name: Parcourir un dictionnaire
  hosts: node1
  gather_facts: false
  vars:
    employee:
      name: Alice
      title: Administratrice Systeme
      company: TechCorp
  tasks:
    - name: Afficher chaque paire
      ansible.builtin.debug:
        msg: "{{ item.key }}: {{ item.value }}"
      loop: "{{ employee | dict2items }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/05-dictionnaire.yml
```

`dict2items` produit une liste d’éléments possédant une clé `key` et une valeur `value`. Le résultat affiche name, title et company.

## 4. Parcourir une plage numérique

Fichier fourni : [playbooks/05-plage.yml](laboratoire-docker-desktop/playbooks/05-plage.yml).

```yaml
---
- name: Afficher les nombres de 5 a 14
  hosts: node1
  gather_facts: false
  tasks:
    - name: Afficher le nombre courant
      ansible.builtin.debug:
        msg: "Nombre : {{ item }}"
      loop: "{{ range(5, 15) | list }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/05-plage.yml
```

`range(5, 15)` inclut 5 et exclut 15 ; `list` transforme la plage en liste. Le résultat va de 5 à 14.

## 5. Déléguer une tâche aux hôtes de l’inventaire

Fichier fourni : [playbooks/05-inventaire.yml](laboratoire-docker-desktop/playbooks/05-inventaire.yml).

```yaml
---
- name: Verifier les six connexions depuis le controleur
  hosts: node1
  gather_facts: false
  tasks:
    - name: Deleguer le test au noeud courant
      ansible.builtin.ping:
      delegate_to: "{{ item }}"
      loop: "{{ groups['node_containers'] }}"
      loop_control:
        label: "{{ item }}"
```

```powershell
docker compose exec controleur ansible-playbook playbooks/05-inventaire.yml
```

L’ensemble de tâches a node1 comme hôte de départ, mais le contrôleur ouvre une connexion vers chaque cible donnée à `delegate_to`. **Les connexions partent du contrôleur Ansible**, et non de node1. Le module `ping` vérifie SSH et Python sur chaque cible ; ce n’est pas un test ICMP de node1 vers les autres nœuds. [Délégation Ansible](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_delegation.html).

Résultat attendu : six réponses `pong`. Aucun transfert de clé privée vers node1 n’est requis.

## 6. Introduire une pause entre les itérations

Fichier fourni : [playbooks/05-pause.yml](laboratoire-docker-desktop/playbooks/05-pause.yml).

```yaml
---
- name: Compter de 10 a 1 avec une pause entre les iterations
  hosts: node1
  gather_facts: false
  tasks:
    - name: Afficher la valeur courante
      ansible.builtin.debug:
        msg: "Valeur : {{ item }}"
      loop: "{{ range(10, 0, -1) | list }}"
      loop_control:
        pause: 1
    - name: Afficher la fin
      ansible.builtin.debug:
        msg: Termine
```

```powershell
docker compose exec controleur ansible-playbook playbooks/05-pause.yml
```

`loop_control.pause: 1` insère une pause d’une seconde **entre** les itérations. Il y a dix valeurs et neuf intervalles, auxquels s’ajoute le temps d’exécution : cet exemple ne constitue pas un chronomètre exact de dix secondes. Le mot-clé `delay` concerne notamment les répétitions avec `until`, pas la pause d’une boucle. [Contrôle des boucles](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_loops.html).

## 7. Approfondir

- `loop_control.label` rend la sortie plus lisible, comme avec le nom des utilisateurs.
- `loop_control.index_var` expose un indice nommé.
- `loop_control.extended: true` fournit les métadonnées `ansible_loop.index`, `ansible_loop.first` et `ansible_loop.last`.
- Pour traiter une erreur, examiner son code et définir une condition adaptée ; ignorer systématiquement les erreurs masque les échecs réels.

## 8. Vérification finale

Les six playbooks de ce chapitre doivent s’exécuter sans échec. Le groupe database doit contenir les trois comptes attendus sur ses deux nœuds. Les commandes se lancent toutes depuis PowerShell avec le préfixe `docker compose exec controleur`.
