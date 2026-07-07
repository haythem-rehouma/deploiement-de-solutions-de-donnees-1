# Chapitre 7 - Configurer les accès Docker Hub dans Jenkins

Pour que Jenkins puisse publier l'image sur Docker Hub, on lui donne un **token** rangé dans
le système de **credentials** (identifiants) de Jenkins. On ne met **jamais** son mot de
passe en clair.

## Étape 1 : créer un Access Token sur Docker Hub

1. Connecte-toi sur https://hub.docker.com/
2. Avatar (en haut à droite) -> **« Account settings »**.
3. Menu **« Personal access tokens »** (ou « Security »).
4. **« Generate new token »**.
5. Description : `jenkins`. Permissions : **« Read & Write »**.
6. **« Generate »**, puis **COPIE LE TOKEN** immédiatement (il ne sera plus jamais affiché).

## Étape 2 : créer les credentials dans Jenkins

1. Sur le tableau de bord Jenkins, va dans **« Manage Jenkins »** (Administrer Jenkins).
2. Clique sur **« Credentials »**.
3. Clique sur **« System »** -> **« Global credentials (unrestricted) »**.
4. Clique sur **« Add Credentials »** (Ajouter des identifiants).
5. Remplis :
   - **Kind** : `Username with password`
   - **Username** : ton **Docker ID** (nom d'utilisateur Docker Hub)
   - **Password** : colle ton **token** Docker Hub
   - **ID** : `dockerhub`  ← **TRÈS IMPORTANT, exactement ce texte**
   - **Description** : `Docker Hub (token)`
6. Clique sur **« Create »**.

> L'**ID** doit être exactement `dockerhub`, car le `Jenkinsfile` l'appelle par ce nom :
> `credentialsId: 'dockerhub'`.

## Étape 3 : vérifier

Dans la liste des credentials, tu dois voir une entrée avec l'ID `dockerhub` de type
« Username with password ».

## Pourquoi ne pas écrire le token dans le Jenkinsfile ?

Parce que le `Jenkinsfile` est dans ton dépôt (souvent public). Un token en clair pourrait
être volé. Les credentials Jenkins sont **chiffrés** et **masqués** dans les logs
(ils apparaissent comme `****`). C'est une règle de sécurité fondamentale.

## Prochaine étape

[Chapitre 8 - Créer et lancer le job](08-lancer-et-observer.md).
