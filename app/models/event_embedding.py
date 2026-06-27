from uuid import uuid4
from datetime import datetime, UTC

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class EventEmbedding(Base):
    __tablename__ = "event_embeddings"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    event_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("events.id", ondelete="CASCADE"),
        unique=True
    )

    embedding: Mapped[list] = mapped_column(
        JSONB,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    event = relationship(
        "Event",
        back_populates="embedding"
    )


print("EventEmbedding model loaded")