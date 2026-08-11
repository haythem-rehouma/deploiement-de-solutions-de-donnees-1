"""Petite application web de demonstration pour Kubernetes.

Elle affiche le NOM DU POD (hostname du conteneur) qui repond. En lancant
plusieurs repliques via un Deployment + Service, on voit le nom changer d'une
requete a l'autre : c'est la preuve visuelle de la repartition de charge.

Toute la configuration passe par des VARIABLES D'ENVIRONNEMENT, injectees
depuis un ConfigMap Kubernetes (APP_TITLE, BG_COLOR, APP_VERSION).
"""

import os
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


def _config():
    return {
        "title": os.environ.get("APP_TITLE", "Bonjour depuis Kubernetes !"),
        "version": os.environ.get("APP_VERSION", "1.0.0"),
        "bg_color": os.environ.get("BG_COLOR", "#0f172a"),
        "pod": socket.gethostname(),
    }


@app.route("/")
def home():
    cfg = _config()

    if "application/json" in request.headers.get("Accept", ""):
        return jsonify(pod=cfg["pod"], titre=cfg["title"],
                       version=cfg["version"], fond=cfg["bg_color"])

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Kubernetes — Deployments &amp; Pods</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background:{cfg["bg_color"]}; color:#e2e8f0;
           display:flex; min-height:100vh; align-items:center; justify-content:center; margin:0; }}
    .card {{ background:#1e293b; padding:40px 56px; border-radius:16px; text-align:center;
            box-shadow:0 10px 40px rgba(0,0,0,.4); }}
    h1 {{ margin:0 0 8px; }}
    .pod {{ color:#38bdf8; font-size:2rem; font-weight:700; }}
    p {{ color:#94a3b8; }}
    .v {{ margin-top:16px; font-size:.85rem; color:#64748b; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>{cfg["title"]}</h1>
    <p>Cette reponse vient du pod :</p>
    <div class="pod">{cfg["pod"]}</div>
    <p>Rechargez la page (Ctrl+R) : le nom change quand le Service repartit la charge.</p>
    <div class="v">version {cfg["version"]}</div>
  </div>
</body>
</html>"""


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
