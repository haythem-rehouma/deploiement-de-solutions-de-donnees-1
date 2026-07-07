"""Tests unitaires de la logique métier pure (app/logic.py)."""

import pytest

from app.logic import (
    ValidationError,
    normalize_priority,
    priority_rank,
    validate_title,
)


@pytest.mark.parametrize(
    "entree,attendu",
    [
        (None, "medium"),
        ("", "medium"),
        ("   ", "medium"),
        ("HIGH", "high"),
        ("  Low ", "low"),
        ("urgent", "high"),
        ("moyenne", "medium"),
    ],
)
def test_normalize_priority_valide(entree, attendu):
    assert normalize_priority(entree) == attendu


def test_normalize_priority_invalide():
    with pytest.raises(ValidationError):
        normalize_priority("super-urgent")


def test_validate_title_nettoie_les_espaces():
    assert validate_title("  Acheter du pain  ") == "Acheter du pain"


@pytest.mark.parametrize("mauvais_titre", [None, "", "   "])
def test_validate_title_vide(mauvais_titre):
    with pytest.raises(ValidationError):
        validate_title(mauvais_titre)


def test_validate_title_trop_long():
    with pytest.raises(ValidationError):
        validate_title("x" * 121)


def test_priority_rank_ordre():
    assert priority_rank("high") < priority_rank("medium") < priority_rank("low")
