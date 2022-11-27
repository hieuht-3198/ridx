from collections import deque
import re


def cpe_to_dict(cpe_str): 
    cpe = CPEUtil(cpe_str)
    return {**cpe.to_dict(), 'id': cpe_str}

class CPEUtil():

    attrs = ["part", "vendor", "product", "version", "update", "edition"]

    def __init__(self, cpe_str):
        self.part = ""
        self.vendor = ""
        self.product = ""
        self.version = ""
        self.update = ""
        self.edition = ""

        cpe_str = cpe_str.replace("cpe:2.3:", "")

        parts = deque(cpe_str.split(":"))
        to_set = deque(self.attrs)
        while len(parts) > 0 and len(to_set) > 0:
            next_attr = to_set.popleft()
            setattr(self, next_attr, parts.popleft())

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

    def to_dict(self):
        return {
            "part": self.part, 
            "vendor": self.get_human("vendor"), 
            "product": self.get_human("product"), 
            "version": self.get_human("version"), 
            "update": self.get_human("update"),
            "edition": self.get_human("edition"),
        }
