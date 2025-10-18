from pydantic import UUID4, BaseModel, Field


class Tasks(BaseModel):
    uid: UUID4 = Field(
        description="UID задачи",
        default=None
    )
    UID_proj: UUID4 = Field(
        description="UID проекта",
        default=None
    )
    ZP: str = Field(
        description="вознаграждение",
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
