<a id="top"></a>

# Quiz — Séance 15 — Monitoring et observabilité (Prometheus, Grafana, logs, alertes)

> **Évaluation sommative** · Quiz de fin de séance 15 (15 septembre 2026) · Pondération 0,5 % · QCM individuel en fin de séance
>
> **Contenus évalués :** Prometheus, Grafana, logs, métriques, alertes

---

**Question 1 :** Selon quel modèle Prometheus collecte-t-il les métriques par défaut ?

a) Push : chaque application envoie ses métriques au serveur

b) Pull : Prometheus interroge périodiquement (scrape) les endpoints des cibles

c) Stream : les métriques transitent par un bus Kafka

d) Batch : un export complet une fois par jour

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Prometheus fonctionne en mode pull : il « scrape » à intervalle régulier les endpoints HTTP (souvent `/metrics`) exposés par les cibles configurées.

</details>

---

**Question 2 :** Quel est le rôle principal de Grafana dans une stack d'observabilité ?

a) Stocker les séries temporelles à long terme

b) Collecter les logs des conteneurs

c) Visualiser les métriques sous forme de tableaux de bord (dashboards)

d) Envoyer les notifications par courriel

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Grafana est l'outil de visualisation : il se connecte à des sources de données (dont Prometheus) pour construire des tableaux de bord interactifs. Il ne stocke pas lui-même les métriques.

</details>

---

**Question 3 :** Quel type de métrique Prometheus représente une valeur cumulative qui ne fait qu'augmenter (ex. nombre total de requêtes) ?

a) Gauge

b) Counter

c) Summary

d) Histogram

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Un `Counter` est monotone croissant (il ne décroît qu'en cas de redémarrage). Une `Gauge`, à l'inverse, peut monter et descendre (ex. utilisation mémoire).

</details>

---

**Question 4 :** En PromQL, quelle fonction calcule le taux de croissance moyen par seconde d'un counter sur une fenêtre de 5 minutes ?

a) `increase(http_requests_total)`

b) `avg(http_requests_total)`

c) `rate(http_requests_total[5m])`

d) `sum(http_requests_total[5m])`

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — `rate(metric[5m])` calcule le taux d'accroissement par seconde d'un counter sur la fenêtre de temps indiquée entre crochets, en gérant les remises à zéro (resets).

</details>

---

**Question 5 :** Quel composant de l'écosystème Prometheus est responsable de l'envoi effectif des notifications (courriel, Slack, PagerDuty) lorsqu'une alerte se déclenche ?

a) Node Exporter

b) Alertmanager

c) Pushgateway

d) Grafana Loki

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : b)** — Prometheus évalue les règles d'alerte et transmet les alertes actives à l'`Alertmanager`, qui se charge du routage, du regroupement, de la suppression des doublons et de l'envoi vers les récepteurs configurés.

</details>

---

**Question 6 :** Dans le modèle des « trois piliers » de l'observabilité, lequel correspond à l'enregistrement détaillé et horodaté d'événements applicatifs (ex. un message d'erreur) ?

a) Les métriques (metrics)

b) Les traces

c) Les logs

d) Les alertes

<details>
<summary>💡 Voir la solution</summary>

✅ **Réponse : c)** — Les trois piliers sont les métriques (valeurs numériques agrégées), les logs (événements horodatés détaillés) et les traces (suivi d'une requête à travers les services). L'erreur applicative relève des logs.

</details>

---

<p align="center">
  <em>Tous droits réservés. Toute reproduction, diffusion, utilisation ou adaptation de ce cours, en tout ou en partie, est strictement interdite sans l'autorisation écrite préalable de Dr. Haythem REHOUMA.</em>
</p>

<p align="center">
  <strong>Cours créé par Dr. Haythem REHOUMA — Développement et déploiement de solutions de données</strong>
</p>
