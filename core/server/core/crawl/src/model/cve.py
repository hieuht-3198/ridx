import json
import os


class Mapping:
    cpe23Uri: str


class CPE:
    vulnerable: str
    cpe23Uri: str
    versionStartExcluding: str
    versionStartIncluding: str
    versionEndExcluding: str
    versionEndIncluding: str

    def __init__(self, vulnerable, cpe23Uri, versionStartExcluding, versionStartIncluding,
                 versionEndExcluding, versionEndIncluding):
        self.vulnerable = vulnerable
        self.cpe23Uri = cpe23Uri
        self.versionStartIncluding = versionStartIncluding
        self.versionStartExcluding = versionStartExcluding
        self.versionEndExcluding = versionEndExcluding
        self.versionEndIncluding = versionEndIncluding


class Item:
    cve_id: str
    parser_item: list

    def __init__(self, cve_id):
        self.cve_id = cve_id
        self.parser_item = []

    def add_parser_item(self, config):
        self.parser_item.append(config)

    def set_parser_item(self, configs):
        self.parser_item = configs

class Parser:
    cves: dict

    def __init__(self):
        self.cves = {}

    def addItem(self, item):
        self.cves[item.cve_id] = item.parser_item

    def toJson(self, filename):
        try:
            os.makedirs(os.path.dirname(filename), exist_ok=True)
        except:
            pass
        finally:
            with open(filename, 'w') as f:
                json.dump(self.cves, f)


class Summary:
    l: dict

    def __init__(self):
        self.l = {}

    def addItem(self, key, values):
        self.l[key] = values

    def toJson(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.l, f)
