from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    user_id: Optional[int] = None  # default as any CRUD user exists at the moment
    text: str

    class Config:
        orm_mode = True


class CommentSchema(CommentBase):
    character_id: Optional[int] = None
    episode_id: Optional[int] = None
    appearance_id: Optional[int] = None


class CommentCreate(CommentSchema):
    pass


class CommentUpdate(BaseModel):
    text: str


class Comment(CommentSchema):
    id: int
