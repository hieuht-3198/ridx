from ..repository.cwes import *

from .base import *

cwes_router = APIRouter(prefix='/api/cwes', tags=['CWE'])

# Get CWE
@cwes_router.get('')
async def get(request: Request):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    data = await CWERepository.get(condition, current, page_size)
    count = await CWERepository.count(condition)
    return BaseResponse(
        data= data,
        options= {
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get CWE by CWE_ID
@cwes_router.get('/{cwe_id}')
async def get(cwe_id: str, user: dict = Depends(get_current_user)):
    target = await CWERepository.get({
        'cwe_id': cwe_id,
    })
    if len(target):
        return BaseResponse(target[0])
    
    raise CustomHTTPException(STATUS_404_NOT_FOUND)
