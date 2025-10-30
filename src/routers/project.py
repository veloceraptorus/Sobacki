from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models.project import Project
from src.schemes.project import ProjCreate, ProjectDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ProjectDB]:
    query_result = await db_session.execute(select(Project))
    return query_result.scalars().all()


@router.post('/create')
async def create(body: ProjCreate, db_session: AsyncSession = Depends(get_session)) -> ProjectDB:
    obj = Project(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj
