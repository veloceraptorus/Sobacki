import uuid

from pydantic import UUID4
from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Subtask(Base):
    __tablename__ = 'subtasks'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_task: Mapped[UUID4] = mapped_column(UUID, ForeignKey("tasks.uid"), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=True)
    description: Mapped[str] = mapped_column(String)

    