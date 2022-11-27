// @ts-ignore

import api from "@/services/api";

/* eslint-disable */

export async function getSystemProfilesWithDeploymentScenarios(params, options) {
  return api('/api/system_profiles/deployment_scenarios', {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function generateCoordinates(body, options) {
  return api(`/api/helper/generate_coordinates`, {
    method: 'POST',
    data: body,
    ...(options || {}),
  });
}

export async function getDeploymentScenarioBySystemProfile(system_profile_id, params, options) {
  return api(`/api/system_profiles/${system_profile_id}/deployment_scenarios`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function postScanVulnerability(deployment_scenario_id, body, options) {
  return api(`/api/risk_monitoring/${deployment_scenario_id}/scan_vulnerability`, {
    method: 'POST',
    data: body,
    ...(options || {}),
  });
}