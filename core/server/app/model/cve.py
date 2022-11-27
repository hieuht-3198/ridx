from .base import *
from ..config.database import database

CVE = database.get_collection("cves")
CVE.create_index('cve_id', unique = True)

class CVESchema(BaseModel):
    cve_id: str = Field(...)
    cve_name: str = Field(...)
    description: str = Field(...)

    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'cve_name': 'Testing',
    #             'description': 'Testing description'
    #         }
    #     }
