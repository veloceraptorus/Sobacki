from pydantic import UUID4, BaseModel, Field


class Client(BaseModel):
    uid: UUID4 = Field(
        description="UID клиента",
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
