import uuid

from pydantic import UUID4
from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class Worker(Base):
    __tablename__ = 'workers'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    telephone_number: Mapped[str] = mapped_column(String, nullable=False)
    colour: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
