from typing import List

from app.schemas.base import CharacterBase, EpisodeBase


class CharacterSchema(CharacterBase):
    episodes: List[EpisodeBase]


class CharacterCreate(CharacterSchema):
    pass


class Character(CharacterSchema):
    id: int
