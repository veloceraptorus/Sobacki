from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.project import Project
from pydantic import UUID4
from src.schemes.project import ProjCreate, ProjectOutput


from src.db import get_session


class ProjectServise:
    @staticmethod
    async def get_list(db_session: AsyncSession = Depends(get_session)):
        query_result = await db_session.execute(select(Project))
        query_list = query_result.scalars().all()
        return [i for i in query_list]

    @staticmethod
    async def get(uid: UUID4, db_session: AsyncSession = Depends(get_session)) -> ProjectOutput:
        query = select(Project).where(Project.uid == uid)
        query_obj = await db_session.execute(query)
        query_obj = query_obj.scalar()
        return query_obj

    @staticmethod
    async def create(body: ProjCreate, db_session: AsyncSession = Depends(get_session)) -> ProjectOutput:
        obj = Project(**body.model_dump(exclude_unset=True))
        db_session.add(obj)
        await db_session.commit()
        await db_session.refresh(obj)
        client_obj = await ProjectServise.get(obj.uid_client, db_session)
        if client_obj is not None:
            return ProjectOutput(
                client=client_obj.__dict__,
                **obj.__dict__
            )
        else:
            return ProjectOutput(
                client=None,
                **obj.__dict__
            )

    @staticmethod
    async def update(body: ProjectOutput, db_session: AsyncSession = Depends(get_session)) -> ProjectOutput:
        query = await db_session.execute(select(Project).where(Project.uid == body.uid))
        query = query.scalar()
        if query:
            for key, value in body.model_dump(exclude_unset=True).items():
                setattr(query, key, value)
            await db_session.commit()
        return query
