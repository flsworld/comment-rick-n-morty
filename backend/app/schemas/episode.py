from typing import List

from pydantic import BaseModel


class EpisodeBase(BaseModel):
    name: str
    air_date: str
    segment: str
    characters: List[int]


class EpisodeCreate(EpisodeBase):
    pass


class Episode(EpisodeBase):
    id: int

    class Config:
        orm_mode = True
