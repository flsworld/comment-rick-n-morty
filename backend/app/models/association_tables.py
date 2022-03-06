from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.session import Base


class CharacterEpisode(Base):
    __tablename__ = "character_episode"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    episode_id = Column(Integer, ForeignKey("episode.id"))

    comments = relationship("Comment", back_populates="appearance")
    character = relationship("Character", back_populates="episodes")
    episode = relationship("Episode", back_populates="characters")

    __table_args__ = (
        UniqueConstraint("character_id", "episode_id", name="_character_episode_uc"),
    )
