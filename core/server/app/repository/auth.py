from app.repository.base import BaseRepository
from ..config.auth import *
from ..model.user import User
from ..helper.base import *


class AuthenticationRepository:
    
    async def authenticate_user(user_data: dict):
        current_user = await User.find_one({'email': user_data['email']})
        if not current_user:
            return False
        if not verify_password(user_data['password'] , current_user['password']):
            return False
        return user_helper(current_user)