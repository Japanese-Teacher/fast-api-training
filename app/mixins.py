from datetime import datetime

from sqlalchemy import text, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        nullable=False,
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("now()"),
        onupdate=text("now()"),
        nullable=False,
    )


class DeletedAtMixin:
    deleted_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True),)
