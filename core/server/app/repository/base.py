from datetime import datetime
import sys
from app.helper.base import base_converter
from bson.objectid import ObjectId


DEFAULT_CURRENT_LIST = 1
DEFAULT_PAGE_SIZE_LIST = 10
MAX_SIZE_LIST = sys.maxsize
class BaseRepository:
    async def create(Collection, obj, timestamps: bool = True):
        if timestamps:
            o = await Collection.insert_one({
                **obj,
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
            })
        else:
            o = await Collection.insert_one(obj)
        new_o = await BaseRepository.find(Collection, o.inserted_id)
        return new_o

    async def get(Collection, condition: dict = {}, current: int = 1, page_size: int = 10):
        skip = page_size*(current-1)
        limit = page_size
        l = await Collection.find(condition).skip(skip).limit(limit).to_list(page_size)
        return l

    async def count(Collection, condition: dict = {}):
        l = await Collection.count_documents(condition)
        return l
    
    async def find(Collection, id: str):
        o = await Collection.find_one({'_id': ObjectId(id)})
        return o
    
    async def update(Collection, id: str, payload: dict, timestamps: bool = True):
        if timestamps:
            payload['updated_at'] = datetime.now()
            o = await Collection.update_one({
                '_id': ObjectId(id)
            }, {
                '$set': payload
            })
        else:
            o = await Collection.update_one({
                '_id': ObjectId(id)
            }, {
                '$set': payload
            })
        if o.matched_count == 1:
            return True
        return False

    async def update_with_condition(Collection, condition: dict, payload: dict, timestamps: bool = True):
        if timestamps:
            payload['updated_at'] = datetime.now()
            o = await Collection.update_one(condition, {
                '$set': payload
            })
        else:
            o = await Collection.update_one(condition, {
                '$set': payload
            })
        if o.matched_count == 1:
            return True
        return False
    
    async def delete(Collection, id: str):
        o = await Collection.delete_one({
            '_id': ObjectId(id)
        })
        if o.deleted_count == 1:
            return True
        return False