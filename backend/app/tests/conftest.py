from datetime import datetime

import pytest
from starlette.testclient import TestClient

from app import crud
from app.api.deps import get_db
from app.db.session import Base
from app.main import app
from app.models import Episode, Character, CharacterEpisode, Comment
from app.schemas.appearance import AppearanceCreate
from app.schemas.comment import CommentCreate
from app.tests.database import TestingSessionLocal
from app.tests.database import engine as test_engine


@pytest.fixture()
def db():
    Base.metadata.create_all(bind=test_engine)
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        Base.metadata.drop_all(bind=test_engine)
        db.close()


def override_get_db():
    Base.metadata.create_all(bind=test_engine)
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        Base.metadata.drop_all(bind=test_engine)
        db.close()


@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def setup(db):
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
    data = {
        "name": "Costa del Sol",
        "air_date": datetime.strptime("2022-06-01", "%Y-%m-%d"),
        "segment": "s01e04",
    }
    ep_obj = Episode(**data)
    db.add(ep_obj)
    data = {
        "name": "Gold Saucer",
        "air_date": datetime.strptime("2022-07-01", "%Y-%m-%d"),
        "segment": "s01e05",
    }
    ep_obj = Episode(**data)
    db.add(ep_obj)

    # Characters
    data = {
        "name": "Cloud Strife",
        "status": "Alive",
        "species": "Human",
        "type": "Volunteer",
        "gender": "Male",
    }
    char_obj = Character(**data)
    db.add(char_obj)
    data = {
        "name": "Barret Wallace",
        "status": "Alive",
        "species": "Human",
        "type": "Grumpy",
        "gender": "Male",
    }
    char_obj = Character(**data)
    db.add(char_obj)
    data = {
        "name": "Tifa Lockhart",
        "status": "Alive",
        "species": "Human",
        "type": "Sexy",
        "gender": "Female",
    }
    char_obj = Character(**data)
    db.add(char_obj)
    data = {
        "name": "Aerith Gainsborough",
        "status": "Dead",
        "species": "Human",
        "type": "Inoffensive",
        "gender": "Female",
    }
    char_obj = Character(**data)
    db.add(char_obj)
    data = {
        "name": "Nanaki",
        "status": "Alive",
        "species": "unknown",
        "type": "Purr",
        "gender": "Male",
    }
    char_obj = Character(**data)
    db.add(char_obj)

    # Comments
    data = {"text": "Badass", "character_id": 1}
    com_obj = Comment(**data)
    db.add(com_obj)
    data = {"text": "Too long !", "episode_id": 1}
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
