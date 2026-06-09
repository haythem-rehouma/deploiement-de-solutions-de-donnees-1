<a id="top"></a>

# Quiz — Séance 13 — Ansible (inventaires, playbooks, rôles, idempotence)

> **Évaluation sommative** · Quiz de fin de séance 13 (1 septembre 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** inventaires, playbooks, rôles, handlers, idempotence

---

**Question 1 :** Dans un inventaire Ansible au format INI, quelle syntaxe permet de définir un groupe de machines nommé `webservers` ?

a) `group: webservers`

b) `[webservers]`

c) `<webservers>`

d) `webservers = {}`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Dans le format INI, un groupe se déclare entre crochets `[webservers]`, suivi de la liste des hôtes qui lui appartiennent.

</details>

---

**Question 2 :** Quelle commande exécute le playbook `site.yml` en utilisant l'inventaire `hosts.ini` ?

a) `ansible-playbook -i hosts.ini site.yml`

b) `ansible run site.yml --inventory hosts.ini`

c) `ansible site.yml -i hosts.ini`

d) `ansible-play site.yml hosts.ini`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : a)** — On lance un playbook avec `ansible-playbook`, l'option `-i` (ou `--inventory`) désignant le fichier d'inventaire, suivi du nom du playbook.

</details>

---

**Question 3 :** Qu'est-ce que l'idempotence dans le contexte d'Ansible ?

a) La capacité d'exécuter des tâches en parallèle sur plusieurs hôtes

b) Le chiffrement des variables sensibles avec Ansible Vault

c) Le fait qu'une même exécution répétée produit toujours le même état final sans changement supplémentaire

d) Le fait de relancer automatiquement une tâche en cas d'échec

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Un playbook idempotent peut être ré-exécuté autant de fois que nécessaire : si l'état désiré est déjà atteint, Ansible ne fait rien (statut `ok`) et ne signale `changed` que lorsqu'une modification réelle a lieu.

</details>

---

**Question 4 :** À quoi sert un `handler` dans un playbook Ansible ?

a) À gérer les erreurs avec un bloc `rescue`

b) À exécuter une action déclenchée par une tâche via `notify`, généralement en fin de play

c) À définir les variables globales du playbook

d) À se connecter en SSH aux machines distantes

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Un handler est une tâche spéciale qui ne s'exécute que si elle est notifiée par une autre tâche (mot-clé `notify`), et seulement si celle-ci a produit un changement. Typiquement : redémarrer un service après modification de sa configuration.

</details>

---

**Question 5 :** Dans la structure standard d'un rôle Ansible, quel répertoire contient les tâches principales chargées par défaut ?

a) `defaults/main.yml`

b) `handlers/main.yml`

c) `vars/main.yml`

d) `tasks/main.yml`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : d)** — Le fichier `tasks/main.yml` est le point d'entrée des tâches d'un rôle. Les autres répertoires (`defaults`, `vars`, `handlers`, `templates`, `files`) ont chacun leur rôle, mais ce sont les tâches qui constituent le cœur exécuté.

</details>

---

**Question 6 :** Pourquoi est-il recommandé d'utiliser le module `ansible.builtin.copy` ou `template` plutôt que le module `shell` avec `echo` pour créer un fichier de configuration ?

a) Parce que le module `shell` est plus lent à l'exécution

b) Parce que `copy`/`template` sont idempotents et ne modifient le fichier que si son contenu change

c) Parce que le module `shell` n'est pas disponible sur Linux

d) Parce que `copy`/`template` exécutent automatiquement les handlers

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Les modules dédiés comme `copy` et `template` sont idempotents : ils comparent l'état actuel à l'état voulu et ne signalent `changed` que si une modification est nécessaire. Le module `shell` exécute la commande à chaque run et rompt donc l'idempotence.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
