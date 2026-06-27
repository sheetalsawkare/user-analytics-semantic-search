from datetime import datetime
from typing import Any
from pydantic import BaseModel, Field

class EventTrackRequest(BaseModel):
    userId: str = Field(..., min_length=1)

    event: str = Field(
        ...,
        min_length=3,
        max_length=500
    )

    event_metadata: dict[str, Any] | None = None

    timestamp: datetime | None = None


class EventTrackResponse(BaseModel):
    message: str
    event_id: str
