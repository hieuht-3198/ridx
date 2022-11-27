from enum import Enum
from pydantic import EmailStr

from .base import *
from ..config.database import database

User = database.get_collection("users")
User.create_index('email', unique=True)


class UserRole(Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'


class UserSchema(MixinTimestampsBaseModel):
    email: EmailStr = Field(...)
    password: str
    role: UserRole = Field(...)
