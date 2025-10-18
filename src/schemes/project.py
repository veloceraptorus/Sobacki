from datetime import date
from pydantic import UUID4, BaseModel, Field


class Proj(BaseModel):
    uid: UUID4 = Field(
        description="UID проекта",
        default=None
    )
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
    UID_creator: UUID4 = Field(
        description="создатель",
        default=None
    )
    UID_client: UUID4 | None = Field(
        description="заказчик",
        default=None
    )
    Initial_budget: float | None = Field(
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
