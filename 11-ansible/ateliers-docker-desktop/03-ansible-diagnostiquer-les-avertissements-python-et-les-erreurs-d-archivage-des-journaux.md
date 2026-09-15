# 03 — Diagnostiquer Docker Desktop, SSH, Python et les archives

**Terminal des commandes ci-dessous : PowerShell sous Windows**, depuis le laboratoire :

```powershell
Set-Location "C:\Users\rehou\Downloads\Compressed\deploiement-de-solutions-de-donnees-main\deploiement-de-solutions-de-donnees-main\12-ansible-playbooks-roles\laboratoire-docker-desktop"
```

## 1. Docker ne répond pas

```powershell
docker version
docker info --format '{{.OSType}}'
docker compose version
```

Ouvrir Docker Desktop et attendre le démarrage du moteur. Le type attendu est `linux`. Une erreur de canal Docker ou une absence de partie Server se traite d’abord dans Docker Desktop. Une erreur « no configuration file provided » indique généralement que PowerShell n’est pas dans le dossier contenant `compose.yaml`.

## 2. Un conteneur démarre mal

```powershell
docker compose ps -a
docker compose logs --tail 80 controleur
docker compose logs --tail 80 node3
```

Le contrôleur doit produire la clé publique avant le démarrage des nœuds. Les images installent Python et SSH pendant la construction. En cas d’échec de téléchargement, corriger l’accès Internet ou le proxy Docker Desktop, puis relancer :

```powershell
docker compose up -d --build --wait
```

Un port déjà utilisé se corrige en choisissant un autre port Windows dans `compose.yaml`, puis en ajustant l’URL de test.

## 3. Ansible ne trouve pas une cible

```powershell
docker compose exec controleur ansible-inventory --graph
docker compose exec controleur getent hosts node1
docker compose exec controleur ansible node1 -m ansible.builtin.ping -vvv
```

Le groupe et le nom doivent exister dans `inventory.ini`. Le contrôleur utilise le DNS du réseau Compose pour résoudre `node1`. Une IP visible dans Docker Desktop est une adresse interne ; pour le navigateur Windows, utiliser le port publié sur `localhost`.

## 4. Permission denied en SSH

```powershell
docker compose exec controleur ls -l /keys/id_ed25519
docker compose exec node1 ls -ld /root/.ssh
docker compose exec node1 ls -l /root/.ssh/authorized_keys
docker compose logs --tail 50 node1
```

La clé privée du contrôleur doit avoir les permissions 600, le dossier SSH de la cible 700 et `authorized_keys` 600. Les scripts les règlent au démarrage. L’authentification par mot de passe est désactivée ; les exercices utilisent la clé propre au laboratoire.

Après modification des scripts de construction, reconstruire le laboratoire. Après recréation d’une cible, traiter sa clé d’hôte comme décrit ci-dessous.

## 5. REMOTE HOST IDENTIFICATION HAS CHANGED

Cette erreur peut apparaître après avoir supprimé puis recréé les nœuds : ils génèrent de nouvelles clés d’hôte. Confirmer qu’il s’agit bien d’une recréation de votre laboratoire.

Retirer **uniquement** l’entrée du nœud recréé dans le contrôleur :

```powershell
docker compose exec controleur ssh-keygen -R node1 -f /root/.ssh/known_hosts
docker compose exec controleur ansible node1 -m ansible.builtin.ping
```

Si vous avez recréé les six nœuds :

```powershell
1..6 | ForEach-Object {
    docker compose exec -T controleur ssh-keygen -R "node$_" -f /root/.ssh/known_hosts
}
docker compose exec controleur ansible all -m ansible.builtin.ping
```

Ces commandes agissent sur le fichier dédié au laboratoire dans le volume du contrôleur. L’acceptation initiale des clés s’appuie sur `StrictHostKeyChecking=accept-new` dans `ansible.cfg`.

## 6. Python introuvable ou interpréteur inattendu

```powershell
docker compose exec controleur ansible all -m ansible.builtin.raw -a "python3 --version"
docker compose exec controleur ansible-inventory --host node3
```

Le module `raw` permet ce diagnostic même si les modules Python ne démarrent pas. Les images installent `/usr/bin/python3` et l’inventaire fixe ce chemin. Définir un chemin d’interpréteur ne suffit pas à installer Python ; si le binaire manque, reconstruire la bonne image.

Comparer les versions de Python et Ansible avec la [matrice de compatibilité](https://docs.ansible.com/projects/ansible/latest/reference_appendices/release_and_maintenance.html) avant de changer les images de base.

## 7. Archive absente ou module archive introuvable

```powershell
docker compose exec controleur ansible-galaxy collection list community.general
docker compose exec controleur ansible-doc community.general.archive
docker compose exec controleur ansible-playbook playbooks/03-multitaches.yml --tags archive_logs -vvv
docker compose exec controleur ansible all -m ansible.builtin.stat -a "path=/tmp/logs.tar.gz"
docker compose exec controleur ansible all -m ansible.builtin.command -a "tar -tzf /tmp/logs.tar.gz"
```

La collection est installée dans le contrôleur lors de la construction. Le module s’exécute sur les nœuds. L’archive `/tmp/logs.tar.gz` appartient donc à chaque nœud et apparaît sous Windows seulement après une copie explicite :

```powershell
docker compose cp node1:/tmp/logs.tar.gz ./logs-node1.tar.gz
```

Le bon paramètre pour exclure `wtmp` et `btmp` à l’intérieur de `/var/log` est `exclusion_patterns`. Vérifier que le récapitulatif de la tâche ne signale pas d’échec. [Documentation archive](https://docs.ansible.com/projects/ansible/latest/collections/community/general/archive_module.html).

## 8. La page localhost ne s’ouvre pas

```powershell
docker compose port node1 80
docker compose exec node1 pgrep -a apache2
docker compose exec node1 cat /var/www/html/index.html
docker compose exec controleur ansible-playbook playbooks/01-apache-multidistribution.yml --limit node1
(Invoke-WebRequest -UseBasicParsing http://localhost:8081).Content
```

Pour AlmaLinux, tester `httpd` et le port du nœud concerné. Les cibles fournies n’exécutent pas systemd ; le rôle Apache utilise les commandes de contrôle d’Apache et vérifie ensuite HTTP.

Si un outil résout `localhost` uniquement vers l’adresse IPv6 `::1`, utiliser `http://127.0.0.1:8081` pour node1, ou le port correspondant aux autres nœuds. Le laboratoire publie explicitement ses ports sur la boucle locale IPv4. PowerShell peut accéder aux URL `localhost` indiquées dans les chapitres ; ce point peut varier selon l’outil client et la configuration de Windows.

## 9. Un exemple de boucle échoue

- `Could not match supplied host pattern: database` : restaurer le groupe database de l’inventaire commun.
- Option `delay` invalide dans `loop_control` : utiliser `pause: 1`. Le mot-clé `delay` a un autre usage avec les tentatives `until`.
- `bad interpreter` ou caractère de retour chariot dans un script : enregistrer les scripts shell en UTF-8 avec fins de ligne LF. Les Dockerfiles fournis normalisent aussi ces scripts à la construction.
- Fichier YAML introuvable : conserver la structure `playbooks/`, `tasks/` et `vars/`.

## 10. Vérifier une reprise complète

`stop` puis `start` conserve les fichiers des mêmes conteneurs. Après `down` puis `up`, les fichiers et paquets ajoutés aux nœuds sont à recréer avec les playbooks ; mettre à jour les entrées SSH des cibles recréées avant de relancer Ansible.
