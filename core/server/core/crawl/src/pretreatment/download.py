from os import mkdir
from progressbar import *
import urllib.request
from datetime import date

from ..hepler.io import make_dir

pbar = None

CPE_MATCH_IN = './core/crawl/default/nvdcpematch-1.0.json.zip'
CPE_DICT_IN = './core/crawl/default/official-cpe-dictionary_v2.3.xml.zip'

def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None


def download_cve(isUpdate: bool = True):    
    
    file_list = dict()
    if isUpdate:
        output='./core/crawl/input/zip/cve/update/'
        file_list['nvdcve-1.1-modified.json.zip'] = 'https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.zip'
    else:
        output='./core/crawl/input/zip/cve/common/'
        for year in range(2002, int(date.today().year) + 1):
            file_list["nvdcve-1.1-{}.json.zip".format(year)] = "https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-{}.json.zip".format(year)
    
    make_dir(output)

    print('Downloading')
    for target in file_list:
        print(target)
        urllib.request.urlretrieve(
            file_list[target], output + target, show_progress)
    print('Done!')

def download_cpe_match():
    link = 'https://nvd.nist.gov/feeds/json/cpematch/1.0/nvdcpematch-1.0.json.zip'
    print('Downloading')
    urllib.request.urlretrieve(link, CPE_MATCH_IN, show_progress)
    print('Done!')


def download_cpe_dict():
    link = 'https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip'
    print('Downloading')
    urllib.request.urlretrieve(link, CPE_DICT_IN, show_progress)
    print('Done!')
