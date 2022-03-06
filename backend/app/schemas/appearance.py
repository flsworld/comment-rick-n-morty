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


class AppearanceUpdate(BaseModel):
    """
    Because of the unique constraint on ("character_id", "episode_id"), updates
    on `character_id` and `episode_id` is not allowed.
    Delete the link and create a new one.
    """
    comment_id: int
