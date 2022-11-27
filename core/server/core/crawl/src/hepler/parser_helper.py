import os
import json
from ..hepler.io import make_dir

from ..model.cve import CPE

from types import SimpleNamespace


AND = 'AND'
OR = 'OR'
NULL = ''
NUMBER_PARSER = 4


def get_value(obj, key):
    if hasattr(obj, key):
        return getattr(obj, key)
    return NULL


def parser_cpe(cpe):
    try:
        vulnerable = cpe.vulnerable
    except:
        vulnerable = None
    cpe23Uri = cpe.cpe23Uri
    versionStartExcluding = get_value(cpe, 'versionStartExcluding')
    versionStartIncluding = get_value(cpe, 'versionStartIncluding')
    versionEndExcluding = get_value(cpe, 'versionEndExcluding')
    versionEndIncluding = get_value(cpe, 'versionEndIncluding')
    return CPE(vulnerable, cpe23Uri, versionStartExcluding, versionStartIncluding,
               versionEndExcluding, versionEndIncluding)


def toJson(filename, l):
    make_dir(filename)
    with open(filename, 'w') as f:
        json.dump(l, f)


def sns_to_dict(target):
    result = target.__dict__
    for key in result:
        if isinstance(result[key], SimpleNamespace):
            result[key] = sns_to_dict(result[key])    
    return result
