<a id="top"></a>

# Projet 5 — Extraction, transformation et publication automatisées d'offres d'emploi

> **Examen pratique** · **30 points** (+3 bonus) · Module [05 — Jenkins : pipeline CI/CD](../README.md)
>
> **Mission :** construire un **pipeline CI/CD piloté par Jenkins** qui extrait des offres d'emploi depuis plusieurs sources, les stocke en **CSV**, les transforme en **page HTML**, **publie** automatiquement cette page, et **s'arrête intelligemment** s'il n'y a aucune nouvelle offre.
>
> Pressé ? Voir l'**[aide-mémoire des commandes](COMMANDES.md)**.

---

## 1. Ce qu'on construit

```mermaid
flowchart LR
    subgraph Jenkins["Pipeline Jenkins (Docker, Python 3)"]
        I["Install<br/>venv + pip"] --> S["Scraping<br/>scraper.py"]
        S --> D{"DetectChanges<br/>SHA-256<br/>nouveau ?"}
        D -- non --> STOP["Stop<br/>(SUCCESS)"]
        D -- oui --> C["Conversion<br/>html_generator.py"]
        C --> T["Tests<br/>>=10 offres + table"]
        T --> A["Archive<br/>csv + html + log"]
        A --> P["Deploy<br/>publication HTML"]
    end
    S -. ecrit .-> csv["data/jobs.csv"]
    C -. ecrit .-> html["public/index.html"]
```

L'image Docker fournie contient déjà **Jenkins + JDK 17 + Python 3 + venv + Git** : tout s'exécute sans rien installer sur votre poste.

---

## 2. Compétences visées

| Compétence | Description |
|---|---|
| **Automatisation** | Chaîne complète : scraping → transformation → tests → publication. |
| **CI/CD** | Intégration et déploiement continus via Jenkins. |
| **Détection de changements** | Arrêt prématuré du pipeline si aucune nouveauté. |
| **Déploiement Web** | Mise en ligne publique du rapport HTML. |
| **Documentation** | Explications claires dans ce `README.md`. |

---

## 3. Arborescence du projet

```text
projet05-pipeline-offres-emploi/
├── docker-compose.yml          <- lance Jenkins (Python inclus)
├── Dockerfile                  <- Jenkins + JDK 17 + Python 3 + venv + git
├── README.md                   <- ce fichier (l'enonce)
├── COMMANDES.md                <- aide-memoire
└── depot-exemple/              <- a pousser sur VOTRE depot GitHub
    ├── Jenkinsfile             <- le pipeline complet, commente
    ├── scraper.py              <- scraping multi-sources -> data/jobs.csv
    ├── html_generator.py       <- data/jobs.csv -> public/index.html
    ├── requirements.txt        <- requests, beautifulsoup4, lxml, pandas
    ├── .gitignore
    ├── data/                   <- jobs.csv + jobs_previous.csv (generes)
    ├── public/                 <- index.html (genere)
    └── logs/                   <- log.txt (genere)
```

> Les dossiers `data/`, `public/`, `logs/` contiennent un fichier `.gitkeep` pour exister dans Git ; leur contenu généré est **ignoré** (voir `.gitignore`).

---

## 4. Le pipeline étape par étape

Le `Jenkinsfile` est **déclaratif**. Voici l'ordre retenu (et pourquoi) :

| # | Stage | Rôle |
|---|---|---|
| 1 | **Install** | Crée un `venv` et installe `requirements.txt` (`pip install -r`). |
| 2 | **Scraping** | Lance `scraper.py` → génère `data/jobs.csv`. |
| 3 | **DetectChanges** | Compare `jobs.csv` à `jobs_previous.csv` (SHA-256). **Placé tôt** pour éviter tout travail inutile (bonus). |
| 4 | **Conversion** | Lance `html_generator.py` → `public/index.html`. *(seulement si changement)* |
| 5 | **Tests** | Vérifie ≥ 10 offres dans le CSV **et** une `<table>` + ≥ 10 lignes dans le HTML. Échec → `exit 1`. |
| 6 | **Archive** | Archive `jobs.csv`, `index.html`, `logs/log.txt` dans Jenkins. |
| 7 | **Deploy** | Publie le rapport HTML (visible dans le job). |

Les étapes 4 à 7 sont **conditionnées** par `when { environment name: 'HAS_CHANGES', value: 'true' }`.

### Mécanisme exact de détection de changements

En pipeline **déclaratif**, on ne peut pas faire `return` au milieu. La technique propre :

1. Le stage `DetectChanges` calcule le **SHA-256** de `data/jobs.csv` et le compare à celui de `data/jobs_previous.csv`.
2. Il pose une variable d'environnement `HAS_CHANGES` à `'true'` ou `'false'`.
3. Si `'true'`, il copie `jobs.csv → jobs_previous.csv` (nouvelle référence) ; sinon il journalise *« Aucune nouvelle offre »*.
4. Les stages suivants ne s'exécutent **que si** `HAS_CHANGES == 'true'`. Le build reste **vert** (SUCCESS) même quand il n'y a rien de neuf.

> `jobs_previous.csv` persiste dans le *workspace* Jenkins entre deux exécutions du même job : c'est ce qui permet la comparaison d'un build à l'autre.

---

