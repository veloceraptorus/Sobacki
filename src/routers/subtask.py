from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.schemes.subtask import SubtaskCreate, SubtaskDB
from src.services.subtask import SubtaskServise

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[SubtaskDB]:
    return await SubtaskServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> SubtaskDB:
    return await SubtaskServise.get(uid, db_session)


@router.post('/create')
async def create(body: SubtaskCreate, db_session: AsyncSession = Depends(get_session)) -> SubtaskDB:
        return await SubtaskServise.create(body, db_session)


@router.put('/update')
async def update(body: SubtaskDB, db_session: AsyncSession = Depends(get_session)):
        return await SubtaskServise.update(body, db_session)
