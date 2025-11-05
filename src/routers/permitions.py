from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.models.permitions import Permission
from src.schemes.permitions import PermissionsCreate, PermissionsDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[PermissionsDB]:
    query_result = await db_session.execute(select(Permission))
    return query_result.scalars().all()


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PermissionsDB:
    return (await db_session.execute(select(Permission).where(Permission.uid == uid))).scalar_one_or_none()


@router.post('/create')
async def create(body: PermissionsCreate, db_session: AsyncSession = Depends(get_session)) -> PermissionsDB:
    obj = Permission(**body.model_dump(exclude_unset=True))
    db_session.add(obj)
    await db_session.commit()
    await db_session.refresh(obj)
    return obj


@router.put('/update')
async def update(body: PermissionsDB, db_session: AsyncSession = Depends(get_session)):
    query = await db_session.execute(select(Permission).where(Permission.uid == body.uid))
    query = query.scalar()
    if query:
        for key, value in body.model_dump(exclude_unset=True).items():
            setattr(query, key, value)
        await db_session.commit()
        await db_session.refresh(query)
    return query
