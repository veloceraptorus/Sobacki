from pydantic import UUID4, BaseModel, Field


class WorkerTaskCreate(BaseModel):
    uid_task: UUID4 = Field(
        description="UID задачи",
        default=None
    )
    uid_worker: UUID4 = Field(
        description="UID разработчика",
        default=None
    )


class WorkerTaskDB(BaseModel):
    uid: UUID4 = Field(
        description="UID разраб_проекта"
    )
    uid_task: UUID4 = Field(
        description="UID задачи"
    )
    uid_worker: UUID4 = Field(
        description="UID разработчика"
    )
