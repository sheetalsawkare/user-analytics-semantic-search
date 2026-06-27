from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.event import Event
from app.services.embedding_service import embedding_service
from app.services.event_embedding_service import EventEmbeddingService
    
class EventService:

    @staticmethod
    async def create_event(
        db: AsyncSession,
        user_id: str,
        event_text: str,
        event_metadata: dict | None,
        timestamp: datetime | None
    ) -> Event:

        event = Event(
            user_id=user_id,
            event=event_text,
            event_metadata=event_metadata,
            timestamp=timestamp or datetime.utcnow()
        )

        try:
            db.add(event)

            await db.commit()
            await db.refresh(event)

        except Exception:
            await db.rollback()
            raise

        embedding = embedding_service.generate_embedding(
            event.event
        )

        # Save embedding
        await EventEmbeddingService.create_embedding(
            db=db,
            event_id=event.id,
            embedding=embedding
        )

        return event
