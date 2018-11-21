from . import BaseGenerator
import re

class Url(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.name_data = self._load_json('name.json')
    
    def generate(self):
        tld = self.company._fake.tld()
        url = self.company.name.lower()
        corps = [corp[0].lower() for corp in self.name_data['company']]
        url = re.sub('(' + '|'.join(corps) + ')', '', url)
        url = re.sub(r'(^the|\&| and | of |\'s)', '', url)
        url = re.sub(r'\W+', '', url)
        return f'{url}.{tld}'
