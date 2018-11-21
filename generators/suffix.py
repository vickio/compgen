from . import BaseGenerator
import re
import random

class Suffix(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.data = self._load_json('suffix.json')
        self.name_data = self._load_json('name.json')
    
    def generate(self):
        corps = [corp[0] for corp in self.name_data['company']]
        if re.search('(' + '|'.join(corps) + ')', self.company.name) == None and random.random() > 0.5:
            return ', ' + self._choose(self.data['suffix'])
        else:
            return ""
