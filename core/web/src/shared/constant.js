export const KEY_DATA_GRAPH = 'dataGraph'
export const KEY_AUTH_TOKEN = 'AUTH_TOKEN'

export const NODE_UTILITY = 'NODE_UTILITY'
export const NODE_CPT = 'NODE_CPT'
export const NODE_DECISION = 'NODE_DECISION'

export const NODE_DECISION_TRUE = 'True'
export const NODE_DECISION_FALSE = 'False'
export const MAX_INT = Number.MAX_SAFE_INTEGER

export const DEPLOYMENT_SCENARIO_REQUIREMENTS_ANALYSIS = 'Requirements Analysis'
export const DEPLOYMENT_SCENARIO_DEPLOYMENTS = 'Deployments'
export const DEPLOYMENT_SCENARIO_OPERATIONS = 'Operations'
export const DEPLOYMENT_SCENARIO_STAGE = ['Requirements Analysis', 'Deployments', 'Operations']

export const CRITICAL_COLOR = '#D01117'
export const HIGH_COLOR = '#EA6913 '
export const MEDIUM_COLOR = '#EC9D15'
export const LOW_COLOR = '#41C545'
export const UNDER_LOW_COLOR = '#2E8EAE'

export const AV_LOCAL = 'LOCAL'
export const AV_PHYSICAL = 'PHYSICAL'
export const AV_ADJACENT_NETWORK = 'ADJACENT_NETWORK'
export const AV_NETWORK = 'NETWORK'


export const PR_NONE = 'NONE'
export const PR_OS_USER = 'OS_USER'
export const PR_OS_ADMIN = 'OS_ADMIN'
export const PR_APP_USER = 'APP_USER'
export const PR_APP_ADMIN = 'APP_ADMIN'

export const ASSET_OS = 'OS'
export const ASSET_APPLICATION = 'APPLICATION'
export const ASSET_HARDWARE = 'HARDWARE'

export const AV_ALL = [AV_NETWORK, AV_ADJACENT_NETWORK, AV_LOCAL, AV_PHYSICAL]
export const PR_ALL = [PR_NONE, PR_APP_USER, PR_APP_ADMIN, PR_OS_USER, PR_OS_ADMIN]


export const ROLE_ADMIN = 'ADMIN'
export const ROLE_USER = 'USER'


export const SEVERITY_LIST = [
    {
        type: 'Negligible',
        value: 1,
    },
    {
        type: 'Low',
        value: 2,
    },
    {
        type: 'Moderate',
        value: 3,
    },
    {
        type: 'Significant',
        value: 4,
    },
    {
        type: 'Catastrophic',
        value: 5,
    },
]

export const LIKELIHOOD_LIST = [
    {
        type: 'Improbable',
        value: 1,
    },
    {
        type: 'Remote',
        value: 2,
    },
    {
        type: 'Occasional',
        value: 3,
    },
    {
        type: 'Probale',
        value: 4,
    },
    {
        type: 'Frequent',
        value: 5,
    },
]

export const RISK_LEVEL_LIST = [
    {
        type: 'Low',
        value: 1,
        min: -1,
        max: 3,
    },
    {
        type: 'Medium',
        value: 2,
        min: 4,
        max: 6,
    },
    {
        type: 'High',
        value: 3,
        min: 8,
        max: 12,
    },
    {
        type: 'Critical',
        value: 4,
        min: 15,
        max: 100,
    },
]

