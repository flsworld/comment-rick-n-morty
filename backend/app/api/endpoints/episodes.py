from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Episode])
def read_episodes(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    episodes = crud.get_multi_episodes(db, skip=skip, limit=limit)
    return episodes
