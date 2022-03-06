import pytest

from app import crud
from app.schemas import CharacterCreate


def test_get_character(db, fake):
    char_in = CharacterCreate(
        name=fake.name(), status="Alive", species="Human", type="Volunteer", gender="Male"
    )
    char = crud.character.create(db, char_in)

    assert crud.character.get(db, char.id)


def test_get_multi_character(db, fake):
    char_in = CharacterCreate(
        name=fake.name(), status="Alive", species="Human", type="Volunteer", gender="Male"
    )
    crud.character.create(db, char_in)
    char_in = CharacterCreate(
        name=fake.name(), status="Alive", species="Human", type="Volunteer", gender="Male"
    )
    crud.character.create(db, char_in)

    assert len(crud.character.get_multi_characters(db)) == 2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"status": "Alive"}, 2),
        ({"species": "Poopybutthole"}, 1),
        ({"gender": "Female"}, 1),
     ],
)
def test_get_multi_character_with_filters(db, setup, test_input, expected):
    assert len(crud.character.get_multi_characters(db, **test_input)) == expected
