import operator

from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models
from app.schemas.episode import EpisodeSearch

COMPARISON_OP = {"lte": operator.le, "gte": operator.ge}


def get_episode(db: Session, pk: int):
    return db.query(models.Episode).get(pk)


def get_multi_episodes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Episode).offset(skip).limit(limit).all()


def search_episodes(db: Session, obj_in: EpisodeSearch, skip: int = 0, limit: int = 10):
    criterion = []
    search_data = {k: v for (k, v) in obj_in.dict().items() if v}
    for key, value in search_data.items():
        l = key.split("__")
        if len(l) > 1:
            field, op = l
            if "air_date" in l:
                # le(a, b) is equivalent to a <= b
                criterion.append(COMPARISON_OP[op](models.Episode.air_date, value))
            elif "name" in l:
                criterion.append(models.Episode.name.ilike(f"%{value}%"))
        else:
            if "segment" in l:
                criterion.append(func.lower(models.Episode.segment) == value.lower())

    return db.query(models.Episode).filter(*criterion).offset(skip).limit(limit).all()
