from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps
from app.api.errors import fire_error_msg

router = APIRouter()


QP_VALUES = {
    "status": {"unknown", "Dead", "Alive"},
    "species": {
        "Alien",
        "Disease",
        "Poopybutthole",
        "Robot",
        "Cronenberg",
        "Humanoid",
        "Human",
        "Mythological Creature",
        "unknown",
        "Animal",
    },
    "gender": {"Male", "unknown", "Genderless", "Female"},
}


@router.get("/{character_id}", response_model=schemas.Character)
def read_character(*, db: Session = Depends(deps.get_db), character_id: int):
    character = crud.character.get(db, character_id)
    return character


@router.get("/", response_model=list[schemas.Character])
def read_characters(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    species: Optional[str] = None,
    gender: Optional[str] = None,
):
    if status and status not in QP_VALUES["status"]:
        fire_error_msg("status", QP_VALUES["status"])
    if species and species not in QP_VALUES["species"]:
        fire_error_msg("species", QP_VALUES["species"])
    if gender and gender not in QP_VALUES["gender"]:
        fire_error_msg("gender", QP_VALUES["gender"])
    characters = crud.character.get_multi(db, skip=skip, limit=limit, status=status, species=species, gender=gender)
    return characters
