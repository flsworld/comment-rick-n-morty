from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    user_id: Optional[int] = None  # default as None as any user concept was introduced
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
