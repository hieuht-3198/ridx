// @ts-ignore

import api from "@/services/api";

/* eslint-disable */

export async function getAssessments(id, params, options) {
  return api(`/api/assessments/${id}`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function getAttackGraphs(params, options) {
  return api('/api/attack_graphs', {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function getCountermeasures(params, options) {
  return api('/api/countermeasures', {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function postStatisAssessments(deployment_scenario_id, body, options) {
  return api(`/api/deployment_scenarios/${deployment_scenario_id}/assessment`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}


export async function postRiskMonitoring(deployment_scenario_id, body, options) {
  return api(`/api/risk_monitoring/${deployment_scenario_id}/monitoring`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

export async function getAssetsInDeploymentScenario(id, params, options) {
  return api(`/api/deployment_scenarios/${id}/assets`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}


export async function getNodeAttackGraph(deployment_scenario_id, params, options) {
  return api(`/api/risk_monitoring/${deployment_scenario_id}/monitoring/attack_graph_cve`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function getCountermeasuresInDeploymentScenario(id, params, options) {
  return api(`/api/deployment_scenarios/${id}/countermeasures`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function getAttackGraphDeploymentScenario(id, params, options) {
  return api(`/api/deployment_scenarios/${id}/attack_graph`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function getVulsInAssetInDeploymentScenario(deployment_scenario_id, asset_id, params, options) {
  return api(`/api/deployment_scenarios/${deployment_scenario_id}/assets/${asset_id}/cves`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function getVulsInAssetOnAttackGraph(deployment_scenario_id, asset_id, params, options) {
  return api(`/api/deployment_scenarios/${deployment_scenario_id}/attack_graph/assets/${asset_id}/cves`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function updateVulInAssetInDeploymentScenario(deployment_scenario_id, asset_id, cve_id, body, options) {
  return api(`/api/deployment_scenarios/${deployment_scenario_id}/assets/${asset_id}/cves/${cve_id}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

export async function updateVulInAssetOnAttackGraph(deployment_scenario_id, asset_id, body, options) {
  return api(`/api/deployment_scenarios/${deployment_scenario_id}/assets/${asset_id}/cves`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

export async function selectVulInAssetOnAttackGraph(deployment_scenario_id, asset_id, body, options) {
  return api(`/api/deployment_scenarios/${deployment_scenario_id}/attack_graph/assets/${asset_id}/cves`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}

export const detectThreat = async (deployment_scenario_id, body, options) => {
  return api(`/api/risk_monitoring/${deployment_scenario_id}/detect_threat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    data: body,
    ...(options || {}),
  });
}