from .base import *
from ..config.database import database

CPEMatches = database.get_collection("cpe_matches")

CPE = database.get_collection("cpes")


class CPEToCVE(BaseModel):
    cpe: str