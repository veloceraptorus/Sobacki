from pydantic import UUID4, BaseModel, Field


class Worker(BaseModel):
    uid: UUID4 = Field(
        description="UID разработчика",
        default=None
    )
    name: str = Field(
        description="ФИО",
        default=None
    )
    telephone_number: str = Field(
        description="номер телефона",
        default=None
    )
    colour: str = Field(
        description="определительный цвет",
        default=None
    )
    role: str = Field(
        description="роль",
        default=None
    )
