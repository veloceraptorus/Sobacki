from pydantic import UUID4, BaseModel, Field


class WorkerCreate(BaseModel):
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
    email: str = Field(
        description="почта",
        dafault=None
    )


class WorkerDB(BaseModel):
    uid: UUID4 = Field(
        description="UID разработчика"
    )
    name: str = Field(
        description="ФИО"
    )
    telephone_number: str = Field(
        description="номер телефона"
    )
    colour: str = Field(
        description="определительный цвет"
    )
    role: str = Field(
        description="роль"
    )
    email: str = Field(
        description="почта"
    )
