from datetime import datetime

from app import crud
from app.schemas import EpisodeCreate
from app.tests.utils import random_segment


def test_get_episode(db, fake):
    dt = datetime.strptime("2022-03-04", "%Y-%m-%d")
    ep_in = EpisodeCreate(
        name=fake.bs(), air_date="2022-03-04", segment=random_segment()
    )
    ep = crud.episode.create(db, ep_in)

    assert crud.episode.get(db, ep.id)


# def test_get_multi_character(db, fake):
#     char_in = CharacterCreate(
#         name=fake.bs(), status="Alive", species="Human", type="Volunteer", gender="Male"
#     )
#     crud.character.create(db, char_in)
#     char_in = CharacterCreate(
#         name=fake.bs(), status="Alive", species="Human", type="Volunteer", gender="Male"
#     )
#     crud.character.create(db, char_in)
#
#     assert len(crud.character.get_multi_characters(db)) == 2
#
#
# def test_get_multi_character_with_filters(db, fake):
#     char_in = CharacterCreate(
#         name=fake.name(), status="Alive", species="Human", type="Volunteer", gender="Male"
#     )
#     crud.character.create(db, char_in)
#     char_in = CharacterCreate(
#         name=fake.name(), status="Alive", species="Poopybutthole", type="Lazy", gender="Female"
#     )
#     crud.character.create(db, char_in)
#
#     assert len(crud.character.get_multi_characters(db, status="Alive")) == 2
#     assert len(crud.character.get_multi_characters(db, species="Poopybutthole")) == 1
#     assert len(crud.character.get_multi_characters(db, gender="Female")) == 1
