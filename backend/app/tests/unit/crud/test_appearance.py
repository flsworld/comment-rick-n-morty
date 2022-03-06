from app import crud


def test_get_appearance(db, setup):
    assert crud.appearance.get_from_assoc(db, character_id=2, episode_id=1)
    assert not crud.appearance.get_from_assoc(db, character_id=5, episode_id=1)
    assert not crud.appearance.get(db, pk=3)


def test_delete_appearance(db, setup):
    appearance = crud.appearance.get_from_assoc(db, character_id=2, episode_id=1)
    crud.appearance.remove(db, appearance.id)

    assert not crud.appearance.get_from_assoc(db, character_id=2, episode_id=1)