export const RISK_MATRIX = [
    {
        "Risk level": "Low",
        "Likelihood": "Improbable",
        "Severity": "Negligible",
        "value": 1
    },
    {
        "Risk level": "Low",
        "Likelihood": "Improbable",
        "Severity": "Low",
        "value": 2
    },
    {
        "Risk level": "Low",
        "Likelihood": "Improbable",
        "Severity": "Moderate",
        "value": 3
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Improbable",
        "Severity": "Significant",
        "value": 4
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Improbable",
        "Severity": "Catastrophic",
        "value": 5
    },
    {
        "Risk level": "Low",
        "Likelihood": "Remote",
        "Severity": "Negligible",
        "value": 2
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Remote",
        "Severity": "Low",
        "value": 4
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Remote",
        "Severity": "Moderate",
        "value": 6
    },
    {
        "Risk level": "High",
        "Likelihood": "Remote",
        "Severity": "Significant",
        "value": 8
    },
    {
        "Risk level": "High",
        "Likelihood": "Remote",
        "Severity": "Catastrophic",
        "value": 10
    },
    {
        "Risk level": "Low",
        "Likelihood": "Occasional",
        "Severity": "Negligible",
        "value": 3
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Occasional",
        "Severity": "Low",
        "value": 6
    },
    {
        "Risk level": "High",
        "Likelihood": "Occasional",
        "Severity": "Moderate",
        "value": 9
    },
    {
        "Risk level": "High",
        "Likelihood": "Occasional",
        "Severity": "Significant",
        "value": 12
    },
    {
        "Risk level": "Critical",
        "Likelihood": "Occasional",
        "Severity": "Catastrophic",
        "value": 15
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Probale",
        "Severity": "Negligible",
        "value": 4
    },
    {
        "Risk level": "High",
        "Likelihood": "Probale",
        "Severity": "Low",
        "value": 8
    },
    {
        "Risk level": "High",
        "Likelihood": "Probale",
        "Severity": "Moderate",
        "value": 12
    },
    {
        "Risk level": "Critical",
        "Likelihood": "Probale",
        "Severity": "Significant",
        "value": 16
    },
    {
        "Risk level": "Critical",
        "Likelihood": "Probale",
        "Severity": "Catastrophic",
        "value": 20
    },
    {
        "Risk level": "Medium",
        "Likelihood": "Frequent",
        "Severity": "Negligible",
        "value": 5
    },
    {
        "Risk level": "High",
        "Likelihood": "Frequent",
        "Severity": "Low",
        "value": 10
    },
    {
        "Risk level": "Critical",
        "Likelihood": "Frequent",
        "Severity": "Moderate",
        "value": 15
    },
    {
        "Risk level": "Critical",
        "Likelihood": "Frequent",
        "Severity": "Significant",
        "value": 20
    },
    {
        "Risk level": "Critical",
        "Likelihood": "Frequent",
        "Severity": "Catastrophic",
        "value": 25
    }
]

export const VULNERABILITY_LIST = [
    {
        type: 'None',
        value: 1,
        color: UNDER_LOW_COLOR,
    },
    {
        type: 'Low',
        value: 2,
        color: LOW_COLOR,
    },
    {
        type: 'Medium',
        value: 3,
        color: MEDIUM_COLOR,
    },
    {
        type: 'High',
        value: 4,
        color: HIGH_COLOR,
    },
    {
        type: 'Critical',
        value: 5,
        color: CRITICAL_COLOR,
    },
]

export const STRIDE_S = 'Spoofing Identity'
export const STRIDE_T = 'Tampering With Data'
export const STRIDE_R = 'Repudiation Threats'
export const STRIDE_I = 'Information Disclosure'
export const STRIDE_D = 'Denial of Service'
export const STRIDE_E = 'Elevation of Privileges'


export const ATTACKER_TYPE = ['Spoofing Identity', 'Tampering With Data', 'Repudiation Threats', 'Information Disclosure', 'Denial of Service', 'Elevation of Privileges']

export const EXPLOITABILITY = [
    {
        type: 'Unproven',
        value: 0.85,
    },
    {
        type: 'Proof-of-Concept',
        value: 0.9,
    },
    {
        type: 'Functional',
        value: 0.95,
    },
    {
        type: 'High',
        value: 1.00,
    },
    {
        type: 'Not Defined',
        value: 1.00,
    },
]
export const REMEDIATION_LEVEL = [
    {
        type: 'Official Fix',
        value: 0.87,
    },
    {
        type: 'Temporary Fix',
        value: 0.9,
    },
    {
        type: 'Workaround',
        value: 0.95,
    },
    {
        type: 'Unavailable',
        value: 1.00,
    },
    {
        type: 'Not Defined',
        value: 1.00,
    },
]
export const REPORT_CONFIDENCE = [
    {
        type: 'Unconfirmed',
        value: 0.90,
    },
    {
        type: 'Uncorroborated',
        value: 0.95,
    },
    {
        type: 'Confirmed',
        value: 1.00,
    },
    {
        type: 'Not Defined',
        value: 1.00,
    },
]