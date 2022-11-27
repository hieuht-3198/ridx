from app.repository.cves import CVERepository
from ..model.cpe import *
from ..helper.base import *
from .base import *

import re

class CPERepository:

    MODEL = CPE

    async def guess_cpe(keyword: str):
        words = re.split('[, _\-!?:]+', keyword.lower())
        l = await BaseRepository.get(CPERepository.MODEL, {
            "title": {"$all": words}
        }, page_size=MAX_SIZE_LIST)
        return base_converter(l, select = ['name'])


    async def get_cves(cpe: str):
        cpes = await CVERepository.get({
            'cpe': {
                '$in': [cpe]
            }
        }, page_size=MAX_SIZE_LIST, select=['cve_id', 'cwe_id', 'description', 'condition', 'attackVector', 'impact'])
        return cpes

