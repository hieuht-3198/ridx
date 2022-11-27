import pprint

from app.repository.deployment_scenario import DeploymentScenarioRepository
from app.services.cve import CVEService
from core.bayes.model.inetwork import exploitability_cvss, report_confidence_cvss, remediation_level_cvss
from core.bayes.model.network import BayesianNetwork, DynamicBayesianNetwork
from core.bayes.model.node import NODE_CPT_TRUE
from core.bayes.test_2 import reverse_reasoning

from .base import *
from app.repository.risk_monitoring import RiskMonitoringRepository
from ..model.deployment_scenario import DeploymentScenarioStatus, ThreatType
from ..model.risk_monitoring import DetectThreat, InitRiskMonitoring
from ..repository.cves import CVERepository
from ..services.cwe import MAPPING_CWE_STRIDE

risk_monitoring_router = APIRouter(
    prefix='/api/risk_monitoring',
    tags=['Risk monitoring'],
)

# Scan CVE
@risk_monitoring_router.post('/{id}/scan_vulnerability')
async def scan_vulnerability(id: str, user: dict = Depends(get_current_user)):
    await get_item_by_id(DeploymentScenarioRepository, id, user)
    results = await CVEService.scan_vulneraibility(id)
    return BaseResponse(
        options={
            **results
        }
    )

# Get AG
@risk_monitoring_router.get('/{id}/monitoring/attack_graph_cve')
async def get_asset_cves_in_attack_graph(id: str, user: dict = Depends(get_current_user)):
    target = await get_deployment_scenario(id, user)
    tmp_cves = {}
    for node in target['attack_graph']['nodes']:
        if not node['is_attacker']:
            if node['asset_id'] in tmp_cves:
                tmp_cves[node['asset_id']] = tmp_cves[node['asset_id']] + [node['cve_id']]
            else:
                tmp_cves[node['asset_id']] = [node['cve_id']]
    all_assets = []
    for asset in target['assets']:
        if asset['id'] in tmp_cves:
            all_assets.append({
                'asset_id': asset['id'],
                'asset_name': asset['name'],
                'cves': tmp_cves[asset['id']]
            })
        else:
            all_assets.append({
                'asset_id': asset['id'],
                'asset_name': asset['name'],
                'cves': []
            })

    return BaseResponse(
        data=all_assets
    )


# Filling param monitoring 
@risk_monitoring_router.post('/{id}/monitoring')
async def monitoring(id: str, request: InitRiskMonitoring, user: dict = Depends(get_current_user)):
    target = await get_deployment_scenario(id, user)
    request = jsonable_encoder(request)
    attack_graph = target['attack_graph']
    base_impact = target['base_impact']
    base_benefit = target['base_benefit']
    if request['node_temporals'] == ['All']:
        tmp = []
        for asset in target['active']:
            tmp.append({
                'asset_id': asset,
                'cves': target['active'][asset],
            })
        target['temporal_node'] = tmp
    else:
        target['temporal_node'] = request['node_temporals']
    
    exploitability =  target['exploitability']
    remediation_level = target['remediation_level']
    report_confidence = target['report_confidence']

    network1 = DynamicBayesianNetwork(
        deployment_scenario=target,
        attack_graph=attack_graph,
        base_impact=base_impact,
        base_benefit=base_benefit,
        time_step=request['time_step'],
        observer_data=request['observer_data'],
        exploitability=exploitability, 
        remediation_level=remediation_level,
        report_confidence=report_confidence,
    )

    return {
        'status': True,
        'data': {
            'countermeasures': network1.get_decisions(),
            'cia': network1.get_cia_assets(),
            'likelihood': network1.get_likelihood(),
            'security_goals': target['security_goals'],
        }
    }


async def get_deployment_scenario(id, user, select = []):
    target = await get_item_by_id(DeploymentScenarioRepository, id, user, select)
    if target['status'] != DeploymentScenarioStatus.OPERATIONS.value:
        raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
            f"Please move the deployment scenario to stage '{DeploymentScenarioStatus.OPERATIONS.value}' before monitoring."
        ])
    return target

