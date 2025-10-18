from pydantic import UUID4, BaseModel, Field


class ClientProject(BaseModel):
    uid: UUID4 = Field(
        description="UID клиент_проекта",
        default=None
    )
    UID_client: UUID4 = Field(
        description="UID клиента",
        default=None
    )
    UID_proj: UUID4 = Field(
        description="UID проекта",
        default=None
    )
