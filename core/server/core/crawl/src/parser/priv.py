# v3 or v2
import pprint

AV_LOCAL = 'LOCAL'
AV_NETWORK = 'NETWORK'
AV_ADJACENT = 'ADJACENT_NETWORK'
AV_PHYSICAL = 'PHYSICAL'
attack_vectors = [AV_NETWORK, AV_ADJACENT, AV_LOCAL, AV_PHYSICAL]

# v2
AUTH_NONE = 'NONE'
AUTH_MULTIPLE = 'MULTIPLE'
AUTH_SINGLE = 'SINGLE'
authentications = [AUTH_NONE, AUTH_MULTIPLE, AUTH_SINGLE]

# v2
IMPACTS_ALL_COMPLETE = 'ALL COMPLETE'
IMPACTS_PARTIAL = 'PARTIAL'
IMPACTS_NONE = 'NONE'

IMPACT_NONE = 'NONE'
IMPACT_PARTIAL = 'PARTIAL'
IMPACT_COMPLETE = 'COMPLETE'

# v3
PRIV_NONE = 'NONE'
PRIV_LOW = 'LOW'
PRIV_HIGH = 'HIGH'
privileges = [PRIV_NONE, PRIV_LOW, PRIV_HIGH]

# parse_type
CPE_OS = 'cpe:2.3:o'
CPE_APP = 'cpe:2.3:a'
CPE_HW = 'cpe:2.3:h'

# Pre-Condition
PRE_NONE = 'NONE'
PRE_OS_USER = 'OS_USER'
PRE_OS_ADMIN = 'OS_ADMIN'
PRE_APP_USER = 'APP_USER'
PRE_APP_ADMIN = 'APP_ADMIN'

# Post-Condition
POST_NONE = 'NONE'
POST_OS_USER = 'OS_USER'
POST_OS_ADMIN = 'OS_ADMIN'
POST_APP_USER = 'APP_USER'
POST_APP_ADMIN = 'APP_ADMIN'


def get_attr_cve(cve: dict, attr: str):
    attrs = attr.split('.')
    val = cve
    try:
        for attribute in attrs:
            val = val[attribute]
        return val
    except:
        return ''


def parser_av(cve: dict):
    av = get_attr_cve(cve, 'impact.baseMetricV3.cvssV3.attackVector')
    if av == "":
        av = get_attr_cve(cve, 'impact.baseMetricV2.cvssV2.accessVector')
    return av


def __parser_pre_condition(cve_id: str, av: str, auth: str, privilege: str, cpe_type: int, description: str,
                           miss_condition: int = 0):
    if av not in attack_vectors:
        return ''
    # if auth not in authentications or privilege not in privileges:
    #     return ''
    if privilege == PRIV_NONE:
        return PRE_NONE

    if av == AV_LOCAL:
        if privilege == PRIV_LOW and cpe_type == 1:
            return PRE_OS_USER
        if privilege == PRIV_HIGH and cpe_type == 1:
            return PRE_OS_ADMIN
        if auth != AUTH_NONE:
            if privilege == PRIV_LOW and cpe_type != 1:
                return PRE_APP_USER
            if privilege == PRIV_HIGH and cpe_type != 1:
                return PRE_APP_ADMIN
        if auth == AUTH_NONE:
            if privilege == PRIV_LOW and cpe_type != 1:
                return PRE_OS_USER
            if privilege == PRIV_HIGH and cpe_type != 1:
                return PRE_OS_ADMIN
    if auth != AUTH_NONE:
        if privilege == PRIV_LOW and cpe_type == 1:
            return PRE_OS_USER
        if privilege == PRIV_HIGH and cpe_type == 1:
            return PRE_OS_ADMIN
        if privilege == PRIV_LOW and cpe_type != 1:
            return PRE_APP_USER
        if privilege == PRIV_HIGH and cpe_type != 1:
            return PRE_APP_ADMIN

    # case 12
    des_lower = description.lower()
    tmp_des = des_lower.split('.')

    for sentence in tmp_des:
        if ('allow' in sentence and 'guest OS user'.lower() in sentence) or (
                'allow' in sentence and 'PV guest user'.lower() in sentence) or (
                'user on a guest operating system' in sentence):
            return PRE_OS_USER
        if ('allow' in sentence and 'guest OS admin'.lower() in sentence) or (
                'allow' in sentence and 'PV guest admin'.lower() in sentence) or (
                'allow' in sentence and 'guest OS kernel admin'.lower() in sentence):
            return PRE_OS_ADMIN
    if 'allows local users' in des_lower or 'allowing local users' in des_lower or 'allow local users' in des_lower or 'allows the local user' in des_lower:
        return PRE_OS_USER
    if 'allows local administrators' in des_lower or 'allow local administrators' in des_lower or 'allows the local administrator' in des_lower:
        return PRE_OS_ADMIN
    if (
            'remote authenticated user' in des_lower and 'remote authenticated users with administrative privileges' not in des_lower) and cpe_type != 1:
        return PRE_APP_USER
    if (
            'remote authenticated user' in des_lower or 'remote authenticated users with administrative privileges' in des_lower) and cpe_type != 1:
        return PRE_APP_ADMIN
    if 'remote authenticated users' in des_lower and cpe_type == 1:
        return PRE_OS_USER
    if 'remote authenticated admin' in des_lower and cpe_type == 1:
        return PRE_OS_ADMIN
    return ''