## 5. Démarrage

### Étape A — Lancer Jenkins

Dans ce dossier (`projet05-pipeline-offres-emploi`) :

```bash
docker compose up -d --build
```

Ouvrez **http://localhost:8080** (aucun mot de passe : l'assistant est désactivé).

> Port 8080 occupé ? Voir l'**[Annexe — Le port 8080 est déjà occupé ?](COMMANDES.md#annexe--le-port-8080-est-déjà-occupé-)**.

### Étape B — Pousser le projet sur GitHub

Copiez le contenu de [`depot-exemple/`](depot-exemple) dans un dépôt GitHub (ex. `pipeline-offres`), puis poussez-le.

### Étape C — Créer le job dans Jenkins

| # | Action |
|---|---|
| 01 | **New Item** → nom → type **Pipeline** → **OK**. |
| 02 | *Build Triggers* : **Poll SCM** ou laisser le `cron` du `Jenkinsfile` (`H */6 * * *`). |
| 03 | *Pipeline* → **Definition = Pipeline script from SCM** → **SCM = Git**. |
| 04 | **Repository URL** = votre dépôt (+ credential si privé). |
| 05 | **Script Path** = `Jenkinsfile`. **Save**. |

### Étape D — Lancer

**Build Now**. Au **1er run** : tout s'exécute (pas de référence précédente). Relancez **sans rien changer** : le pipeline détecte *« Aucune nouvelle offre »* et **s'arrête tôt** (stages 4-7 *skipped*), build toujours vert.

Le rapport est visible via **« Offres d emploi »** dans le menu du job (et `index.html` est téléchargeable dans les artefacts).

---

## 6. Déploiement public — option retenue

**Option retenue : publication HTML dans Jenkins** (plugin *HTML Publisher*), simple et sans secret. Le rapport est consultable directement depuis l'interface Jenkins.

Pour un **vrai déploiement public**, voici les options possibles (à documenter selon votre choix) :

| Option | Commande minimale |
|---|---|
| **A. NGINX local** | `scp public/index.html user@192.168.X.X:/var/www/html/` |
| **B. Bucket S3** | `aws s3 cp public/index.html s3://mon-bucket/ --acl public-read` |
| **C. GitHub Pages** | push automatique de `public/index.html` sur la branche `gh-pages` |
| **D. VPS perso** | `rsync -az public/ user@serveur:/var/www/html/` |

> **Exemple Option C (GitHub Pages)** — à mettre dans le stage `Deploy`, avec un credential Jenkins `gh-token` (jamais en clair !) :
>
> ```groovy
> withCredentials([string(credentialsId: 'gh-token', variable: 'GH_TOKEN')]) {
>   sh '''
>     git config user.email "ci@exemple.com"
>     git config user.name "Jenkins CI"
>     git checkout -B gh-pages
>     cp public/index.html index.html
>     git add index.html
>     git commit -m "Publication auto des offres" || echo "Rien a committer"
>     git push https://x-access-token:${GH_TOKEN}@github.com/VOTRE-COMPTE/pipeline-offres.git gh-pages --force
>   '''
> }
> ```
>
> La page sera alors servie sur `https://VOTRE-COMPTE.github.io/pipeline-offres/`.

---

## 7. Déclenchement automatique

Le pipeline démarre **sans action manuelle** grâce à :

- le **`cron`** du `Jenkinsfile` : `triggers { cron('H */6 * * *') }` (toutes les ~6 h) ;
- **et/ou** un **webhook GitHub** (push) si vous activez *GitHub hook trigger* ;
- combiné au stage **DetectChanges** qui évite les exécutions inutiles.

---

## 8. Barème (30 points)

| Critère | Pts |
|---|---|
| Pipeline Jenkins (Install → Deploy) fonctionnel | 5 |
| Exécution réussie de `scraper.py` | 3 |
| Génération valide de `jobs.csv` | 3 |
| Génération correcte de `index.html` | 5 |
| Détection et gestion des changements | 4 |
| Archivage des artefacts dans Jenkins | 2 |
| Déploiement public opérationnel | 5 |
| Documentation (`README.md`) claire | 3 |
| **Bonus** : arrêt intelligent (hash + journalisation propre) | +3 |

---

## 9. Règles et conseils

- **Aucune variable sensible** (clé AWS, jeton, mot de passe) en clair dans le dépôt : utilisez les **Credentials Jenkins** + `withCredentials`.
- Code **commenté** et conforme **PEP 8**.
- Tout échec d'étape doit **faire échouer le build** (`exit code ≠ 0`).
- Utilisez **`logging`** plutôt que `print()` (déjà appliqué dans `scraper.py` et `html_generator.py`).

---

## 10. Livrables

- `Jenkinsfile` complet et commenté.
- `html_generator.py` fonctionnel.
- `README.md` détaillant : architecture, choix de déploiement, mécanisme de détection.
- Captures d'écran Jenkins : exécution réussie, artefacts, étape de déploiement.
- Artefacts générés : `jobs.csv`, `index.html`, `log.txt`.

---

## Arrêter / réinitialiser

```bash
docker compose stop          # arreter (donnees conservees)
docker compose down          # supprimer le conteneur (volume conserve)
docker compose down -v       # tout supprimer (config Jenkins incluse)
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
