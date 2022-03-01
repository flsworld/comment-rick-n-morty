from typing import Optional

from pydantic import BaseModel


class Appearance(BaseModel):
    character_id: int
    episode_id: int
    comment_id: Optional[int] = None

    class Config:
        orm_mode = True


class AppearanceCreate(Appearance):
    pass


class AppearanceUpdate(Appearance):
    pass
