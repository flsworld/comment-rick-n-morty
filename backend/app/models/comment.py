from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    episode_id = Column(Integer, ForeignKey("episode.id"))
    appearance_id = Column(Integer, ForeignKey("character_episode.id"))

    user = relationship("User", back_populates="comments")
    character = relationship("Character", back_populates="comments")
    episode = relationship("Episode", back_populates="comments")
    appearance = relationship("CharacterEpisode", back_populates="comments")
