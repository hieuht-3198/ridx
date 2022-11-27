from fastapi import Body, Form

from .base import *
from ..model.auth import SignUp, Login
from ..repository.user import *

auth_router = APIRouter(
    prefix='/api', 
    tags=['Auth']
)

# Create new account
@auth_router.post('/admin/users')
async def sign_up(user: SignUp = Body(...), admin: dict = Depends(get_current_user)):
    user_data = jsonable_encoder(user)
    if await UserRepository.get_user_by_email(user_data['email']):
        raise CustomHTTPException(
            STATUS_422_INVALID_PARAMETER,
            errors=[error_message('user.email.exist')]
        )
    new_user = await UserRepository.create(user_data)
    return new_user

# Login
@auth_router.post('/login')
async def log_in(user: Login = Body(...)):
    user_data = jsonable_encoder(user)
    current_user = await AuthenticationRepository.authenticate_user(user_data)
    if not current_user:
        raise CustomHTTPException(
            STATUS_401_UNAUTHORIZED
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': current_user['email']}, expires_delta=access_token_expires
    )
    return {
        'status': STATUS_OK,
        'user': current_user,
        'token': {
            'token_type': 'bearer',
            'access_token': access_token,
        }
    }

# Logout
@auth_router.post('/logout')
async def log_out(user: dict = Depends(get_current_user)):
    return {
        'status': STATUS_OK,
    }

# Get current user info
@auth_router.get('/current_user')
async def get_user(user: dict = Depends(get_current_user)):
    return user

# refresh token 
@auth_router.post('/refresh_token')
async def refresh_token(user: dict = Depends(get_current_user)):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user['email']}, expires_delta=access_token_expires
    )
    content = {
        'status': STATUS_OK,
    }
    response = JSONResponse(content=content)
    response.set_cookie(key='auth_token', value=access_token)
    return response

# get token 
@auth_router.post('/token')
async def get_token(username: str = Form(...), password: str = Form(...)):
    current_user = await AuthenticationRepository.authenticate_user({'email': username, 'password': password})
    if not current_user:
        raise CustomHTTPException(
            STATUS_401_UNAUTHORIZED
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': current_user['email']}, expires_delta=access_token_expires
    )
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }
