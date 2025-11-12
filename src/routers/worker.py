from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.worker import Worker
from src.schemes.worker import WorkerCreate, WorkerDB
from src.services.worker import WorkerServise

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[WorkerDB]:
    return await WorkerServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> WorkerDB:
    return await WorkerServise.get(uid, db_session)


@router.post('/create')
async def create(body: WorkerCreate, db_session: AsyncSession = Depends(get_session)) -> WorkerDB:
    return await WorkerServise.create(body, db_session)


@router.put('/update')
async def update(body: WorkerDB, db_session: AsyncSession = Depends(get_session)):
    return await WorkerServise.update(body, db_session)
