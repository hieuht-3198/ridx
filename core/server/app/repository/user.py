from ..helper.base import *
from ..model.user import *
from .base import *
from ..config.auth import *

class UserRepository:

    MODEL = User

    async def create(user_data: dict):
        password = generator_password()
        print(user_data['email'], password)
        user_data['password'] = get_password_hash(password)
        user_data['role'] = UserRole.USER.value
        user_data['active'] = True
        new_user = await BaseRepository.create(User, user_data)
        return user_helper(new_user)


    async def get_user_by_email(email: str):
        existing_user = await User.find_one({"email": email})
        if existing_user is not None:
            return user_helper(existing_user)
        return False
    
    async def find(id: str):
        o = await BaseRepository.find(UserRepository.MODEL, id)
        return base_converter(o)

    async def update(id: str, payload: dict) -> bool:
        return await BaseRepository.update(UserRepository.MODEL, id, payload)

    async def get(condition: dict = {}, current: int = 1, page_size: int = 10, select = []):
        l = await BaseRepository.get(UserRepository.MODEL, condition, current, page_size)
        return base_converter(l, select)

    async def count(condition: dict):
        count = await BaseRepository.count(UserRepository.MODEL, condition)
        return count
    
    async def delete(id: str):
        return await BaseRepository.delete(UserRepository.MODEL, id)