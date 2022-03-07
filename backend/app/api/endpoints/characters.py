from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps
from app.api.errors import fire_error_msg
from app.schemas import CharacterCreate
from app.schemas.character import CHOICES as CHARACTER_CHOICES

router = APIRouter()


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
    if status and status not in CHARACTER_CHOICES["status"]:
        fire_error_msg("status", CHARACTER_CHOICES["status"])
    if species and species not in CHARACTER_CHOICES["species"]:
        fire_error_msg("species", CHARACTER_CHOICES["species"])
    if gender and gender not in CHARACTER_CHOICES["gender"]:
        fire_error_msg("gender", CHARACTER_CHOICES["gender"])
    characters = crud.character.get_multi_characters(db, skip=skip, limit=limit, status=status, species=species, gender=gender)
    return characters


@router.post("/", response_model=schemas.Character)
def create_character(
    *,
    db: Session = Depends(deps.get_db),
    char_in: CharacterCreate,
):
    character = crud.character.create(db, obj_in=char_in)
    return character
