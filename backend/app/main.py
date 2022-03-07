from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

description = """
Comment R&M API helps you do awesome stuff 🚀

## Characters

Characters from the animated series

## Episodes

Episodes from the animated series

## Appearances

An appearance represents a character in an episode

## Comments

Comment made by a user either on
* character
* episode
* appearance

## User

(_not implemented_)
"""


def get_application():
    app = FastAPI(
        title=settings.PROJECT_NAME, version=settings.VERSION, description=description
    )
    return app


app = get_application()
app.include_router(api_router, prefix=settings.API_PREFIX)
