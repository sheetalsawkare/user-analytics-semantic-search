from pydantic import BaseModel


class UserEventCount(BaseModel):
    user_id: str
    event_count: int


class AnalyticsResponse(BaseModel):
    total_events: int
    events_per_user: dict[str, int]
    most_active_users: list[UserEventCount]