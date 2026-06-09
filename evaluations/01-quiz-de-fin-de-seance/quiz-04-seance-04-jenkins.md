<a id="top"></a>

# Quiz — Séance 4 — Installation et configuration de Jenkins

> **Évaluation sommative** · Quiz de fin de séance 4 (30 juin 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** installation de Jenkins, configuration, plugins, agents, premier job.

---

**Question 1 :** Quel type d'outil est Jenkins ?

a) Un éditeur de code source.

b) Un serveur d'automatisation open source pour l'intégration et la livraison continues (CI/CD).

c) Un système de gestion de bases de données relationnelles.

d) Un gestionnaire de paquets pour Linux.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Jenkins est un serveur d'automatisation open source largement utilisé pour orchestrer les pipelines d'intégration et de livraison continues.

</details>

---

**Question 2 :** Quel prérequis est indispensable pour exécuter Jenkins ?

a) Une base de données Oracle.

b) Un environnement d'exécution Java (JDK/JRE).

c) Une carte graphique dédiée.

d) Le langage Python 3 uniquement.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Jenkins est une application Java ; un JDK/JRE compatible doit être installé sur la machine hôte pour qu'il puisse démarrer.

</details>

---

**Question 3 :** Sur quel port HTTP Jenkins écoute-t-il par défaut après une installation standard ?

a) `80`

b) `443`

c) `8080`

d) `3306`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Par défaut, l'interface web de Jenkins est accessible sur le port `8080` (par exemple `http://localhost:8080`).

</details>

---

**Question 4 :** À quoi servent les *plugins* dans Jenkins ?

a) À supprimer définitivement les anciens builds.

b) À étendre les fonctionnalités de Jenkins (intégration Git, Maven, Docker, notifications, etc.).

c) À remplacer le système d'exploitation du serveur.

d) À chiffrer le code source des applications.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — L'écosystème de plugins est ce qui rend Jenkins extensible : on y ajoute le support de Git, Maven, Docker, les notifications et bien d'autres intégrations.

</details>

---

**Question 5 :** Dans l'architecture de Jenkins, quel est le rôle d'un *agent* (anciennement *slave*) ?

a) Stocker la configuration de sécurité du contrôleur.

b) Exécuter les tâches (builds) déléguées par le contrôleur (*controller*), afin de répartir la charge.

c) Servir uniquement d'interface graphique pour l'administrateur.

d) Remplacer les plugins manquants automatiquement.

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Le contrôleur orchestre, mais ce sont les agents qui exécutent réellement les builds. Cette séparation permet de distribuer la charge sur plusieurs machines ou environnements.

</details>

---

**Question 6 :** Vous souhaitez créer un *job* simple qui exécute une commande shell à chaque déclenchement. Quel type de projet choisir dans Jenkins pour ce premier job de base ?

a) *Pipeline multibranche*

b) *Dossier (Folder)*

c) *Projet free-style (Freestyle project)*

d) *Vue de tableau de bord*

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Le projet *free-style* est le type le plus simple pour un premier job : il se configure à l'interface et permet d'ajouter facilement une étape de build « Exécuter un script shell ».

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
