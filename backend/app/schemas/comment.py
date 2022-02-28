from typing import Optional

from pydantic import BaseModel


class CommentSchema(BaseModel):
    text: str
    user_id: int
    character_id: Optional[int] = None
    episode_id: Optional[int] = None


class CommentCreate(CommentSchema):
    pass


class Comment(CommentSchema):
    id: int

    class Config:
        orm_mode = True
