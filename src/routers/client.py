from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.client import Client
from src.schemes.client import ClientCreate, ClientDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ClientDB]:
    query_result = await db_session.execute(select(Client))
    return query_result.scalars().all()


# Создать во всех файлах роутеров методы get по uid и update по телу запроса
@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    return (await db_session.execute(select(Client).where(Client.uid == uid))).scalar_one_or_none()
# Переписать в многострочный вариант


@router.post('/create')
async def create(body: ClientCreate, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    obj = Client(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj


# Метод Update
@router.put('/update')
async def update(body: ClientDB, db_session: AsyncSession = Depends(get_session)):
    query = await db_session.execute(select(Client).where(Client.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        await db_session.refresh(query)
    return query
