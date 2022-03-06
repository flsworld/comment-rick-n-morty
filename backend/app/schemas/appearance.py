from pydantic import BaseModel


class Appearance(BaseModel):
    character_id: int
    episode_id: int

    class Config:
        orm_mode = True


class AppearanceCreate(Appearance):
    pass
