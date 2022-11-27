// @ts-ignore

import api from "@/services/api";

/* eslint-disable */

export async function cwe(params, options) {
  return api('/api/assets', {
    method: 'GET',
    params: { ...params },
    ...(options || {}),
  });
}

export async function updateCWE(data, options) {
  return api('/api/assets', {
    data,
    method: 'PUT',
    ...(options || {}),
  });
}
