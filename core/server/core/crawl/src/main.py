import os
from time import time

import json

from core.crawl.src.pretreatment.download import CPE_DICT_IN, CPE_MATCH_IN, download_cpe_dict, download_cpe_match, download_cve
from core.crawl.src.pretreatment.unzip import CPE_DICT_OUT, CPE_MATCH_OUT, unzip_cpe_dict, unzip_cpe_match, unzip_lib
from core.crawl.src.parser.cve import parser_cve
from core.crawl.src.import_data import CPE_MATCHES_JSON, import_cpe_dict, import_cve, import_cwe, import_cpe_matches
import shutil
from app.model.cve import CVE
from app.model.cpe import CPEMatches


async def get_cve(isUpdate: bool = True, delete: bool = True):
    print('-----------CVE------------')
    download_cve(isUpdate)
    unzip_lib(isUpdate)
    parser_cve(isUpdate)
    await import_cve(isUpdate)
    if delete:
        shutil.rmtree('./core/crawl/output/')
        shutil.rmtree('./core/crawl/input/')
        print('Deleting file')
    print('--------------------------')


async def get_cwe():
    print('-----------CWE------------')
    await import_cwe()
    print('--------------------------')


async def get_cpe():
    print('---------CPE_Match--------')
    download_cpe_match()
    unzip_cpe_match()
    await import_cpe_matches()
    os.remove(CPE_MATCH_OUT)
    os.remove(CPE_MATCH_IN)
    print('Deleting file')
    print('--------------------------')

async def get_cpe_dict():
    print('---------CPE_Dict---------')
    download_cpe_dict()
    unzip_cpe_dict()
    await import_cpe_dict()
    os.remove(CPE_DICT_IN)
    os.remove(CPE_DICT_OUT)
    print('Deleting file')
    print('--------------------------')


async def mapping_config():
    print('-------Mapping-Config-----')

    def query(configuration, cpe_matches):
        cpe23Uri = configuration['cpe23Uri']
        versionStartIncluding = configuration['versionStartIncluding']
        versionStartExcluding = configuration['versionStartExcluding']
        versionEndExcluding = configuration['versionEndExcluding']
        versionEndIncluding = configuration['versionEndIncluding']
        query_condition = {
            'cpe23Uri': cpe23Uri,
        }
        if versionStartIncluding != '':
            query_condition['versionStartIncluding'] = versionStartIncluding
        if versionStartExcluding != '':
            query_condition['versionStartExcluding'] = versionStartExcluding
        if versionEndExcluding != '':
            query_condition['versionEndExcluding'] = versionEndExcluding
        if versionEndIncluding != '':
            query_condition['versionEndIncluding'] = versionEndIncluding
        str_query_condition = str(query_condition)
        if str_query_condition in cpe_matches:
            result = data[str_query_condition]
            if len(result) == 0:
                return [cpe23Uri]
            return result
        else:
            print(str_query_condition)
            return []

    cves = await CVE.find({}).to_list(None)
    with open(CPE_MATCHES_JSON, 'r') as fp:
        data = json.load(fp)
    for cve in cves:
        # Parser 1
        results = []
        cpe_all = []
        for configurations in cve['configurations'][0]:
            tmp_result = []
            for configuration in configurations:
                if configuration['vulnerable']:
                    tmp_result += query(configuration, data)
                else:
                    print(cve['cve_id'])
            list_cpe = list(set(tmp_result))
            cpe_all += list_cpe
            results.append(list_cpe)
        cve['configurations'][0] = results

        # Parser 2
        results = []
        for configurations in cve['configurations'][1]:
            tmp_result_true = []
            tmp_result_false = []
            for configuration in configurations:
                target = query(configuration, data)
                if configuration['vulnerable']:
                    tmp_result_true += target
                else:
                    tmp_result_false += target
            list_cpe = list(set(tmp_result_true))
            cpe_all += list_cpe
            results.append({
                'true': list_cpe,
                'false': list(set(tmp_result_false)),
            })
        cve['configurations'][1] = results

        # Parser 3
        results = []
        for configurations in cve['configurations'][2]:
            tmp_result_true = []
            tmp_result_false = []
            for configuration in configurations:
                target = query(configuration, data)
                if configuration['vulnerable']:
                    tmp_result_true += target
                else:
                    tmp_result_false += target
            list_cpe = list(set(tmp_result_true))
            cpe_all += list_cpe
            results.append({
                'true': list_cpe,
                'false': list(set(tmp_result_false)),
            })
        cve['configurations'][2] = results

        # Parser 4
        results = []
        for configurations in cve['configurations'][3]:
            tmp_result = []
            tmp_result_true = []
            tmp_result_false = []
            for configuration in configurations:
                for config in configuration:
                    target = query(config, data)
                    if config['vulnerable']:
                        tmp_result_true += target
                    else:
                        tmp_result_false += target
            list_cpe = list(set(tmp_result_true))
            cpe_all += list_cpe
            tmp_result.append({
                'true': list_cpe,
                'false': list(set(tmp_result_false)),
            })
            results.append(tmp_result)
        cve['configurations'][3] = results
        cve['cpe'] = cpe_all

    await CVE.delete_many({})
    await CVE.insert_many(cves)
    print('--------------------------')

