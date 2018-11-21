from . import BaseGenerator

class State(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.data = self._load_json('state.json')
    
    def generate(self):
        return self._choose(self.data['state'])
