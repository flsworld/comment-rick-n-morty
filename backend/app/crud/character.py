from sqlalchemy.orm import Session

from app import models


def get_multi_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Character).offset(skip).limit(limit).all()
