from app.schemas.base import CharacterBase, EpisodeBase


class CharacterSchema(CharacterBase):
    episodes: list[EpisodeBase]
    # episodes: list[int] = Field(alias="char_episodes")
    #
    # class Config:
    #     allow_population_by_field_name = True


class CharacterCreate(CharacterSchema):
    pass


class Character(CharacterSchema):
    id: int

    class Config:
        orm_mode = True
