from app.core.config import settings


def test_create_comment(client):
    # Create character
    data = {"name": "Foo", "status": "unknown", "species": "unknown", "gender": "unknown"}
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


def test_read_characters_under_pagination(setup):
    pass


def test_read_characters_with_filters():
    pass


def test_read_episodes_with_search():
    pass

