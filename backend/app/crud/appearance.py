from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models
from app.schemas.appearance import AppearanceCreate, AppearanceUpdate


def get_appearance(db: Session, pk: int):
    return db.query(models.CharacterEpisode).get(pk)


def create_appearance(db: Session, obj_in: AppearanceCreate):
    db_obj = models.CharacterEpisode(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_appearance(
    db: Session, *, db_obj: models.CharacterEpisode, obj_in: AppearanceUpdate
):
    obj_data = jsonable_encoder(db_obj)
    update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def remove_appearance(db: Session, *, pk: int):
    db_obj = db.query(models.CharacterEpisode).get(pk)
    db.delete(db_obj)
    db.commit()
    return db_obj
