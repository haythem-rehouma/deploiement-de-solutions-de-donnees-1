"""Application web de demonstration pour comprendre les SERVICES Kubernetes.

Chaque reponse affiche le NOM DU POD (hostname) : en interrogeant un Service
qui pointe vers plusieurs Pods, on voit le nom changer -> le Service repartit
la charge. On l'utilise pour comparer ClusterIP, NodePort et LoadBalancer.
"""

import os
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


def _config():
    return {
        "role": os.environ.get("APP_ROLE", "backend"),
        "bg_color": os.environ.get("BG_COLOR", "#0f172a"),
        "pod": socket.gethostname(),
    }


@app.route("/")
def home():
    cfg = _config()

    if "application/json" in request.headers.get("Accept", ""):
        return jsonify(pod=cfg["pod"], role=cfg["role"])

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Kubernetes — Services</title>
  <style>
    body {{ font-family: system-ui, sans-serif; background:{cfg["bg_color"]}; color:#e2e8f0;
           display:flex; min-height:100vh; align-items:center; justify-content:center; margin:0; }}
    .card {{ background:#1e293b; padding:40px 56px; border-radius:16px; text-align:center;
            box-shadow:0 10px 40px rgba(0,0,0,.4); }}
    h1 {{ margin:0 0 8px; }}
    .pod {{ color:#38bdf8; font-size:2rem; font-weight:700; }}
    .role {{ color:#a3e635; text-transform:uppercase; letter-spacing:2px; font-size:.8rem; }}
    p {{ color:#94a3b8; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="role">{cfg["role"]}</div>
    <h1>Service Kubernetes</h1>
    <p>Reponse servie par le pod :</p>
    <div class="pod">{cfg["pod"]}</div>
    <p>Rechargez : le Service repartit la charge entre les Pods.</p>
  </div>
</body>
</html>"""


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
