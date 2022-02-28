from sqlalchemy.orm import Session

from app import models, schemas


def get_multi_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def create_comment(db: Session, comment_in: schemas.CommentCreate):
    db_comment = models.Comment(**comment_in.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def remove(self, db: Session, *, id: int):
    obj = db.query(self.model).get(id)
    db.delete(obj)
    db.commit()
    return obj
