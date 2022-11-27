from enum import Enum
from typing import List, Optional
from .base import *
from ..config.database import database


RiskAssessment = database.get_collection("risk_assessments")

class RiskAssessmentSchema(MixinUserBaseModel):
    deployment_scenario: dict = Field(...)
    result: dict = Field(...)


class RiskAssessmentSave(BaseModel):
    name: str = Field(...)
