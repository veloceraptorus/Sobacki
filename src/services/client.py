from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.client import Client
from pydantic import UUID4
from src.schemes.client import ClientCreate, ClientDB

from src.db import get_session


class ClientServise:
    @staticmethod
    async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ClientDB]:
        query_result = await db_session.execute(select(Client))
        return query_result.scalars().all()

    @staticmethod
    async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
        query = select(Client).where(Client.uid == uid)
        query_obj = await db_session.execute(query)
        query_obj = query_obj.scalar()
        return query_obj

    @staticmethod
    async def create(body: ClientCreate, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
        obj = Client(**body.model_dump(exclude_unset=True))
        db_session.add(obj)
        await db_session.commit()
        await db_session.refresh(obj)
        return obj  

    @staticmethod
    async def update(body: ClientDB, db_session: AsyncSession = Depends(get_session)):
        query = await db_session.execute(select(Client).where(Client.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query
