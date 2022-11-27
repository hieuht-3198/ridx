from app.helper.base import base_converter
from app.model.deployment_scenario import *
from .base import *

class DeploymentScenarioRepository:

    MODEL = DeploymentScenario

    async def create(payload: dict):
        obj = await BaseRepository.create(DeploymentScenarioRepository.MODEL, payload)
        return base_converter(obj)
    
    async def find(id: str, select = []):
        o = await BaseRepository.find(DeploymentScenarioRepository.MODEL, id)
        return base_converter(o, select)

    async def update(id: str, payload: dict) -> bool:
        return await BaseRepository.update(DeploymentScenarioRepository.MODEL, id, payload)

    async def get(condition: dict = {}, current: int = 1, page_size: int = 10, select = []):
        skip = page_size*(current-1)
        limit = page_size
        # l = await DeploymentScenarioRepository.MODEL.find(condition).skip(skip).limit(limit).to_list(page_size)
        l = await DeploymentScenarioRepository.MODEL.aggregate([
            {
                "$match": condition,
            },
            {
                "$skip": skip,
            },
            {
                "$limit": limit,
            },
            {
                "$lookup": {
                    "from": "system_profiles",
                    "localField": "system_profile_id",
                    "foreignField": "_id",
                    "as": "system_profile"
                }
            }
        ]).to_list(page_size)
        return base_converter(l, select)

    async def count(condition: dict):
        count = await BaseRepository.count(DeploymentScenarioRepository.MODEL, condition)
        return count
    
    async def delete(id: str):
        return await BaseRepository.delete(DeploymentScenarioRepository.MODEL, id)



class AssetCVERepository:
    MODEL = AssetCVE

    async def create(payload: dict):
        obj = await BaseRepository.create(AssetCVERepository.MODEL, payload)
        return base_converter(obj)

    async def update(condition: dict, payload: dict) -> bool:
        return await BaseRepository.update_with_condition(AssetCVERepository.MODEL, condition, payload)

    async def get(condition: dict = {}, current: int = 1, page_size: int = 10, select = []):
        skip = page_size*(current-1)
        limit = page_size
        l = await AssetCVERepository.MODEL.find(condition).skip(skip).limit(limit).to_list(page_size)
        return base_converter(l, select)
    
    async def delete(condition: dict):
        return await AssetCVERepository.MODEL.delete(condition)
