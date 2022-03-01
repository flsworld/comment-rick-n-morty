from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.appearance import Appearance, AppearanceCreate, AppearanceUpdate

router = APIRouter()


@router.post("/", response_model=Appearance)
def create_appearance(*, db: Session = Depends(deps.get_db), obj_in: AppearanceCreate):
    appearance = crud.create_appearance(db, obj_in=obj_in)
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
    appearance = crud.get_appearance(db, pk=id)
    if not appearance:
        raise HTTPException(
            status_code=404,
            detail="Appearance not found",
        )
    appearance = crud.update_appearance(db, db_obj=appearance, obj_in=obj_in)
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
    appearance = crud.get_appearance(db, pk=id)
    if not appearance:
        raise HTTPException(
            status_code=404,
            detail="Appearance not found",
        )
    appearance = crud.remove_appearance(db, pk=id)
    return appearance
