import json
from pprint import pprint

from app.helper.cpe import cpe_to_dict
from app.model.risk_assessment import RiskAssessmentSave
from app.repository.cpe import CPERepository
from app.services.cve import CVEService
from app.services.graph import GraphService
from app.services.nvd import NVDService
from core.bayes.model.network import BayesianNetwork

from .base import *
from app.model.countermeasure import *
from app.repository.deployment_scenario import *
from app.repository.system_profile import SystemProfileRepository
from app.repository.cves import CVERepository
from app.repository.risk_assessment import RiskAssessmentRepository

deployment_scenarios_router = APIRouter(
    prefix='/api/deployment_scenarios', tags=['Deployment scenarios'])

# Mapping asset to CPE
@deployment_scenarios_router.get('/mapping_cpe')
async def mapping_cpe(keyword: str = ''):
    # cpes = NVDService.get_cpe_by_keyword(keyword)
    cpes = await CPERepository.guess_cpe(keyword)
    results = []
    print(cpes)
    for cpe in cpes:
        results.append(cpe_to_dict(cpe['name']))
    return {
        'status': True,
        'cpes': results
    }

# Mapping CPE to CVE
@deployment_scenarios_router.get('/mapping_cve')
async def mapping_cve(cpe_name: str = ''):

    cves = await CVERepository.get({
        'cpe': {
            '$in': [cpe_name]
        }
    }, select=['cve_id', 'description', 'impact'], page_size=MAX_SIZE_LIST)

    return {
        'status': True,
        'cves': cves
    }

# Get deployment scenarios
@deployment_scenarios_router.get('')
async def index(request: Request, user: dict = Depends(get_current_user)):
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)
    condition = add_created_by(condition, user['id'])
    data = await DeploymentScenarioRepository.get(condition, current, page_size, select=['name', 'description', 'created_at', 'updated_at', 'status', 'system_profile'])

    # q = add_created_by({}, user['id'])
    # system_profiles = await SystemProfileRepository.get(q, page_size=MAX_SIZE_LIST)
    # for ds in data:
    #     ds['system_profile'] = next(
    #         (item for item in system_profiles if item['id'] == ds['system_profile_id']), None)

    count = await DeploymentScenarioRepository.count(condition)
    return BaseResponse(
        data=data,
        options={
            'total': count,
            'pageSize': page_size,
            'current': current,
        }
    )

# Get deployment scenario
@deployment_scenarios_router.get('/{id}')
async def show(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id, select=['asset_relationships', 'assets', 'countermeasures', 'description', 'name', 'security_goals', 'status', 'system_profile_id', 'target', 'exploitability', 'remediation_level', 'report_confidence'])
    if target:
        if target['created_by'] == user['id']:
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


# Update deployement scenario
@deployment_scenarios_router.put('/{id}')
async def update(id: str, request: UpdateDeploymentScenario, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id, select=['name', 'status'])
    if target:
        if target['created_by'] == user['id']:
            request = jsonable_encoder(request)
            request = update_by_user_request(request, user['id'])
            if target['name'] == request['name']:
                pass
            else:
                same_name = await DeploymentScenarioRepository.get({
                    'name': request['name'],
                    'created_by': ObjectId(user['id']),
                })
                if len(same_name) > 0:
                    raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                        'Deployment scenario name is existed'
                    ])

            if request['status'] == DeploymentScenarioStatus.OPERATIONS.value:
                if target['status'] != DeploymentScenarioStatus.DEPLOYMENTS.value:
                    raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                        "Can't switch to stage"
                    ])
            if request['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                if target['status'] != DeploymentScenarioStatus.REQUIREMENTS_ANALYSIS.value:
                    raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                        "Can't switch to stage"
                    ])
            await DeploymentScenarioRepository.update(target['id'], request)
            return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Update deployment scenario
