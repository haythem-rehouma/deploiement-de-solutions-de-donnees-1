# Chapitre 5 : Utilisation des Boucles dans Ansible

## Introduction

Dans ce chapitre, nous allons explorer l'utilisation des **boucles** dans Ansible pour automatiser des tâches répétitives de manière efficace. Les boucles vous permettent d'exécuter une action plusieurs fois sans avoir à répéter manuellement le code pour chaque élément. Cette fonctionnalité est particulièrement utile pour :

- **Créer ou gérer plusieurs utilisateurs**.
- **Déployer des configurations sur plusieurs serveurs ou fichiers**.
- **Automatiser des tâches sur des listes d'éléments**.

---

## Table des Matières

1. [Étape Préparatoire : Création du Dossier de Travail](#etape-preparatoire)
2. [Configurer l'Inventaire Ansible](#configurer-inventaire)
3. [Partie 1 : Boucler sur une Liste](#partie1)
4. [Partie 2 : Boucler sur une Liste de Dictionnaires](#partie2)
5. [Partie 3 : Boucler sur un Dictionnaire](#partie3)
6. [Partie 4 : Boucler sur une Plage de Nombres](#partie4)
7. [Partie 5 : Boucler sur les Hôtes de l'Inventaire](#partie5)
8. [Partie 6 : Utiliser une Pause dans une Boucle](#partie6)
9. [Conclusion](#conclusion)

---

<a name="etape-preparatoire"></a>
## Étape Préparatoire : Création du Dossier de Travail

1. **Créer un dossier pour le projet Ansible** :

   ```bash
   mkdir ansible_project_loops
   ```

   Ce dossier `ansible_project_loops` servira à stocker tous les fichiers et playbooks nécessaires pour cette pratique.

2. **Naviguer dans le dossier** :

   ```bash
   cd ansible_project_loops
   ```

---

<a name="configurer-inventaire"></a>
## Configurer l'Inventaire Ansible

1. **Créer un fichier `inventory.ini`** pour définir les nœuds :

   ```bash
   nano inventory.ini
   ```

2. **Ajouter les informations des nœuds** :

   ```ini
   [node_containers]
   node1 ansible_host=172.20.0.2 ansible_user=root ansible_python_interpreter=/usr/bin/python3
   node2 ansible_host=172.20.0.3 ansible_user=root ansible_python_interpreter=/usr/bin/python3
   node3 ansible_host=172.20.0.4 ansible_user=root ansible_python_interpreter=/usr/bin/python3
   node4 ansible_host=172.20.0.5 ansible_user=root ansible_python_interpreter=/usr/bin/python3
   node5 ansible_host=172.20.0.6 ansible_user=root ansible_python_interpreter=/usr/bin/python3
   node6 ansible_host=172.20.0.7 ansible_user=root ansible_python_interpreter=/usr/bin/python3
   ```

   **Remarque :** L'ajout de `ansible_python_interpreter=/usr/bin/python3` permet d'éviter les avertissements liés à la découverte automatique de l'interpréteur Python.

3. **Enregistrer et quitter l'éditeur**.

---

<a name="partie1"></a>
## Partie 1 : Boucler sur une Liste

### Étape 1 : Écrire un Playbook pour Afficher les Éléments d'une Liste

1. **Créer un fichier nommé `print-list.yml`** :

   ```bash
   nano print-list.yml
   ```

2. **Ajouter le contenu suivant** pour afficher une liste de nombres premiers :

   ```yaml
   ---
   - name: Afficher une Liste de Nombres Premiers
     hosts: node1
     become: yes
     vars:
       prime_numbers:
         - 2
         - 3
         - 5
         - 7
         - 11
     tasks:
       - name: Afficher les Nombres Premiers
         debug:
           msg: "Nombre premier : {{ item }}"
         loop: "{{ prime_numbers }}"
   ```

   **Explications** :

   - **`vars`** : Définit une variable `prime_numbers` qui est une liste de nombres premiers.
   - **`loop`** : Itère sur chaque élément de la liste `prime_numbers`.
   - **`{{ item }}`** : Représente l'élément courant de la boucle.

3. **Enregistrer et quitter l'éditeur**.

4. **Exécuter le playbook** :

   ```bash
   ansible-playbook -i inventory.ini print-list.yml
   ```

   **Résultat attendu :**

   Le playbook affichera chaque nombre premier de la liste.

---

<a name="partie2"></a>
## Partie 2 : Boucler sur une Liste de Dictionnaires

### Étape 1 : Ajouter Plusieurs Utilisateurs avec une Boucle

1. **Créer un fichier `add-users.yml`** pour ajouter plusieurs utilisateurs avec des mots de passe :

   ```bash
   nano add-users.yml
   ```

2. **Ajouter le contenu suivant** :

   ```yaml
   ---
   - name: Ajouter Plusieurs Utilisateurs
     hosts: database
     become: yes
     vars:
       db_users:
         - username: "alice"
           password: "password1"
           uid: 1001
         - username: "bob"
           password: "password2"
           uid: 1002
         - username: "charlie"
           password: "password3"
           uid: 1003
     tasks:
       - name: Créer les Utilisateurs
         user:
           name: "{{ item.username }}"
           uid: "{{ item.uid }}"
           password: "{{ item.password | password_hash('sha512') }}"
           shell: "/bin/bash"
           state: present
         loop: "{{ db_users }}"
   ```

   **Explications** :

   - **`db_users`** : Liste de dictionnaires, chaque dictionnaire contenant les informations d'un utilisateur.
   - **Module `user`** : Utilisé pour gérer les comptes utilisateurs sur les hôtes cibles.
   - **`password_hash('sha512')`** : Hash le mot de passe en utilisant l'algorithme SHA-512 pour la sécurité.
   - **`loop: "{{ db_users }}"`** : Itère sur chaque utilisateur dans la liste `db_users`.

3. **Enregistrer et quitter l'éditeur**.

4. **Exécuter le playbook** :

   ```bash
   ansible-playbook -i inventory.ini add-users.yml
   ```

5. **Vérification** :

   Utilisez la commande suivante pour confirmer que les utilisateurs ont été ajoutés :

   ```bash
   ansible database -m command -a "getent passwd alice bob charlie" -i inventory.ini
   ```

   **Remarque :** La commande `getent passwd` affiche les entrées des utilisateurs spécifiés.

---

<a name="partie3"></a>
## Partie 3 : Boucler sur un Dictionnaire

Ansible ne peut pas boucler directement sur un dictionnaire. Il faut le transformer en une liste de paires clé/valeur en utilisant le filtre `dict2items`.

### Étape 1 : Afficher les Paires Clé/Valeur d'un Dictionnaire

1. **Créer un fichier nommé `print-dictionary.yml`** :

   ```bash
   nano print-dictionary.yml
   ```

2. **Ajouter le contenu suivant** :

   ```yaml
   ---
   - name: Afficher les Informations d'un Employé
     hosts: node1
     become: yes
     vars:
       employee:
         name: "Alice"
         title: "Administratrice Système"
         company: "TechCorp"
     tasks:
       - name: Afficher le Dictionnaire Employé
         debug:
           msg: "{{ item.key }}: {{ item.value }}"
         loop: "{{ employee | dict2items }}"
   ```

   **Explications** :

   - **`employee`** : Un dictionnaire contenant des informations sur un employé.
   - **`dict2items`** : Convertit le dictionnaire en une liste de paires clé/valeur.
   - **`{{ item.key }}` et `{{ item.value }}`** : Représentent respectivement la clé et la valeur de chaque élément.

3. **Enregistrer et quitter l'éditeur**.

4. **Exécuter le playbook** :

   ```bash
   ansible-playbook -i inventory.ini print-dictionary.yml
   ```

   **Résultat attendu :**

   Le playbook affichera chaque attribut de l'employé, par exemple :

   ```
   name: Alice
   title: Administratrice Système
   company: TechCorp
   ```

---

<a name="partie4"></a>
## Partie 4 : Boucler sur une Plage de Nombres

### Étape 1 : Afficher une Plage de Nombres

1. **Créer un fichier `range-loop.yml`** :

   ```bash
   nano range-loop.yml
   ```

2. **Ajouter le contenu suivant** :

   ```yaml
   ---
   - name: Boucler sur une Plage de Nombres
     hosts: node1
     become: yes
     tasks:
       - name: Afficher les Nombres de 5 à 14
         debug:
           msg: "Nombre : {{ item }}"
         loop: "{{ range(5, 15) | list }}"
   ```

   **Explications** :

   - **`range(5, 15)`** : Génère un itérable de nombres de 5 à 14 (15 est exclu).
   - **`| list`** : Convertit l'itérable en une liste.

3. **Enregistrer et quitter l'éditeur**.

4. **Exécuter le playbook** :

   ```bash
   ansible-playbook -i inventory.ini range-loop.yml
   ```

   **Résultat attendu :**

   Le playbook affichera les nombres de 5 à 14.

---

<a name="partie5"></a>
## Partie 5 : Boucler sur les Hôtes de l'Inventaire

### Étape 1 : Exécuter une Tâche sur Tous les Nœuds de l'Inventaire

1. **Créer un fichier `loop-inventory.yml`** :

   ```bash
   nano loop-inventory.yml
   ```

2. **Ajouter le contenu suivant** :

   ```yaml
   ---
   - name: Boucler sur les Hôtes de l'Inventaire
     hosts: node1
     become: yes
     tasks:
       - name: Vérifier la Connectivité avec Tous les Hôtes
         ping:
           data: "Ping depuis node1"
         delegate_to: "{{ item }}"
         loop: "{{ groups['all'] }}"
   ```

   **Explications** :

   - **`groups['all']`** : Contient tous les hôtes définis dans l'inventaire.
   - **`delegate_to: "{{ item }}"`** : Exécute la tâche sur l'hôte spécifié par `item` au lieu du nœud cible (`node1`).
   - **Module `ping`** : Vérifie la connectivité Ansible entre les hôtes.

3. **Enregistrer et quitter l'éditeur**.

4. **Exécuter le playbook** :

   ```bash
   ansible-playbook -i inventory.ini loop-inventory.yml
   ```

   **Résultat attendu :**

   Le playbook testera la connectivité avec chaque hôte de l'inventaire depuis `node1`.

---

<a name="partie6"></a>
## Partie 6 : Utiliser une Pause dans une Boucle

### Étape 1 : Créer un Compte à Rebours avec une Pause

1. **Créer un fichier `countdown.yml`** :

   ```bash
   nano countdown.yml
   ```

2. **Ajouter le contenu suivant** :

   ```yaml
   ---
   - name: Compte à Rebours de 10 Secondes
     hosts: node1
     become: yes
     tasks:
       - name: Afficher le Compte à Rebours
         debug:
           msg: "{{ item }} secondes restantes..."
         loop: "{{ range(10, 0, -1) | list }}"
         loop_control:
           delay: 1
       - name: Afficher le Message Final
         debug:
           msg: "C'est l'heure !"
   ```

   **Explications** :

   - **`range(10, 0, -1)`** : Génère une liste de nombres de 10 à 1 en décrémentant de 1.
   - **`loop_control: delay: 1`** : Insère une pause de 1 seconde entre chaque itération de la boucle.
   - **`{{ item }}`** : Représente le nombre de secondes restantes.

3. **Enregistrer et quitter l'éditeur**.

4. **Exécuter le playbook** :

   ```bash
   ansible-playbook -i inventory.ini countdown.yml
   ```

   **Résultat attendu :**

   Le playbook affichera un compte à rebours de 10 à 1 avec une pause d'une seconde entre chaque nombre, puis affichera "C'est l'heure !".

---

<a name="conclusion"></a>
## Conclusion

Dans ce chapitre, vous avez appris à :

- **Utiliser les boucles simples avec `loop`** pour itérer sur des listes.
- **Boucler sur des listes de dictionnaires** pour effectuer des tâches complexes comme la création d'utilisateurs.
- **Transformer et boucler sur des dictionnaires** en utilisant le filtre `dict2items`.
- **Utiliser des plages de nombres** avec `range()` pour générer des séquences numériques.
- **Boucler sur les hôtes de l'inventaire** pour effectuer des actions sur plusieurs nœuds.
- **Introduire des pauses dans les boucles** avec `loop_control` pour contrôler le timing des tâches.

Ces techniques vous permettent de rendre vos playbooks plus dynamiques et efficaces, en automatisant des tâches répétitives sans répéter le code.

---

## Conseils Supplémentaires

- **Filtres Jinja2** : Explorez d'autres filtres comme `items2dict`, `map`, et `select` pour manipuler vos données.
- **Boucles avec `with_items`** : Bien que `loop` soit recommandé, vous pouvez rencontrer `with_items` dans des playbooks plus anciens.
- **Contrôle des Boucles** : Utilisez `loop_control` pour accéder à des variables spéciales comme `index`, `index0`, `first`, `last`.
- **Gestion des Échecs dans les Boucles** : Pour continuer l'exécution en cas d'erreur sur un élément, utilisez `ignore_errors` ou `failed_when`.

---

## Ressources Utiles

- [Documentation Ansible - Looping Over Items](https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html)
- [Ansible Loop Control](https://docs.ansible.com/ansible/latest/user_guide/playbooks_loops.html#loop-control)
- [Jinja2 Template Designer Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)

---

## Félicitations !

Vous avez amélioré vos compétences en Ansible en apprenant à utiliser les boucles pour automatiser des tâches répétitives. Continuez à explorer ces fonctionnalités pour rendre vos playbooks encore plus puissants et efficaces.

