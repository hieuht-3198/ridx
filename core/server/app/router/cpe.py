from app.model.asset import AssetQueryCPE
from app.model.cpe import CPEToCVE
from app.repository.cpe import CPERepository
from app.repository.cves import CVERepository
from .base import *

cpe_router = APIRouter(prefix='/api/cpes', tags=['CPE'])

# Get CPE
@cpe_router.get('')
async def get(request: Request):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    data = await CVERepository.get(condition, current, page_size)
    count = await CVERepository.count(condition)
    return BaseResponse(
        data= data,
        options= {
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Create CVE of CPE
@cpe_router.post('/cves')
async def get_cves(request: CPEToCVE):
    cves = await CPERepository.get_cves(request.cpe)
    return BaseResponse(
        data = {
            'cpe': request.cpe,
            'cves': cves,
        },
        options= {
            'total': len(cves)
        }
    )



