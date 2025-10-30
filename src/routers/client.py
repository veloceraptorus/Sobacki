from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_session
from src.models.client import Client
from src.schemes.client import ClientCreate, ClientDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ClientDB]:
    query_result = await db_session.execute(select(Client))
    return query_result.scalars().all()


@router.post('/create')
async def create(body: ClientCreate, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    obj = Client(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj
