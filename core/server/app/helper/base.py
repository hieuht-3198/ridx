from bson import ObjectId, json_util, objectid
import random
import string
chars = string.ascii_letters + string.digits

def __include_attribute(d: dict, keys):
    if len(keys) == 0:
        keys = list(d.keys())
    else:
        keys.append('_id')
    result = {}
    for key in keys:
        if key in d:
            if isinstance(d[key], ObjectId):
                if key == '_id':
                    result['id'] = str(d[key])
                else:
                    result[key] = str(d[key])
            elif isinstance(d[key], dict):
                result[key] = __include_attribute(d[key], [])
            elif isinstance(d[key], list):
                result[key] = []
                for tmp in d[key]:
                    if isinstance(tmp, dict):
                        result[key].append(__include_attribute(tmp, []))
                    else:
                        result[key].append(tmp)
            else: 
                result[key] = d[key]

    return result


def user_helper(user):
    return {
        'id': str(user['_id']),
        'email': str(user['email']),
        'role': str(user['role']),
        'active': user['active'],
    }


def cve_helper(cve):
    return {
        'id': str(cve['_id']),
        'cve_name': str(cve['cve_name']),
        'description': str(cve['description']),
    }


def base_converter(target, select=[], default=[]):
    if not target:
        return default
    if isinstance(target, list):
        result = []
        for tmp in target:
            _id = {}
            if 'created_by' in tmp:
                _id = {**_id, 'created_by': str(tmp['created_by'])}
            if 'updated_by' in tmp:
                _id = {**_id, 'updated_by': str(tmp['updated_by'])}
            _att = __include_attribute(tmp, select)
            result.append({**_att, **_id})
        return result
    else:
        _id = {}
        if 'created_by' in target:
            _id = {**_id, 'created_by': str(target['created_by'])}
        if 'updated_by' in target:
            _id = {**_id, 'updated_by': str(target['updated_by'])}
        _att = __include_attribute(target, select)
        return {**_att, **_id}

def create_by_user_request(request: dict, user_id):
    return {
        **request,
        'created_by': ObjectId(user_id),
        'updated_by': ObjectId(user_id),
    }


def update_by_user_request(request: dict, user_id):
    return {
        **request,
        'updated_by': ObjectId(user_id),
    }

def add_created_by(request: dict, user_id):
    return {
        **request,
        'created_by': ObjectId(user_id)
    }


def search_by_id(l: list, val):
    for k in l:
        if k['id'] == val:
            return k
    return None

def generator_id():
    return str(objectid.ObjectId())

def generator_password(size = 10):
    return ''.join(random.choice(chars) for _ in range(size))