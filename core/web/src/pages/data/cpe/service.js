// @ts-ignore

import api from "@/services/api";

/* eslint-disable */

export async function getCPEs(params, options) {
  return api('/api/cpes', {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function updateCWE(data, options) {
  return api('/api/cwes', {
    data,
    method: 'PUT',
    ...(options || {}),
  });
}
