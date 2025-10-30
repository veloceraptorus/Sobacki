import uuid

from pydantic import UUID4
from sqlalchemy import UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.db import Base


class WorkerTask(Base):
    __tablename__ = 'workers_tasks'

    uid: Mapped[UUID4] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    uid_task: Mapped[UUID4] = mapped_column(UUID, ForeignKey("tasks.uid"), nullable=False)
    uid_worker: Mapped[UUID4] = mapped_column(UUID, ForeignKey("workers.uid"), nullable=False)
