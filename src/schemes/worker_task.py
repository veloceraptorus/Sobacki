from pydantic import UUID4, BaseModel, Field


class WorkerTask(BaseModel):
    uid: UUID4 = Field(
        description="UID разраб_проекта",
        default=None
    )
    UID_task: UUID4 = Field(
        description="UID задачи",
        default=None
    )
    UID_worker: UUID4 = Field(
        description="UID разработчика",
        default=None
    )
