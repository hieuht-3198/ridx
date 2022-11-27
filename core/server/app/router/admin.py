import json
import secrets

from app.repository.cves import CVERepository
from app.services.graph import GraphService
from core.bayes.model.network import BayesianNetwork
from .base import *

SECRETS_LENGTH = 24

admin_router = APIRouter(
    prefix='/api/admin',
    tags=['Admin'],
)


@admin_router.get('/users')
async def get_users(request: Request, user: dict = Depends(get_admin)):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition['role'] = UserRole.USER.value
    data = await UserRepository.get(condition, current, page_size, select=['email', 'created_at', 'updated_at', 'role', 'active'])
    count = await UserRepository.count(condition)
    return BaseResponse(
        data= data,
        options= {
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

@admin_router.put('/users/{id}')
async def change_state(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await UserRepository.find(id)
    if target:
        await UserRepository.update(id, {
            'active': not target['active'],
        })
        return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)
