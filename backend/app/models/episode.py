from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base


class Episode(Base):
    __tablename__ = "episode"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(String)
    segment = Column(String, unique=True)

    characters = relationship("Character", secondary="character_episode", back_populates='episodes')
    # characters = relationship("CharacterEpisode", back_populates='episode')

    def __repr__(self):
        return 'Episode(%s)' % repr(self.name)
