from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models.subtask import Subtask
from src.schemes.subtask import SubtaskCreate, SubtaskDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[SubtaskDB]:
    query_result = await db_session.execute(select(Subtask))
    return query_result.scalars().all()


@router.post('/create')
async def create(body: SubtaskCreate, db_session: AsyncSession = Depends(get_session)) -> SubtaskDB:
    obj = Subtask(**body.model_dump(exclude_unset=True))
    print('|')
    db_session.add(obj)
    print('|')
    await db_session.commit()
    print('|')
    await db_session.refresh(obj)
    print('|')
    return obj
