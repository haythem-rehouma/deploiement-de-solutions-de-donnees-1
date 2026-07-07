# Chapitre 9 - Expériences pédagogiques

La meilleure façon de comprendre le CI/CD, c'est de **jouer avec**. Voici des expériences à
faire (parfaites pour une démo devant une classe).

## Expérience 1 : casser un test exprès (la plus importante)

But : prouver que **rien n'est publié si un test échoue**.

1. Ouvre [`app/logic.py`](../app/logic.py).
2. Trouve la fonction `priority_rank` et change volontairement l'ordre, par exemple mets
   `"high": 5` au lieu de `"high": 0`.
3. Envoie le changement :

```powershell
git add .
git commit -m "Casser un test exprès"
git push
```

4. Va dans l'onglet **Actions**. Observe :
   - le job `test` devient **rouge** (le test `test_priority_rank_ordre` échoue) ;
   - le job `docker` **ne démarre même pas** (il est ignoré grâce à `needs: test`).

5. **Conclusion pédagogique** : aucune image cassée n'atteint Docker Hub. Le filet de
   sécurité fonctionne.

6. Répare en remettant `"high": 0`, puis `git add . && git commit -m "Réparer" && git push`.
   Le pipeline redevient vert et publie à nouveau.

## Expérience 2 : le flux de travail avec une Pull Request

But : montrer comment on travaille en équipe, avec une revue avant de fusionner.

```powershell
git checkout -b nouvelle-fonctionnalite
```

Fais une modification (par exemple ajoute une route ou un test), puis :

```powershell
git add .
git commit -m "Ajout d'une fonctionnalité"
git push -u origin nouvelle-fonctionnalite
```

1. Va sur GitHub : un bandeau propose de créer une **Pull Request** (PR). Clique dessus.
2. Sur la page de la PR, tu verras la CI se lancer (le job `test` uniquement, car la
   publication n'a lieu que sur `main`).
3. Si tout est vert, tu peux cliquer sur **« Merge »** pour fusionner dans `main`.
4. La fusion déclenche alors le pipeline complet sur `main`, avec la publication Docker.

Point pédagogique : la PR permet de **vérifier le code avant** de l'intégrer. C'est le cœur
du travail en équipe.

## Expérience 3 : ajouter un nouveau test

1. Ouvre [`tests/test_logic.py`](../tests/test_logic.py).
2. Ajoute un cas de test, par exemple :

```python
def test_normalize_priority_accepte_h():
    assert normalize_priority("h") == "high"
```

3. Lance en local d'abord : `pytest`
4. Puis `git add . && git commit -m "Nouveau test" && git push`.

Tu verras le nombre de tests augmenter dans les logs du pipeline.

## Expérience 4 : lire le rapport de tests (artifact)

1. Dans l'onglet Actions, ouvre une exécution réussie.
2. En bas de la page, dans la section **« Artifacts »**, télécharge `rapport-tests`.
3. Tu obtiens le fichier `report.xml` : le rapport détaillé de tous les tests.

## Expérience 5 : voir la couverture de code

Dans les logs du job `test`, déplie l'étape « Lancer les tests ». Tu verras un tableau
« coverage » indiquant le pourcentage de code testé, fichier par fichier. Essaie de deviner
pourquoi certaines lignes ne sont pas couvertes.

## Prochaine étape

Si quelque chose coince : [Chapitre 10 - Dépannage (FAQ)](10-depannage-faq.md).
