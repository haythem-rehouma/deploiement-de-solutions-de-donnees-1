# Chapitre 3 - Comprendre le projet

Avant de lancer quoi que ce soit, comprenons **à quoi sert chaque fichier**. Pas besoin de
tout retenir : reviens ici quand tu as un doute.

## La structure des dossiers

```
jenkins-python-pytest-demo-1/
├── app/                      <- Le code de l'application
│   ├── __init__.py           <- Indique que "app" est un module Python
│   ├── logic.py              <- La logique métier (fonctions simples à tester)
│   └── main.py               <- L'API web (les routes /health, /tasks, ...)
│
├── tests/                    <- Les tests automatiques
│   ├── __init__.py
│   ├── test_logic.py         <- Teste les fonctions de logic.py
│   └── test_api.py           <- Teste l'API de main.py
│
├── docs/                     <- Ce guide que tu es en train de lire
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml         <- LE PIPELINE : dit à GitHub quoi faire automatiquement
│
├── Dockerfile                <- La recette pour construire l'image Docker
├── .dockerignore             <- Fichiers à ne PAS mettre dans l'image
├── requirements.txt          <- La liste des bibliothèques Python nécessaires
├── pytest.ini                <- La configuration des tests
├── .gitignore                <- Fichiers que Git doit ignorer
└── README.md                 <- Présentation rapide du projet
```

## L'application : un gestionnaire de tâches

Notre application est une **API web** minuscule qui gère une liste de tâches (comme une
liste de choses à faire). Elle a 5 « portes d'entrée » (qu'on appelle des **routes**) :

| Méthode | Route | Ce que ça fait |
|---------|-------|----------------|
| GET | `/health` | Dit si l'application est en vie |
| GET | `/tasks` | Donne la liste de toutes les tâches |
| POST | `/tasks` | Ajoute une nouvelle tâche |
| GET | `/tasks/{id}` | Donne le détail d'une tâche précise |
| DELETE | `/tasks/{id}` | Supprime une tâche |

> **GET, POST, DELETE** sont des « verbes » HTTP : lire, créer, supprimer. C'est le langage
> standard du web.

## Pourquoi séparer `logic.py` et `main.py` ?

C'est une bonne pratique très importante :

- **`logic.py`** contient des **fonctions pures** : elles prennent une entrée, renvoient une
  sortie, sans dépendre d'internet ou d'une base de données. Exemple : « nettoyer le titre
  d'une tâche ». C'est **très facile à tester**.

- **`main.py`** contient l'**API web** : elle utilise les fonctions de `logic.py` et les
  expose sur internet.

Séparer les deux rend le code plus clair et les tests plus simples.

## À quoi servent les tests ?

Les tests sont du code qui **vérifie que ton autre code fonctionne**. Par exemple :

```python
def test_creer_tache():
    resp = client.post("/tasks", json={"title": "Écrire des tests", "priority": "high"})
    assert resp.status_code == 201   # 201 = "créé avec succès"
```

Le mot-clé `assert` veut dire « je m'attends à ce que ça soit vrai ». Si ce n'est pas vrai,
le test **échoue**, et le pipeline s'arrête. C'est notre filet de sécurité.

## Le fichier le plus important : `ci-cd.yml`

C'est lui qui transforme un simple dépôt de code en une **usine automatique**. On le détaille
entièrement au [Chapitre 6](06-comprendre-le-pipeline.md).

## Prochaine étape

Faisons tourner tout ça sur ta machine : [Chapitre 4 - Lancer en local](04-lancer-en-local.md).
