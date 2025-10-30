from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models.task import Task
from src.schemes.tasks import TasksCreate, TasksDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[TasksDB]:
    query_result = await db_session.execute(select(Task))
    return query_result.scalars().all()


@router.post('/create')
async def create(body: TasksCreate, db_session: AsyncSession = Depends(get_session)) -> TasksDB:
    obj = Task(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj
