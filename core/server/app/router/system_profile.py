from app.repository.deployment_scenario import DeploymentScenarioRepository
from app.repository.system_profile import *
from .base import *

system_profile_router = APIRouter(
    prefix='/api/system_profiles',
    tags=['System Profile']
)

# CRUD System profile
@system_profile_router.get('')
async def index(request: Request, user: dict = Depends(get_current_user)):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition = add_created_by(condition, user['id'])
    data = await SystemProfileRepository.get(condition, current, page_size)
    count = await SystemProfileRepository.count(condition)
    return BaseResponse(
        data=data,
        options={
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get deployment scenario in system profile
@system_profile_router.get('/deployment_scenarios')
async def index(request: Request, user: dict = Depends(get_current_user)):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition = add_created_by(condition, user['id'])
    data = await SystemProfileRepository.get(condition, current, page_size)

    payload = add_created_by({}, user['id'])

    deployment_scenarios = await DeploymentScenarioRepository.get(payload, page_size=MAX_SIZE_LIST, select= ['name', 'created_at', 'updated_at', 'status', 'system_profile_id'])
    for index, tmp in enumerate(data):
        system_profile_id = tmp['id']
        ds_all = []
        for ds in deployment_scenarios:
            if ds['system_profile_id'] == system_profile_id:
                ds_all.append(ds)
        data[index]['deployment_scenarios'] = ds_all

    count = await SystemProfileRepository.count(condition)
    return BaseResponse(
        data=data,
        options={
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get deployment scenario in system profile
@system_profile_router.get('/{id}/deployment_scenarios')
async def show(id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    target = await SystemProfileRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            condition['system_profile_id'] =  ObjectId(id)
            deployment_scenarios = await DeploymentScenarioRepository.get(condition, page_size=MAX_SIZE_LIST, select=['name', 'created_at', 'updated_at', 'status'])
            skip = page_size*(current-1)
            limit = page_size
            return BaseResponse(
                data=deployment_scenarios[skip: skip + limit],
                options={
                    'total': len(deployment_scenarios),
                    'pageSize': page_size,
                    'current': current,
                }
            )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


@system_profile_router.get('/{id}')
async def show(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await SystemProfileRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)



@system_profile_router.post('')
async def create(request: SystemProfileCreate, user: dict = Depends(get_current_user)):
    request = jsonable_encoder(request)
    request = create_by_user_request(request, user['id'])
    target = await SystemProfileRepository.create(request)
    return BaseResponse(target)


@system_profile_router.put('/{id}')
async def update(id: str, request: SystemProfileUpdate, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await SystemProfileRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        request = update_by_user_request(request, user['id'])
        target = await SystemProfileRepository.update(id, request)
        return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


@system_profile_router.delete('/{id}')
async def delete(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await SystemProfileRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        target = await SystemProfileRepository.delete(id)
        return BaseResponse(status=target)
    raise CustomHTTPException(STATUS_404_NOT_FOUND)
