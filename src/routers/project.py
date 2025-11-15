from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import UUID4

from src.db import get_session
from src.services.project import ProjectServise
from src.schemes.project import ProjCreate, ProjectOutput

router = APIRouter()

# async def getter(uid: UUID4 ,db_session: AsyncSession = Depends(get_session)):
#     c = select(Client)
#     c = c.where(Client.uid == uid)
#     cc = await db_session.execute(c)
#     ccc = cc.scalar_one_or_none()
#     return ccc


# async def getter(uid: UUID4 ,db_session: AsyncSession = Depends(get_session)):
#     t = select(Task)
#     t = t.where(Task.uid == uid)
#     tt = await db_session.execute(t)
#     ttt = tt.scalar_one_or_none()
#     return ttt


# Изучить пару репозиториев в гитхаб с пайтоном, на понимание кода (Отпишись)
# Создать класс ProjectOutput для выводных данных, а-то чёт не удобно уже
#       с ProjectDB не очень хорошо работать

@router.get('/list')
async def get_list(db_session: AsyncSession = Depends(get_session)):
    return await ProjectServise.get_list(db_session)


@router.get('/{uid}')
async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ProjectOutput:
    return await ProjectServise.get(uid, db_session)


@router.post('/create')
async def create(body: ProjCreate, db_session: AsyncSession = Depends(get_session)) -> ProjectOutput:
    return await ProjectServise.create(body, db_session)


@router.put('/update')
async def update(body: ProjectOutput, db_session: AsyncSession = Depends(get_session)):
    return await ProjectServise.create(body, db_session)
