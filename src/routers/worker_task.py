from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models.worker_task import WorkerTask
from src.schemes.worker_task import WorkerTaskCreate, WorkerTaskDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WorkerTaskDB]:
    query_result = await db_session.execute(select(WorkerTask))
    return query_result.scalars().all()


@router.post('/create')
async def create(body: WorkerTaskCreate, db_session: AsyncSession = Depends(get_session)) -> WorkerTaskDB:
    obj = WorkerTask(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj
