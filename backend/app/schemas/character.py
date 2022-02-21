from typing import List

from pydantic import BaseModel


class CharacterBase(BaseModel):
    name: str
    status: str
    species: str
    type: str
    gender: str
    episode: List[int]


class CharacterCreate(CharacterBase):
    pass


class Character(CharacterBase):
    id: int

    class Config:
        orm_mode = True
