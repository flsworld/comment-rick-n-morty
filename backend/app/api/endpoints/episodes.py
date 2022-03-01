from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps

router = APIRouter()


@router.get("/{episode_id}", response_model=schemas.Character)
def read_episode(*, db: Session = Depends(deps.get_db), episode_id: int):
    episode = crud.get_episode(db, episode_id)
    return episode


@router.get("/", response_model=list[schemas.Episode])
def read_episodes(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    episodes = crud.get_multi_episodes(db, skip=skip, limit=limit)
    return episodes
