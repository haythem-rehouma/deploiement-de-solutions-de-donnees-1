"""API FastAPI : un mini gestionnaire de tâches en mémoire.

Sert de support à la démo CI/CD. Les données sont stockées en mémoire
(dictionnaire), ce qui suffit largement pour illustrer le pipeline.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

from . import __version__
from .logic import ValidationError, normalize_priority, priority_rank, validate_title

app = FastAPI(title="Task API - Démo CI/CD", version=__version__)

# Stockage en mémoire : { id: tâche }
_tasks: dict[int, dict] = {}
_next_id = 1


class TaskIn(BaseModel):
    title: str
    priority: str | None = None


class Task(BaseModel):
    id: int
    title: str
    priority: str


def _reset_state() -> None:
    """Réinitialise l'état (utile pour les tests)."""
    global _tasks, _next_id
    _tasks = {}
    _next_id = 1


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": __version__}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[dict]:
    return sorted(_tasks.values(), key=lambda t: priority_rank(t["priority"]))


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskIn) -> dict:
    global _next_id
    try:
        title = validate_title(payload.title)
        priority = normalize_priority(payload.priority)
    except ValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    task = {"id": _next_id, "title": title, "priority": priority}
    _tasks[_next_id] = task
    _next_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> dict:
    task = _tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tâche introuvable.")
    return task


@app.delete("/tasks/{task_id}", status_code=204, response_class=Response)
def delete_task(task_id: int) -> Response:
    if task_id not in _tasks:
        raise HTTPException(status_code=404, detail="Tâche introuvable.")
    del _tasks[task_id]
    return Response(status_code=204)
