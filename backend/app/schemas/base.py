from pydantic import BaseModel


class CharacterBase(BaseModel):
    name: str
    status: str
    species: str
    type: str
    gender: str

    class Config:
        orm_mode = True


class EpisodeBase(BaseModel):
    name: str
    air_date: str
    segment: str

    class Config:
        orm_mode = True
