from app.helper.base import base_converter
from app.model.countermeasure import *
from .base import *

class CountermeasureRepository:

    MODEL = Countermeasure

    async def create(payload: dict):
        obj = await BaseRepository.create(CountermeasureRepository.MODEL, payload)
        return base_converter(obj)
    
    async def find(id: str):
        o = await BaseRepository.find(CountermeasureRepository.MODEL, id)
        return base_converter(o)

    async def update(id: str, payload: dict) -> bool:
        return await BaseRepository.update(CountermeasureRepository.MODEL, id, payload)

    async def get(condition: dict = {}, current: int = 1, page_size: int = 10):
        l = await BaseRepository.get(CountermeasureRepository.MODEL, condition, current, page_size)
        return base_converter(l)

    async def count(condition: dict):
        count = await BaseRepository.count(CountermeasureRepository.MODEL, condition)
        return count
    
    async def delete(id: str):
        return await BaseRepository.delete(CountermeasureRepository.MODEL, id)