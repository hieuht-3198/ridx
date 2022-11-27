from typing import Optional
from .base import *
from ..config.database import database
from enum import Enum

Asset = database.get_collection("assets")


class AssetType(Enum):
    APPLICATION = 'a'
    OPERATING_SYSTEM = 'o'
    HARDWARE = 'h'


class AssetSchema(MixinUserBaseModel):
    name: str = Field(...) # product
    part: AssetType = Field(...)

    vendor: Optional[str] = Field(...)
    product: Optional[str] = Field(...)
    version: Optional[str] = ''
    cpe: Optional[str] = ''

    custom_fields: Optional[dict] = Field(...)

    # class Config:
    #     schema_extra = {
    #         'example': {
    #             'cve_name': 'Testing',
    #             'description': 'Testing description'
    #         }
    #     }

class AssetCreate(BaseModel):
    name: str = Field(...)
    part: AssetType = Field(...)

class AssetUpdate(AssetCreate):
    pass


class AssetQueryCPE(BaseModel):
    product: str = Field(...)
    part: AssetType = Field(...)
    vendor: str = Field(...)
    version: Optional[str] = ''


class AssetInDeploymentScenario(BaseModel):
    id: str = Field(...)
    server: str = Field(...)
    name: str = Field(...)
    part: AssetType = Field(...)

    vendor: str = Field(...)
    product: str = Field(...)
    version: str = Field(...)
    cpe: Optional[str] = ''

    custom_fields: Optional[dict] = Field(...)


