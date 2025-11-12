from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.schemes.worker_task import WorkerTaskCreate, WorkerTaskDB
from src.services.worker_task import WorkerServise

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WorkerTaskDB]:
    return await WorkerServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> WorkerTaskDB:
    return await WorkerServise.get(uid, db_session)


@router.post('/create')
async def create(body: WorkerTaskCreate, db_session: AsyncSession = Depends(get_session)) -> WorkerTaskDB:
    return await WorkerServise.create(body, db_session)


@router.put('/update')
async def update(body: WorkerTaskDB, db_session: AsyncSession = Depends(get_session)):
    return await WorkerServise.update(body, db_session)
