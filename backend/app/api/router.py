from fastapi import APIRouter

from app.api.endpoints.characters import router as characters_router
from app.api.endpoints.episodes import router as episodes_router

api_router = APIRouter()
api_router.include_router(characters_router, prefix="/characters", tags=["characters"])
api_router.include_router(episodes_router, prefix="/episodes", tags=["episodes"])
