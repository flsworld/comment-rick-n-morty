from typing import TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import Base

# Actual type substituted (explicitly or implicitly) for the type variable
# must be a subclass of the boundary type
SAModel = TypeVar("SAModel", bound=Base)
PydanticModel = TypeVar("PydanticModel", bound=BaseModel)


class CRUDBase:
    def __init__(self, model: SAModel):
        self.model = model

    def get(self, db: Session, pk: int):
        return db.query(self.model).get(pk)

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: PydanticModel):
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: SAModel, obj_in: PydanticModel):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, pk: int):
        db_obj = db.query(self.model).get(pk)
        db.delete(db_obj)
        db.commit()
        return db_obj
