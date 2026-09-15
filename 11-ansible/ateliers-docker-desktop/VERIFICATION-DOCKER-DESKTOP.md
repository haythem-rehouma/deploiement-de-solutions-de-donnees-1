# Vérification de l’adaptation Docker Desktop

Vérification réalisée le 15 septembre 2026 sur ce poste Windows.

## Périmètre

Les huit documents d’origine ont été lus et adaptés individuellement. Le dossier laboratoire-docker-desktop contient les configurations et les 19 playbooks utilisés dans les documents. Les noms des documents et l’absence d’emojis ont été conservés.

## Contrôle fichier par fichier

| Fichier | Problème relevé | Correction | Vérification |
|---|---|---|---|
| [00-ansible-installer-un-laboratoire-docker-configurer-ssh-et-creer-un-premier-playbook-apache.md](00-ansible-installer-un-laboratoire-docker-configurer-ssh-et-creer-un-premier-playbook-apache.md) | Installation sur un hôte Ubuntu, IP fixes et accès direct aux conteneurs | Configuration Docker Desktop, contrôleur Ansible, clés internes et ports publiés | Premier playbook exécuté ; HTTP sur node1 et node2 |
| [01-ansible-deployer-et-configurer-apache-sur-des-conteneurs-docker-ubuntu-debian-et-almalinux.md](01-ansible-deployer-et-configurer-apache-sur-des-conteneurs-docker-ubuntu-debian-et-almalinux.md) | Installation Apache différente selon les exemples ; dépendance aux services classiques | Rôle commun APT/DNF, détection du processus et reprise au démarrage | Six pages HTTP ; second passage sans changement ; redémarrage AlmaLinux |
| [02-ansible-organiser-les-inventaires-en-groupes-et-administrer-les-serveurs-en-commandes-ad-hoc.md](02-ansible-organiser-les-inventaires-en-groupes-et-administrer-les-serveurs-en-commandes-ad-hoc.md) | Groupes de distributions mixtes traités avec un seul gestionnaire de paquets | Groupes fonctionnels et groupes de distributions partagés ; commandes PowerShell | Vim sur database ; uptime sur mail ; rechargement Apache sur web |
| [03-ansible-concevoir-des-playbooks-multitaches-reutiliser-les-taches-et-gerer-les-tags.md](03-ansible-concevoir-des-playbooks-multitaches-reutiliser-les-taches-et-gerer-les-tags.md) | Paramètre excludes incorrect et collection archive non fournie | Collection installée dans le contrôleur, exclusion_patterns, importations et tags autonomes | Archive sur six nœuds ; tâches importées ; tags et exclusions de tags |
| [03-ansible-diagnostiquer-les-avertissements-python-et-les-erreurs-d-archivage-des-journaux.md](03-ansible-diagnostiquer-les-avertissements-python-et-les-erreurs-d-archivage-des-journaux.md) | Diagnostic centré sur des IP et installation de collection au mauvais endroit | Diagnostic Docker Desktop, chemins du contrôleur, clé d’hôte ciblée et ports Windows | Ancienne clé refusée après recréation ; correction ciblée puis ping réussi |
| [04-ansible-maitriser-les-variables-les-facts-et-register-pour-des-playbooks-conditionnels.md](04-ansible-maitriser-les-variables-les-facts-et-register-pour-des-playbooks-conditionnels.md) | Interpréteur et facts dépendants du contexte ; résultat Git antérieur à son installation | Facts explicites, vérification après installation, paquets disponibles dans les images | Six playbooks exécutés ; branche Git absent puis branche Git présent |
| [05-ansible-automatiser-les-taches-avec-des-boucles-sur-listes-dictionnaires-et-hotes-de-l-inventaire.md](05-ansible-automatiser-les-taches-avec-des-boucles-sur-listes-dictionnaires-et-hotes-de-l-inventaire.md) | Groupe database absent, mot de passe d’exemple, délégation mal expliquée et pause invalide | Inventaire commun, comptes verrouillés, délégation depuis le contrôleur et loop_control.pause | Six playbooks exécutés ; trois comptes sur deux nœuds ; second passage sans changement |
| [README.md](README.md) | Fichier vide | Guide de démarrage, architecture, parcours et cycle de vie | Liens locaux contrôlés et parcours relié aux fichiers fournis |

## Environnement réellement testé

- Windows avec Docker Desktop 4.68.0 ; moteur Linux 29.3.1 ; Compose 5.1.1.
- Contrôleur : Python 3.12.14, Ansible Core 2.20.9 et community.general 12.6.5.
- Cibles : Ubuntu 24.04, Debian 12 et AlmaLinux 9.
- Projet de test distinct : codex-ansible-verification.

## Résultats

- Construction des images et démarrage des sept services réussis.
- Six connexions SSH/Python avec réponse pong.
- Syntaxe des 19 playbooks vérifiée, puis exécution réelle de chacun.
- Syntaxe des 60 blocs PowerShell vérifiée séparément.
- Six pages HTTP vérifiées depuis PowerShell sur localhost:8081 à localhost:8086.
- Second passage des playbooks Apache et utilisateurs sans modification.
- Archives, groupes, utilisateurs, tags et délégation vérifiés sur les cibles.
- Apache relancé après redémarrage AlmaLinux, puis après arrêt/reprise des sept services.
- Recréation de node6 testée : l’ancienne clé d’hôte est refusée ; retrait de son entrée, nouvelle connexion et redéploiement réussis.
- 71 contrôles automatisés consignés, avec les contrôles HTTP PowerShell complémentaires.

## Portée des résultats

Les essais ont utilisé Docker Desktop déjà installé sur ce poste. L’installation de Docker Desktop sur un autre Windows n’a pas été rejouée. Les téléchargements nécessitent un accès Internet. Les branches de versions des dépendances sont bornées dans les fichiers requirements ; de futurs correctifs ou mises à jour des images peuvent modifier les versions précises.

Les sources sont conservées dans Windows. Les modifications des nœuds survivent à stop/start mais disparaissent lors de la suppression des conteneurs ; ce comportement est décrit dans le cours. Les clés sont conservées dans des volumes du laboratoire.

Le client HTTP de test Node résolvait localhost seulement vers ::1 sur ce poste : ses contrôles utilisent donc 127.0.0.1. Les six URL localhost ont été vérifiées séparément avec Invoke-WebRequest dans PowerShell. Cette particularité et son contournement figurent dans le dépannage.

## Sources officielles utilisées

- [Ansible : contrôleur et installation en conteneur](https://docs.ansible.com/projects/ansible/latest/installation_guide/intro_installation.html)
- [Docker Desktop et WSL 2](https://docs.docker.com/desktop/features/wsl/)
- [Réseau et noms de services Compose](https://docs.docker.com/compose/how-tos/networking/)
- [Ports publiés Docker Desktop](https://docs.docker.com/desktop/features/networking/)
- [Compatibilité des versions Ansible et Python](https://docs.ansible.com/projects/ansible/latest/reference_appendices/release_and_maintenance.html)
- [Module archive](https://docs.ansible.com/projects/ansible/latest/collections/community/general/archive_module.html)
- [Boucles Ansible](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_loops.html)
- [Délégation Ansible](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_delegation.html)
