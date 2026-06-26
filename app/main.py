import app.models
from fastapi import FastAPI

from app.api.track import router as track_router
from app.api.analytics import router as analytics_router
from app.api.search import router as search_router

app = FastAPI(
    title="User Analytics API"
)

app.include_router(track_router)
app.include_router(analytics_router)
app.include_router(search_router)
