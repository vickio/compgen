from . import BaseGenerator

class Founder(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.data = self._load_json('founder.json')
    
    def generate(self):
        first_name = self._choose(self.data[self.company.founder_gender])
        last_name = self.company._fake.last_name()
        return ' '.join([first_name, last_name])
