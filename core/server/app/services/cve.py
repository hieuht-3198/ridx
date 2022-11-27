from app.model.deployment_scenario import DeploymentScenarioStatus
from app.repository.base import MAX_SIZE_LIST
from app.repository.cves import CVERepository
from app.repository.deployment_scenario import DeploymentScenarioRepository


class CVEService:

    async def get_cve_id_by_cpe(cpe_name):
        return await CVERepository.get({
            'cpe': {
                '$in': [cpe_name]
            }
        }, select=['cve_id'], page_size=MAX_SIZE_LIST)

    async def scan_vulneraibility(deployment_scenario_id):
        print('Start scan')
        deployment_scenario = await DeploymentScenarioRepository.find(deployment_scenario_id)
        assets = {}
        for asset in deployment_scenario['assets']:
            assets[asset['id']] = {
                'cpe': asset['cpe'],
            }
        for asset_cve in deployment_scenario['cves']:
            cves = [cve['cve_id'] for cve in asset_cve['cves']]
            assets[asset_cve['asset_id']] = {
                **assets[asset_cve['asset_id']],
                'cves': cves,
            }
        new_cves = []
        remove_cves = []
        print('Number Asset:', len(assets))
        for asset_id in assets:
            cves = await CVEService.get_cve_id_by_cpe(assets[asset_id]['cpe'])
            print('Asset_id: ', asset_id)
            cves = [cve['cve_id'] for cve in cves]
            new_cves.append({
                'asset_id': asset_id,
                'cves': [cve_id for cve_id in cves if cve_id not in assets[asset_id]['cves']],
            })
            remove_cves.append({
                'asset_id': asset_id,
                'cves': [cve_id for cve_id in assets[asset_id]['cves'] if cve_id not in cves],
            })        
        return {
            'new_cves': new_cves,
            'remove_cves': remove_cves,
            'assets': deployment_scenario['assets'],
        }