from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import models, schemas


def get_comment(db: Session, pk: int):
    return db.query(models.Comment).get(pk)


def get_multi_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def create_comment(db: Session, comment_in: schemas.CommentCreate):
    db_comment = models.Comment(**comment_in.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def update_comment(
        db: Session,
        *,
        db_obj: models.Comment,
        comment_in: schemas.CommentUpdate
):
    obj_data = jsonable_encoder(db_obj)
    update_data = comment_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def remove_comment(db: Session, *, pk: int):
    comment = db.query(models.Comment).get(pk)
    db.delete(comment)
    db.commit()
    return comment
