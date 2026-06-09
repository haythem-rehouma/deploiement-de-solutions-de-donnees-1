<a id="top"></a>

# TP1 — Git et GitHub

> **Travail pratique noté** · Pondération **5 %** · Remise : **dimanche 21 juin 2026** (fin de journée, en ligne) · **Travail individuel**
>
> **Modules couverts :** [01 — Introduction au DevOps et Git](../../01-introduction-devops-et-git/README.md), [02 — Git avancé et GitHub](../../02-git-avance-et-github/README.md)

---

## Objectifs

À la fin de ce TP, vous serez capable de :

- Initialiser un dépôt Git, créer des commits propres et atomiques.
- Travailler avec des branches et fusionner sans tout casser.
- Publier un dépôt sur GitHub et collaborer via `push` / `pull`.
- Créer et fusionner une **pull request** avec une revue de code.

---

## Contexte

Vous démarrez un petit projet versionné qui servira de base pour les TP suivants. L'objectif n'est pas le code lui-même, mais **la maîtrise du flux de travail Git/GitHub**.

---

## Consignes (étapes)

1. **Dépôt local**
   - Créez un dossier de projet et initialisez un dépôt (`git init`).
   - Ajoutez un `README.md` et un `.gitignore` (au moins une entrée, ex. `.env`).
   - Faites **au moins 3 commits** avec des messages clairs à l'impératif.

2. **Branches**
   - Créez une branche `feature-accueil`, ajoutez-y du contenu, committez.
   - Fusionnez-la dans `main` (`git merge`), puis supprimez la branche.

3. **GitHub**
   - Créez un dépôt distant et liez-le (`git remote add origin …`).
   - Poussez `main` (`git push -u origin main`).

4. **Pull request**
   - Créez une branche `feature-section2`, poussez-la.
   - Ouvrez une **pull request** vers `main` (interface GitHub ou `gh pr create`).
   - Rédigez une description, puis fusionnez la PR.

5. **Provoquer et résoudre un conflit** (bonus recommandé)
   - Modifiez la **même ligne** d'un fichier sur deux branches différentes, fusionnez, et résolvez le conflit manuellement.

---

## Livrables attendus

| Livrable | Détail |
|---|---|
| **URL du dépôt GitHub** | Dépôt public (ou accès accordé à l'enseignant) |
| **Historique** | Au moins 5 commits avec messages clairs, visibles dans `git log` |
| **Branches & fusion** | Trace d'au moins une branche fusionnée dans `main` |
| **Pull request** | Au moins une PR ouverte **et** fusionnée |
| **Fichier `REPONSES.md`** | Captures (ou liens) + courte explication de chaque étape |

---

## Barème de correction (sur 5 %)

| Critère | Pondération |
|---|---|
| Dépôt initialisé + `.gitignore` correct | 0,5 % |
| Qualité et clarté des messages de commit | 1 % |
| Branches créées et fusionnées correctement | 1 % |
| Dépôt publié sur GitHub (`push` fonctionnel) | 1 % |
| Pull request ouverte et fusionnée | 1 % |
| Résolution de conflit + `REPONSES.md` | 0,5 % |

---

## Conseils

> _Faites `git status` avant chaque `git add`, et `git pull` avant chaque `git push`. La majorité des problèmes Git viennent d'un oubli de ces deux réflexes._

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
