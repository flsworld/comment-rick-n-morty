from sqlalchemy.orm import Session

from app import models


def get_multi_characters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Character).offset(skip).limit(limit).all()


def get_multi_episodes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Episode).offset(skip).limit(limit).all()


def remove(self, db: Session, *, id: int):
    obj = db.query(self.model).get(id)
    db.delete(obj)
    db.commit()
    return obj
