from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.worker import Worker
from src.schemes.worker import WorkerCreate, WorkerDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WorkerDB]:
    query_result = await db_session.execute(select(Worker))
    return query_result.scalars().all()


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> WorkerDB:
    return (await db_session.execute(select(Worker).where(Worker.uid == uid))).scalar_one_or_none()


@router.post('/create')
async def create(body: WorkerCreate, db_session: AsyncSession = Depends(get_session)) -> WorkerDB:
    obj = Worker(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj


@router.put('/update')
async def update(body: WorkerDB, db_session: AsyncSession = Depends(get_session)):
    query = await db_session.execute(select(Worker).where(Worker.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        await db_session.refresh(query)
    return query
