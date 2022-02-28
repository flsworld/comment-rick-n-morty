from sqlalchemy.orm import Session

from app import models


def get_multi_episodes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Episode).offset(skip).limit(limit).all()
