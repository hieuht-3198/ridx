from enum import Enum
from typing import List, Optional, Any
from .base import *
from ..config.database import database


RiskMonitoring = database.get_collection("risk_monitorings")

class RiskMonitoringSchema(MixinUserBaseModel):
    deployment_scenario: dict = Field(...)
    result: dict = Field(...)

class InitRiskMonitoring(BaseModel):
    time_step: int = Field(..., ge=2, le=20)
    observer_data: list = Field(...)
    node_temporals: Any = Field(...)


class DetectThreat(BaseModel):
    cve_id: str = Field(...)
    asset_id: str = Field(...)
    observer_probability: float = Field(..., ge=0, le=1)