@deployment_scenarios_router.post('')
async def create(request: DeploymentScenarioCreate, user: dict = Depends(get_current_user)):
    # TODO: validator
    request = jsonable_encoder(request)
    request = create_by_user_request(request, user['id'])
    if await check_exists(request, user):
        raise CustomHTTPException(
            STATUS_422_INVALID_PARAMETER,
            errors=[{
                'name': 'exists',
            }]
        )
    request['system_profile_id'] = ObjectId(request['system_profile_id'])
    cves = []
    active = {}
    for asset in request['assets']:
        cves.append({
            'asset_id': asset['id'],
            'cves': [],
        })
        active[asset['id']] = []
    request['cves'] = cves
    request['active'] = active
    request['attack_graph'] = {}
    request['target'] = {}
    request['attackers'] = []
    request['exploitability'] = ExploitabilityCVSS.H.value
    request['remediation_level'] = RemediationLevelCVSS.U.value
    request['report_confidence'] = ReportConfidenceCVSS.C.value
    target = await DeploymentScenarioRepository.create(request)
    return BaseResponse(target)

# CRUD Attacker
@deployment_scenarios_router.get('/{id}/attackers')
async def show(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            if 'attackers' in target:
                return BaseResponse(
                    data=target['attackers']
                )
            return BaseResponse(
                data=[]
            )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


@deployment_scenarios_router.post('/{id}/attackers')
async def update(id: str, request: AttackerCreate, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            request = jsonable_encoder(request)
            payload = update_by_user_request({}, user['id'])
            request['id'] = generator_id()
            if 'attackers' in target:
                payload['attackers'] = target['attackers'] + [request]
            else:
                payload['attackers'] = [request]
            if target['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                payload['attack_graph'] = {}
                payload['target'] = {}
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

@deployment_scenarios_router.delete('/{id}/attackers/{attacker_id}')
async def delete_attacker(id: str, attacker_id: str, user: dict = Depends(get_current_user)):
    is_valid_id(attacker_id)
    target = await get_item_by_id(DeploymentScenarioRepository, id, user, select=['attackers', 'status'])
    payload = update_by_user_request({}, user['id'])
    if 'attackers' in target:
        flag = False
        for index, attacker in enumerate(target['attackers']):
            if attacker['id'] == attacker_id:
                flag = True
                del target['attackers'][index]
                break
        if flag:
            payload['attackers'] = target['attackers']
            if target['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                payload['attack_graph'] = {}
                payload['target'] = {}
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()
    
    return CustomHTTPException(STATUS_404_NOT_FOUND)


@deployment_scenarios_router.put('/{id}/attackers/{attacker_id}')
async def update_attacker(id: str, attacker_id: str, request: AttackerUpdate, user: dict = Depends(get_current_user)):
    is_valid_id(attacker_id)
    target = await get_item_by_id(DeploymentScenarioRepository, id, user, select=['attackers', 'status'])
    request = jsonable_encoder(request)
    payload = update_by_user_request({}, user['id'])
    if 'attackers' in target:
        flag = False
        for index, attacker in enumerate(target['attackers']):
            if attacker['id'] == attacker_id:
                flag = True
                target['attackers'][index] = {
                    **request,
                    'id': attacker_id,
                }
                break
        if flag:
            payload['attackers'] = target['attackers']
            if target['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                payload['attack_graph'] = {}
                payload['target'] = {}
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()
    
    return CustomHTTPException(STATUS_404_NOT_FOUND)


# Create cves of asset
@deployment_scenarios_router.post('/{id}/assets/{asset_id}/cves')
async def update(id: str, asset_id: str, request: UpdateCVEOnAsset, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        payload = update_by_user_request({}, user['id'])
        flag = False
        for index, asset in enumerate(target['assets']):
            if asset['id'] == asset_id:
                payload['cves'] = target['cves']
                for i, cve in enumerate(payload['cves']):
                    if cve['asset_id'] == asset_id:
                        payload['cves'][i] = {
                            'asset_id': asset_id,
                            'cves': request['cves'],
                        }
                flag = True
                break
        if flag:
            if target['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                payload['attack_graph'] = {}
                payload['target'] = {}
            target = await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Update cve of asset
@deployment_scenarios_router.put('/{id}/assets/{asset_id}')
async def update(id: str, asset_id: str, request: AssetInDeploymentScenario, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        payload = update_by_user_request({}, user['id'])
        flag = False
        payload['assets'] = target['assets']
        for index, asset in enumerate(payload['assets']):
            if asset['id'] == asset_id:
                payload['assets'][index] = request
                payload['cves'] = target['cves']
                if 'active' in target:
                    payload['active'] = target['active']
                    if asset_id in target['active']:
                        payload['active'][asset_id] = []
                for i, cve in enumerate(payload['cves']):
                    if cve['asset_id'] == asset_id:
                        cves = await CVERepository.get({
                            'cpe': {
                                '$in': [request['cpe']]
                            }
                        }, select=['cve_id', 'cwe_id', 'description', 'attackVector', 'impact', 'condition', 'status'], page_size=MAX_SIZE_LIST)

                        tmp_cves = []

                        for t, cve in enumerate(cves):
                            tmp_cve = {}
                            tmp_cve['cve_id'] = cve['cve_id']
                            tmp_cve['cwe_id'] = cve['cwe_id']
                            tmp_cve['description'] = cve['description']
                            tmp_cve['impact'] = cve['impact']
                            tmp_cve['attack_vector'] = cve['attackVector']
                            tmp_cve['condition'] = cve['condition'][asset['part']]
                            tmp_cves.append(tmp_cve)

                        payload['cves'][i] = {
                            'asset_id': asset_id,
                            'cves': tmp_cves,
                        }
                flag = True
                break
        if flag:
            target = await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Create cve of assets
@deployment_scenarios_router.post('/{id}/assets/{asset_id}/cves/{cve_id}')
async def update(id: str, asset_id: str, cve_id: str, request: CVEOnAsset, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        payload = update_by_user_request({}, user['id'])
        flag = False
        for index, asset in enumerate(target['cves']):
            if asset['asset_id'] == asset_id:
                for i, cve in enumerate(asset['cves']):
                    if cve['cve_id'] == cve_id:
                        payload[f'cves.{index}.cves.{i}'] = request
                        flag = True
                        break
                break
        if flag:
            target = await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Update cve of asset
@deployment_scenarios_router.put('/{id}/assets/{asset_id}/cves')
async def update(id: str, asset_id: str, request: UpdateCVEOnAsset, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        request = jsonable_encoder(request)
        payload = update_by_user_request({}, user['id'])
        flag = False
        for index, asset in enumerate(target['cves']):
            if asset['asset_id'] == asset_id:
                cves_request = [cve['cve_id'] for cve in request['cves']]
                for i, cve in enumerate(asset['cves']):
                    if cve['cve_id'] in cves_request:
                        payload[f'cves.{index}.cves.{i}'] = next(
                            (x for x in request['cves'] if x['cve_id'] == cve['cve_id']))
                flag = True
                break
        if flag:
            if target['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                payload['attack_graph'] = {}
                payload['target'] = {}
            target = await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse(target)

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


# CRUD Countermeasures

@deployment_scenarios_router.get('/{id}/countermeasures')
async def get_countermeasures(id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            skip = page_size*(current-1)
            limit = page_size
            return BaseResponse(
                data=target['countermeasures'][skip: skip + limit],
                options={
                    'total': len(target['countermeasures']),
                    'pageSize': page_size,
                    'current': current,
                }
            )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


@deployment_scenarios_router.post('/{id}/countermeasures')
async def update(id: str, request: CountermeasureInDeploymentScenarioCreate, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            request = jsonable_encoder(request)
            payload = update_by_user_request({}, user['id'])
            request['id'] = generator_id()
            if 'countermeasures' in target:
                payload['countermeasures'] = target['countermeasures'] + [request]
            else:
                payload['countermeasures'] = [request]
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

@deployment_scenarios_router.delete('/{id}/countermeasures/{countermeasure_id}')
async def delete_attacker(id: str, countermeasure_id: str, user: dict = Depends(get_current_user)):
    is_valid_id(countermeasure_id)
    target = await get_item_by_id(DeploymentScenarioRepository, id, user, select=['countermeasures', 'status'])
    payload = update_by_user_request({}, user['id'])
    if 'countermeasures' in target:
        flag = False
        for index, attacker in enumerate(target['countermeasures']):
            if attacker['id'] == countermeasure_id:
                flag = True
                del target['countermeasures'][index]
                break
        if flag:
            payload['countermeasures'] = target['countermeasures']
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()
    
    return CustomHTTPException(STATUS_404_NOT_FOUND)


@deployment_scenarios_router.put('/{id}/countermeasures/{countermeasure_id}')
async def update_attacker(id: str, countermeasure_id: str, request: CountermeasureInDeploymentScenarioUpdate, user: dict = Depends(get_current_user)):
    is_valid_id(countermeasure_id)
    target = await get_item_by_id(DeploymentScenarioRepository, id, user, select=['countermeasures', 'status'])
    request = jsonable_encoder(request)
    payload = update_by_user_request({}, user['id'])
    if 'countermeasures' in target:
        flag = False
        for index, attacker in enumerate(target['countermeasures']):
            if attacker['id'] == countermeasure_id:
                flag = True
                target['countermeasures'][index] = {
                    **request,
                    'id': countermeasure_id,
                }
                break
        if flag:
            payload['countermeasures'] = target['countermeasures']
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()
    
    return CustomHTTPException(STATUS_404_NOT_FOUND)



# Get asset
@deployment_scenarios_router.get('/{id}/assets')
async def get_assets(id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            skip = page_size*(current-1)
            limit = page_size
            return BaseResponse(
                data={
                    'assets': target['assets'][skip: skip + limit],
                    'active': target['active'],
                },
                options={
                    'total': len(target['assets']),
                    'pageSize': page_size,
                    'current': current,
                }
            )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Get AG
@deployment_scenarios_router.get('/{id}/attack_graph')
async def get_attack_graph(id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            if 'attackers' not in target:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    'Please setup Attacker'
                ])
            active = target['active']
            cves_active = []
            for vuls_asset in target['cves']:
                asset_id = vuls_asset['asset_id']
                asset = next(
                    (x for x in target['assets'] if x['id'] == asset_id))
                cves = []
                for cve in vuls_asset['cves']:
                    if cve['cve_id'] in active[asset_id]:
                        if cve['condition']['preCondition'] == '' or cve['condition']['postCondition'] == '' or cve['attack_vector'] == '':
                            raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                                'Please setting all value of CVE on Asset'
                            ])
                        cves.append(cve)
                cves_active.append({
                    'asset_id': asset_id,
                    'cves': cves,
                    'asset_name': asset['name'],
                })

            if 'attack_graph' in target:
                if target['attack_graph'] != {}:
                    return BaseResponse(
                        options={
                            'attack_graph': target['attack_graph'],
                            'cves': cves_active,
                            'attackers': target['attackers'],
                        }
                    )
            target['cves'] = cves_active
            attackers = [attacker['name'] for attacker in target['attackers']]
            graph = GraphService.generation_attack_graph(target)
            results = {
                'nodes': [],
                'edges': [],
            }
            index = 0
            for node in graph['nodes']:
                if node in attackers:
                    attacker_id = 0
                    for attacker in target['attackers']:
                        if attacker['name'] == node:
                            attacker_id = attacker['id']
                            break
                    label = node
                    style = {
                        'type': 'node',
                        'shape': 'flow-circle',
                        'is_attacker': True,
                        'color': '#FA8C16',
                        'attacker_id': attacker_id,
                    }
                else:
                    tmp = node.split('_')
                    label = tmp[1]
                    style = {
                        'type': 'node',
                        'shape': 'flow-capsule',
                        'is_attacker': False,
                        'color': '#722ED1',
                        'asset_id': tmp[0],
                        'cve_id': label,
                    }
                results['nodes'].append({
                    'id': f"{index}",
                    'label': label,
                    **style,
                })
                index += 1

            for edge in graph['edges']:
                results['edges'].append({
                    'id': f"{index}",
                    'source': f"{graph['nodes'].index(edge['source'])}",
                    'target': f"{graph['nodes'].index(edge['target'])}",
                })
                index += 1

            attack_graph = GraphService.generate_coordinates(
                results, ranksep=0.25, nodesep = 0.25)
            return BaseResponse(
                options={
                    'attack_graph': attack_graph,
                    'cves': cves_active,
                    'attackers': target['attackers'],
                }
            )

            # return BaseResponse(
            #     options={
            #         'attack_graph': data['attack_graph'],
            #     }
            # )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Create AG
@deployment_scenarios_router.post('/{id}/attack_graph')
async def create_attack_graph(id: str, request: UpdateAttackGraph, user: dict = Depends(get_current_user)):
    is_valid_id(id)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            payload = update_by_user_request({}, user['id'])
            payload['attack_graph'] = request.attack_graph
            payload['target'] = request.target
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Get CVE in AG
@deployment_scenarios_router.get('/{id}/attack_graph/cves')
async def get_cves_on_attack_graph(id: str, user = Depends(get_current_user)):
    is_valid_id(id)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        assets = []
        for asset in target['assets']:
            assets.append({
                'id': asset['id'],
                'name': asset['name'],
            })
        if target['attack_graph']:
            if 'nodes' in target['attack_graph']:
                nodes = target['attack_graph']['nodes']
                cves = []
                for node in nodes:
                    if not node['is_attacker']:
                        cves.append({
                            'cve_id': node['cve_id'],
                            'asset_id': node['asset_id'],
                        })
                return BaseResponse(
                    data={
                        'cves': cves,
                        'assets': assets,
                    }
                )
                
            return BaseResponse([])
    
    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Create CVE in AG
@deployment_scenarios_router.post('/{id}/attack_graph/assets/{asset_id}/cves')
async def create_cves_on_asset(id: str, asset_id: str, request: CVEOnAttackGraph, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            payload = update_by_user_request({}, user['id'])
            if 'active' in target:
                payload['active'] = target['active']
                payload['active'] = {
                    **target['active'],
                    asset_id: request.cves
                }
            else:
                payload['active'] = {
                    asset_id: request.cves
                }
            if target['status'] == DeploymentScenarioStatus.DEPLOYMENTS.value:
                payload['attack_graph'] = {}
                payload['target'] = {}
            await DeploymentScenarioRepository.update(id, payload)
            return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Get CVE active in Asset
@deployment_scenarios_router.get('/{id}/attack_graph/assets/{asset_id}/cves')
async def get_cves_active_on_asset(id: str, asset_id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            flag = False
            all_cves = []
            for asset in target['cves']:
                if asset['asset_id'] == asset_id:
                    all_cves = asset['cves']
                    flag = True
            if flag:
                cves_id = target['active'][asset_id]
                results = []
                for cve in all_cves:
                    if cve['cve_id'] in cves_id:
                        results.append(cve)
                return BaseResponse(
                    data=results
                )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Get CVE in asset
@deployment_scenarios_router.get('/{id}/assets/{asset_id}/cves')
async def get_cves_on_asset(id: str, asset_id: str, request: Request, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    is_valid_id(asset_id)
    params = dict(request.query_params)
    current, page_size, condition = parse_query_params(params)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            cves = []
            for asset in target['cves']:
                if asset['asset_id'] == asset_id:
                    cves = asset['cves']
            skip = page_size*(current-1)
            limit = page_size
            return BaseResponse(
                data=cves[skip: skip + limit],
                options={
                    'total': len(cves),
                    'pageSize': page_size,
                    'current': current,
                }
            )

    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Delete deployment scenario
@deployment_scenarios_router.delete('/{id}')
async def delete(id: str, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] != user['id']:
            raise CustomHTTPException(STATUS_404_NOT_FOUND)
        target = await DeploymentScenarioRepository.delete(id)
        return BaseResponse(status=target)
    raise CustomHTTPException(STATUS_404_NOT_FOUND)

# Create assessment
@deployment_scenarios_router.post('/{id}/assessment')
async def risk_assessment(id: str, request: StaticAssessment, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    request = jsonable_encoder(request)

    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            if target['status'] != DeploymentScenarioStatus.DEPLOYMENTS.value and target['status'] != DeploymentScenarioStatus.REQUIREMENTS_ANALYSIS.value:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    f"Please move the deployment scenario to stage '{DeploymentScenarioStatus.DEPLOYMENTS.value}' or '{DeploymentScenarioStatus.REQUIREMENTS_ANALYSIS.value}' before assessment."
                ])
            if 'attack_graph' not in target:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    "Please setup attack graph"
                ])
            if target['attack_graph'] == {}:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    "Please setup attack graph"
                ])

            attack_graph = target['attack_graph']
            base_impact = request['damage_criterion']
            base_benefit = request['benefit_criterion']
            exploitability =  request['exploitability']
            remediation_level = request['remediation_level']
            report_confidence = request['report_confidence']
            network1 = BayesianNetwork(deployment_scenario=target, attack_graph=attack_graph,
                                       base_impact=base_impact, base_benefit=base_benefit, 
                                       exploitability=exploitability, remediation_level=remediation_level,report_confidence=report_confidence,)
            network2 = BayesianNetwork(deployment_scenario=target, attack_graph=attack_graph,
                                       base_impact=base_impact, base_benefit=base_benefit, countermeasures=False,
                                       exploitability=exploitability, remediation_level=remediation_level,report_confidence=report_confidence,)

            payload = update_by_user_request({}, user['id'])
            payload['base_impact'] = base_impact
            payload['base_benefit'] = base_benefit
            payload['exploitability'] = exploitability
            payload['remediation_level'] = remediation_level
            payload['report_confidence'] = report_confidence

            await DeploymentScenarioRepository.update(id, payload)

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

# Save assessment
@deployment_scenarios_router.post('/{id}/save_assessment')
async def save_risk_assessment(id: str, request: RiskAssessmentSave, user: dict = Depends(get_current_user)):
    is_valid_id(id)
    request = jsonable_encoder(request)
    target = await DeploymentScenarioRepository.find(id)
    if target:
        if target['created_by'] == user['id']:
            if target['status'] != DeploymentScenarioStatus.DEPLOYMENTS.value and target['status'] != DeploymentScenarioStatus.REQUIREMENTS_ANALYSIS.value:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    f"Please move the deployment scenario to stage '{DeploymentScenarioStatus.DEPLOYMENTS.value}' or '{DeploymentScenarioStatus.REQUIREMENTS_ANALYSIS.value}' before assessment."
                ])
            if 'attack_graph' not in target or 'target' not in target or 'base_impact' not in target or 'base_benefit' not in target:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    "Please setup attack graph, base_impact, base_benefit"
                ])
            if target['attack_graph'] == {}:
                raise CustomHTTPException(STATUS_422_INVALID_PARAMETER, errors=[
                    "Please setup attack graph"
                ])

            attack_graph = target['attack_graph']
            base_impact = target['base_impact']
            base_benefit = target['base_benefit']
            exploitability =  target['exploitability']
            remediation_level = target['remediation_level']
            report_confidence = target['report_confidence']
            network1 = BayesianNetwork(deployment_scenario=target, attack_graph=attack_graph,
                                       base_impact=base_impact, base_benefit=base_benefit, 
                                       exploitability=exploitability, remediation_level=remediation_level,report_confidence=report_confidence,)
            network2 = BayesianNetwork(deployment_scenario=target, attack_graph=attack_graph,
                                       base_impact=base_impact, base_benefit=base_benefit, countermeasures=False,
                                       exploitability=exploitability, remediation_level=remediation_level,report_confidence=report_confidence,)



            payload = create_by_user_request({}, user['id'])
            cves = []
            for asset_id in target['active']:
                cve_ids = []
                for asset_cves in target['cves']:
                    if asset_cves['asset_id'] == asset_id:
                        for cve in asset_cves['cves']:
                            if cve['cve_id'] in target['active'][asset_id]:
                                cve_ids.append(cve)
                        break
                cves.append({
                    'asset_id': asset_id,
                    'cves': cve_ids
                })
            del target['cves']
            payload['deployment_scenario'] = {
                **target,
                'cves': cves
            }
            cia_countermeasures = network1.get_cia_assets()
            cia_not_countermeasures = network2.get_cia_assets()
            likelihood_countermeasures = network1.get_likelihood()
            likelihood_not_countermeasures = network2.get_likelihood()

            severity_countermeasures = get_severity(cia_countermeasures)
            severity_not_countermeasures = get_severity(cia_not_countermeasures)

            likelihood_countermeasures = get_likelihood(likelihood_countermeasures)
            likelihood_not_countermeasures = get_likelihood(likelihood_not_countermeasures)
            
            payload['result'] = {
                'countermeasures': network1.get_decisions(),
                'cia': {
                    'countermeasures': cia_countermeasures,
                    'not_countermeasures': cia_not_countermeasures,
                },
                'likelihood': {
                    'countermeasures': likelihood_countermeasures,
                    'not_countermeasures': likelihood_not_countermeasures,
                },
                'risk': {
                    'severity': {
                        'countermeasures': severity_countermeasures,
                        'not_countermeasures': severity_not_countermeasures,
                    },
                    'likelihood': {
                        'countermeasures': likelihood_countermeasures,
                        'not_countermeasures': likelihood_not_countermeasures,
                    },
                    'risk_level': {
                        'countermeasures': get_risk_level(severity_countermeasures[1], likelihood_countermeasures[1]),
                        'not_countermeasures': get_risk_level(severity_not_countermeasures[1], likelihood_not_countermeasures[1]),
                    },
                }
            }

            payload['name'] = request['name']

            await RiskAssessmentRepository.create(payload)

            return BaseResponse()

    raise CustomHTTPException(STATUS_404_NOT_FOUND)


# Scan CVE
@deployment_scenarios_router.post('/${id}/scan_vulnerability')
async def scan_vulnerability(id: str, user: dict = Depends(get_current_user)):
    await get_item_by_id(DeploymentScenarioRepository, id, user)
    return await CVEService.scan_vulneraibility(id)



async def check_exists(request, user):
    target = await DeploymentScenarioRepository.get({
        'name': {
            '$regex': f"^{request['name']}$",
            '$options': 'i',
        },
        'created_by': ObjectId(user['id']),
        'system_profile_id': ObjectId(request['system_profile_id']),
    })
    if target:
        return True
    return False


def get_severity(cia: list):
    severity = 0
    for i in range(len(cia)):
        severity += cia[i]['cia']
    severity /= len(cia)
    severity = 9 - severity
    
    print(severity)
    if severity <= 1.8:
        return ['Negligible', 1]
    if severity <= 3.6:
        return ['Low', 2]
    if severity <= 5.4:
        return ['Moderate', 3]
    if severity <= 7.2:
        return ['Significant', 4]
    return ['Catastrophic', 5]

def get_likelihood(likelihood: dict):
    lh = likelihood['outcomes']['True']
    if lh <= 0.2:
        return ['Improbable', 1]
    if lh <= 0.4:
        return ['Remote', 2]
    if lh <= 0.6:
        return ['Occsional', 3]
    if lh <= 0.8:
        return ['Probale', 4]
    return ['Frequent', 5]

def get_risk_level(severity: int, likelihood: int):
    le = severity * likelihood
    if le > 12:
        return ['Critical', 4]
    if le > 7:
        return ['High', 3]
    if le > 3:
        return ['Medium', 2]
    return ['Low', 1]