"""Logique métier pure, sans dépendance à FastAPI.

Ces fonctions sont volontairement isolées pour être faciles à tester
unitairement (elles ne dépendent ni du réseau ni d'un état global).
"""

from __future__ import annotations

VALID_PRIORITIES = ("low", "medium", "high")


class ValidationError(ValueError):
    """Erreur levée lorsqu'une tâche est invalide."""


def normalize_priority(priority: str | None) -> str:
    """Normalise une priorité en une valeur canonique.

    - None ou chaîne vide -> "medium" (valeur par défaut)
    - insensible à la casse et aux espaces
    - accepte quelques synonymes courants
    """
    if priority is None:
        return "medium"

    cleaned = priority.strip().lower()
    if not cleaned:
        return "medium"

    synonyms = {
        "l": "low",
        "lo": "low",
        "basse": "low",
        "m": "medium",
        "med": "medium",
        "moyenne": "medium",
        "h": "high",
        "hi": "high",
        "haute": "high",
        "urgent": "high",
    }
    cleaned = synonyms.get(cleaned, cleaned)

    if cleaned not in VALID_PRIORITIES:
        raise ValidationError(
            f"Priorité invalide: {priority!r}. "
            f"Valeurs attendues: {', '.join(VALID_PRIORITIES)}."
        )
    return cleaned


def validate_title(title: str | None) -> str:
    """Valide et nettoie le titre d'une tâche."""
    if title is None:
        raise ValidationError("Le titre est obligatoire.")

    cleaned = title.strip()
    if not cleaned:
        raise ValidationError("Le titre ne peut pas être vide.")
    if len(cleaned) > 120:
        raise ValidationError("Le titre ne peut pas dépasser 120 caractères.")
    return cleaned


def priority_rank(priority: str) -> int:
    """Renvoie un rang numérique pour trier les tâches par priorité."""
    ranks = {"high": 0, "medium": 1, "low": 2}
    return ranks[normalize_priority(priority)]
