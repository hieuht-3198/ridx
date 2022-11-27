from fastapi import Depends, APIRouter, Body, Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from jose import JWTError

from app.handle.error_message import error_message
from app.model.base import *
from app.model.user import UserRole
from app.repository.user import UserRepository

from ..config.http_status import *
from ..handle.exception import CustomHTTPException
from ..repository.auth import *

from bson import ObjectId

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token', auto_error=False)

CURRENT_LIST = 'current'
PAGE_SIZE = 'pageSize'

DEFAULT_CURRENT_LIST = 1
DEFAULT_PAGE_SIZE_LIST = 10

# Token to current user
async def get_current_user(auth_token: str = Depends(oauth2_scheme)):
    credentials_exception = CustomHTTPException(STATUS_401_UNAUTHORIZED)
    try:
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    except AttributeError:
        raise credentials_exception
    user = await UserRepository.get_user_by_email(email=email)
    if user is None:
        raise credentials_exception
    return user

# Check admin
async def get_admin(user: dict = Depends(get_current_user)):
    if user['role'] == UserRole.ADMIN.value:
        return user
    raise CustomHTTPException(STATUS_403_FORBIDDEN)

# hepler 
def parse_query_params(d):
    current = DEFAULT_CURRENT_LIST
    if CURRENT_LIST in d:
        current = int(d[CURRENT_LIST])
        del d[CURRENT_LIST]
    page_size = DEFAULT_PAGE_SIZE_LIST
    if PAGE_SIZE in d:
        page_size = int(d[PAGE_SIZE])
        del d[PAGE_SIZE]
    for key in d:
        d[key] = {
            '$regex': d[key],
            '$options': 'i',
        }
    return current, page_size, d

def is_valid_id(id: str):
    if not ObjectId.is_valid(id):
        raise CustomHTTPException(STATUS_404_NOT_FOUND)


async def get_item_by_id(Repository, id, user, select: list = None):
    if select is None or select == []:
        select = []
    else:
        if 'created_by' not in select:
            select.append('created_by')
    is_valid_id(id)
    item = await Repository.find(id, select)
    if item['created_by'] == user['id']:
        return item
    raise CustomHTTPException(STATUS_404_NOT_FOUND)
