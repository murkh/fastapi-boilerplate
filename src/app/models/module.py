from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from ..core.db.database import Base
from ..core.db.models import UUIDMixin, TimestampMixin, SoftDeleteMixin


class Module(Base, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "modules"

    module_name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true", nullable=False
    )

    def __repr__(self):
        return f"<Module(id={self.id}, module_name={self.module_name}, is_active={self.is_active})>"
