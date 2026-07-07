# Chapitre 9 - Expériences pédagogiques

La meilleure façon de comprendre le CI/CD, c'est de **jouer avec**. Parfait pour une démo.

## Expérience 1 : casser un test exprès (la plus importante)

But : prouver que **rien n'est publié si un test échoue**.

1. Ouvre [`app/logic.py`](../app/logic.py).
2. Dans `priority_rank`, change `"high": 0` en `"high": 5`.
3. Envoie :

```powershell
git add .
git commit -m "Casser un test exprès"
git push
```

4. Dans Jenkins, relance le build (« Build Now ») ou attends le polling. Observe :
   - le stage **Test** devient **rouge** ;
   - le stage **Build & Push** **n'est jamais atteint** (le pipeline s'arrête avant).

5. **Conclusion** : aucune image cassée n'atteint Docker Hub.

6. Répare (`"high": 0`), commit, push, relance : le pipeline redevient vert et publie.

## Expérience 2 : comparer avec GitHub Actions

Ouvre le projet jumeau `jenkins-python-pytest-demo-1` (celui avec GitHub Actions) et compare :

| Concept | GitHub Actions | Jenkins |
|---------|----------------|---------|
| Fichier | `.github/workflows/ci-cd.yml` | `Jenkinsfile` |
| Étape | `job` / `step` | `stage` / `step` |
| « ne pas publier si test rouge » | `needs: test` | ordre des `stages` |
| Condition de branche | `if: github.ref == ...` | `when { branch 'main' }` |
| Secrets | `secrets.DOCKERHUB_TOKEN` | `credentialsId: 'dockerhub'` |
| Où ça tourne | Cloud GitHub | Ta machine (Docker) |

C'est le meilleur moyen de comprendre que **les concepts sont les mêmes**, seule la syntaxe
change.

## Expérience 3 : ajouter un test

Dans [`tests/test_logic.py`](../tests/test_logic.py), ajoute :

```python
def test_normalize_priority_accepte_h():
    assert normalize_priority("h") == "high"
```

Lance `pytest` en local, puis `git push` et relance le build. Le nombre de tests augmente.

## Expérience 4 : explorer l'interface Jenkins

- **Console Output** : les logs bruts, ligne par ligne.
- **Stage View** : la vue en colonnes des stages, avec les durées.
- **Test Result** : le rapport JUnit (courbe de tests dans le temps).
- **Build History** : l'historique de tous les builds (bleu/vert = ok, rouge = échec).

## Expérience 5 : la couverture de code

Dans la Console Output du stage Test, repère le tableau « coverage » : le pourcentage de
code testé, fichier par fichier.

## Prochaine étape

[Chapitre 10 - Dépannage (FAQ)](10-depannage-faq.md).
