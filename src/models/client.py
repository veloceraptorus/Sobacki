import uuid
from sqlalchemy import String, Integer, UUID
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import UUID4

from src.db.session import Base


class Client(Base):
    __tablename__ = 'clients'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String, nullable=False)
    telephone_number: Mapped[str] = mapped_column(String, nullable=False)
