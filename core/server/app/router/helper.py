from app.repository.cves import CVERepository
from app.services.graph import GraphService
from .base import *

helper_router = APIRouter(prefix='/api/helper', tags=['Helper'])

# Auto generate coordinates
@helper_router.post('/generate_coordinates')
async def generate_coordinates(request = Body(...)):
    nodesep = 1
    ranksep = 2
    if 'nodesep' in request:
        nodesep = request['nodesep']
    if 'ranksep' in request:
        ranksep = request['ranksep']
    graph = GraphService.generate_coordinates(gph=request['graph'], nodesep=nodesep, ranksep=ranksep)
    return BaseResponse(
        data= {
            'graph': graph,
        }
    )
