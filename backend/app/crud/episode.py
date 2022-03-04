import operator

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Episode
from app.schemas.episode import EpisodeSearch

COMPARISON_OP = {"lte": operator.le, "gte": operator.ge}


class CRUDEpisode(CRUDBase):

    def search(self, db: Session, obj_in: EpisodeSearch, skip: int = 0, limit: int = 10):
        criterion = []
        search_data = {k: v for (k, v) in obj_in.dict().items() if v}
        for key, value in search_data.items():
            lookups = key.split("__")
            if len(lookups) > 1:
                field, op = lookups
                if "air_date" in lookups:
                    # le(a, b) is equivalent to a <= b
                    criterion.append(COMPARISON_OP[op](self.model.air_date, value))
                elif "name" in lookups:
                    criterion.append(self.model.name.ilike(f"%{value}%"))
            else:
                if "segment" in lookups:
                    criterion.append(func.lower(self.model.segment) == value.lower())

        return db.query(self.model).filter(*criterion).offset(skip).limit(limit).all()


episode = CRUDEpisode(Episode)
