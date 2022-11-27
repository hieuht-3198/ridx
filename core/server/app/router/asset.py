from app.services.nvd import NVDService

from .base import *
from app.repository.assets import *

assets_router = APIRouter(prefix='/api/assets', tags=['Assets'])


# Keyword to CPE
@assets_router.get('/match_cpe')
async def mapping_cpe(keyword: str = ''):
    return {
        'status': True,
        'cpes': NVDService.get_cpe_by_keyword(keyword)
    }

# CPE to CVE
@assets_router.get('/match_cve')
async def mapping_cve(cpe_name: str = ''):
    return {
        'status': True,
        'cves': NVDService.get_cve_by_cpe_name(cpe_name)
    }

# Get list asset
@assets_router.get('')
async def index(request: Request, user: dict = Depends(get_current_user)):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition = add_created_by(condition, user['id'])
    data = await AssetRepository.get(condition, current, page_size)
    count = await AssetRepository.count(condition)
    return BaseResponse(
        data= data,
        options= {
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get a asset
@assets_router.get('/{id}')
async def show(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await AssetRepository.find(id)
    if target:
        if target['created_by'] == user['id']:   
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Create new asset
@assets_router.post('')
async def create(request: AssetCreate, user: dict = Depends(get_current_user)):
    request = jsonable_encoder(request)
    request = create_by_user_request(request, user['id'])
    if await check_exists(request, user):
        raise CustomHTTPException(
            STATUS_422_INVALID_PARAMETER,
            errors=[{
                'name': 'exists',
            }]
        )
    target = await AssetRepository.create(request)
    return BaseResponse(target)

# Update asset
@assets_router.put('/{id}')
async def update(id: str, request: AssetUpdate, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await AssetRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        request = update_by_user_request(request, user['id'])
        target = await AssetRepository.update(id, request)
        return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Delete asset
@assets_router.delete('/{id}')
async def delete(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await AssetRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        target = await AssetRepository.delete(id)
        return BaseResponse(status=target)    
    raise CustomHTTPException(STATUS_404_NOT_FOUND)


async def check_exists(request, user):
    target = await AssetRepository.get({
        'name': {
            '$regex': f"^{request['name']}$",
            '$options': 'i',
        },
        'created_by': ObjectId(user['id']),
    })
    if target:
        return True
    return False