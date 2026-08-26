"""Portail — tableau de bord multi-environnement.

Ce Pod affiche l'environnement dans lequel il tourne (DEV / STAGING / PROD),
la version applicative, le nombre de replicas, et l'etat du backend.

Toutes les valeurs affichees viennent de VARIABLES D'ENVIRONNEMENT injectees
par Helm depuis values-<env>.yaml. Le meme code s'adapte a chaque
environnement sans aucune modification.
"""

import os
import socket
import time
import urllib.error
import urllib.request

from flask import Flask, jsonify, request

app = Flask(__name__)
DEMARRAGE = time.time()


def cfg():
    return {
        "env": os.environ.get("ENVIRONMENT", "inconnu"),
        "version": os.environ.get("APP_VERSION", "0.0.0"),
        "theme": os.environ.get("THEME_COLOR", "#64748b"),
        "message": os.environ.get("BANNIERE_MESSAGE", "Deploye avec Helm"),
        "backend_url": os.environ.get("BACKEND_URL", "http://api"),
        "replicas_info": os.environ.get("REPLICAS_INFO", "?"),
        "pod": socket.gethostname(),
        "uptime": int(time.time() - DEMARRAGE),
    }


def tester_backend(url):
    try:
        with urllib.request.urlopen(url + "/ping", timeout=1.5) as reponse:
            corps = reponse.read(200).decode("utf-8", "ignore")
        return "ok", corps.strip()
    except urllib.error.HTTPError as err:
        return "http", "HTTP %s" % err.code
    except Exception as err:
        return "ko", type(err).__name__


@app.route("/health")
def health():
    return "OK", 200


@app.route("/api-json")
def api_json():
    """Route utile pour la validation automatique."""
    c = cfg()
    etat, detail = tester_backend(c["backend_url"])
    return jsonify(pod=c["pod"], env=c["env"], version=c["version"],
                   backend=etat, backend_detail=detail, uptime=c["uptime"])


@app.route("/")
def accueil():
    c = cfg()
    etat, detail = tester_backend(c["backend_url"])

    if etat == "ok":
        pastille = "OK"
        pastille_bg = "#16a34a"
    else:
        pastille = "KO"
        pastille_bg = "#b91c1c"

    return """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="3">
  <title>Portail {env} — v{version}</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ font-family: system-ui, sans-serif; background:#0f172a; color:#e2e8f0;
            margin:0; padding:0; min-height:100vh; }}
    .bandeau {{ background:{theme}; padding:28px 40px; box-shadow:0 6px 20px rgba(0,0,0,.4); }}
    .bandeau h1 {{ margin:0; font-size:2.2rem; letter-spacing:3px; }}
    .bandeau .msg {{ opacity:.85; margin-top:4px; }}
    main {{ padding:40px; max-width:1100px; margin:0 auto; }}
    .grille {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:16px; }}
    .carte {{ background:#1e293b; border-radius:12px; padding:20px 22px;
              box-shadow:0 6px 20px rgba(0,0,0,.3);
              border-left:6px solid {theme}; }}
    .carte .titre {{ font-size:.75rem; letter-spacing:2px; color:#94a3b8;
                     text-transform:uppercase; }}
    .carte .valeur {{ font-size:1.5rem; font-weight:700; margin-top:6px; }}
    .pastille {{ display:inline-block; padding:6px 12px; border-radius:6px;
                 font-weight:700; letter-spacing:1px;
                 color:#fff; background:{pastille_bg}; }}
    .pied {{ margin-top:28px; color:#64748b; font-size:.85rem; text-align:center; }}
    code {{ background:#0f172a; padding:2px 6px; border-radius:4px; color:#94a3b8; }}
  </style>
</head>
<body>
  <header class="bandeau">
    <h1>{env}</h1>
    <div class="msg">{message}</div>
  </header>
  <main>
    <div class="grille">
      <div class="carte">
        <div class="titre">Version applicative</div>
        <div class="valeur">v{version}</div>
      </div>
      <div class="carte">
        <div class="titre">Replicas declares</div>
        <div class="valeur">{replicas_info}</div>
      </div>
      <div class="carte">
        <div class="titre">Pod servant cette requete</div>
        <div class="valeur"><code>{pod}</code></div>
      </div>
      <div class="carte">
        <div class="titre">Backend joignable</div>
        <div class="valeur"><span class="pastille">{pastille}</span></div>
      </div>
      <div class="carte">
        <div class="titre">Uptime pod</div>
        <div class="valeur">{uptime} s</div>
      </div>
      <div class="carte">
        <div class="titre">URL backend</div>
        <div class="valeur" style="font-size:1rem;"><code>{backend}</code></div>
      </div>
    </div>
    <div class="pied">Rafraichissement automatique toutes les 3 s &middot;
      backend detail : <code>{detail}</code></div>
  </main>
</body>
</html>""".format(env=c["env"].upper(), version=c["version"], theme=c["theme"],
                  message=c["message"], replicas_info=c["replicas_info"],
                  pod=c["pod"], pastille=pastille, pastille_bg=pastille_bg,
                  uptime=c["uptime"], backend=c["backend_url"], detail=detail)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
