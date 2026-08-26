"""API — backend simple pour l'exemple Helm.

Retourne l'environnement d'execution (DEV / STAGING / PROD), la version
applicative, et l'identifiant du Pod. Le portail interroge /ping et affiche
le resultat sur son tableau de bord.
"""

import os
import socket
import time

from flask import Flask, jsonify

app = Flask(__name__)
DEMARRAGE = time.time()

ENV = os.environ.get("ENVIRONMENT", "inconnu")
VERSION = os.environ.get("APP_VERSION", "0.0.0")


@app.route("/")
@app.route("/ping")
def ping():
    return jsonify(service="api", env=ENV, version=VERSION,
                   pod=socket.gethostname(),
                   uptime=int(time.time() - DEMARRAGE))


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
