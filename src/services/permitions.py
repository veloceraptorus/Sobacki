from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.permitions import Permition
from src.schemes.permitions import PermissionsCreate, PermissionsDB

# from src.db import get_session


class PermitionServise:
    @staticmethod
    async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[PermissionsDB]:
        query_result = await db_session.execute(select(Permition))
        return query_result.scalars().all()

    @staticmethod
    async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PermissionsDB:
        query = select(Permition).where(Permition.uid == uid)
        query_obj = await db_session.execute(query)
        query_obj = query_obj.scalar()
        return query_obj

    @staticmethod
    async def create(body: PermissionsCreate, db_session: AsyncSession = Depends(get_session)) -> PermissionsDB:
        obj = Permition(**body.model_dump(exclude_unset=True))
        db_session.add(obj)
        await db_session.commit()
        await db_session.refresh(obj)
        return obj

    @staticmethod
    async def update(body: PermissionsDB, db_session: AsyncSession = Depends(get_session)):
        query = await db_session.execute(select(Permition).where(Permition.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
            await db_session.refresh(query)
        return query