# Detect threat
@risk_monitoring_router.post('/{id}/detect_threat')
async def detect_threat(id: str, request: DetectThreat, user: dict = Depends(get_current_user) ):
    is_valid_id(id)

    target = await get_deployment_scenario(id, user)

    request = jsonable_encoder(request)
    request['time_step'] = 2
    request['observer_data'] = []
    request['node_temporals'] = ['All']

    flag = False
    for node in target['attack_graph']['nodes']:
        if not node['is_attacker']:
            if node['cve_id'] == request['cve_id'] and node['asset_id'] == request['asset_id']:
                flag = True
                break
    
    if not flag:
        raise CustomHTTPException(STATUS_404_NOT_FOUND)

    attack_graph = target['attack_graph']
    base_impact = target['base_impact']
    base_benefit = target['base_benefit']
    if request['node_temporals'] == ['All']:
        tmp = []
        for asset in target['active']:
            tmp.append({
                'asset_id': asset,
                'cves': target['active'][asset],
            })
        target['temporal_node'] = tmp
    else:
        target['temporal_node'] = request['node_temporals']

    exploitability = exploitability_cvss.get(target['exploitability'], 1.00)
    remediation_level = remediation_level_cvss.get(target['remediation_level'], 1.00)
    report_confidence = report_confidence_cvss.get(target['report_confidence'], 1.00)

    network1 = DynamicBayesianNetwork(
        deployment_scenario=target,
        attack_graph=attack_graph,
        base_impact=base_impact,
        base_benefit=base_benefit,
        time_step=request['time_step'],
        observer_data=request['observer_data'],
        exploitability=target['exploitability'],
        remediation_level=target['remediation_level'],
        report_confidence=target['report_confidence'],
    )

    node_handle = -1
    for handle in network1.nodes:
        if not network1.nodes[handle].is_attacker:
            if network1.nodes[handle].cve_id == request['cve_id'] and network1.nodes[handle].asset_id == request['asset_id']:
                node_handle = handle
                break
    if node_handle == -1:
        raise CustomHTTPException(STATUS_404_NOT_FOUND)
    
    output = network1.get_posteriors(node_handle)
    number_parents = len(network1.network.get_parents(node_handle))
    cve = False
    for a_i in target['cves']:
        if a_i['asset_id'] == request['asset_id']:
            for c in a_i['cves']:
                if c['cve_id'] == request['cve_id']:
                    cve = c
                    break
        if cve:
            break

    exploitability_score = cve['impact']['baseMetricV2']['exploitabilityScore'] * exploitability * remediation_level * report_confidence
    prob = exploitability_score / 10

    mer_pob = 1 - pow(1 - prob, number_parents)
    all_pro = 1 - pow(1 - prob, number_parents + 1)
    cpts_merge = [all_pro, prob, mer_pob, 0]
    # print(network1.network.get_node_def)
    # merge node
    k = reverse_reasoning(
        parent_real=0,
        obs=output['outcomes'][1][NODE_CPT_TRUE],
        cpts=cpts_merge
    )
    m = reverse_reasoning(
        parent_real=k,
        obs=request['observer_probability'],
        cpts=[all_pro, mer_pob, prob, 0]
    )

    cve = await CVERepository.get_cves_by_cve_id([request['cve_id']])
    cwe_id = cve[0]['cwe_id']


    return BaseResponse(
        data={
            "est": m,
            "outcomes": output['outcomes'],
            "cwe_id": cwe_id,
            "threat_types": MAPPING_CWE_STRIDE.get(cwe_id, [ThreatType.SPOOFING_IDENTITY, ThreatType.TAMPERING_WITH_DATA, ThreatType.REPUDIATION_THREATS, ThreatType.INFORMATION_DISCLOSURE, ThreatType.DENIAL_OF_SERVICE, ThreatType.ELEVATION_OF_PRIVILEGES])
        }
    )

