from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models import CharacterEpisode


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    status = Column(String)
    species = Column(String)
    type = Column(String)
    gender = Column(String)

    episodes = relationship("CharacterEpisode", back_populates="character")
    comments = relationship("Comment", back_populates="character")

    association_ids = association_proxy(
        "episodes",
        "episode_id",
        creator=lambda eid: CharacterEpisode(episode_id=eid),
    )
