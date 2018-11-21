from . import BaseGenerator

class StateName(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.states = self._load_json('state_names.json')
    
    def generate(self):
        return self.states[self.company.state]
