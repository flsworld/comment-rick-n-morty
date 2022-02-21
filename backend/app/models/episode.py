from sqlalchemy import Column, Integer, String

from app.db.session import Base


class Episode(Base):
    __tablename__ = "episode"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    air_date = Column(String)
    segment = Column(String, unique=True)
