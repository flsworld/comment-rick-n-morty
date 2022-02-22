from typing import List

from app.schemas.base import EpisodeBase, CharacterBase


class EpisodeSchema(EpisodeBase):
    characters: List[CharacterBase]


class EpisodeCreate(EpisodeSchema):
    pass


class Episode(EpisodeSchema):
    id: int
