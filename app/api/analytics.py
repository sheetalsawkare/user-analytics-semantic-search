from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.analytics import AnalyticsResponse
from app.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="",
    tags=["Analytics"]
)

@router.get(
    "/analytics",
    response_model=AnalyticsResponse
)
async def get_analytics(
        event: str | None = None,
        from_date: datetime | None = None,
        to_date: datetime | None = None,
        db: AsyncSession = Depends(get_db)
    ):

    return await AnalyticsService.get_analytics(
        db=db,
        event=event,
        from_date=from_date,
        to_date=to_date
    )