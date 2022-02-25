from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.session import Base


class CharacterEpisode(Base):
    __tablename__ = "character_episode"

    character_id = Column(Integer, ForeignKey("character.id"), primary_key=True)
    episode_id = Column(Integer, ForeignKey("episode.id"), primary_key=True)
    comment_id = Column(Integer, ForeignKey("comment.id"))

    comment = relationship("Comment", backref="association_recs")
    # character = relationship("Character", backref="association_recs")

    # character = relationship("Character", back_populates="episodes")
    # episode = relationship("Episode", back_populates="characters")

    # # proxies
    # char_episodes = association_proxy(target_collection="character", attr="episodes")
    # epi_characters = association_proxy(target_collection="episode", attr="characters")
