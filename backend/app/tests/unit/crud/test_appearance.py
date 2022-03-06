from app import crud
from app.schemas.appearance import AppearanceUpdate


def test_get_appearance(db, setup):
    assert crud.appearance.get_from_assoc(db, character_id=2, episode_id=1)
    assert not crud.appearance.get(db, pk=3)


def test_update_appearance(db, setup):
    db_obj = crud.appearance.get(db, 1)  # comment_id: null
    obj_in = AppearanceUpdate(comment_id=2)

    appearance = crud.appearance.update(db, db_obj, obj_in)

    assert appearance.comment_id == 2
