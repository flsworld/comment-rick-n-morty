from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app import schemas
from app.api import deps
from app.schemas.episode import EpisodeSearch

router = APIRouter()


@router.get("/{episode_id}", response_model=schemas.Character)
def read_episode(*, db: Session = Depends(deps.get_db), episode_id: int):
    episode = crud.get_episode(db, episode_id)
    return episode


@router.get("/", response_model=list[schemas.Episode])
def read_episodes(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    episodes = crud.get_multi_episodes(db, skip=skip, limit=limit)
    return episodes


@router.post("/search", response_model=list[schemas.Episode])
def search_episodes(
    *,
    db: Session = Depends(deps.get_db),
    obj_in: EpisodeSearch,
    skip: int = 0,
    limit: int = 100
):
    episodes = crud.search_episodes(db, obj_in, skip=skip, limit=limit)
    return episodes
