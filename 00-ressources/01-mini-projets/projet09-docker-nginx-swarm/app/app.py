"""Petite application web de demonstration.

Elle affiche le NOM DU CONTENEUR qui repond. En lancant plusieurs repliques
derriere Nginx, on voit le nom changer d'une requete a l'autre : c'est la
preuve visuelle de la repartition de charge (load balancing).
"""

import os
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    hostname = socket.gethostname()
    # Couleur de fond configurable via la variable d'environnement BG_COLOR
    # (ex. dans docker-compose.yml). Valeur par defaut : bleu nuit.
    bg_color = os.environ.get("BG_COLOR", "#0f172a")
    # Format demande via l'en-tete Accept : JSON pour les tests, sinon HTML.
    if "application/json" in request.headers.get("Accept", ""):
        return jsonify(conteneur=hostname, message="Bonjour depuis Docker", fond=bg_color)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Docker + Nginx + Swarm</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background:{bg_color}; color:#e2e8f0;
           display:flex; min-height:100vh; align-items:center; justify-content:center; margin:0; }}
    .card {{ background:#1e293b; padding:40px 56px; border-radius:16px; text-align:center;
            box-shadow:0 10px 40px rgba(0,0,0,.4); }}
    h1 {{ margin:0 0 8px; }}
    .host {{ color:#38bdf8; font-size:2rem; font-weight:700; }}
    p {{ color:#94a3b8; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Bonjour depuis Docker !</h1>
    <p>Cette reponse vient du conteneur :</p>
    <div class="host">{hostname}</div>
    <p>Rechargez la page (Ctrl+R) : le nom change quand Nginx repartit la charge.</p>
  </div>
</body>
</html>"""


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
