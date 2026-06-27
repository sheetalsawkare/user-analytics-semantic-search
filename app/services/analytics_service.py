from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.event import Event

class AnalyticsService:

    @staticmethod
    async def get_analytics(
        db: AsyncSession,
        event: str | None = None,
        from_date=None,
        to_date=None
    ):

        filters = []

        if event:
            filters.append(
                Event.event.ilike(f"%{event}%")
            )

        if from_date:
            filters.append(
                Event.timestamp >= from_date
            )

        if to_date:
            filters.append(
                Event.timestamp <= to_date
            )

        # Total Events
        total_events_query = (
            select(func.count())
            .select_from(Event)
            .where(*filters)
        )

        total_events = await db.scalar(
            total_events_query
        )

        # Events Per User
        events_per_user_query = (
            select(
                Event.user_id,
                func.count(Event.id)
            )
            .where(*filters)
            .group_by(Event.user_id)
        )

        result = await db.execute(
            events_per_user_query
        )

        events_per_user = {
            row[0]: row[1]
            for row in result.all()
        }

        # Most Active Users
        most_active_users_query = (
            select(
                Event.user_id,
                func.count(Event.id).label("event_count")
            )
            .where(*filters)
            .group_by(Event.user_id)
            .order_by(
                func.count(Event.id).desc()
            )
            .limit(5)
        )

        result = await db.execute(
            most_active_users_query
        )

        most_active_users = [
            {
                "user_id": row.user_id,
                "event_count": row.event_count
            }
            for row in result.all()
        ]

        return {
            "total_events": total_events,
            "events_per_user": events_per_user,
            "most_active_users": most_active_users
        }
    