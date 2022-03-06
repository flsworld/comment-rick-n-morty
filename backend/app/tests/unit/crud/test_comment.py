from app import crud


def test_get_comment(db, setup):
    comment = crud.comment.get(db, pk=4)

    assert comment.text == "Colossal"
    assert comment.episode_id == 2
    assert comment.character is None
