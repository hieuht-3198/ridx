from collections import deque
import json
import re
import fnmatch


class CPEException(Exception):
    pass


class CPE(object):
    attrs = ["part", "vendor", "product", "version", "update", "edition"]

    def __init__(self, cpe_str):
        """Create a new CPE object that represents the cpe_str
        :param str cpe_str: The cpe string
        """
        self.part = ""
        self.vendor = ""
        self.product = ""
        self.version = ""
        self.update = ""
        self.edition = ""

        if cpe_str.startswith("cpe:/"):
            cpe_str = cpe_str.replace("cpe:/", "")
        elif cpe_str.startswith("cpe:2.3:"):
            cpe_str = cpe_str.replace("cpe:2.3:", "")
        else:
            raise CPEException("Invalid cpe string {!r}".format(cpe_str))

        parts = deque(cpe_str.split(":"))
        to_set = deque(self.attrs)
        while len(parts) > 0 and len(to_set) > 0:
            next_attr = to_set.popleft()
            setattr(self, next_attr, parts.popleft())

    def has_wildcards(self):
        """Return true or false if any of this cpe's fields contain
        wildcards
        """
        if "*" in self.part:
            return True
        if "?" in self.part:
            return True
        elif "?" in self.vendor:
            return True
        elif "*" in self.vendor:
            return True
        elif "*" in self.product:
            return True
        elif "?" in self.product:
            return True
        elif "?" in self.version:
            return True
        elif "*" in self.version:
            return True
        elif "*" in self.update:
            return True
        elif "?" in self.update:
            return True
        elif "?" in self.edition:
            return True
        elif "*" in self.edition:
            return True
        else:
            return False

    def get_human(self, attr):
        val = getattr(self, attr)
        val = val.replace("_", " ")

        product_mapping = {
            "ie": "Internet Explorer"
        }
        if attr == "product" and val in product_mapping:
            val = product_mapping[val]

        # if there's lowercase letters in the value, make it a title
        # (if there'FAILEDs not, leave it alone - e.g. SP3)
        if re.search('[a-z]', val) is not None:
            val = val.title()

        if val.upper() in ["SP0", "SP1", "SP2", "SP3", "SP4", "SP5", "SP6"]:
            val = val.upper()
        if val.lower() in ["x86", "x64"]:
            val = val.lower()

        return val

    def __eq__(self, cpe_obj):
        """Return true or false if this CPE object matches
        the provided cpe_obj EXACTLY
        :param CPE cpe_obj: The cpe object to compare against
        """

        if self.part != cpe_obj.part:
            return False
        if self.vendor != cpe_obj.vendor:
            return False
        if self.product != cpe_obj.product:
            return False
        if self.version != cpe_obj.version:
            return False
        if self.update != cpe_obj.update:
            return False
        if self.edition != cpe_obj.edition:
            return False

        return True

    def matches(self, cpe):
        """Return true or false if this CPE object matches
        the provided cpe_str, using wildcards.
        :param cpe: The cpe to compare against
        """
        # TODO see issue #3

        if self.vendor and not fnmatch.fnmatch(cpe.vendor, self.vendor):
            print("vendor was false")
            return False
        elif self.product and not fnmatch.fnmatch(cpe.product, self.product):
            print("product was false")
            return False
        elif self.version and not fnmatch.fnmatch(cpe.version, self.version):
            print("version was false")
            return False
        elif self.update and not fnmatch.fnmatch(cpe.update, self.update):
            print("update was false")
            return False
        elif self.edition and not fnmatch.fnmatch(cpe.edition, self.edition):
            print("edition was false")
            return False
        elif self.part and not fnmatch.fnmatch(cpe.part, self.part):
            print("part was false")
            return False
        else:
            return True

    def human(self):
        """Makes cpe version of it user friendly"""
        res = []
        if self.vendor != "":
            res.append(self.get_human("vendor"))
        if self.product != "":
            res.append(self.get_human("product"))
        if self.version != "":
            res.append(self.get_human("version"))
        if self.update != "":
            res.append(self.get_human("update"))
        if self.edition != "":
            res.append(self.get_human("edition"))
        return " ".join(res)

    def to_dict(self):
        return {"part": self.part, "vendor": self.vendor, "product": self.product, "version": self.version,
                "update": self.update, "edition": self.edition}

    def to_dict_simple(self):
        return {
            'product': self.product,
            'version': self.version,
            'update': self.update,
            'edition': self.edition
        }

    def to_json(self):
        cpe1_json = json.dumps(self.to_dict())
        return cpe1_json


def expand_cpe(cpe_str, cpe_list):
    """Expand the provided cpe_str into any matching CPEs
    in the provided cpe list
    :param str cpe_str: The cpe string to expand
    :param list cpe_list: A list of cpe strings
    """
    cpe = CPE(cpe_str)
    result_cpe = []

    for other_cpe_str in cpe_list:
        other_cpe = CPE(other_cpe_str)
        if cpe.matches(other_cpe):
            result_cpe.append(other_cpe_str)

    return result_cpe


def to_cpe_simple(cpe: dict):
    data = cpe.copy()
    if 'version' not in data:
        data['version'] = '*'
    if 'update' not in data:
        data['update'] = '*'
    if 'edition' not in data:
        data['edition'] = '*'
    if 'part' not in data or 'vendor' not in data or 'product' not in data:
        raise Exception('CPE fail')
    for key in data:
        data[key] = data[key].replace(' ', '_').lower()
    return "cpe:2.3:{}:{}:{}:{}:{}:{}:".format(data['part'], data['vendor'], data['product'], data['version'], data['update'], data['edition'])
