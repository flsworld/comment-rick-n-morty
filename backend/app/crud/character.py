from typing import Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Character


class CRUDCharacter(CRUDBase):
    def get_multi_characters(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        status: Optional[str] = None,
        species: Optional[str] = None,
        gender: Optional[str] = None,
    ):
        criterion = []
        if status:
            criterion.append(self.model.status == status)
        if species:
            criterion.append(self.model.species == species)
        if gender:
            criterion.append(self.model.gender == gender)

        return db.query(self.model).filter(*criterion).offset(skip).limit(limit).all()


character = CRUDCharacter(Character)
