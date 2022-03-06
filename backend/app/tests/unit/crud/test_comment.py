from app import crud
from app.schemas.comment import CommentUpdate


def test_get_comment(db, setup):
    comment = crud.comment.get(db, pk=4)

    assert comment.text == "Colossal"
    assert comment.episode_id == 2
    assert comment.character is None


def test_update_comment(db, setup):
    comment = crud.comment.get(db, pk=3)
    assert comment.text == "NSPP"
    assert comment.appearance_id == 1
    assert comment.character is None
    assert comment.episode is None

    text = "Mais tu n'es pas là. Et même si j'ai envie d'aller là-bas"
    # je dors plus la nuit
    com_in = CommentUpdate(text=text)
    comment = crud.comment.update(db, comment, com_in)

    assert comment.text == text


def test_delete_comment(db, setup):
    comment = crud.comment.get(db, pk=3)
    crud.comment.remove(db, comment.id)
    assert not crud.comment.get(db, pk=3)
