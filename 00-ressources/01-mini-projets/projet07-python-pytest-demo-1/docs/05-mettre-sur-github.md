# Chapitre 5 - Mettre le code sur GitHub

Maintenant, on envoie le code sur GitHub. C'est GitHub qui fera tourner la CI/CD.

## Étape 1 : configurer Git (une seule fois)

Dis à Git qui tu es (remplace par ton nom et ton email GitHub) :

```powershell
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@example.com"
```

## Étape 2 : créer un dépôt sur GitHub

1. Connecte-toi sur https://github.com/
2. En haut à droite, clique sur le **+** puis **« New repository »**.
3. Donne un nom, par exemple `demo-cicd-pytest`.
4. Laisse-le en **Public** (plus simple pour la démo, et les Actions sont gratuites).
5. **NE COCHE RIEN** (pas de README, pas de .gitignore) : on a déjà tous les fichiers.
6. Clique sur **« Create repository »**.

GitHub t'affiche alors une page avec des commandes. Garde-la ouverte.

## Étape 3 : transformer ton dossier en dépôt Git

Dans PowerShell, depuis le dossier du projet :

```powershell
cd c:\00-dream\jenkins-python-pytest-demo-1
git init
git add .
git commit -m "Premier commit : démo CI/CD"
```

Explications :
- `git init` : crée un dépôt Git local (un dossier caché `.git`).
- `git add .` : sélectionne **tous** les fichiers à sauvegarder (le point veut dire « tout »).
- `git commit -m "..."` : enregistre une « photo » du code avec un message.

## Étape 4 : relier ton dossier au dépôt GitHub

Sur la page GitHub, copie l'URL de ton dépôt (elle ressemble à
`https://github.com/TON_USER/demo-cicd-pytest.git`). Puis :

```powershell
git branch -M main
git remote add origin https://github.com/TON_USER/demo-cicd-pytest.git
git push -u origin main
```

Explications :
- `git branch -M main` : nomme la branche principale `main`.
- `git remote add origin ...` : dit à Git où se trouve ton dépôt sur GitHub.
- `git push` : **envoie** ton code sur GitHub.

> La première fois, GitHub va te demander de te connecter (une fenêtre s'ouvre dans le
> navigateur). Accepte, c'est normal.

## Étape 5 : vérifier

Rafraîchis la page de ton dépôt sur GitHub : tu dois voir tous tes fichiers.

**Et surtout** : clique sur l'onglet **« Actions »** en haut. Tu devrais voir que le
pipeline s'est **déjà lancé tout seul** ! Le job `test` va s'exécuter.

> Le job `docker` (publication) échouera pour l'instant, car on n'a pas encore configuré
> les secrets Docker Hub. C'est normal, on le fait au [Chapitre 7](07-configurer-docker-hub.md).

## Bon à savoir : la boucle de travail quotidienne

À chaque fois que tu modifies le code ensuite, tu répètes :

```powershell
git add .
git commit -m "Description de mon changement"
git push
```

Et le pipeline se relance automatiquement à chaque `push`. C'est ça, l'intégration continue.

## Prochaine étape

[Chapitre 6 - Comprendre le pipeline](06-comprendre-le-pipeline.md).
