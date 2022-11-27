import imp
from .base import *
from pydantic import EmailStr


class Login(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)

class SignUp(BaseModel):
    email: EmailStr = Field(...)
