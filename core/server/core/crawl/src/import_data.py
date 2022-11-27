from xml.dom import minidom
from core.crawl.src.hepler.io import get_all_files
from app.model.cpe import CPEMatches, CPE
from app.model.cve import CVE
from app.model.cwe import CWE
import json
import xmltodict

from core.crawl.src.pretreatment.unzip import CPE_DICT_OUT, CPE_MATCH_OUT

CPE_MATCHES_JSON = './core/crawl/default/cpe_matches.json'

async def import_cve(isUpdate: bool = True):
    print('Importing CVE')
    if isUpdate:
        path_data = './core/crawl/output/cve/update/'
        filenames = get_all_files(path_data)
        filenames.sort()
        for target in filenames:
            print(target)
            with open(path_data+target) as f:
                file_data = json.load(f)
            cve_list  = [cve['cve_id'] for cve in file_data]
            await CVE.delete_many({'cve_id': {'$in': cve_list}})
            await CVE.insert_many(file_data)
    else:
        path_data = './core/crawl/output/cve/common/'
        filenames = get_all_files(path_data)
        await CVE.delete_many({})
        filenames.sort(reverse=True)
        for target in filenames:
            print(target)
            with open(path_data+target) as f:
                file_data = json.load(f)
            await CVE.insert_many(file_data)                
    
    print('Done!')

async def import_cwe():
    print('Importing CWE')
    with open('./core/crawl/default/cwes.json') as f:
        file_data = json.load(f)
        cwe_list_id  = [cwe['cwe_id'] for cwe in file_data]
        cwe_list  = [{'cwe_id': cwe['cwe_id'],'cwe_name': cwe['name'], 'description': cwe['description']} for cwe in file_data]
        await CWE.delete_many({'cwe_id': {'$in': cwe_list_id}})
        await CWE.insert_many(cwe_list)
    
    print('Done!')


async def import_cpe_matches():
    print('Importing CPE matches')
    with open(CPE_MATCH_OUT) as f:
        file_data = json.load(f)
        await CPEMatches.delete_many({})
        list_import = []
        for target in file_data['matches']:
            import_data = target.copy()
            import_data['cpe_name'] = [tmp['cpe23Uri'] for tmp in target['cpe_name']]
            list_import.append(import_data)
        await CPEMatches.insert_many(list_import)

    print('Done!')
    print('Save to Json')
    cpe_matches = await CPEMatches.find({}).to_list(None)
    cpy_cpe_matches = {}
    for tmp in cpe_matches:
        cpy_tmp = tmp.copy()
        del cpy_tmp['cpe_name']
        del cpy_tmp['_id']
        cpy_cpe_matches[str(cpy_tmp)] = tmp['cpe_name']
    with open(CPE_MATCHES_JSON, 'w') as fp:
        json.dump(cpy_cpe_matches, fp)
    print('Done!')


async def import_cpe_dict():
    print('Importing CPE dict')
    # dom = minidom.parse(CPE_DICT_OUT)
    # elements = dom.getElementsByTagName('cpe-23:cpe23-item')
    # await CPE.delete_many({})
    # for ele in elements:
    #     list_import.append({
    #         'name': ele.attributes['name'].value
    #     })
    # await CPE.insert_many(list_import)
    # with open('./core/crawl/default/cpe.json') as f:
    #     file_data = json.load(f)
    #     await CPE.insert_many(file_data)
    with open(CPE_DICT_OUT) as fd:
        await CPE.delete_many({})
        d = xmltodict.parse(fd.read())
        cpes = []
        for tmp in d['cpe-list']['cpe-item']:
            title = set()
            if isinstance(tmp['title'], list):
                for t in tmp['title']:
                    title.update(t['#text'].lower().split(' '))
            else:
                title.update(tmp['title']['#text'].lower().split(' '))
            cpe = {
                'title': list(title),
                'name': tmp['cpe-23:cpe23-item']['@name']
            }
            cpes.append(cpe)
        
        await CPE.insert_many(cpes)
    print('Done!')

