from datetime import datetime, UTC
from sqlalchemy import Boolean, DateTime, func, text, UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from uuid import uuid4, UUID as UUID_type


class UUIDMixin:
    id: Mapped[UUID_type] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        init=False,
        nullable=False,
    )


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(),
        default=None,
        init=False,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(),
        default=None,
        init=False,
        onupdate=func.now(),
        nullable=False,
    )


class SoftDeleteMixin:
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, init=False, kw_only=True
    )
    is_deleted: Mapped[bool] = mapped_column(
        Boolean, init=False, default=False, kw_only=True
    )
