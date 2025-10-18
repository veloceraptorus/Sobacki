from pydantic import UUID4, BaseModel, Field


class WorkerProject(BaseModel):
    uid: UUID4 = Field(
        description="UID разраб_проекта",
        default=None
    )
    UID_worker: UUID4 = Field(
        description="UID разработчика",
        default=None
    )
    UID_proj: UUID4 = Field(
        description="UID проекта",
        default=None
    )
