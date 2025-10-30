import uuid

from pydantic import UUID4
from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Task(Base):
    __tablename__ = 'tasks'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_proj: Mapped[UUID4] = mapped_column(UUID, ForeignKey("projects.uid"), nullable=False)
    price: Mapped[str] = mapped_column(String, nullable=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String, nullable=False)
