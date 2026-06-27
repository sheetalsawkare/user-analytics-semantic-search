from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.event import Event
from app.models.event_embedding import EventEmbedding
from app.services.embedding_service import embedding_service
from app.utils.similarity import cosine_similarity


class SearchService:

    @staticmethod
    async def search(
        db: AsyncSession,
        query: str
    ):

        query_embedding = (
            embedding_service.generate_embedding(
                query
            )
        )

        stmt = (
            select(
                Event,
                EventEmbedding
            )
            .join(
                EventEmbedding,
                Event.id == EventEmbedding.event_id
            )
        )

        result = await db.execute(stmt)

        rows = result.all()

        results = []

        for event, embedding_record in rows:

            score = cosine_similarity(
                query_embedding,
                embedding_record.embedding
            )

            if score >= 0.60:
                results.append(
                    {
                        "event_id": str(event.id),
                        "user_id": event.user_id,
                        "event": event.event,
                        "similarity_score": round(
                            float(score),
                            4
                        )
                    }
                )

        results.sort(
            key=lambda x: x["similarity_score"],
            reverse=True
        )

        results = results[:10]

        return {
            "query": query,
            "total_results": len(results),
            "results": results
        }
