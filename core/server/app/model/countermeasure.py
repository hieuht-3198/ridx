from typing import Optional

from app.helper.base import generator_id
from .base import *
from ..config.database import database

Countermeasure = database.get_collection("countermeasures")

class CountermeasureSchema(MixinUserBaseModel):
    name: str = Field(...)
    cost: float = Field(..., ge= 0)
    coverage: float = Field(..., ge= 0, le= 1)
    cover_cves: Optional[list] = Field(...)


class CountermeasureCreate(BaseModel):
    name: str = Field(...)
    # cost: float = Field(..., ge= 0)
    # coverage: float = Field(..., ge= 0, le= 1)
    cover_cves: Optional[list] = Field(...)


class CountermeasureUpdate(CountermeasureCreate):
    pass


class CountermeasureInDeploymentScenarioUpdate(BaseModel):
    name: str = Field(...)
    cost: float = Field(..., ge= 0)
    coverage: float = Field(..., ge= 0, le= 1)
    cover_cves: list = Field(...)


class CountermeasureInDeploymentScenarioCreate(CountermeasureInDeploymentScenarioUpdate):
    id: Optional[str] = generator_id()