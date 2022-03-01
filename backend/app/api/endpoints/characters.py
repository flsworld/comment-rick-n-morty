from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps

router = APIRouter()


@router.get("/{character_id}", response_model=schemas.Character)
def read_character(*, db: Session = Depends(deps.get_db), character_id: int):
    character = crud.get_character(db, character_id)
    return character


@router.get("/", response_model=list[schemas.Character])
def read_characters(
    skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)
):
    characters = crud.get_multi_characters(db, skip=skip, limit=limit)
    return characters
