import uuid

from pydantic import UUID4
from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Permission(Base):
    __tablename__ = 'permissions'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_worker: Mapped[UUID4] = mapped_column(UUID, ForeignKey("workers.uid"), nullable=False)
    uid_proj: Mapped[UUID4] = mapped_column(UUID, ForeignKey("projects.uid"), nullable=False)
    permission_name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
