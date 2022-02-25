from pydantic import BaseModel


class CommentSchema(BaseModel):
    text: str
    user_id: int


class CommentCreate(CommentSchema):
    pass


class Comment(CommentSchema):
    id: int

    class Config:
        orm_mode = True
