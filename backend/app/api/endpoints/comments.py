from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.comment import Comment, CommentUpdate, CommentCreate

router = APIRouter()


@router.get("/", response_model=list[Comment])
def read_comments(db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100):
    comments = crud.get_multi_comments(db, skip=skip, limit=limit)
    return comments


@router.post("/", response_model=Comment)
def create_comment(
    *,
    db: Session = Depends(deps.get_db),
    comment_in: CommentCreate,
    # current_user: models.User
):
    comment = crud.create_comment(db, comment_in=comment_in)
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
    comment = crud.get_comment(db, pk=comment_id)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found",
        )
    comment = crud.update_comment(db, db_obj=comment, comment_in=comment_in)
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
    comment = crud.get_comment(db, pk=comment_id)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment not found",
        )
    comment = crud.remove_comment(db, pk=comment_id)
    return comment
