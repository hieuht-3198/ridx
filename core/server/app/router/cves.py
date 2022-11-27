from app.repository.cves import CVERepository
from .base import *

cves_router = APIRouter(prefix='/api/cves', tags=['CVE'])

# Get CVE
@cves_router.get('')
async def get(request: Request):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    data = await CVERepository.get(condition, current, page_size, select=['cve_id', 'cwe_id', 'description', 'impact'])
    count = await CVERepository.count(condition)
    return BaseResponse(
        data= data,
        options= {
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get CVE by CVE_ID
@cves_router.get('/{cve_id}')
async def get(cve_id: str, request: Request, user: dict = Depends(get_current_user)):
    target = await CVERepository.get({
        'cve_id': cve_id,
    }, select=['cve_id', 'cwe_id', 'description', 'impact'])
    if len(target):
        return BaseResponse(target[0])
    
    raise CustomHTTPException(STATUS_404_NOT_FOUND)
    
