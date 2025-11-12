from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.schemes.tasks import TasksCreate, TasksDB
from src.services.tasks import TaskServise

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[TasksDB]:
    return await TaskServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> TasksDB:
    return await TaskServise.get(uid, db_session)


@router.post('/create')
async def create(body: TasksCreate, db_session: AsyncSession = Depends(get_session)) -> TasksDB:
    return await TaskServise.create(body, db_session)


@router.put('/update')
async def update(body: TasksDB, db_session: AsyncSession = Depends(get_session)):
    return await TaskServise.update(body, db_session)
