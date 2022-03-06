from datetime import datetime

import pytest

from app import crud
from app.models import Episode, Character, CharacterEpisode, Comment
from app.schemas.appearance import AppearanceCreate
from app.schemas.comment import CommentCreate


@pytest.fixture()
def setup(db, fake):
    # Episodes
    data = {
        "name": "Midgar",
        "air_date": datetime.strptime("2022-03-01", "%Y-%m-%d"),
        "segment": "s01e01",
    }
    ep_obj = Episode(**data)
    db.add(ep_obj)
    data = {
        "name": "Kalm",
        "air_date": datetime.strptime("2022-04-01", "%Y-%m-%d"),
        "segment": "s01e02",
    }
    ep_obj = Episode(**data)
    db.add(ep_obj)
    data = {
        "name": "Junon",
        "air_date": datetime.strptime("2022-05-01", "%Y-%m-%d"),
        "segment": "s01e03",
    }
    ep_obj = Episode(**data)
    db.add(ep_obj)

    # Characters
    data = {
        "name": fake.name(),
        "status": "Alive",
        "species": "Human",
        "type": "Volunteer",
        "gender": "Male",
    }
    char_obj = Character(**data)
    db.add(char_obj)
    data = {
        "name": fake.name(),
        "status": "Alive",
        "species": "Poopybutthole",
        "type": "Lazy",
        "gender": "Female",
    }
    char_obj = Character(**data)
    db.add(char_obj)

    # Comments
    data = {"text": "Nul", "character_id": 1}
    com_obj = Comment(**data)
    db.add(com_obj)
    data = {"text": "Super", "episode_id": 1}
    com_obj = Comment(**data)
    db.add(com_obj)
    data = {"text": "NSPP", "appearance_id": 1}
    com_obj = Comment(**data)
    db.add(com_obj)

    # Appearances
    data = {
        "episode_id": 1,
        "character_id": 1,
    }
    ap_obj = CharacterEpisode(**data)
    db.add(ap_obj)

    db.commit()

    # Use not tested pydantic models here, so it is tested somewhere also
    # Appearance id=2
    data = {
        "episode_id": 1,
        "character_id": 2,
    }
    obj_in = AppearanceCreate(**data)
    crud.appearance.create(db, obj_in)
    # Comment id=4
    com_in = CommentCreate(text="Colossal", episode_id=2)
    crud.comment.create(db, com_in)
