from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status as sc
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps

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


def fire_error_msg(field: str, values_set: set):
    raise HTTPException(
        status_code=sc.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=[
            {
                "loc": ["query", field],
                "msg": f"value must be in {values_set}",
                "type": "value_error",
            }
        ],
    )


@router.get("/{character_id}", response_model=schemas.Character)
def read_character(*, db: Session = Depends(deps.get_db), character_id: int):
    character = crud.get_character(db, character_id)
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
    characters = crud.get_multi_characters(db, skip=skip, limit=limit, status=status, species=species, gender=gender)
    return characters


"""
queryset = Purchase.objects.all()
username = self.request.query_params.get('username')
if username is not None:
    queryset = queryset.filter(purchaser__username=username)
return queryset
"""
