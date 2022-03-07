from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from app.db.session import Base
from app.models import CharacterEpisode


class Episode(Base):
    __tablename__ = "episode"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(Date)
    segment = Column(String, unique=True)

    characters = relationship("CharacterEpisode", back_populates="episode")
    comments = relationship("Comment", back_populates="episode")

    association_ids = association_proxy(
        "characters",
        "character_id",
        creator=lambda cid: CharacterEpisode(character_id=cid),
    )
