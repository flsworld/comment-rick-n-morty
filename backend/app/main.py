from fastapi import FastAPI

from app.core.config import settings


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)
    return app


app = get_application()


@app.get("/")
def read_root():
    return {"Hello": "World"}
