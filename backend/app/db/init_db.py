import json
import logging
import os

from sqlalchemy.orm import Session

from app import models
from app.core.config import settings

logger = logging.getLogger(__name__)


def init_db(db: Session) -> None:
    path = settings.FIXTURES_PATH
    for filename in os.listdir(path):
        logger.info(filename)
        with open(os.path.join(path, filename), "r") as f:  # open in readonly mode
            fixtures = json.load(f)
            for f in fixtures:
                if "character" in filename:
                    db_obj = models.Character(
                        id=f.get("id"),
                        name=f.get("name"),
                        status=f.get("status"),
                        species=f.get("species"),
                        type=f.get("type"),
                        gender=f.get("gender"),
                    )
                    values = [(f.get("id"), eid) for eid in f.get("episode")]
                    db.execute(models.appearance_association.insert().values(values))
                elif "episode" in filename:
                    db_obj = models.Episode(
                        id=f.get("id"),
                        name=f.get("name"),
                        air_date=f.get("air_date"),
                        segment=f.get("episode"),
                    )
                db.add(db_obj)
                db.commit()
