from typing import Any, Optional

from pydantic import BaseModel
from pydantic.utils import GetterDict

from app.schemas.comment import CommentBase


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
    type: str
    gender: str
    comments: Optional[list[CommentBase]] = None
    episodes: list[CharacterEpisodeSchema]

    class Config:
        orm_mode = True


class CharacterCreate(CharacterSchema):
    pass


class Character(CharacterSchema):
    id: int
