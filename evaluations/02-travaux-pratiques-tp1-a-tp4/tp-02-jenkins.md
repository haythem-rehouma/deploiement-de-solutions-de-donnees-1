<a id="top"></a>

# TP2 — Jenkins

> **Travail pratique noté** · Pondération **5 %** · Remise : **dimanche 5 juillet 2026** (fin de journée, en ligne) · **Travail individuel**
>
> **Modules couverts :** [04 — Jenkins : installation](../../04-jenkins-installation/README.md), [05 — Jenkins : pipeline CI/CD](../../05-jenkins-pipeline-cicd/README.md)

---

## Objectifs

À la fin de ce TP, vous serez capable de :

- Installer et configurer une instance Jenkins fonctionnelle.
- Installer les plugins essentiels et sécuriser l'accès.
- Écrire un **Jenkinsfile déclaratif** versionné dans Git.
- Construire un pipeline CI/CD qui clone un dépôt, compile avec Maven et lance les tests.

---

## Contexte

Vous automatisez le build du projet versionné au TP1 (ou d'un projet Maven fourni). Le but : passer du build manuel au **build automatisé déclenché par Jenkins**.

---

## Consignes (étapes)

1. **Installation**
   - Démarrez Jenkins (Docker recommandé : `docker run -p 8080:8080 …`) et déverrouillez l'instance.
   - Installez les plugins suggérés + **Git**, **Pipeline**, **Maven Integration**.

2. **Configuration**
   - Créez un utilisateur administrateur.
   - Activez la sécurité (authentification + matrice d'autorisations de base).

3. **Pipeline déclaratif**
   - Ajoutez un **`Jenkinsfile`** à la racine de votre dépôt Git.
   - Le pipeline doit comporter au moins les `stages` :
     - `Checkout` (récupération du code, `checkout scm`)
     - `Build` (`mvn -B package`)
     - `Test` (exécution + publication des rapports JUnit)
   - Ajoutez un bloc `post` (ex. message en cas de `success` / `failure`).

4. **Exécution**
   - Créez un job de type **Pipeline** pointant vers votre dépôt.
   - Lancez le build, puis corrigez jusqu'à obtenir un build **vert**.

5. **Déclencheur** (bonus recommandé)
   - Configurez un déclenchement automatique (webhook GitHub ou `pollSCM`).

---

## Livrables attendus

| Livrable | Détail |
|---|---|
| **`Jenkinsfile`** | Versionné dans le dépôt Git, avec les stages demandés |
| **Captures Jenkins** | Stage View du build réussi (vert) + console de log |
| **Rapport de tests** | Résultats JUnit visibles dans Jenkins |
| **Fichier `REPONSES.md`** | Étapes d'installation/config + explications + captures |

---

## Barème de correction (sur 5 %)

| Critère | Pondération |
|---|---|
| Jenkins installé et déverrouillé | 0,5 % |
| Plugins installés + sécurité configurée | 0,5 % |
| `Jenkinsfile` déclaratif correct (structure) | 1,5 % |
| Pipeline qui clone + build Maven + tests | 1,5 % |
| Build vert + `REPONSES.md` (captures) | 1 % |

---

## Conseils

> _Versionnez votre `Jenkinsfile` dès le début : « Pipeline as Code » signifie que le pipeline vit dans le dépôt, pas dans des clics. Un build qui échoue n'est pas un échec — lisez la console, c'est là qu'est la réponse._

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
