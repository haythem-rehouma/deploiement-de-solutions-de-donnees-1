# Chapitre 3 - Comprendre le projet

Comprenons **à quoi sert chaque fichier**. Reviens ici quand tu as un doute.

## La structure des dossiers

```
jenkins-python-pytest-demo-2/
├── app/                      <- Le code de l'application
│   ├── __init__.py
│   ├── logic.py              <- La logique métier (fonctions à tester)
│   └── main.py               <- L'API web (routes /health, /tasks, ...)
│
├── tests/                    <- Les tests automatiques
│   ├── test_logic.py
│   └── test_api.py
│
├── docs/                     <- Ce guide
│
├── jenkins/
│   └── Dockerfile            <- Image Jenkins personnalisée (Jenkins + Python + docker CLI)
│
├── Jenkinsfile               <- LE PIPELINE : dit à Jenkins quoi faire
├── docker-compose.yml        <- Lance Jenkins dans Docker
├── Dockerfile                <- Recette de l'image de l'APPLICATION
├── .dockerignore
├── requirements.txt          <- Bibliothèques Python nécessaires
├── pytest.ini                <- Configuration des tests
├── .gitignore
└── README.md
```

## Deux « Dockerfile » : ne pas confondre

C'est le point qui trouble le plus les débutants :

- **`jenkins/Dockerfile`** : construit l'image de **Jenkins lui-même**, en y ajoutant
  Python (pour lancer pytest) et le client Docker (pour construire des images). Utilisé une
  seule fois, au démarrage de Jenkins.

- **`Dockerfile`** (à la racine) : construit l'image de **notre application** (l'API). C'est
  cette image qui sera publiée sur Docker Hub à chaque pipeline réussi.

## L'application : un gestionnaire de tâches

Une **API web** minuscule avec 5 routes :

| Méthode | Route | Ce que ça fait |
|---------|-------|----------------|
| GET | `/health` | Dit si l'application est en vie |
| GET | `/tasks` | Liste toutes les tâches |
| POST | `/tasks` | Ajoute une tâche |
| GET | `/tasks/{id}` | Détail d'une tâche |
| DELETE | `/tasks/{id}` | Supprime une tâche |

## Pourquoi séparer `logic.py` et `main.py` ?

- **`logic.py`** = fonctions pures, faciles à tester unitairement.
- **`main.py`** = l'API web qui utilise ces fonctions.

## Le fichier le plus important : `Jenkinsfile`

C'est lui qui décrit le pipeline (les étapes que Jenkins exécute). On le détaille
entièrement au [Chapitre 6](06-comprendre-le-jenkinsfile.md).

## Prochaine étape

[Chapitre 4 - Lancer en local](04-lancer-en-local.md).
