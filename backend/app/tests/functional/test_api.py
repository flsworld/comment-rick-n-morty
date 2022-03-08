import urllib

import pytest

from app.core.config import settings
from app.schemas.character import CHOICES as CHARACTER_CHOICES


def test_create_comment(client):
    # Create character
    data = {
        "name": "Foo",
        "status": "unknown",
        "species": "unknown",
        "gender": "unknown",
    }
    response = client.post(f"{settings.API_PREFIX}/characters/", json=data)
    content = response.json()
    character_id = content["id"]
    assert response.status_code == 200
    # Create episode
    data = {"name": "Fighters", "air_date": "2022-01-01", "segment": "s04e19"}
    response = client.post(f"{settings.API_PREFIX}/episodes/", json=data)
    content = response.json()
    episode_id = content["id"]
    assert response.status_code == 200
    # Create appearance
    data = {"character_id": character_id, "episode_id": episode_id}
    response = client.post(f"{settings.API_PREFIX}/appearances/", json=data)
    assert response.status_code == 200
    # Create comment for an appearance (character in an episode)
    data = {"appearance_id": 1, "text": "RIP Nirvana"}
    response = client.post(f"{settings.API_PREFIX}/comments/", json=data)
    assert response.status_code == 200
    content = response.json()
    assert content["text"] == data["text"]
    assert "id" in content


def test_retrieve_comment_from_character_and_episode(client, setup):
    response = client.get(f"{settings.API_PREFIX}/comments/?character_id=1&episode_id=1")
    content = response.json()
    assert all(c["id"] for c in content)


def test_read_characters_under_pagination(client, setup):
    response = client.get(f"{settings.API_PREFIX}/characters?skip=1&limit=2")
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2
    assert content[0]["id"] == 2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"status": "Dead"}, 1),
        ({"species": "unknown"}, 1),
        ({"gender": "Female"}, 2),
        ({"status": "Alive", "gender": "Male"}, 3),
        ({"status": "Alive", "species": "Human", "gender": "Male"}, 2),
    ],
)
def test_read_characters_with_filters(client, setup, test_input, expected):
    params = urllib.parse.urlencode(test_input)
    response = client.get(f"{settings.API_PREFIX}/characters?{params}")
    assert response.status_code == 200
    content = response.json()
    assert len(content) == expected


@pytest.mark.parametrize(
    "field,value,values_set",
    [
        ("status", "dead", CHARACTER_CHOICES["status"]),
        ("species", "alien", CHARACTER_CHOICES["species"]),
        ("gender", "genderless", CHARACTER_CHOICES["gender"]),
    ],
)
def test_read_characters_with_wrong_filters(client, field, value, values_set):
    params = urllib.parse.urlencode({field: value})
    response = client.get(f"{settings.API_PREFIX}/characters?{params}")
    assert response.status_code == 422
    content = response.json()
    assert content["detail"] == [
        {
            "loc": ["query", field],
            "msg": f"value must be in {values_set}",
            "type": "value_error",
        }
    ]


def test_read_episodes_with_search(client, setup):
    data = {
        "air_date__gte": "2022-03-01",
        "air_date__lte": "2022-07-01",
        "segment": None,
        "name__icontains": "a",
    }
    response = client.post(f"{settings.API_PREFIX}/episodes/search", json=data)
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 4
