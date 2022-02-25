from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str


class UserCreate(UserSchema):
    pass


class Character(UserSchema):
    id: int
    comments: list[int] = []

    class Config:
        orm_mode = True
