from ..model.cwe import *
from ..helper.base import *
from .base import *


class CWERepository:

    async def create(cve_data: dict):
        new_cve = await BaseRepository.create(CWE, cve_data)
        return base_converter(new_cve)

    async def get(condition: dict = {}, current: int = DEFAULT_CURRENT_LIST, page_size: int = DEFAULT_PAGE_SIZE_LIST):
        l = await BaseRepository.get(CWE, condition, current, page_size)
        return base_converter(l)

    async def count(condition: dict = {}):
        count = await BaseRepository.count(CWE, condition)
        return count