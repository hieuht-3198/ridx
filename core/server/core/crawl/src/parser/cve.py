from ..hepler.io import get_all_files

from ..hepler.parser_helper import *
from ..model.cve import *

# v3 or v2
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


def get_attr_cve(cve: dict, attr: str, default=''):
    attrs = attr.split('.')
    val = cve
    try:
        for attribute in attrs:
            val = val[attribute]
        return val
    except:
        return default


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
    if privilege == "":
        if auth == AUTH_NONE:
            privilege = PRIV_NONE
        elif auth == AUTH_SINGLE:
            privilege == PRIV_LOW
        elif auth == AUTH_MULTIPLE:
            privilege == PRIV_HIGH
        pass
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


def parser_config(cve_item):
    cve_id = cve_item.cve.CVE_data_meta.ID
    results = []
    for i in range(NUMBER_PARSER):
        results.append(Item(cve_id))

    nodes = cve_item.configurations.nodes

    for node in nodes:
        operator = node.operator
        # Parser 1
        if len(node.children) == 0 and operator == OR:
            cpe_match = node.cpe_match
            if len(cpe_match) > 0:
                configs = []
                for cpe in cpe_match:
                    configs.append(parser_cpe(cpe).__dict__)
                results[0].add_parser_item(configs)

        # Parser 2
        if len(node.children) == 0 and operator == AND:
            cpe_match = node.cpe_match
            if len(cpe_match) > 0:
                configs = []
                for cpe in cpe_match:
                    configs.append(parser_cpe(cpe).__dict__)
                results[1].add_parser_item(configs)

        # Parser 3
        if len(node.children) != 0 and operator == AND:
            configs = []
            for child in node.children:
                if child.operator == OR and len(child.cpe_match) != 0:
                    for cpe in child.cpe_match:
                        configs.append(parser_cpe(cpe).__dict__)
            results[2].add_parser_item(configs)

        # Parser 4
        if len(node.children) != 0 and operator == OR:
            print(cve_id)
            configs = []
            for child in node.children:
                if child.operator == AND and len(child.cpe_match) != 0:
                    configs_AND = []
                    for cpe in child.cpe_match:
                        configs_AND.append(parser_cpe(cpe).__dict__)
                    configs.append(configs_AND)
            results[3].add_parser_item(configs)
    return [target.parser_item for target in results]


# get filename
# filenames = next(walk(path_data), (None, None, []))[2]


cves_list = []


def parser_cve(isUpdate: bool = True):
    path_data = ''
    output = ''
    if isUpdate:
        output = './core/crawl/output/cve/update'
        path_data = './core/crawl/input/json/cve/update/'
    else:
        output = './core/crawl/output/cve/common'
        path_data = './core/crawl/input/json/cve/common/'

    filenames = get_all_files(path_data)
    filenames.sort()
    print('Parsering')
    for filename in filenames:
        print(filename, end='\t-->\t')
        cves_list = []
        file = open(path_data + filename)
        data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))
        configs = []
        summaries_config = []
        for i in range(NUMBER_PARSER):
            configs.append(Parser())
            summaries_config.append(Summary())
        descriptions = Parser()
        # impacts = Parser()
        cwe_ids = Parser()
        # Parser
        print(len(data.CVE_Items))
        for item in data.CVE_Items:
            cve_id = item.cve.CVE_data_meta.ID
            cwe_id = Item(cve_id=cve_id)
            try:
                problemtype_datas = item.cve.problemtype.problemtype_data
                for problemtype_data in problemtype_datas:
                    for cwe in problemtype_data.description:
                        cwe_id.add_parser_item(cwe.value)
            except:
                print(cve_id)
                exit(0)
            cwe_ids.addItem(cwe_id)
            description = Item(cve_id=cve_id)
            try:
                description_datas = item.cve.description.description_data
                for description_data in description_datas:
                    description.add_parser_item(description_data.value)
            except:
                print(cve_id)
                exit(0)
            descriptions.addItem(description)
            configurations = parser_config(item)

            target_description = description.parser_item[0] if len(description.parser_item) > 0 else ""
            target_cwe_id = cwe_id.parser_item[0] if len(cwe_id.parser_item) > 0 else ""
            target_impact = sns_to_dict(item.impact)
            target_cve = {
                'cve_id': cve_id,
                'cwe_id': target_cwe_id,
                'configurations': configurations,
                'description': target_description,
                'impact': target_impact,
                'publishedDate': item.publishedDate,
                'lastModifiedDate': item.lastModifiedDate
            }
            target_cve = {**target_cve, **parser_all_condition(target_cve)}
            cves_list.append(target_cve)

        toJson("{}/{}.json".format(output, filename[:-5]), cves_list)

        file.close()
    print('Done!')
