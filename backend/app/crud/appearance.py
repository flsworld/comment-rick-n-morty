from app.crud.base import CRUDBase
from app.models import CharacterEpisode


class Appearance(CRUDBase):
    pass


appearance = Appearance(CharacterEpisode)
