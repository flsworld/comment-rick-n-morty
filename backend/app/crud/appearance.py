from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import CharacterEpisode


class Appearance(CRUDBase):
    def get_from_assoc(self, db: Session, character_id: int, episode_id: int):
        return (
            db.query(self.model)
            .filter(
                self.model.character_id == character_id,
                self.model.episode_id == episode_id,
            )
            .one_or_none()
        )


appearance = Appearance(CharacterEpisode)
