# Aide-mémoire des commandes (Maven via Docker)

> Ouvrez un terminal **dans ce dossier** (`projet1-introduction-a-maven`), là où se trouve `docker-compose.yml`.
> Toutes les commandes ont la forme : `docker compose run --rm maven <commande>`.

## 0. Vérifier que Docker fonctionne

```bash
docker --version
docker compose version
```

## 1. Compiler le projet

```bash
docker compose run --rm maven compile
```

## 2. Exécuter les tests unitaires

```bash
docker compose run --rm maven test
```

## 3. Construire le projet (compile + test + JAR)

```bash
docker compose run --rm maven package
```

## 4. Nettoyer le projet (supprime `target/`)

```bash
docker compose run --rm maven clean
```

## 5. Installer dans le dépôt local Maven

```bash
docker compose run --rm maven install
```

## 6. Générer le site du projet

```bash
docker compose run --rm maven site
```

## Combinaisons utiles

```bash
# Tout nettoyer puis reconstruire
docker compose run --rm maven clean package

# Lancer mvn test par defaut (sans rien preciser)
docker compose run --rm maven
```

## Mode interactif (plusieurs commandes à la suite)

```bash
docker compose run --rm --entrypoint bash maven
# dans le conteneur :
mvn compile
mvn test
exit
```

## Résultat attendu pour `test` / `package`

```text
Tests run: 5, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```

---

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
