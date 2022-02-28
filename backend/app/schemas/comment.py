from typing import Optional

from pydantic import BaseModel


class CommentSchema(BaseModel):
    text: str
    character_id: Optional[int] = None
    episode_id: Optional[int] = None


class CommentCreate(CommentSchema):
    user_id: int


class CommentUpdate(CommentSchema):
    pass


class Comment(CommentSchema):
    id: int
    user_id: int

    class Config:
        orm_mode = True
