from typing import Any, Optional

from pydantic import BaseModel, validator
from pydantic.utils import GetterDict

from app.schemas.comment import CommentBase

CHOICES = {
    "status": {"unknown", "Dead", "Alive"},
    "species": {
        "Alien",
        "Disease",
        "Poopybutthole",
        "Robot",
        "Cronenberg",
        "Humanoid",
        "Human",
        "Mythological Creature",
        "unknown",
        "Animal",
    },
    "gender": {"Male", "unknown", "Genderless", "Female"},
}


class CharacterEpisodeGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {"id", "name", "air_date", "segment"}:
            return getattr(self._obj.episode, key)
        else:
            return super().get(key, default)


class CharacterEpisodeSchema(BaseModel):
    id: int
    name: str
    comments: Optional[list[CommentBase]] = None

    class Config:
        orm_mode = True
        getter_dict = CharacterEpisodeGetter


class CharacterSchema(BaseModel):
    name: str
    status: str
    species: str
    type: str = ""
    gender: str
    comments: list[CommentBase] = []
    episodes: list[CharacterEpisodeSchema] = []

    @validator("status")
    def valid_status_choice(cls, v):
        if v not in CHOICES["status"]:
            raise ValueError("value not accepted")
        return v

    @validator("species")
    def valid_species_choice(cls, v):
        if v not in CHOICES["species"]:
            raise ValueError("value not accepted")
        return v

    @validator("gender")
    def valid_gender_choice(cls, v):
        if v not in CHOICES["gender"]:
            raise ValueError("value not accepted")
        return v

    class Config:
        orm_mode = True


class CharacterCreate(CharacterSchema):
    pass


class Character(CharacterSchema):
    id: int
