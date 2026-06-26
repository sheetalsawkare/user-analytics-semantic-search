from uuid import uuid4
from datetime import datetime, UTC

from sqlalchemy import String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[str] = mapped_column(
        String,
        index=True,
        nullable=False
    )

    event: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    event_metadata: Mapped[dict] = mapped_column(
        JSONB,
        nullable=True
    )

    # timestamp: Mapped[datetime] = mapped_column(
    #     DateTime,
    #     nullable=False
    # )

    # created_at: Mapped[datetime] = mapped_column(
    #     DateTime,
    #     default=datetime.utcnow
    # )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    embedding = relationship(
        "EventEmbedding",
        back_populates="event",
        uselist=False,
        cascade="all, delete-orphan"
    )