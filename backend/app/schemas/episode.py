from typing import List, Optional, Any

from pydantic import BaseModel
from pydantic.utils import GetterDict


class EpisodeCharacterGetter(GetterDict):
    def get(self, key: str, default: Any = None) -> Any:
        if key in {"id", "name"}:
            return getattr(self._obj.character, key)
        else:
            return super().get(key, default)


class EpisodeCharacterSchema(BaseModel):
    id: int
    name: str
    comment_id: Optional[int]

    class Config:
        orm_mode = True
        getter_dict = EpisodeCharacterGetter


class EpisodeSchema(BaseModel):
    name: str
    air_date: str
    segment: str
    characters: List[EpisodeCharacterSchema]

    class Config:
        orm_mode = True


class EpisodeCreate(EpisodeSchema):
    pass


class Episode(EpisodeSchema):
    id: int
