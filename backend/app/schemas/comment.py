from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    user_id: int
    text: str

    class Config:
        orm_mode = True


class CommentSchema(CommentBase):
    character_id: Optional[int] = None
    episode_id: Optional[int] = None


class CommentCreate(CommentSchema):
    pass


class CommentUpdate(CommentSchema):
    pass


class Comment(CommentSchema):
    id: int
