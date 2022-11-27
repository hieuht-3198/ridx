from core.crawl.src.main import CPE_MATCH_IN
from core.crawl.src.pretreatment.download import CPE_DICT_IN

from ..hepler.io import get_all_files, make_dir
from ..hepler.unzip_helper import unzip_file

CPE_MATCH_OUT = './core/crawl/default/nvdcpematch-1.0.json'
CPE_DICT_OUT = './core/crawl/default/official-cpe-dictionary_v2.3.xml'

def unzip_lib(isUpdate: bool = True):
    output = ''
    input = ''
    if isUpdate:
        output = './core/crawl/input/json/cve/update/'
        input = './core/crawl/input/zip/cve/update/'
    else:
        output = './core/crawl/input/json/cve/common/'
        input = './core/crawl/input/zip/cve/common/'
    make_dir(output)
    filenames = get_all_files(input)
    print('Unzipping')
    for target in filenames:
        print(target)
        unzip_file(input+target, output)
    print('Done!')

def unzip_cpe_match():
    print('Unzipping')
    unzip_file(CPE_MATCH_IN, './core/crawl/default/')
    print('Done!')


def unzip_cpe_dict():
    print('Unzipping')
    unzip_file(CPE_DICT_IN, './core/crawl/default/')
    print('Done!')
