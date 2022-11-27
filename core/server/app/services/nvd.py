import nvdlib
from app.config.env import NVD_KEY


class NVDService:
    
    def get_cpe_by_keyword(keyword: str):
        r = nvdlib.searchCPE(keyword= keyword, key= NVD_KEY, includeDeprecated= False)
        return [cpe.name for cpe in r]

    def get_cve_by_cpe_name(cpe_name: str):
        cves = nvdlib.searchCVE(cpeName= cpe_name, key= NVD_KEY)
        return [cve.id for cve in cves]

