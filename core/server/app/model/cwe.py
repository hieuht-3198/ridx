from pydantic import BaseModel, Field
from ..config.database import database

CWE = database.get_collection("cwes")
CWE.create_index('cwe_id', unique = True)

class CWESchema(BaseModel):
    cwe_id: str = Field(...)
    cwe_name: str = Field(...)
    description: str = Field(...)
