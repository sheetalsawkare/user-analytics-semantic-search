from sqlalchemy.ext.asyncio import AsyncSession
from app.models.event_embedding import EventEmbedding

class EventEmbeddingService:

    @staticmethod
    async def create_embedding(
        db: AsyncSession,
        event_id,
        embedding: list[float]
    ):

        record = EventEmbedding(
            event_id=event_id,
            embedding=embedding
        )

        try:
            db.add(record)
            await db.commit()
            await db.refresh(record)
            return record
        except Exception:
            await db.rollback()
            raise
        