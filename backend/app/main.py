from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    return app


app = get_application()
app.include_router(api_router, prefix=settings.API_PREFIX)
