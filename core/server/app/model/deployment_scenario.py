from enum import Enum
from typing import List, Optional

from app.helper.base import generator_id

from app.model.asset import AssetInDeploymentScenario
from app.model.countermeasure import CountermeasureInDeploymentScenarioCreate
from .base import *
from ..config.database import database

DeploymentScenario = database.get_collection("deployment_scenarios")
AssetCVE = database.get_collection('asset_cves')


class DeploymentScenarioStatus(Enum):
    REQUIREMENTS_ANALYSIS = 'Requirements Analysis'
    DEPLOYMENTS = 'Deployments'
    OPERATIONS = 'Operations'

class DeploymentScenarioSchema(MixinUserBaseModel):
    name: str = Field(...)
    user_id: str = Field(...)
    assets: list = []
    asset_relationships: dict = {}
    security_goal: dict = {}
    countermeasures: list = []
    attack_graph: Optional[dict] = {}


class SecurityGoal(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    asset_id: str = Field(...)
    confidentiality: str = Field(...)
    availability: str = Field(...)
    integrity: str = Field(...)


class UpdateDeploymentScenario(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    status: DeploymentScenarioStatus = Field(...)

class AccessVector(Enum):
    LOCAL = 'LOCAL'
    NETWORK = 'NETWORK'
    ADJACENT = 'ADJACENT_NETWORK'
    PHYSICAL = 'PHYSICAL'

class Privilege(Enum):
    NONE = 'NONE'
    OS_USER = 'OS_USER'
    OS_ADMIN = 'OS_ADMIN'
    APP_USER = 'APP_USER'
    APP_ADMIN = 'APP_ADMIN'

class ThreatType(Enum):
    SPOOFING_IDENTITY = 'Spoofing Identity'
    TAMPERING_WITH_DATA = 'Tampering With Data'
    REPUDIATION_THREATS = 'Repudiation Threats'
    INFORMATION_DISCLOSURE = 'Information Disclosure'
    DENIAL_OF_SERVICE = 'Denial of Service'
    ELEVATION_OF_PRIVILEGES = 'Elevation of Privileges'

class AssetRelationship(BaseModel):
    id: str = Field(...)
    source: str = Field(...)
    target: str = Field(...)
    access_vector: AccessVector = Field(...)
    privilege: Privilege = Field(...)


class CVEOnAsset(BaseModel):
    cve_id: str = Field(...)
    cwe_id: str = Field(...)
    description: str = Field(...)
    impact: dict = Field(...)
    attack_vector: str = Field(...)
    condition: dict = Field(...)

class DeploymentScenarioCreate(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    status: DeploymentScenarioStatus = Field(...)
    system_profile_id: str = Field(...)
    security_goals: List[SecurityGoal] = Field(...)
    countermeasures: List[CountermeasureInDeploymentScenarioCreate] = Field(...)
    assets: List[AssetInDeploymentScenario]
    asset_relationships: List[AssetRelationship]

    cves: Optional[List[CVEOnAsset]] = []
    attack_graph: Optional[dict] = {}


class ExploitabilityCVSS(Enum):
    U = 'Unproven'
    POC = 'Proof-of-Concept'
    F = 'Functional'
    H = 'High'
    ND = 'Not Defined'

class RemediationLevelCVSS(Enum):
    OF = 'Official Fix'
    TF = 'Temporary Fix'
    W = 'Workaround'
    U = 'Unavailable'
    ND = 'Not Defined'

class ReportConfidenceCVSS(Enum):
    UC = 'Unconfirmed'
    UR = 'Uncorroborated'
    C = 'Confirmed'
    ND = 'Not Defined'


class StaticAssessment(BaseModel):
    damage_criterion: float = Field(...)
    benefit_criterion: float = Field(...)
    exploitability: ExploitabilityCVSS = Field(...)
    remediation_level: RemediationLevelCVSS = Field(...)
    report_confidence: ReportConfidenceCVSS = Field(...)
    

class UpdateAttackGraph(BaseModel):
    attack_graph: dict = Field(...)
    target: dict = Field(...)

class UpdateCVEOnAsset(BaseModel):
    cves: List[CVEOnAsset] = []


class CVEOnAttackGraph(BaseModel):
    cves: List[str] = Field(...)


class TargetInAttacker(BaseModel):
    asset_id: str = Field(...)
    attack_vector: str = Field(...)
    privilege: str = Field(...)



class AttackerUpdate(BaseModel):
    targets: List[TargetInAttacker] = Field(...)
    name: str = Field(...)
    description: str = Field(...)
    type: ThreatType = Field(...)


class AttackerCreate(AttackerUpdate):
    id: Optional[str] = generator_id()
    

