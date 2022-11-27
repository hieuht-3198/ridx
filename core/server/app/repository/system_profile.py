from app.helper.base import base_converter
from .base import *
from app.model.system_profile import *

class SystemProfileRepository:

    MODEL = SystemProfile

    async def create(payload: dict):
        obj = await BaseRepository.create(SystemProfileRepository.MODEL, payload)
        return base_converter(obj)
    
    async def find(id: str):
        o = await BaseRepository.find(SystemProfileRepository.MODEL, id)
        return base_converter(o)

    async def update(id: str, payload: dict):
        return await BaseRepository.update(SystemProfileRepository.MODEL, id, payload)

    async def get(condition: dict = {}, current: int = 1, page_size: int = 10):
        l = await BaseRepository.get(SystemProfileRepository.MODEL, condition, current, page_size)
        return base_converter(l)

    async def count(condition: dict):
        count = await BaseRepository.count(SystemProfileRepository.MODEL, condition)
        return count
    
    async def delete(id: str):
        return await BaseRepository.delete(SystemProfileRepository.MODEL, id)