from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schemas.event import (
    EventTrackRequest,
    EventTrackResponse
)
from app.services.event_service import EventService


router = APIRouter(
    prefix="/track",
    tags=["Tracking"]
)


@router.post(
    "",
    response_model=EventTrackResponse
)
async def track_event(
    payload: EventTrackRequest,
    db: AsyncSession = Depends(get_db)
):

    event = await EventService.create_event(
        db=db,
        user_id=payload.userId,
        event_text=payload.event,
        event_metadata=payload.event_metadata,
        timestamp=payload.timestamp
    )

    return EventTrackResponse(
        message="event tracked successfully",
        event_id=str(event.id)
    )