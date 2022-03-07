import random

import pytest
from pydantic import ValidationError

from app.schemas.character import CHOICES as CHARACTER_CHOICES
from app.schemas.character import CharacterSchema


def test_status_validator():
    with pytest.raises(ValidationError):
        CharacterSchema(status="Biggs")


def test_species_validator():
    with pytest.raises(ValidationError):
        CharacterSchema(species="Wedge")


def test_gender_validator():
    with pytest.raises(ValidationError):
        CharacterSchema(species="Jesse")


def test_valid_character_pydantic_model():
    status = random.choice(list(CHARACTER_CHOICES["status"]))
    species = random.choice(list(CHARACTER_CHOICES["species"]))
    gender = random.choice(list(CHARACTER_CHOICES["gender"]))

    assert CharacterSchema(
        name="fake.name()", status=status, species=species, gender=gender
    )