def __parser_post_condition(cve_id: str, description: str, impacts: str, cpe_type: int):
    if impacts not in [IMPACTS_NONE, IMPACTS_PARTIAL, IMPACTS_ALL_COMPLETE]:
        return ''
    des_lower = description.lower()
    if (impacts == IMPACTS_ALL_COMPLETE) and (
            'gain root' in des_lower or ('gain unrestricted' in des_lower and 'root shell access' in des_lower) or
            'obtain root' in des_lower
    ):
        return POST_OS_ADMIN
    if (impacts == IMPACTS_ALL_COMPLETE) and (
            'gain privilege' in des_lower or 'gain host OS privilege' in des_lower or
            'gain admin' in des_lower or 'obtain local admin' in des_lower or
            'obtain admin' in des_lower or 'gain unauthorized access' in des_lower or
            'to root' in des_lower or 'to the root' in des_lower or
            'elevate the privilege' in des_lower or 'elevate privilege' in des_lower or
            'root privileges via buffer overflow' in des_lower
    ):
        return POST_OS_ADMIN
    if (
            'unspecified vulnerability' in des_lower or 'unspecified other impact' in des_lower or
            'unspecified impact' in des_lower or 'other impacts' in des_lower
    ):
        if impacts == IMPACTS_ALL_COMPLETE:
            return POST_OS_ADMIN
        if impacts == IMPACTS_PARTIAL and cpe_type == 1:
            return POST_OS_USER
    if (
            'gain privilege' in des_lower or 'gain unauthorized access' in des_lower) and impacts == IMPACTS_PARTIAL and cpe_type == 1:
        return POST_OS_USER
    if ('gain admin' in des_lower or 'obtain admin' in des_lower) and impacts == IMPACTS_PARTIAL:
        return POST_APP_ADMIN
    if (
            'hijack the authentication of admin' in des_lower or
            'hijack the authentication of super admin' in des_lower or
            'hijack the authentication of moderator' in des_lower
    ):
        return POST_APP_ADMIN
    if (
            'hijack the authentication of users' in des_lower or
            'hijack the authentication of arbitrary users' in des_lower or
            'hijack the authentication of unspecified victims' in des_lower
    ):
        return POST_APP_USER
    flag_9_10_11 = False
    if 'obtain password' in des_lower or 'obtain credential' in des_lower:
        flag_9_10_11 = True
    for tmp_des in des_lower.split('.'):
        if 'sniff' in tmp_des and 'credentials' in tmp_des:
            flag_9_10_11 = True
            break
        if 'sniff' in tmp_des and 'passwords' in tmp_des:
            flag_9_10_11 = True
            break
        if 'steal' in tmp_des and 'credentials' in tmp_des:
            flag_9_10_11 = True
            break
        if 'steal' in tmp_des and 'passwords' in tmp_des:
            flag_9_10_11 = True
            break
    if flag_9_10_11:
        if impacts == IMPACTS_ALL_COMPLETE and cpe_type == 1:
            return POST_OS_ADMIN
        if impacts == IMPACTS_PARTIAL:
            if cpe_type == 1:
                return POST_OS_USER
            else:
                return POST_APP_ADMIN
    if 'cleartext credential' in des_lower or 'cleartext password' in des_lower or 'obtain plaintext' in des_lower or 'obtain cleartext' in des_lower or 'discover cleartext' in des_lower or 'read network traffic' in des_lower or 'un-encrypted' in des_lower or 'unencrypted' in des_lower or 'intercept transmission' in des_lower or 'intercept communication' in des_lower or 'obtain and decrypt passwords' in des_lower or 'conduct offline password guessing' in des_lower or 'bypass authentication' in des_lower:
        if impacts == IMPACTS_ALL_COMPLETE and cpe_type == 1:
            return POST_OS_ADMIN
        if impacts == IMPACTS_PARTIAL:
            if cpe_type == 1:
                return POST_OS_USER
            else:
                return POST_APP_ADMIN
    if 'buffer overflow' in des_lower or 'command injection' in des_lower or 'write arbitrary,file' in des_lower or 'command execution' in des_lower or 'execute command' in des_lower or 'execute root command' in des_lower or 'execute commands as root' in des_lower or 'execute arbitrary' in des_lower or 'execute dangerous' in des_lower or 'execute php' in des_lower or 'execute script' in des_lower or 'execute local' in des_lower or 'execution of arbitrary' in des_lower or 'execution of command' in des_lower or 'remote execution' in des_lower or (
            'execute code' in des_lower and 'execute arbitrary SQL'.lower() not in des_lower):
        if impacts == IMPACTS_ALL_COMPLETE:
            return POST_OS_ADMIN
        if impacts == IMPACTS_PARTIAL:
            return POST_OS_USER
    if 'SQL injection'.lower() in des_lower and cpe_type != 1:
        return POST_APP_ADMIN
    if impacts == IMPACTS_NONE:
        return POST_NONE
    return ''


