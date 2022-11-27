from datetime import datetime
from .base import *
from ..config.database import database

SystemProfile = database.get_collection("system_profiles")


class SystemProfileSchema(MixinUserBaseModel):
    name: str = Field(...)
    description: str = Field(...)
    custom_fields: dict = {}


class SystemProfileCreate(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    custom_fields: dict = {}


class SystemProfileUpdate(SystemProfileCreate):
    pass
