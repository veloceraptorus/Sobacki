from pydantic import UUID4, BaseModel, Field


class ClientCreate(BaseModel):
    name: str = Field(
        description="ФИО",
        default=None
    )
    telephone_number: str = Field(
        description="номер телефона",
        default=None
    )
    email: str = Field(
        description="почта",
        dafault=None
    )


class ClientDB(BaseModel):
    uid: UUID4 = Field(
        description="UID клиента"
    )
    name: str = Field(
        description="ФИО"
    )
    telephone_number: str = Field(
        description="номер телефона"
    )
    email: str = Field(
        description="почта"
    )
