from pydantic import UUID4, BaseModel, Field


class PermissionsCreate(BaseModel):
    uid_worker: UUID4 = Field(
        description="UID разработчика",
        default=None
    )
    uid_proj: UUID4 = Field(
        description="UID проекта",
        default=None
    )
    permission_name: str = Field(
        description="название права",
        default=None
    )
    description: str = Field(
        description="описание",
        default=None
    )


class PermissionsDB(BaseModel):
    uid: UUID4 = Field(
        description="UID права"
    )
    uid_worker: UUID4 = Field(
        description="UID разработчика"
    )
    uid_proj: UUID4 = Field(
        description="UID проекта"
    )
    permission_name: str = Field(
        description="название права"
    )
    description: str = Field(
        description="описание"
    )
