"""Tests d'API via TestClient (app/main.py)."""

import pytest
from fastapi.testclient import TestClient

from app.main import app, _reset_state

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_state():
    """Repart d'un état propre avant chaque test."""
    _reset_state()
    yield


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_liste_vide_au_depart():
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.json() == []


def test_creer_tache():
    resp = client.post("/tasks", json={"title": "Écrire des tests", "priority": "high"})
    assert resp.status_code == 201
    body = resp.json()
    assert body["id"] == 1
    assert body["title"] == "Écrire des tests"
    assert body["priority"] == "high"


def test_creer_tache_priorite_par_defaut():
    resp = client.post("/tasks", json={"title": "Sans priorité"})
    assert resp.status_code == 201
    assert resp.json()["priority"] == "medium"


def test_creer_tache_titre_vide_rejete():
    resp = client.post("/tasks", json={"title": "   "})
    assert resp.status_code == 422


def test_creer_tache_priorite_invalide_rejetee():
    resp = client.post("/tasks", json={"title": "Test", "priority": "énorme"})
    assert resp.status_code == 422


def test_get_tache_introuvable():
    resp = client.get("/tasks/999")
    assert resp.status_code == 404


def test_supprimer_tache():
    cree = client.post("/tasks", json={"title": "À supprimer"}).json()
    resp = client.delete(f"/tasks/{cree['id']}")
    assert resp.status_code == 204
    assert client.get(f"/tasks/{cree['id']}").status_code == 404


def test_supprimer_tache_introuvable():
    assert client.delete("/tasks/12345").status_code == 404


def test_liste_triee_par_priorite():
    client.post("/tasks", json={"title": "basse", "priority": "low"})
    client.post("/tasks", json={"title": "haute", "priority": "high"})
    client.post("/tasks", json={"title": "moyenne", "priority": "medium"})
    priorites = [t["priority"] for t in client.get("/tasks").json()]
    assert priorites == ["high", "medium", "low"]
