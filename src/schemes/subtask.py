from pydantic import UUID4, BaseModel, Field


class SubtaskCreate(BaseModel):
    uid_task: UUID4 = Field(
        description="UID задачи",
        default=None
    )
    title: str = Field(
        description="оглавление",
        default=None
    )
    description: str = Field(
        description="описание",
        default=None
    )


class SubtaskDB(BaseModel):
    uid: UUID4 = Field(
        description="UID подзадачи"
    )
    uid_task: UUID4 = Field(
        description="UID задачи"
    )
    title: str = Field(
        description="оглавление"
    )
    description: str = Field(
        description="описание"
    )
