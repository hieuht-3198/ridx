from ..model.cve import *
from ..helper.base import *
from .base import *

class CVERepository:

    async def get_cves_by_cve_id(cve_id: list, select = []):
        tmp = await CVE.find({'cve_id': {'$in': cve_id}}).to_list(None)
        return base_converter(tmp, select)

    async def get(condition: dict = {}, current: int = DEFAULT_CURRENT_LIST, page_size: int = DEFAULT_PAGE_SIZE_LIST, select = []):
        l = await BaseRepository.get(CVE, condition, current, page_size)
        return base_converter(l, select)

    async def count(condition: dict = {}):
        count = await BaseRepository.count(CVE, condition)
        return count

