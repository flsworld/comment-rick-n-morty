from app.crud.base import CRUDBase
from app.models import Comment


class CRUDComment(CRUDBase):
    pass


comment = CRUDComment(Comment)
