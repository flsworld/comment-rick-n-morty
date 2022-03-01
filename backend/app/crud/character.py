from typing import Optional

from sqlalchemy.orm import Session

from app import models


def get_character(db: Session, pk: int):
    return db.query(models.Character).get(pk)


def get_multi_characters(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    species: Optional[str] = None,
    gender: Optional[str] = None,
):
    criterion = []
    if status:
        criterion.append(models.Character.status == status)
    if species:
        criterion.append(models.Character.species == species)
    if gender:
        criterion.append(models.Character.gender == gender)

    return (
        db.query(models.Character)
        .filter(*criterion)
        .offset(skip)
        .limit(limit)
        .all()
    )
