# Chapitre 7 - Configurer Docker Hub

Pour que GitHub puisse publier l'image sur ton compte Docker Hub, il faut lui donner une
**clé d'accès** (un token). On ne met **jamais** son mot de passe directement : on utilise un
token, qu'on range dans un coffre-fort appelé **secrets**.

## Étape 1 : créer un Access Token sur Docker Hub

1. Connecte-toi sur https://hub.docker.com/
2. En haut à droite, clique sur ton avatar, puis **« Account settings »**.
3. Dans le menu, va sur **« Personal access tokens »** (ou « Security »).
4. Clique sur **« Generate new token »**.
5. Donne une description, par exemple `github-actions`.
6. Choisis les permissions **« Read & Write »** (lecture et écriture).
7. Clique sur **« Generate »**.
8. **COPIE LE TOKEN IMMÉDIATEMENT** et garde-le quelque part : Docker Hub ne te le
   remontrera **jamais**. Si tu le perds, il faudra en créer un nouveau.

## Étape 2 : ajouter les secrets sur GitHub

On va donner deux informations à GitHub : ton nom d'utilisateur Docker Hub, et le token.

1. Va sur ton dépôt GitHub.
2. Clique sur l'onglet **« Settings »** (paramètres du dépôt, pas de ton compte).
3. Dans le menu de gauche : **« Secrets and variables »** puis **« Actions »**.
4. Clique sur **« New repository secret »**.

Crée le **premier secret** :
- **Name** : `DOCKERHUB_USERNAME`
- **Secret** : ton Docker ID (ton nom d'utilisateur Docker Hub)
- Clique sur « Add secret ».

Crée le **deuxième secret** :
- Clique à nouveau sur « New repository secret ».
- **Name** : `DOCKERHUB_TOKEN`
- **Secret** : colle le token que tu as copié à l'étape 1.
- Clique sur « Add secret ».

## Étape 3 : vérifier

Tu dois maintenant voir **deux secrets** dans la liste :

| Nom | À quoi ça sert |
|-----|----------------|
| `DOCKERHUB_USERNAME` | Identifie ton compte Docker Hub |
| `DOCKERHUB_TOKEN` | Autorise GitHub à publier en ton nom |

> Ces noms doivent être **exactement** ceux-là (majuscules comprises), car le fichier
> `ci-cd.yml` les appelle par ces noms précis : `${{ secrets.DOCKERHUB_USERNAME }}` et
> `${{ secrets.DOCKERHUB_TOKEN }}`.

## Pourquoi des secrets et pas juste écrire le token dans le code ?

Parce que ton code est **public** sur GitHub. Si tu écrivais ton token en clair, n'importe
qui pourrait le voler et publier des images à ta place (ou pire). Les secrets sont
**chiffrés** et **jamais affichés** dans les logs. C'est une règle de sécurité fondamentale.

## Prochaine étape

Tout est prêt ! Lançons la démo : [Chapitre 8 - Lancer et observer](08-lancer-et-observer.md).
