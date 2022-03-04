from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.comment import Comment, CommentUpdate, CommentCreate

router = APIRouter()


@router.get("/", response_model=list[Comment])
def read_comments(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    comments = crud.comment.get_multi(db, skip=skip, limit=limit)
    return comments


@router.post("/", response_model=Comment)
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_in: CommentCreate,
    # current_user: models.User
):
    comment = crud.comment.create(db, comment_in=comment_in)
    return comment


@router.put("/{comment_id}", response_model=Comment)
def update_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_id: int,
    comment_in: CommentUpdate,
):
    """
    Update a comment.
    """
    comment = crud.comment.get(db, pk=comment_id)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found",
        )
    comment = crud.comment.update(db, db_obj=comment, comment_in=comment_in)
    return comment


@router.delete("/{comment_id}", response_model=Comment)
def delete_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_id: int,
):
    """
    Delete a comment.
    """
    comment = crud.comment.get(db, pk=comment_id)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found",
        )
    comment = crud.comment.remove(db, pk=comment_id)
    return comment
