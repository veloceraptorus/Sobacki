from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.worker_task import WorkerTask
from src.schemes.worker_task import WorkerTaskCreate, WorkerTaskDB

# from src.db import get_session


class WorkerServise:
    @staticmethod
    async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WorkerTaskDB]:
        query_result = await db_session.execute(select(WorkerTask))
        return query_result.scalars().all()

    @staticmethod
    async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> WorkerTaskDB:
        query = select(WorkerTask).where(WorkerTask.uid == uid)
        query_obj = await db_session.execute(query)
        query_obj = query_obj.scalar()
        return query_obj

    @staticmethod
    async def create(body: WorkerTaskCreate, db_session: AsyncSession = Depends(get_session)) -> WorkerTaskDB:
        obj = WorkerTask(**body.model_dump(exclude_unset=True))
        db_session.add(obj)
        await db_session.commit()
        await db_session.refresh(obj)
        return obj

    @staticmethod
    async def update(body: WorkerTaskDB, db_session: AsyncSession = Depends(get_session)):
        query = await db_session.execute(select(WorkerTask).where(WorkerTask.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query
