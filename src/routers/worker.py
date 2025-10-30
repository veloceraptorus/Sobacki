from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models.worker import Worker
from src.schemes.worker import WorkerCreate, WorkerDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WorkerDB]:
    query_result = await db_session.execute(select(Worker))
    return query_result.scalars().all()


@router.post('/create')
async def create(body: WorkerCreate, db_session: AsyncSession = Depends(get_session)) -> WorkerDB:
    obj = Worker(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj
