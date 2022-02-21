from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

appearance_association = Table(
    "appearance",
    Base.metadata,
    Column("character_id", Integer(), ForeignKey("character.id"), primary_key=True),
    Column("episode_id", Integer(), ForeignKey("episode.id"), primary_key=True),
)


class Character(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    status = Column(String)
    species = Column(String)
    type = Column(String)
    gender = Column(String)

    episodes = relationship(
        "Episode", secondary=appearance_association, backref="characters"
    )
