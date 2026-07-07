# Chapitre 5 - Démarrer Jenkins dans Docker

On va lancer Jenkins sur ta machine grâce à Docker, puis faire la configuration initiale.

> **Docker Desktop doit être lancé** (ouvre-le et attends qu'il soit « running »).

## Étape 1 : construire et démarrer Jenkins

Depuis le dossier du projet :

```powershell
cd c:\00-dream\jenkins-python-pytest-demo-2
docker compose up -d --build
```

Explications :
- `docker compose up` : démarre les services décrits dans `docker-compose.yml`.
- `-d` : en arrière-plan (detached).
- `--build` : construit d'abord notre image Jenkins personnalisée (Python + docker CLI).

La **première fois**, la construction peut prendre quelques minutes (téléchargements).

Vérifie que le conteneur tourne :

```powershell
docker ps
```

Tu dois voir une ligne `jenkins-demo`.

## Étape 2 : récupérer le mot de passe initial

Jenkins génère un mot de passe administrateur au premier démarrage. Affiche-le :

```powershell
docker exec jenkins-demo cat /var/jenkins_home/secrets/initialAdminPassword
```

Copie la longue chaîne affichée.

> Si le fichier n'existe pas encore, attends 30 secondes que Jenkins finisse de démarrer,
> puis réessaie.

## Étape 3 : l'assistant de configuration

1. Ouvre ton navigateur sur **http://localhost:8080**
2. Colle le mot de passe initial, clique « Continue ».
3. Choisis **« Install suggested plugins »** (installe les plugins recommandés).
   - Nos plugins essentiels (Pipeline, Git, Docker, JUnit, Credentials) sont déjà
     pré-installés par notre image, mais laisse l'assistant compléter.
4. Crée ton **compte administrateur** (nom d'utilisateur, mot de passe, email). Note-les.
5. Laisse l'URL Jenkins par défaut, clique « Save and Finish », puis « Start using Jenkins ».

Tu arrives sur le tableau de bord Jenkins. 🎉

## Commandes utiles

| Action | Commande |
|--------|----------|
| Voir les logs de Jenkins | `docker logs -f jenkins-demo` |
| Arrêter Jenkins | `docker compose stop` |
| Redémarrer Jenkins | `docker compose start` |
| Tout supprimer (sauf données) | `docker compose down` |
| Tout supprimer AVEC les données | `docker compose down -v` |

> Les données de Jenkins (jobs, config) sont conservées dans un volume Docker nommé
> `jenkins_home`. Tant que tu ne fais pas `down -v`, tu les gardes.

## Prochaine étape

Avant de créer le job, comprenons le pipeline :
[Chapitre 6 - Comprendre le Jenkinsfile](06-comprendre-le-jenkinsfile.md).
