from app.helper.base import base_converter
from app.model.risk_assessment import *
from .base import *

class RiskAssessmentRepository:

    MODEL = RiskAssessment

    async def create(payload: dict):
        obj = await BaseRepository.create(RiskAssessmentRepository.MODEL, payload)
        return base_converter(obj)
    
    async def find(id: str):
        o = await BaseRepository.find(RiskAssessmentRepository.MODEL, id)
        return base_converter(o)

    async def update(id: str, payload: dict) -> bool:
        return await BaseRepository.update(RiskAssessmentRepository.MODEL, id, payload)

    async def get(condition: dict = {}, current: int = 1, page_size: int = 10, select = []):
        skip = page_size*(current-1)
        limit = page_size
        l = await RiskAssessmentRepository.MODEL.find(condition).skip(skip).limit(limit).to_list(page_size)
        return base_converter(l, select)

    async def count(condition: dict):
        count = await BaseRepository.count(RiskAssessmentRepository.MODEL, condition)
        return count
    
    async def delete(id: str):
        return await BaseRepository.delete(RiskAssessmentRepository.MODEL, id)
