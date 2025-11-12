from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.services.permitions import PermitionServise
from src.schemes.permitions import PermissionsCreate, PermissionsDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[PermissionsDB]:
    return await PermitionServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> PermissionsDB:
    return await PermitionServise.get(uid, db_session)

@router.post('/create')
async def create(body: PermissionsCreate, db_session: AsyncSession = Depends(get_session)) -> PermissionsDB:
    return await PermitionServise.create(body, db_session)

@router.put('/update')
async def update(body: PermissionsDB, db_session: AsyncSession = Depends(get_session)):
    return await PermitionServise.update(body, db_session)