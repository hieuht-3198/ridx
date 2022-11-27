from unittest import result
from app.model.deployment_scenario import DeploymentScenario, DeploymentScenarioSchema, DeploymentScenarioStatus, StaticAssessment
from app.repository.deployment_scenario import DeploymentScenarioRepository
from core.bayes.model.network import BayesianNetwork

from .base import *
from app.repository.risk_assessment import RiskAssessmentRepository

risk_assessment_router = APIRouter(
    prefix='/api/risk_assessment', tags=['Risk assessment'])

# Get assessment
@risk_assessment_router.get('/{id}')
async def show(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await RiskAssessmentRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


# Create assessment

@risk_assessment_router.post('/{id}')
async def risk_assessment(id: str, request: StaticAssessment, user: dict = Depends(get_current_user)):
    is_valid_id(id)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            if target['status'] != DeploymentScenarioStatus.DEPLOYMENTS.value:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    f"Please move the deployment scenario to stage '{DeploymentScenarioStatus.DEPLOYMENTS.value}' before assessment."
                ])
            if 'attack_graph' not in target or 'base_impact' not in target or 'base_benefit' not in target:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    "Please assessment"
                ])
            if target['attack_graph'] == {}:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    "Please setup attack graph"
                ])

            attack_graph = target['attack_graph']
            base_impact = request.damage_criterion
            base_benefit = request.benefit_criterion
            network1 = BayesianNetwork(deployment_scenario=target ,attack_graph=attack_graph, base_impact=base_impact, base_benefit=base_benefit)
            network2 = BayesianNetwork(deployment_scenario=target ,attack_graph=attack_graph, base_impact=base_impact, base_benefit=base_benefit, countermeasures=False)

            return {
                'status': True,
                'data': {
                    'countermeasures': network1.get_decisions(),
                    'not_countermeasures': network2.get_decisions(),
                    'cia': {
                        'countermeasures': network1.get_cia_assets(),
                        'not_countermeasures': network2.get_cia_assets(),
                    },
                    'likelihood': {
                        'countermeasures': network1.get_likelihood(),
                        'not_countermeasures': network2.get_likelihood(),
                    },
                    'assets': target['assets'],
                    'security_goals': target['security_goals'],
                }
            }

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Get assessment of deployment scenario
@risk_assessment_router.get('/deployment_scenarios/{id}')
async def index(id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition = add_created_by(condition, user['id'])
    condition['deployment_scenario.id'] = id
    
    data = await RiskAssessmentRepository.get(condition, current, page_size, select=['name', 'result', 'created_at', 'updated_at'])
    count = await RiskAssessmentRepository.count(condition)

    return BaseResponse(
        data=data,
        options={
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

