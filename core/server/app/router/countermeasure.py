from .base import *
from app.repository.countermeasure import *

countermeasure_router = APIRouter(prefix='/api/countermeasures', tags=['Countermeasure'])

# Get countermeasures
@countermeasure_router.get('')
async def index(request: Request, user: dict = Depends(get_current_user)):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition = add_created_by(condition, user['id'])
    data = await CountermeasureRepository.get(condition, current, page_size)
    count = await CountermeasureRepository.count(condition)
    return BaseResponse(
        data= data,
        options= {
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get countermeasure
@countermeasure_router.get('/{id}')
async def show(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await CountermeasureRepository.find(id)
    if target:
        if target['created_by'] == user['id']:   
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


# Create countermeasure
@countermeasure_router.post('')
async def create(request: CountermeasureCreate, user: dict = Depends(get_current_user)):
    request = jsonable_encoder(request)
    request = create_by_user_request(request, user['id'])
    target = await CountermeasureRepository.create(request)
    return BaseResponse(target)


# Update countermeasure
@countermeasure_router.put('/{id}')
async def update(id: str, request: CountermeasureUpdate, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await CountermeasureRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        request = update_by_user_request(request, user['id'])
        target = await CountermeasureRepository.update(id, request)
        return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Delete countermeasure
@countermeasure_router.delete('/{id}')
async def delete(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await CountermeasureRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        target = await CountermeasureRepository.delete(id)
        return BaseResponse(status=target)    
    raise CustomHTTPException(STATUS_404_NOT_FOUND)