from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=list[schemas.Comment])
def read_comments(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    comments = crud.get_multi_comments(db, skip=skip, limit=limit)
    return comments


@router.post("/", response_model=schemas.Comment)
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_in: schemas.CommentCreate,
    # current_user: models.User
):
    comments = crud.create_comment(db, comment_in=comment_in)
    return comments
