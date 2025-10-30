from datetime import date

from pydantic import UUID4, BaseModel, Field


class ProjCreate(BaseModel):
    title: str = Field(
        description="название",
        default=None
    )
    description: str = Field(
        description="описание",
        default=None
    )
    create_date: date = Field(
        description="дата начала",
        default=None
    )
    uid_creator: UUID4 | None = Field(
        description="создатель",
        default=None
    )
    uid_client: UUID4 | None = Field(
        description="заказчик",
        default=None
    )
    initial_budget: float | None = Field(
        description="начальный бюджет",
        default=None
    )
    result_budget: float | None = Field(
        description="конечный бюджет",
        default=None
    )
    colour: str = Field(
        description="определительный цвет",
        default=None
    )
    status: str = Field(
        description="статус готовости",
        default=None
    )
    deadline: date = Field(
        description="дата, когда проект должен быть готов",
        default=None
    )


class ProjectDB(BaseModel):
    uid: UUID4 = Field(
        description="UID проекта"
    )
    title: str = Field(
        description="название"
    )
    description: str = Field(
        description="описание"
    )
    create_date: date = Field(
        description="дата начала"
    )
    uid_creator: UUID4 | None = Field(
        description="создатель"
    )
    uid_client: UUID4 | None = Field(
        description="заказчик"
    )
    initial_budget: float | None = Field(
        description="начальный бюджет"
    )
    result_budget: float | None = Field(
        description="конечный бюджет"
    )
    colour: str = Field(
        description="определительный цвет"
    )
    status: str = Field(
        description="статус готовости"
    )
    deadline: date = Field(
        description="дата, когда проект должен быть готов"
    )