# CVE-2014-7874
def parser_pre_condition(cve: dict):
    # 1: os, 2: app, 3: hw
    cve_id = get_attr_cve(cve, 'cve_id')
    av = parser_av(cve)
    auth = get_attr_cve(cve, 'impact.baseMetricV2.cvssV2.authentication')
    privilege = get_attr_cve(cve, 'impact.baseMetricV3.cvssV3.privilegesRequired')
    description = get_attr_cve(cve, 'description')
    os = __parser_pre_condition(cve_id, av, auth, privilege, 1, description)
    app = __parser_pre_condition(cve_id, av, auth, privilege, 2, description)
    hw = __parser_pre_condition(cve_id, av, auth, privilege, 3, description)
    return [os, app, hw]


def parser_post_condition(cve: dict):
    # 1: os, 2: app, 3: hw
    cve_id = get_attr_cve(cve, 'cve_id')
    description = get_attr_cve(cve, 'description')
    impacts = ''
    ci = get_attr_cve(cve, 'impact.baseMetricV2.cvssV2.confidentialityImpact')
    ii = get_attr_cve(cve, 'impact.baseMetricV2.cvssV2.integrityImpact')
    ai = get_attr_cve(cve, 'impact.baseMetricV2.cvssV2.availabilityImpact')

    if ci == IMPACT_NONE or ii == IMPACT_NONE or ai == IMPACT_NONE:
        impacts = IMPACTS_NONE
    elif ci == IMPACT_COMPLETE and ii == IMPACT_COMPLETE and ai == IMPACT_COMPLETE:
        impacts = IMPACTS_ALL_COMPLETE
    elif ci == IMPACT_PARTIAL or ii == IMPACT_PARTIAL or ai == IMPACT_PARTIAL:
        impacts = IMPACTS_PARTIAL
    os = __parser_post_condition(cve_id, description, impacts, 1)
    app = __parser_post_condition(cve_id, description, impacts, 2)
    hw = __parser_post_condition(cve_id, description, impacts, 3)

    return [os, app, hw]


def parser_all_condition(cve: dict):
    pre_condition = parser_pre_condition(cve)
    post_condtion = parser_post_condition(cve)
    av = parser_av(cve)
    return {
        'attackVector': av,
        'condition': {
            'o': {
                'preCondition': pre_condition[0],
                'postCondition': post_condtion[0],
            },
            'a': {
                'preCondition': pre_condition[1],
                'postCondition': post_condtion[1],
            },
            'h': {
                'preCondition': pre_condition[2],
                'postCondition': post_condtion[2],
            },
        }
    }


data = {"_id": {"$oid": "62a19f5bf0d01d5b24c1adf3"}, "cve_id": "CVE-2003-0040", "cwe_id": "NVD-CWE-Other",
        "configurations": [[[{"vulnerable": True, "cpe23Uri": "cpe:2.3:a:inter7:courier-imap:1.6:*:*:*:*:*:*:*",
                              "versionStartIncluding": "", "versionStartExcluding": "", "versionEndExcluding": "",
                              "versionEndIncluding": ""}, {"vulnerable": True,
                                                           "cpe23Uri": "cpe:2.3:a:double_precision_incorporated:courier_mta:0.37.3:*:*:*:*:*:*:*",
                                                           "versionStartIncluding": "", "versionStartExcluding": "",
                                                           "versionEndExcluding": "", "versionEndIncluding": ""}]], [],
                           [], []],
        "description": "SQL injection vulnerability in the PostgreSQL auth module for courier 0.40 and earlier allows remote attackers to execute SQL code via the user name.",
        "impact": {"baseMetricV2": {
            "cvssV2": {"version": "2.0", "vectorString": "AV:N/AC:L/Au:N/C:P/I:P/A:P", "accessVector": "NETWORK",
                       "accessComplexity": "LOW", "authentication": "NONE", "confidentialityImpact": "PARTIAL",
                       "integrityImpact": "PARTIAL", "availabilityImpact": "PARTIAL", "baseScore": 7.5},
            "severity": "HIGH", "exploitabilityScore": 10, "impactScore": 6.4, "obtainAllPrivilege": False,
            "obtainUserPrivilege": True, "obtainOtherPrivilege": False, "userInteractionRequired": False}},
        "publishedDate": "2003-02-19T05:00Z", "lastModifiedDate": "2017-10-10T01:30Z", "attackVector": "NETWORK",
        "condition": {"o": {"preCondition": "", "postCondition": ""},
                      "a": {"preCondition": "", "postCondition": "APP_ADMIN"},
                      "h": {"preCondition": "", "postCondition": "APP_ADMIN"}}}
pprint.pprint(parser_all_condition(data))
