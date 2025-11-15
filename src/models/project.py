import uuid
from datetime import date

from pydantic import UUID4
from sqlalchemy import UUID, Date, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.db import Base


class Project(Base):
    __tablename__ = 'projects'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    create_date: Mapped[date] = mapped_column(Date, nullable=True)
    uid_creator: Mapped[UUID4] = mapped_column(UUID, ForeignKey("workers.uid"), default=None, nullable=True)
    uid_client: Mapped[UUID4] = mapped_column(UUID, ForeignKey("clients.uid"), default=None, nullable=True)
    initial_budget: Mapped[float] = mapped_column(Float, nullable=True)
    result_budget: Mapped[float] = mapped_column(Float, nullable=True)
    colour: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    deadline: Mapped[date] = mapped_column(Date, nullable=False)

    client = relationship("Client", backref="project")
