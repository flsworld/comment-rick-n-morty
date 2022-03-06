from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.appearance import Appearance, AppearanceCreate, AppearanceUpdate

router = APIRouter()


@router.get("/", response_model=Appearance)
def get_appearance(*, db: Session = Depends(deps.get_db), character_id: int, episode_id: int):
    appearance = crud.appearance.get_from_assoc(db, character_id, episode_id)
    if not appearance:
        raise HTTPException(
            status_code=404,
            detail="Appearance not found",
        )
    return appearance


@router.post("/", response_model=Appearance)
def create_appearance(*, db: Session = Depends(deps.get_db), obj_in: AppearanceCreate):
    appearance = crud.appearance.create(db, obj_in=obj_in)
    return appearance


@router.put("/{id}", response_model=Appearance)
def update_appearance(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    obj_in: AppearanceUpdate,
):
    """
    Update an appearance.
    """
    appearance = crud.appearance.get(db, pk=id)
    if not appearance:
        raise HTTPException(
            status_code=404,
            detail="Appearance not found",
        )
    appearance = crud.appearance.update(db, db_obj=appearance, obj_in=obj_in)
    return appearance


@router.delete("/{id}", response_model=Appearance)
def delete_appearance(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
):
    """
    Delete an appearance.
    """
    appearance = crud.appearance.get(db, pk=id)
    if not appearance:
        raise HTTPException(
            status_code=404,
            detail="Appearance not found",
        )
    appearance = crud.appearance.remove(db, pk=id)
    return appearance
