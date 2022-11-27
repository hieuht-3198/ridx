// @ts-ignore

import api from "@/services/api";

/* eslint-disable */

export async function getRiskAssessment(id, params, options) {
  return api(`/api/risk_assessment/${id}`, {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}