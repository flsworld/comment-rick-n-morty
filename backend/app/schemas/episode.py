import re
from datetime import date
from typing import List, Any, Optional

from pydantic import BaseModel, validator
from pydantic.utils import GetterDict

from app.schemas.comment import CommentBase


class EpisodeCharacterGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {"id", "name"}:
            return getattr(self._obj.character, key)
        else:
            return super().get(key, default)


class EpisodeCharacterSchema(BaseModel):
    id: int
    name: str
    comments: Optional[list[CommentBase]] = None

    class Config:
        orm_mode = True
        getter_dict = EpisodeCharacterGetter


class EpisodeSchema(BaseModel):
    name: str
    air_date: date
    segment: str
    comments: list[CommentBase]
    characters: List[EpisodeCharacterSchema]

    class Config:
        orm_mode = True


class EpisodeCreate(EpisodeSchema):
    pass


class Episode(EpisodeSchema):
    id: int


class EpisodeSearch(BaseModel):
    air_date__lte: Optional[date] = None
    air_date__gte: Optional[date] = None
    segment: Optional[str] = None
    name__icontains: Optional[str] = None

    @validator("segment")
    def forbidden_segment_value(cls, v):
        if not v:
            return None
        match = re.match(r"[sS]0[1-4][eE][0-1]\d", v)
        if not match:
            raise ValueError("value not accepted")
        return v
