from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.task import Task
from src.schemes.tasks import TasksCreate, TasksDB

# from src.db import get_session


class TaskServise:
    @staticmethod
    async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[TasksDB]:
        query_result = await db_session.execute(select(Task))
        return query_result.scalars().all()

    @staticmethod
    async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> TasksDB:
        query = select(Task).where(Task.uid == uid)
        query_obj = await db_session.execute(query)
        query_obj = query_obj.scalar()
        return query_obj

    @staticmethod
    async def create(body: TasksCreate, db_session: AsyncSession = Depends(get_session)) -> TasksDB:
        obj = Task(**body.model_dump(exclude_unset=True))
        db_session.add(obj)
        await db_session.commit()
        await db_session.refresh(obj)
        return obj

    @staticmethod
    async def update(body: TasksDB, db_session: AsyncSession = Depends(get_session)):
        query = await db_session.execute(select(Task).where(Task.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query
