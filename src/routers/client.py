from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.services.client import ClientServise
from src.schemes.client import ClientCreate, ClientDB

router = APIRouter()


@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)) -> list[ClientDB]:
    return await ClientServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    return await ClientServise.get(uid, db_session)


@router.post('/create')
async def create(body: ClientCreate, db_session: AsyncSession = Depends(get_session)) -> ClientDB:
    return await ClientServise.create(body, db_session)



@router.put('/update')
async def update(body: ClientDB, db_session: AsyncSession = Depends(get_session)):
    return await ClientServise.update(body, db_session)
