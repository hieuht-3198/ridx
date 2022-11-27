import json
import secrets

from app.repository.cves import CVERepository
from app.services.graph import GraphService
from core.bayes.model.network import BayesianNetwork
from .base import *

SECRETS_LENGTH = 24

assessments_router = APIRouter(
    prefix='/api/assessments',
    tags=['CVE'],
    dependencies=[
        Depends(get_current_user)
    ]
)

# Get list assessments
@assessments_router.get('/{id}')
async def get_assessment(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    try:
        file = open('./scenarios/scenario_{}.json'.format(1))
        data = json.loads(file.read())
    except:
        raise CustomHTTPException(STATUS_404_NOT_FOUND)
    cves = await __get_cves(data['cves'])
    attack_graph = GraphService.generate_coordinates(data['attack_graph'])
    countermeasures = data['countermeasures']
    assets = data['assets']

    return {
        'status': True,
        'cves': cves,
        'attack_graph': attack_graph,
        'countermeasures': countermeasures,
        'assets': assets,
    }

# Create a assessment
@assessments_router.post('')
async def post_assessment(request = Body(...)):
    f = open('./scenarios/sample_data.json')
    data_sample = json.load(f)
    attack_graph = data_sample['attack_graph']
    base_impact = data_sample['damage_criterion']
    base_benefit = data_sample['benefit_criterion']
    network1 = BayesianNetwork(deployment_scenario=data_sample ,attack_graph=attack_graph, base_impact=base_impact, base_benefit=base_benefit)
    network2 = BayesianNetwork(deployment_scenario=data_sample ,attack_graph=attack_graph, base_impact=base_impact, base_benefit=base_benefit, countermeasures=False)
    return {
        'status': True,
        'data': {
            'countermeasures': network1.get_all_posteriors(),
            'not_countermeasures': network2.get_all_posteriors(),
            'cia': {
                'countermeasures': network1.get_cia_assets(),
                'not_countermeasures': network2.get_cia_assets(),
            },
            'assets': data_sample['assets'],
            'security_goals': data_sample['security_goals'],
        }
    }


async def __get_cves(list_cves: list):
    cves = await CVERepository.get_cves_by_cve_id(list_cves, select=['cve_id', 'impact', 'description'])
    cvesNone = list_cves[:]
    for cve in cves:
        try:
            cve['description'] = cve['description']
        except:
            cve['description'] = ''
        try:
            cve['exploitabilityScore'] = round(
                cve['impact']['baseMetricV2']['exploitabilityScore']/10, 2)
            cve['impactScore'] = round(
                cve['impact']['baseMetricV2']['impactScore']/10, 2)
        except:
            cve['exploitabilityScore'] = None
            cve['impactScore'] = None
        # del cve['impact']
        cvesNone.remove(cve['cve_id'])
    for cve in cvesNone:
        cves.append({
            'id': secrets.token_urlsafe(SECRETS_LENGTH),
            'cve_id': cve,
            'description': '',
            'exploitabilityScore': None,
            'impactScore': None,
        })
    return cves